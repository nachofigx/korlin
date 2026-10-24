#!/usr/bin/env python3
"""Banco de pruebas del traductor Korlin. Uso: python scripts/test-traductor.py"""
import importlib.util
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("t", RAIZ / "scripts" / "traductor-korlin.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
LEX = m.Lexico()

CASOS_K = [
    ("Mi man-ve man-re.", "comida"),
    ("li an-go-di ku.", "me lo contaron"),
    ("Mi e-sa lin.", "lengua"),
    ("Wi e-sa pes.", "personas"),
    ("Li go-pen a le ho.", "lo deduzco"),
    ("Na-toro na kan-sa vi i mi.", "mentira"),
    ("Halo! Mi e-sa Lin.", "lengua"),
    ("gu-ro", "bondad"),
    ("man-lo", "comedor"),
    ("sa-pe", "sabio"),
    ("na-gu", "malo"),
    ("me ho", "casa"),
]

CASOS_ES = [
    ("Yo como comida.", ["man-sa", "man-re"]),
    ("Nosotros queremos agua.", ["wi", "vo-sa", "wa"]),
    ("Ella fue a la casa.", ["li", "an-go-sa", "ho"]),
    ("El agua es buena.", ["wa", "e", "gu"]),
    ("Mi casa es grande.", ["mi", "ho", "me"]),
    ("El fuego es caliente.", ["fo", "tom"]),
    ("Yo quiero comer.", ["mi", "vo-sa", "man"]),
]

CASOS_EN = [
    ("I want water.", ["mi", "vo-sa", "wa"]),
    ("He went to the house.", ["li", "an-go-sa", "ho"]),
    ("The food is good.", ["man-re", "e", "gu"]),
    ("We are people.", ["wi", "e", "pes"]),
    ("My house is big.", ["mi", "ho", "me"]),
]

fallos = 0


def check(nombre, salida, esperados):
    global fallos
    faltan = [e for e in esperados if e not in salida]
    if faltan:
        fallos += 1
        print(f"  ✗ {nombre!r}\n     salida: {salida}\n     falta:  {faltan}")
    else:
        print(f"  ✓ {nombre!r} → {salida}")


print("== Korlin → ES ==")
for texto, esperado in CASOS_K:
    check(texto, m.korlin_a_otro(texto, LEX, "es"), [esperado])

print("\n== ES → Korlin ==")
for texto, esperados in CASOS_ES:
    # C-01: ya no hay -sa por defecto -> se pasa explicito en los casos
    check(texto, m.otro_a_korlin(texto, LEX, "es", evidencial="-sa"), esperados)

print("\n== EN → Korlin ==")
for texto, esperados in CASOS_EN:
    check(texto, m.otro_a_korlin(texto, LEX, "en", evidencial="-sa"), esperados)

print(f"\n{'✅ TODO OK' if fallos == 0 else f'❌ {fallos} fallos'}")



def test_coherencia_v02():
    import json, re
    try:
        import yaml
    except ImportError:
        yaml = None
    fallos = []

    # 1) cero formas con letras prohibidas
    if yaml is None:
        # sin pyyaml: leer las claves `forma:` del texto
        txt = open("data/lexico.yaml", encoding="utf-8").read()
        formas = re.findall(r"^\s*-?\s*forma:\s*\"?([^\"\n]+)\"?\s*$", txt, re.M)
        formas = [{"forma": f} for f in formas]
    else:
        formas = yaml.safe_load(open("data/lexico.yaml", encoding="utf-8"))["palabras"]
    malas = [str(p["forma"]) for p in formas
             if any(c in str(p["forma"]).lower() for c in "cqxjz")]
    if malas:
        fallos.append(f"formas con c/q/x/j/z: {malas}")
    fm = {str(p["forma"]).lower() for p in formas}
    if "jo" in fm:
        fallos.append("'jo' sigue en el lexico")
    if "ti" not in fm:
        fallos.append("'ti' (dia) no esta en el lexico")
    # sin formas duplicadas (misma forma + categoria)
    if yaml is not None:
        vistos, dup = set(), []
        for p in formas:
            k = (str(p["forma"]), str(p.get("categoria")))
            if k in vistos:
                dup.append(k)
            vistos.add(k)
        if dup:
            fallos.append(f"duplicadas (forma+categoria): {dup}")

    # 2) 21 fonemas (16 C + 5 V) en korlin.json, coherentes con el spec
    d = json.load(open("korlin.json", encoding="utf-8"))
    f = d["reglas"]["fonologia"]
    if f["fonemas"] != 21:
        fallos.append(f"fonemas en json = {f['fonemas']}, esperado 21")
    if len(f["consonantes"]) != 16 or len(f["vocales"]) != 5:
        fallos.append(f"consonantes={len(f['consonantes'])}, vocales={len(f['vocales'])}")
    if "v" not in f["consonantes"]:
        fallos.append("falta 'v' en consonantes")
    if "j" in f["consonantes"]:
        fallos.append("'j' sigue en consonantes")

    # 3) la spec y json coinciden en lo esencial
    spec = open("korlin-spec.md", encoding="utf-8").read()
    for frag in ["21 fonemas: 16 consonantes", "340", "`na` suelto", "`na-` pegado",
                 "raíz desnuda", "pro-drop"]:
        if frag not in spec:
            fallos.append(f"spec no contiene: {frag}")

    # 4) na- pegado NO niega verbos: aparece solo sobre raices nominales
    for frag in ["na-kan-sa", "na-go-ve"]:
        if frag in spec:
            fallos.append(f"spec aun usa '{frag}' (na- sobre verbo)")

    # 5) el traductor respeta v0.2
    import sys as _s
    from subprocess import run
    def tr(t, ev="sa"):
        cmd = [_s.executable, "scripts/traductor-korlin.py", "es"]
        if ev:
            cmd.append("--ev=" + ev)
        r = run(cmd + [t], capture_output=True, text=True)
        return r.stdout.strip().splitlines()[0]
    casos = [("¿Tú comes comida?", "mo"), ("El día es bueno.", "e-sa"),
             ("Él fue.", "an-go")]
    for txt, esp in casos:
        got = tr(txt)
        if esp not in got:
            fallos.append(f"traductor '{txt}' -> '{got}' (esperaba {esp})")

    # PR-22: orden del modificador (adjetivo antes del nucleo) y evidencial
    # en declarativa.  [PR-13/PR-17]
    casos_orden = [
        ("Nosotros construimos una casa grande.", "me ho"),   # no 'ho me'
        ("El agua es buena.", "e-sa"),                        # copula con evidencial
        ("Yo como comida.", "man-sa"),                        # verbo con evidencial
    ]
    for txt, esp in casos_orden:
        got = tr(txt)
        if esp not in got:
            fallos.append(f"orden/evidencial '{txt}' -> '{got}' (esperaba {esp})")
    # pregunta: no debe llevar evidencial
    _p = tr("¿Tú comes comida?")
    if any(e in _p for e in ("-ve", "-pen", "-di", "-sa")):
        fallos.append(f"la pregunta lleva evidencial: '{_p}'")
    # negacion suelta
    _n = tr("Yo no como comida.")
    if "na " not in _n:
        fallos.append(f"negacion sin 'na' suelto: '{_n}'")

    return fallos




# ---- ejecucion de coherencia v0.2 ----
_cof = test_coherencia_v02()
print("\n== Coherencia v0.2 (peticion de Korlin) ==")
for _c in _cof:
    print("  FALLA:", _c)
if _cof:
    fallos += len(_cof)
print(f"\n{'TODO OK' if fallos == 0 else str(fallos)+' fallos'}")
sys.exit(1 if fallos else 0)
