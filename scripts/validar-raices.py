#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validar-raices.py — Valida lotes de raices nuevas para Korlin.

Criterios (acordados con el revisor; ids R0-R6 de la ronda v0.6):

  R0  fonotactica: la forma debe encajar en `(C)V(C)` con coda {m,n,s} y sin
      grupos consonantaticos. (Cubre el viejo rechazo de `tra` y `ak`.)
  R1  no chocar con un AFIJO del inventario.
  R4  no existir ya en el lexico (colision exacta).
  R3  no ser una raiz + afijo DERIVABLE por la regla 17 (`raiz+sufijo`).
  R5  no equivaler a DOS PARTICULAS finales seguidas (`ku ri`).
  R6  no equivaler a una CONSTRUCCION CANONICA de dos palabras:
        - posesion        pron + nombre     (`mi lo`)
        - determinante    det  + nombre     (`le ho`, `se wa`)
        - preposicion     prep + nombre     (`kon mi`, `de su`)
        - complementante  compl + oracion   (`ki li`, `mo mi`)
        - sujeto+negacion nombre + `na`     (`ga na`)
        - verbo+objeto    verbo + nombre    (`ha lu`, `da no`, `fa ma`)
        - Adj-N           adjetivo + nombre (`hi su`)   <- orden real (regla 3)

  OJO: R6 aplicado LITERALMENTE (cualquier particion en dos formas del lexico)
  rechaza TODAS las CVCV: de 6.400 posibles, 0 pasan (`punu`=pu+nu,
  `kotu`=ko+tu...). Hay que acotarlo a los patrones CANONICOS de arriba,
  usando las CATEGORIAS del lexico, no la mera existencia de la forma.
  Con el criterio acotado pasan 5.400 de 6.400.

Uso:
  python3 scripts/validar-raices.py                 # prueba el lote de ejemplo
  python3 scripts/validar-raices.py --archivo lote.txt
     (una linea por candidata: `raiz | ES | EN | categoria`)

Rutas absolutas desde la raiz del repo. Salida: veredicto por raiz + resumen.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

CONSONANTES = "pbtdkgmnfvshlrwy"          # 16; sin c, j, q, x, z (la y SI es consonante)
VOCALES = "aeiou"
CODAS = "mns"

ACTITUD = {"yo", "hu", "we", "fi", "bu", "ri", "pu", "ni", "la"}   # particulas finales
COMPLEMENTANTES = {"ki", "mo"}
DETERMINANTES = {"le", "se", "te", "u"}
PREPOSICIONES = {"de", "kon", "po", "a", "i"}


def carga_lexico():
    """Lee data/lexico.yaml (o korlin.json si falta PyYAML) -> {forma: categoria}."""
    try:
        import yaml
        ruta = RAIZ / "data" / "lexico.yaml"
        d = yaml.safe_load(ruta.read_text(encoding="utf-8"))
        # YAML 1.1: `no`/`yes` se leen como booleanos -> revertir
        rev = {False: "no", True: "ya"}
        return {str(rev.get(p["forma"], p["forma"])).lower(): str(p.get("categoria", ""))
                for p in d["palabras"]}
    except ImportError:
        import json
        d = json.loads((RAIZ / "korlin.json").read_text(encoding="utf-8"))
        return {str(p["forma"]).lower(): str(p.get("categoria", "")) for p in d["palabras"]}


def carga_afijos():
    try:
        import yaml
        d = yaml.safe_load((RAIZ / "data" / "afijos.yaml").read_text(encoding="utf-8"))
        return {str(a["forma"]).strip("-").lower() for a in d["afijos"]}
    except ImportError:
        return set()


def silabas_ok(w):
    """R0: la palabra se segmenta en silabas (C)V(C) con coda {m,n,s}.

    No basta con prohibir dos consonantes seguidas: una coda nasal seguida de
    un onset (`sen-to`, `pa-ran-sa`) es LEGAL. Hay que segmentar de verdad.
    """
    # introspeccion recursiva: (onset opcional)(vocal)(coda opcional) repetido
    def rec(i):
        if i == len(w):
            return True
        for onset in ("", *CONSONANTES):
            if not w.startswith(onset, i):
                continue
            j = i + len(onset)
            if j >= len(w) or w[j] not in VOCALES:
                continue
            j += 1                                    # vocal consumida
            if j < len(w) and w[j] in CODAS:          # coda opcional
                if rec(j + 1):
                    return True
            if rec(j):
                return True
        return False
    return rec(0)


def canonico(a, b, POS):
    """R5/R6: ¿'a b' es una construccion canonica de la lengua?"""
    ca, cb = POS.get(a, ""), POS.get(b, "")
    if a in ACTITUD and b in ACTITUD:
        return "R5 dos particulas finales"
    if "pronombre" in ca and "sust" in cb:
        return "R6 posesion"
    if a in DETERMINANTES and "sust" in cb:
        return "R6 determinante+nombre"
    if a in PREPOSICIONES and "sust" in cb:
        return "R6 preposicion+nombre"
    if a in COMPLEMENTANTES and ("pronombre" in cb or "sust" in cb):
        return "R6 complementante+oracion"
    if "sust" in ca and b == "na":
        return "R6 sujeto+negacion"
    if "verb" in ca and ("sust" in cb or "pronombre" in cb):
        return "R6 verbo+objeto"
    if "adj" in ca and "sust" in cb:
        return "R6 Adj-N"
    return None


def derivable(w, POS):
    """R3: ¿raiz + sufijo derivacional valida por la regla 17?"""
    for suf in ("pe", "lo", "re", "ro", "i", "s"):
        if len(w) > len(suf) + 1 and w.endswith(suf) and w[:-len(suf)] in POS:
            return "R3 %s+%s" % (w[:-len(suf)], suf)
    for pre in ("an", "ne", "na", "me", "pi"):
        if len(w) > len(pre) + 1 and w.startswith(pre) and w[len(pre):] in POS:
            return "R3 %s-+%s" % (pre, w[len(pre):])
    return None


def veredicto(w, POS, AFIJOS):
    """Devuelve (clase, motivo). `ACEPTADA` = pasa todas las reglas."""
    w = w.lower()
    if not silabas_ok(w):
        return "ACEPTADA" if False else ("R0", "rompe (C)V(C)")
    if w in AFIJOS:
        return "R1", "choca con un afijo"
    if w in POS:
        return "R4", "ya existe en el lexico"
    for i in range(1, len(w)):
        c = canonico(w[:i], w[i:], POS)
        if c:
            return c.split()[0], c
    d = derivable(w, POS)
    if d:
        return "R3", d
    return "ACEPTADA", ""


LOTE_EJEMPLO = [
    # (raiz, ES, EN, categoria)
    ("tapa", "trabajar", "work", "verbo"),
    ("kotu", "cerrar", "close", "verbo"),
    ("duka", "mar", "sea", "sustantivo"),
    ("halu", "mar", "sea", "sustantivo"),      # debe salir R6 verbo+objeto
    ("tra", "trabajar", "work", "verbo"),      # debe salir R0
    ("sui", "amarillo", "yellow", "color"),    # debe salir R4 (ya existe)
]


def main():
    POS = carga_lexico()
    AFIJOS = carga_afijos()
    print("lexico: %d formas | afijos: %d" % (len(POS), len(AFIJOS)))
    print()

    if "--archivo" in sys.argv:
        ruta = Path(sys.argv[sys.argv.index("--archivo") + 1])
        lote = []
        for ln in ruta.read_text(encoding="utf-8").splitlines():
            if not ln.strip() or ln.startswith("#"):
                continue
            partes = [x.strip() for x in ln.split("|")]
            lote.append(tuple(partes[:4]))
    else:
        lote = LOTE_EJEMPLO
        print("(lote de ejemplo; usa --archivo lote.txt para el tuyo)")
        print()

    ok, fallos = [], []
    print("%-8s %-12s %-10s %s" % ("raiz", "ES", "clase", "motivo"))
    for fila in lote:
        w, es = fila[0], (fila[1] if len(fila) > 1 else "")
        clase, motivo = veredicto(w, POS, AFIJOS)
        if clase == "ACEPTADA":
            ok.append(w)
        else:
            fallos.append((w, clase, motivo))
        print("%-8s %-12s %-10s %s" % (w, es[:12], clase, motivo))

    print()
    print("ACEPTADAS: %d/%d" % (len(ok), len(lote)))
    if fallos:
        print("RECHAZADAS:")
        for w, clase, motivo in fallos:
            print("   %-8s %s %s" % (w, clase, motivo))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
