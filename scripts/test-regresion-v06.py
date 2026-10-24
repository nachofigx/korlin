#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test-regresion-v06.py — Bateria de REGRESION con IGUALDAD EXACTA (pide Korlin B4b).

Cubre C-05 (parche P1: copula, negacion, tildes, tiempo) y C-06 (ordenes,
numerales, posesion, subordinadas con una clausula por evidencial).

Decision C-01: ya NO hay -sa por defecto; los casos pasan --ev explicito
(o se exige -[?fuente] cuando no se pasa).

Uso:  python3 scripts/test-regresion-v06.py     (desde la raiz del repo)
"""
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent      # rutas absolutas desde RAIZ
TRAD = RAIZ / "scripts" / "traductor-korlin.py"

# (texto_es, evidencial, salida_exacta_esperada)
CASOS = [
    # --- C-05: copula, negacion, tildes, tiempo, plural ---
    ("El agua no es buena.",        "sa",  "le wa na e-sa gu."),
    ("Yo comí comida.",             "sa",  "mi an-man-sa man-re."),
    ("Yo iré a la casa.",           "sa",  "mi ne-go-sa a le ho."),
    ("Él come comida.",             "sa",  "li man-sa man-re."),
    ("Sí, yo quiero agua.",         "sa",  "ya, mi vo-sa wa."),
    ("Esta casa es grande.",        "sa",  "se ho e-sa me."),
    ("Unas casas grandes.",         "sa",  "u me hos."),
    ("Él duerme en la casa.",       "sa",  "li do-sa i le ho."),
    ("Pienso que él irá a la casa.", "sa", "pen-sa ki li ne-go-sa a le ho."),
    ("Yo sé.",                      "sa",  "mi sa-sa."),
    ("Yo veo la casa.",             "sa",  "mi ve-sa le ho."),
    ("México es grande.",           "sa",  "Mekiko e-sa me."),
    # --- C-06: ordenes (raiz desnuda, regla 13) ---
    ("¡Ve!",                        "sa",  "go!"),   # P1: regla 13, Go! = ¡ve!
    ("¡Ve mi!",                     "sa",  "ve mi!"),  # Ve mi! = ¡mírame!
    ("¡Mira!",                      "sa",  "ve!"),
    ("¡Come comida!",               "sa",  "man man-re!"),
    ("¡Ven conmigo!",               "sa",  "ven kon mi!"),
    # --- C-06: numerales (C-17) ---
    ("dos casas",                   "sa",  "du hos"),
    # --- C-06: subordinadas, una clausula por evidencial (C-26) ---
    ("Yo veo que él fue.",          "sa",  "mi ve-sa ki li an-go-sa."),
    ("Él dice que yo como.",        "sa",  "li di-sa ki mi man-sa."),
    # --- regla 15: protasis exenta ---
    ("Si vas, iré.",                "sa",  "si go, ne-go-sa."),
    # --- F2: futuro con --ev=pen (regla de la tabla C-02) ---
    ("Yo iré a la casa.",           "pen", "mi ne-go-pen a le ho."),
    ("Si vas, iré.",                "pen", "si go, ne-go-pen."),
    # --- F2: con --ev=ve ---
    ("El agua no es buena.",        "ve",  "le wa na e-ve gu."),
    ("Yo comí comida.",             "ve",  "mi an-man-ve man-re."),
    ("Él come comida.",             "ve",  "li man-ve man-re."),
    ("Sí, yo quiero agua.",         "ve",  "ya, mi vo-ve wa."),
    ("Esta casa es grande.",        "ve",  "se ho e-ve me."),
    ("Yo veo que él fue.",          "ve",  "mi ve-ve ki li an-go-ve."),
    # --- C-01: SIN --ev => marcador unico -[?fuente] (F1) ---
    ("Yo iré a la casa.",           None,  "mi ne-go-[?fuente] a le ho."),
    ("Yo sé.",                      None,  "mi sa-[?fuente]."),
    ("El agua no es buena.",        None,  "le wa na e-[?fuente] gu."),
]

fallos = 0
for texto, ev, esperado in CASOS:
    cmd = [sys.executable, str(TRAD), "es"]
    if ev:
        cmd.append("--ev=" + ev)
    cmd.append(texto)
    r = subprocess.run(cmd, capture_output=True, text=True)
    salida = r.stdout.strip()
    if salida == esperado:                       # IGUALDAD EXACTA (C-25)
        print(f"  ✓ [{ev or 'sin-ev':>6}] {texto!r}")
    else:
        fallos += 1
        print(f"  ✗ [{ev or 'sin-ev':>6}] {texto!r}")
        print(f"        esperado: {esperado!r}")
        print(f"        obtenido: {salida!r}")

print()
print(f"{'✅ REGRESION OK' if fallos == 0 else f'❌ {fallos} fallos'}"
      f" ({len(CASOS) - fallos}/{len(CASOS)})")
sys.exit(1 if fallos else 0)
