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
    ("Na-toro na-kan-sa vi i mi.", "mentira"),
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
    check(texto, m.otro_a_korlin(texto, LEX, "es"), esperados)

print("\n== EN → Korlin ==")
for texto, esperados in CASOS_EN:
    check(texto, m.otro_a_korlin(texto, LEX, "en"), esperados)

print(f"\n{'✅ TODO OK' if fallos == 0 else f'❌ {fallos} fallos'}")
sys.exit(1 if fallos else 0)
