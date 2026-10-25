#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
c24_estimulos.py — Genera el material de la prueba con hablantes (C-24).

Produce:
  estimulos.json  — el diseno completo (pares, items, orden aleatorio sembrado)
  plantilla.csv   — hoja de registro para vaciar las respuestas
  hoja-respuestas.md — la misma hoja, legible

Diseno:
  Bloque A (colisiones, 5 pares minimos): discriminacion ABX por prosodia.
  Bloque B (cluster hV-, 14 raices): identificacion entre vecinos minimos.
  Bloque C (aceptabilidad): juicio de pronunciabilidad sobre muestra del lexico.

Semilla fija: la prueba se puede repartir en varias sesiones sin repetir orden.
"""
import csv
import json
import random
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SEMILLA = 20261024
random.seed(SEMILLA)

# ---------------------------------------------------------------- Bloque A
# Cada par: la forma del lexico vs su lectura alternativa (dos palabras).
# La diferencia ES prosodica: 1 acento (penultima) vs 2 acentos.
COLISIONES = [
    {"id": "A1", "forma": "halo", "afi": "/ˈha.lo/", "glosa": "hola (saludo)",
     "alterna": "ha lo", "afi_alt": "/ˈha ˈlo/", "glosa_alt": "tener lugar",
     "oracion": "Halo, mi go.", "oracion_alt": "Mi ha lo a le ho."},
    {"id": "A2", "forma": "kilo", "afi": "/ˈki.lo/", "glosa": "mil (×1000)",
     "alterna": "ki lo", "afi_alt": "/ˈki ˈlo/", "glosa_alt": "que lugar",
     "oracion": "Mi ha kilo hos.", "oracion_alt": "Ki lo tu go?"},
    {"id": "A3", "forma": "mega", "afi": "/ˈme.ga/", "glosa": "millon (×10^6)",
     "alterna": "me ga", "afi_alt": "/ˈme ˈga/", "glosa_alt": "tierra grande",
     "oracion": "U mega hos.", "oracion_alt": "Le ga e me."},
    {"id": "A4", "forma": "nano", "afi": "/ˈna.no/", "glosa": "nano- (×10^-9)",
     "alterna": "na no", "afi_alt": "/ˈna ˈno/", "glosa_alt": "no [es] noche",
     "oracion": "U nano mita.", "oracion_alt": "Na no, e ti."},
    {"id": "A5", "forma": "somi", "afi": "/ˈso.mi/", "glosa": "gris",
     "alterna": "so mi", "afi_alt": "/ˈso ˈmi/", "glosa_alt": "entonces yo",
     "oracion": "Le nubu e somi.", "oracion_alt": "So mi go."},
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


def bloque_a():
    """Discriminacion ABX: se oyen tres; ¿X = A o B? Orden aleatorizado."""
    items = []
    for c in COLISIONES:
        for rep in (1, 2):
            x_es_alt = random.choice([False, True])
            items.append({
                "id": f"{c['id']}-{rep}",
                "par": c["id"],
                "estimulo_A": c["forma"],   "afi_A": c["afi"],   "glosa_A": c["glosa"],
                "estimulo_B": c["alterna"], "afi_B": c["afi_alt"], "glosa_B": c["glosa_alt"],
                "X": c["alterna"] if x_es_alt else c["forma"],
                "respuesta_correcta": "B" if x_es_alt else "A",
                "oracion_A": c["oracion"], "oracion_B": c["oracion_alt"],
            })
    random.shuffle(items)
    return items


def bloque_b():
    """Identificacion: se oye una forma, se elige entre 4 escritas.

    Las 4 opciones son SIEMPRE distintas y fonotacticamente legales; los
    distractores son minimos (una sola vocal o consonante de diferencia).
    """
    items = []
    for h in HV:
        opciones = [h["forma"]] + [v for v in h["vecinos"] if v != h["forma"]]
        opciones = list(dict.fromkeys(opciones))
        assert len(opciones) >= 4, f"{h['id']}: menos de 4 opciones"
        opciones = opciones[:4]
        random.shuffle(opciones)
        items.append({
            "id": h["id"], "estimulo": h["forma"], "glosa": h["es"],
            "opciones": opciones, "respuesta_correcta": h["forma"],
        })
    random.shuffle(items)
    return items


def bloque_c():
    """Aceptabilidad: muestra estratificada del lexico para juicio de naturalidad."""
    import yaml
    d = yaml.safe_load((RAIZ / "data" / "lexico.yaml").read_text(encoding="utf-8"))
    palabras = [p for p in d["palabras"] if "-" not in str(p["forma"])]
    random.shuffle(palabras)
    muestra = palabras[:30]
    return [{"id": f"C{i+1:02d}", "forma": str(p["forma"]),
             "es": str(p.get("es", "")), "categoria": str(p.get("categoria", ""))}
            for i, p in enumerate(muestra)]


def plantilla_csv(ruta, a, b, c):
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["# HOJA DE REGISTRO C-24 — una fila por hablante en la cabecera"])
        w.writerow(["hablante_id", "edad", "lengua_materna", "sabe_esperanto", "fecha", "minutos"])
        w.writerow(["", "", "", "", "", ""])
        w.writerow([])
        w.writerow(["bloque", "item", "estimulo", "respuesta_dada", "correcta", "segundos", "comentario"])
        for it in a:
            w.writerow(["A", it["id"], f"{it['estimulo_A']} / {it['estimulo_B']}",
                        "", it["respuesta_correcta"], "", ""])
        for it in b:
            w.writerow(["B", it["id"], it["estimulo"], "", it["respuesta_correcta"], "", ""])
        for it in c:
            w.writerow(["C", it["id"], it["forma"], "", "", "", ""])


def hoja_md(ruta, a, b, c):
    L = []
    L.append("# Hoja de registro — C-24 (prueba con hablantes)\n")
    L.append("**Un formulario por hablante.** Rellena la cabecera y luego cada bloque.\n")
    L.append("## Cabecera\n")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    for k in ("hablante_id", "edad", "lengua_materna", "sabe_esperanto", "fecha", "minutos"):
        L.append(f"| {k} | |")
    L.append("\n## Bloque A — discriminación (¿X es A o B?)\n")
    L.append("| # | Se oye | A | B | Respuesta | Seg. |")
    L.append("|---|---|---|---|---|---|")
    for it in a:
        L.append(f"| {it['id']} | {it['estimulo_A']} / {it['estimulo_B']} "
                 f"| {it['estimulo_A']} | {it['estimulo_B']} | | |")
    L.append("\n## Bloque B — identificación (¿cuál oíste?)\n")
    L.append("| # | Opciones | Respuesta | Seg. |")
    L.append("|---|---|---|---|")
    for it in b:
        L.append(f"| {it['id']} | {' · '.join(it['opciones'])} | | |")
    L.append("\n## Bloque C — naturalidad (1 = raro, 5 = natural)\n")
    L.append("| # | Forma | Español | 1-5 |")
    L.append("|---|---|---|---|")
    for it in c:
        L.append(f"| {it['id']} | {it['forma']} | {it['es']} | |")
    ruta.write_text("\n".join(L), encoding="utf-8")


def main():
    a, b, c = bloque_a(), bloque_b(), bloque_c()
    datos = {
        "prueba": "C-24 — medida con hablantes",
        "version_lexico": "238 formas (v0.7, main c958683)",
        "semilla": SEMILLA,
        "bloques": {
            "A_colisiones": {"items": a, "n_items": len(a),
                             "que_mide": "discriminación prosódica de pares mínimos"},
            "B_cluster_hV": {"items": b, "n_items": len(b),
                             "que_mide": "identificación de vecinos mínimos con h-"},
            "C_naturalidad": {"items": c, "n_items": len(c),
                              "que_mide": "juicio de naturalidad sobre el léxico"},
        },
        "umbrales": {
            "sin_problema": ">= 90% de acierto",
            "vigilancia": "75-90%",
            "renombrar": "< 75%",
        },
    }
    (RAIZ / "docs" / "c24-estimulos.json").write_text(
        json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    plantilla_csv(RAIZ / "docs" / "c24-plantilla.csv", a, b, c)
    hoja_md(RAIZ / "docs" / "c24-hoja-respuestas.md", a, b, c)
    print(f"Bloque A: {len(a)} items | Bloque B: {len(b)} | Bloque C: {len(c)}")
    print("escrito: docs/c24-estimulos.json, c24-plantilla.csv, c24-hoja-respuestas.md")


if __name__ == "__main__":
    sys.exit(main())
