#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
c24_estimulos.py — Genera el material de la prueba con hablantes (C-24).

Produce:
  estimulos.json  — el diseno completo (pares, items, orden aleatorio sembrado)
  plantilla.csv   — hoja de registro para vaciar las respuestas
  hoja-respuestas.md — la misma hoja, legible, de LECTURA (no de audio)

Diseno:
  Bloque A (colisiones): 5 pares minimos por prosodia, mas el homofono
  compuesto A6 (`kilo` ≈ `ki-lo`, un acento en los dos).
  Cada par cubre, donde aplica, tres polos escritos: sin guion, con guion
  y espacio. El guion de `kilo` no se usa en A2: `ki-lo` es la palabra de A6.
  Bloque B (cluster hV-, 14 raices): lectura breve y eleccion entre 4 escritas.
  Bloque C (aceptabilidad): juicio de naturalidad al leer, sobre muestra del lexico.

Semilla fija: la prueba se puede repartir en varias sesiones sin repetir orden.
A6 y los complementos de polo se anaden DESPUES del sorteo de A1-A5/B/C
y no reordenan esos items. Los complementos van detras de A6: la secuencia
ya publicada (A1-A5 sorteados + A6) queda como prefijo.

Las declarativas llevan evidencial `-ve` (regla 4). La pregunta no.
Si el verbo es el blanco (`ha` en `ha lo`), la frase es pregunta: `-ve`
partiria el par.
"""
import csv
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SEMILLA = 20261024

# Orden y polos que la semilla 20261024 ya fijo. No se vuelven a sortear.
SEMILLA_A = [
    ("A1-1", "halo", "A"),
    ("A3-1", "mega", "A"),
    ("A1-2", "halo", "A"),
    ("A4-2", "na no", "B"),
    ("A3-2", "mega", "A"),
    ("A4-1", "nano", "A"),
    ("A2-2", "kilo", "A"),
    ("A5-2", "so mi", "B"),
    ("A2-1", "ki lo", "B"),
    ("A5-1", "so mi", "B"),
]
SEMILLA_A6 = [
    ("A6-1", "kilo", "A"),
    ("A6-2", "ki-lo", "B"),
]
SEMILLA_B = [
    ("B14", ["hilo", "holo", "halo", "helo"]),
    ("B04", ["hili", "ho", "hulu", "hele"]),
    ("B06", ["hapu", "hopu", "hepu", "hipu"]),
    ("B11", ["hedi", "hudi", "hodi", "hadi"]),
    ("B02", ["hili", "holo", "hala", "he"]),
    ("B01", ["hili", "ha", "hala", "hele"]),
    ("B13", ["hesa", "hasa", "husa", "hisa"]),
    ("B07", ["hisu", "hasu", "hosu", "hesu"]),
    ("B05", ["hala", "hili", "hu", "hele"]),
    ("B10", ["huki", "haki", "heki", "hoki"]),
    ("B03", ["hele", "hi", "hulu", "hala"]),
    ("B09", ["hadu", "hodu", "hedu", "hudu"]),
    ("B12", ["hako", "heko", "hiko", "huko"]),
    ("B08", ["hebu", "hubu", "hobu", "habu"]),
]
SEMILLA_C = [
    "kida", "misa", "len", "manu", "go", "duka", "nano", "fan", "kuno", "papa",
    "fu", "di", "Kina", "wi", "le", "kubi", "sa", "ye", "tuni", "puka",
    "peke", "sen", "la", "reme", "ore", "gan", "tani", "wa", "ko", "hoki",
]

# ---------------------------------------------------------------- Bloque A
# Cada par: la forma del lexico vs su lectura alternativa.
# A1-A5: 1 acento (penultima) vs 2 acentos (espacio).
# A6: homofono verdadero, los dos con un acento; el guion es la grafia.
# guion_relevante: partir la forma con guion NO crea otra palabra del lexico.
# A2 es False: `ki-lo` ya es *donde* y lo mide A6.
COLISIONES = [
    {"id": "A1", "forma": "halo", "afi": "/ˈha.lo/", "glosa": "hola (saludo)",
     "alterna": "ha lo", "afi_alt": "/ˈha ˈlo/", "glosa_alt": "tener lugar",
     "oracion": "Halo, mi go-ve.", "oracion_alt": "Tu ha lo i le ho mo?",
     "guion_relevante": True},
    {"id": "A2", "forma": "kilo", "afi": "/ˈki.lo/", "glosa": "mil (×1000)",
     "alterna": "ki lo", "afi_alt": "/ˈki ˈlo/", "glosa_alt": "que lugar",
     "oracion": "Mi ha-ve kilo hos.", "oracion_alt": "Ki lo tu go?",
     "guion_relevante": False},
    {"id": "A3", "forma": "mega", "afi": "/ˈme.ga/", "glosa": "millon (×10^6)",
     "alterna": "me ga", "afi_alt": "/ˈme ˈga/", "glosa_alt": "tierra grande",
     "oracion": "Mi ha-ve mega hos.", "oracion_alt": "Mi ve-ve le me ga.",
     "guion_relevante": True},
    {"id": "A4", "forma": "nano", "afi": "/ˈna.no/", "glosa": "nano- (×10^-9)",
     "alterna": "na no", "afi_alt": "/ˈna ˈno/", "glosa_alt": "no [es] noche",
     "oracion": "Mi ha-ve u nano re.", "oracion_alt": "Na no, e-ve ti.",
     "guion_relevante": True},
    {"id": "A5", "forma": "somi", "afi": "/ˈso.mi/", "glosa": "gris",
     "alterna": "so mi", "afi_alt": "/ˈso ˈmi/", "glosa_alt": "entonces yo",
     "oracion": "Le nubu e-ve somi.", "oracion_alt": "So mi go-ve.",
     "guion_relevante": True},
]

# Homofono compuesto (deuda C-05 / regla 21). NO entra en el sorteo de arriba:
# un Random aparte decide X, y los items se appenden al bloque A.
COLISIONES_EXTRA = [
    {"id": "A6", "forma": "kilo", "afi": "/ˈki.lo/", "glosa": "mil (×1000)",
     "alterna": "ki-lo", "afi_alt": "/ˈki.lo/", "glosa_alt": "donde",
     "oracion": "Mi ha-ve kilo hos.", "oracion_alt": "Ki-lo tu go?",
     "guion_relevante": False},
]

# ---------------------------------------------------------------- Bloque B
# Cluster hV-: vecinos minimos (misma estructura, distinta vocal o consonante).
HV = [
    {"id": "B01", "forma": "ha",   "es": "tener",    "vecinos": ["hala", "hele", "hili"]},
    {"id": "B02", "forma": "he",   "es": "cabeza",   "vecinos": ["hala", "hili", "holo"]},
    {"id": "B03", "forma": "hi",   "es": "alto",     "vecinos": ["hala", "hele", "hulu"]},
    {"id": "B04", "forma": "ho",   "es": "casa",     "vecinos": ["hele", "hili", "hulu"]},
    {"id": "B05", "forma": "hu",   "es": "tristeza", "vecinos": ["hala", "hele", "hili"]},
    {"id": "B06", "forma": "hapu", "es": "abrir",    "vecinos": ["hepu", "hipu", "hopu"]},
    {"id": "B07", "forma": "hesu", "es": "gusto",    "vecinos": ["hasu", "hisu", "hosu"]},
    {"id": "B08", "forma": "hobu", "es": "animal",   "vecinos": ["habu", "hebu", "hubu"]},
    {"id": "B09", "forma": "hodu", "es": "montana",  "vecinos": ["hadu", "hedu", "hudu"]},
    {"id": "B10", "forma": "hoki", "es": "dinero",   "vecinos": ["haki", "heki", "huki"]},
    {"id": "B11", "forma": "hudi", "es": "tocar",    "vecinos": ["hadi", "hedi", "hodi"]},
    {"id": "B12", "forma": "huko", "es": "ciudad",   "vecinos": ["hako", "heko", "hiko"]},
    {"id": "B13", "forma": "husa", "es": "olor",     "vecinos": ["hasa", "hesa", "hisa"]},
    {"id": "B14", "forma": "halo", "es": "hola",     "vecinos": ["helo", "holo", "hilo"]},
]

EVIDENCIALES = ("-ve", "-pen", "-di", "-sa")


def _guion_de(c):
    """Corte escrito de la alterna: `ha lo` → `ha-lo`. No es una raiz nueva."""
    return c["alterna"].replace(" ", "-")


def aplica_guion(oracion, forma, guion):
    """Sustituye la forma pegada por la grafia con guion, una sola vez."""
    def repl(m):
        pal = m.group(0)
        nuevo = guion
        if pal[:1].isupper():
            nuevo = guion[:1].upper() + guion[1:]
        return nuevo
    return re.sub(rf"\b{re.escape(forma)}\b", repl, oracion, count=1, flags=re.IGNORECASE)


def lectura_de(c, condicion):
    """Oracion que el hablante lee. Una sola grafia del par."""
    if c["id"] == "A6":
        if condicion == "con_guion":
            return c["oracion_alt"]
        if condicion == "sin_guion":
            return c["oracion"]
        raise ValueError(f"A6 no tiene condicion {condicion}")
    if condicion == "sin_guion":
        return c["oracion"]
    if condicion == "espacio":
        return c["oracion_alt"]
    if condicion == "con_guion":
        if not c["guion_relevante"]:
            raise ValueError(f"{c['id']}: el guion seria otra palabra; no se aplica")
        return aplica_guion(c["oracion"], c["forma"], _guion_de(c))
    raise ValueError(condicion)


def _base_item(c, item_id, x_es_alt, origen):
    return {
        "id": item_id,
        "par": c["id"],
        "estimulo_A": c["forma"], "afi_A": c["afi"], "glosa_A": c["glosa"],
        "estimulo_B": c["alterna"], "afi_B": c["afi_alt"], "glosa_B": c["glosa_alt"],
        "X": c["alterna"] if x_es_alt else c["forma"],
        "respuesta_correcta": "B" if x_es_alt else "A",
        "oracion_A": c["oracion"], "oracion_B": c["oracion_alt"],
        "origen": origen,
    }


def _anota_seed(item, c):
    """Polo escrito del item ya sorteado. No llama al RNG."""
    rep = int(item["id"].rsplit("-", 1)[1])
    x_es_forma = item["X"] == c["forma"]
    if c["id"] == "A6":
        condicion = "con_guion" if item["X"] == c["alterna"] else "sin_guion"
    elif not x_es_forma:
        condicion = "espacio"
    elif rep == 2 and c["guion_relevante"]:
        condicion = "con_guion"
    else:
        condicion = "sin_guion"
    item["condicion"] = condicion
    item["lectura"] = lectura_de(c, condicion)


def _items_par(c, rng, origen):
    items = []
    for rep in (1, 2):
        x_es_alt = rng.choice([False, True])
        items.append(_base_item(c, f"{c['id']}-{rep}", x_es_alt, origen))
    return items


def bloque_a(rng):
    """Dos pasadas de A1-A5. El RNG decide el polo y luego el orden.

    Solo A1-A5 consumen este RNG (semilla 20261024).
    """
    items = []
    for c in COLISIONES:
        items.extend(_items_par(c, rng, "semilla"))
    rng.shuffle(items)
    return items


class _XFijo:
    """choice() devuelve la secuencia dada. No toca el RNG global."""

    def __init__(self, flags):
        self._flags = iter(flags)

    def choice(self, seq):
        return next(self._flags)


def bloque_a_extra():
    """Pares anadidos sin tocar el orden ya fijado por la semilla global.

    X no se sortea, para no consumir ningun RNG. La repeticion 1 tiene X = la
    forma del lexico; la 2, X = la alterna con guion.
    """
    items = []
    for c in COLISIONES_EXTRA:
        items.extend(_items_par(c, _XFijo([False, True]), "a6"))
    return items


def _por_id(cols):
    return {c["id"]: c for c in cols}


def anota_bloque_a(items):
    cols = _por_id(COLISIONES + COLISIONES_EXTRA)
    for it in items:
        _anota_seed(it, cols[it["par"]])
    return items


def complementos(items):
    """Polos que la semilla no saco. Fijos, sin RNG, despues de A6.

    A2 no recibe `ki-lo` (eso es A6). A6 ya trae sin_guion y con_guion.
    """
    por_par = defaultdict(list)
    for it in items:
        por_par[it["par"]].append(it)
    nuevos = []
    for c in COLISIONES:
        tienen = {it["condicion"] for it in por_par[c["id"]]}
        querer = ["sin_guion", "espacio"]
        if c["guion_relevante"]:
            querer.append("con_guion")
        n = max(int(it["id"].rsplit("-", 1)[1]) for it in por_par[c["id"]])
        for cond in querer:
            if cond in tienen:
                continue
            n += 1
            x_es_alt = cond == "espacio"
            it = _base_item(c, f"{c['id']}-{n}", x_es_alt, "complemento")
            it["condicion"] = cond
            it["lectura"] = lectura_de(c, cond)
            if cond == "con_guion":
                it["X"] = _guion_de(c)
            nuevos.append(it)
            tienen.add(cond)
    return nuevos


def _chequea_semilla(a_base, extra, b, c):
    got_a = [(it["id"], it["X"], it["respuesta_correcta"]) for it in a_base]
    if got_a != SEMILLA_A:
        raise SystemExit(f"la semilla {SEMILLA} ya no reproduce A1-A5:\n{got_a}")
    got_a6 = [(it["id"], it["X"], it["respuesta_correcta"]) for it in extra]
    if got_a6 != SEMILLA_A6:
        raise SystemExit(f"A6 dejo de ser kilo / ki-lo:\n{got_a6}")
    got_b = [(it["id"], it["opciones"]) for it in b]
    if got_b != SEMILLA_B:
        raise SystemExit("la semilla ya no reproduce el bloque B")
    got_c = [it["forma"] for it in c]
    if got_c != SEMILLA_C:
        raise SystemExit("la semilla ya no reproduce el bloque C")


def _chequea_lecturas(items):
    """Cada declarativa lleva evidencial; cada polo aparece en su oracion."""
    polos = defaultdict(set)
    for it in items:
        lec = it["lectura"]
        bajo = lec.lower()
        if "oye" in bajo or "oí" in lec:
            raise SystemExit(f"{it['id']}: la lectura no puede ser de oido ({lec})")
        if lec.endswith("."):
            if not any(s in lec for s in EVIDENCIALES):
                raise SystemExit(f"{it['id']}: declarativa sin evidencial ({lec})")
        cond = it["condicion"]
        polos[it["par"]].add(cond)
        if cond == "sin_guion":
            if it["estimulo_A"].lower() not in bajo:
                raise SystemExit(f"{it['id']}: falta la forma pegada en {lec}")
        elif cond == "espacio":
            if it["estimulo_B"].lower() not in bajo:
                raise SystemExit(f"{it['id']}: falta el espacio en {lec}")
        elif cond == "con_guion":
            guion = it["estimulo_B"] if it["par"] == "A6" else it["estimulo_B"].replace(" ", "-")
            if guion.lower() not in bajo:
                raise SystemExit(f"{it['id']}: falta el guion en {lec}")
            if it["par"] == "A2":
                raise SystemExit("A2 no puede mostrar ki-lo")
        else:
            raise SystemExit(f"condicion desconocida {cond}")
    for c in COLISIONES:
        querer = {"sin_guion", "espacio"}
        if c["guion_relevante"]:
            querer.add("con_guion")
        if not querer <= polos[c["id"]]:
            raise SystemExit(f"{c['id']}: faltan polos {querer - polos[c['id']]}")
    if polos["A6"] != {"sin_guion", "con_guion"}:
        raise SystemExit(f"A6 debe ser kilo vs ki-lo, no {polos['A6']}")


def bloque_b(rng):
    """Identificacion escrita: se muestra una forma, se elige entre 4 escritas.

    Las 4 opciones son SIEMPRE distintas; los distractores son minimos
    (una sola vocal o consonante de diferencia). La forma se tapa antes
    de elegir: no es una copia con la palabra a la vista, ni un audio.
    """
    items = []
    for h in HV:
        opciones = [h["forma"]] + [v for v in h["vecinos"] if v != h["forma"]]
        opciones = list(dict.fromkeys(opciones))
        assert len(opciones) >= 4, f"{h['id']}: menos de 4 opciones"
        opciones = opciones[:4]
        rng.shuffle(opciones)
        items.append({
            "id": h["id"], "estimulo": h["forma"], "glosa": h["es"],
            "opciones": opciones, "respuesta_correcta": h["forma"],
        })
    rng.shuffle(items)
    return items


def bloque_c(rng):
    """Aceptabilidad: muestra estratificada del lexico para juicio de naturalidad."""
    import yaml
    d = yaml.safe_load((RAIZ / "data" / "lexico.yaml").read_text(encoding="utf-8"))
    palabras = [p for p in d["palabras"] if "-" not in str(p["forma"])]
    rng.shuffle(palabras)
    muestra = palabras[:30]
    return [{"id": f"C{i+1:02d}", "forma": str(p["forma"]),
             "es": str(p.get("es", "")), "categoria": str(p.get("categoria", ""))}
            for i, p in enumerate(muestra)]


def plantilla_csv(ruta, a, b, c):
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["# HOJA DE REGISTRO C-24 — una fila por hablante en la cabecera"])
        w.writerow(["# Instrumento ESCRITO. No hay audio. No inventar filas de hablantes."])
        w.writerow(["hablante_id", "edad", "lengua_materna", "sabe_esperanto", "fecha", "minutos"])
        w.writerow(["", "", "", "", "", ""])
        w.writerow([])
        w.writerow(["bloque", "item", "estimulo", "respuesta_dada", "correcta",
                    "segundos", "comentario", "condicion"])
        for it in a:
            w.writerow(["A", it["id"], it["lectura"], "", it["respuesta_correcta"],
                        "", "", it["condicion"]])
        for it in b:
            w.writerow(["B", it["id"], it["estimulo"], "", it["respuesta_correcta"],
                        "", "", ""])
        for it in c:
            w.writerow(["C", it["id"], it["forma"], "", "", "", "", ""])
        w.writerow(["nota", "cierre",
                    "¿Notaste alguna vez que una palabra pudiera leerse de dos maneras?",
                    "", "", "", "", ""])


def hoja_md(ruta, a, b, c):
    L = []
    L.append("# Hoja de registro — C-24 (prueba con hablantes)")
    L.append("")
    L.append("**Un formulario por hablante.** Lo llena quien aplica la prueba.")
    L.append("**Todo es lectura:** se muestra la oración o la tarjeta escrita.")
    L.append("")
    L.append("## Cabecera")
    L.append("")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    for k in ("hablante_id", "edad", "lengua_materna", "sabe_esperanto", "fecha", "minutos"):
        L.append(f"| {k} | |")
    L.append("")
    L.append("## Bloque A — discriminación (lee la oración y elige A o B)")
    L.append("")
    L.append("El hablante **lee** la oración y elige la paráfrasis. No ve la otra grafía del par.")
    L.append("A = sentido de la forma del léxico. B = sentido de la lectura alterna.")
    L.append("")
    L.append("| # | Lees | A | B | Respuesta (A/B) | Seg. |")
    L.append("|---|---|---|---|---|---|")
    for it in a:
        L.append(f"| {it['id']} | {it['lectura']} | {it['glosa_A']} | {it['glosa_B']} | | |")
    L.append("")
    L.append("## Bloque B — identificación (¿cuál leíste?)")
    L.append("")
    L.append("La columna «Forma» es la tarjeta: se muestra escrita, se tapa,")
    L.append("y solo entonces el hablante mira las cuatro opciones y marca cuál leyó.")
    L.append("")
    L.append("| # | Forma (tarjeta; tapar) | Opciones | Leyó | Seg. |")
    L.append("|---|---|---|---|---|")
    for it in b:
        L.append(f"| {it['id']} | {it['estimulo']} | {' · '.join(it['opciones'])} | | |")
    L.append("")
    L.append("## Bloque C — naturalidad al leer (1 = raro, 5 = natural)")
    L.append("")
    L.append("Lee la forma. «¿Qué tan natural te parece, leída, como palabra de un idioma?»")
    L.append("")
    L.append("| # | Forma | Español | 1-5 |")
    L.append("|---|---|---|---|")
    for it in c:
        L.append(f"| {it['id']} | {it['forma']} | {it['es']} | |")
    L.append("")
    L.append("## Cierre del bloque A (sin volver a mostrar el material)")
    L.append("")
    L.append("¿Notaste alguna vez que una palabra pudiera leerse de dos maneras?")
    L.append("")
    L.append("| Respuesta | Si nombra alguna, ¿cuál? |")
    L.append("|---|---|")
    L.append("| | |")
    ruta.write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    # La semilla se fija aqui, antes de A, B y C, y no se vuelve a tocar.
    rng = random.Random(SEMILLA)
    a_base, b, c = bloque_a(rng), bloque_b(rng), bloque_c(rng)
    extra = bloque_a_extra()
    _chequea_semilla(a_base, extra, b, c)
    anota_bloque_a(a_base)
    anota_bloque_a(extra)
    comps = complementos(a_base)
    a = a_base + extra + comps
    _chequea_lecturas(a)
    if [it["id"] for it in a[:len(SEMILLA_A) + len(SEMILLA_A6)]] != [
        x[0] for x in SEMILLA_A + SEMILLA_A6
    ]:
        raise SystemExit("A6 dejo de ir justo detras del bloque sorteado")
    datos = {
        "prueba": "C-24 — medida con hablantes",
        "modo": "escrito",
        "version_lexico": "238 formas (lexico v0.8.4; sin raices nuevas)",
        "version_instrumento": "2026-10-27",
        "semilla": SEMILLA,
        "semilla_nota": (
            "20261024 fija el orden y el polo X de A1-A5, y el orden de B y C. "
            "A6 (kilo ≈ ki-lo) va justo despues: A6-1 es kilo y A6-2 es ki-lo. "
            "Su X no sale de la semilla. Los complementos (origen complemento) "
            "tapan polos que la semilla no saco y se anaden detras de A6: "
            "no reordenan A1-A5, B ni C. A2 no usa el guion ki-lo."
        ),
        "nota_audio": (
            "El TTS no es el instrumento. scripts/c24_audio.py solo documenta "
            "por que la /h/ y el acento no se miden con la voz es-MX."
        ),
        "bloques": {
            "A_colisiones": {
                "items": a, "n_items": len(a),
                "que_mide": (
                    "lectura: pares minimos con guion, espacio y el homofono "
                    "kilo / ki-lo. Sin audio."
                ),
            },
            "B_cluster_hV": {
                "items": b, "n_items": len(b),
                "que_mide": "lectura tapada: identificacion de vecinos minimos con h-",
            },
            "C_naturalidad": {
                "items": c, "n_items": len(c),
                "que_mide": "juicio de naturalidad al leer el lexico",
            },
        },
        "umbrales": {
            "sin_problema": ">= 90% de acierto",
            "vigilancia": "75-90%",
            "renombrar": "< 75%",
        },
    }
    (RAIZ / "docs" / "c24-estimulos.json").write_text(
        json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    plantilla_csv(RAIZ / "docs" / "c24-plantilla.csv", a, b, c)
    hoja_md(RAIZ / "docs" / "c24-hoja-respuestas.md", a, b, c)
    print(f"Bloque A: {len(a)} items | Bloque B: {len(b)} | Bloque C: {len(c)}")
    for it in a:
        print(f"  {it['id']:5} {it['condicion']:10} {it['lectura']}")
    print("escrito: docs/c24-estimulos.json, c24-plantilla.csv, c24-hoja-respuestas.md")


if __name__ == "__main__":
    sys.exit(main())
