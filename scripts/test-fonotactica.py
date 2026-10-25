#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test-fonotactica.py — Audita TODO el lexico contra la fonotactica declarada.

Comprueba, sobre data/lexico.yaml (o korlin.json):
  1. toda forma (sin guion) se segmenta en silabas `(C)V(C)` con coda {m,n,s};
  2. ninguna forma usa letras prohibidas (c, j, q, x, z);
  3. no hay duplicados de forma;
  4. los nombres propios y las marcas (mayuscula inicial en `es`) quedan EXENTOS
     por la regla C-10 (pueden violar la fonotactica; p.ej. `Korlin`).

Uso:  python3 scripts/test-fonotactica.py     (desde la raiz del repo)
"""
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONSONANTES = "pbtdkgmnfvshlrwy"      # 16; sin c, j, q, x, z
VOCALES = "aeiou"
CODAS = "mns"
PROHIBIDAS = set("cjqxz")


def carga():
    try:
        import yaml
        d = yaml.safe_load((RAIZ / "data" / "lexico.yaml").read_text(encoding="utf-8"))
        rev = {False: "no", True: "ya"}
        return [{"forma": str(rev.get(p["forma"], p["forma"])),
                 "es": str(p.get("es", "")),
                 "categoria": str(p.get("categoria", ""))} for p in d["palabras"]]
    except ImportError:
        d = json.loads((RAIZ / "korlin.json").read_text(encoding="utf-8"))
        return d["palabras"]


def silabas_ok(w):
    """(C)V(C) con coda {m,n,s}; coda nasal + onset es legal (`sen-to`)."""
    def rec(i):
        if i == len(w):
            return True
        for onset in ("", *CONSONANTES):
            if not w.startswith(onset, i):
                continue
            j = i + len(onset)
            if j >= len(w) or w[j] not in VOCALES:
                continue
            j += 1
            if j < len(w) and w[j] in CODAS:
                if rec(j + 1):
                    return True
            if rec(j):
                return True
        return False
    return rec(0)


def es_nombre_propio(entrada):
    """C-10: nombres propios y marcas (mayuscula inicial) quedan exentos."""
    forma = str(entrada["forma"])
    return bool(forma) and forma[0].isupper()


def main():
    palabras = carga()
    problemas = []
    vistos = {}
    exentos = 0

    for p in palabras:
        forma = str(p["forma"])
        fel = forma.lower()
        # duplicados
        if fel in vistos:
            problemas.append(f"DUPLICADO: {forma} (con {vistos[fel]})")
        vistos[fel] = p.get("es", "")

        if es_nombre_propio(p):
            exentos += 1
            continue                                    # C-10

        base = fel.replace("-", "")                     # derivados con guion
        if "-" not in fel and not silabas_ok(base):
            problemas.append(f"FONOTACTICA: {forma} no encaja en (C)V(C)")
        malas = PROHIBIDAS & set(base)
        if malas:
            problemas.append(f"LETRA PROHIBIDA: {forma} usa {sorted(malas)}")

    print(f"palabras: {len(palabras)} | exentas (C-10): {exentos}")
    if problemas:
        print(f"❌ {len(problemas)} problemas:")
        for x in problemas:
            print("   " + x)
        return 1
    print("✅ FONOTACTICA OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
