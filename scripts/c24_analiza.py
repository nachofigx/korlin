#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
c24_analiza.py — Analiza los resultados de la prueba con hablantes (C-24).

Entrada: el CSV de registro (docs/c24-plantilla.csv rellenado).
Salida:  informe con los umbrales ya aplicados y el veredicto por par.

Los umbrales estan fijados en el protocolo ANTES de medir:
  >= 90% de acierto  -> sin problema
  75-90%             -> vigilancia
  < 75% en un par    -> renombrar ESE par (uno a uno)
  Bloque C: forma con <= 2 en >= 60% de hablantes -> candidata a renombrar
Minimo para renombrar: 3 hablantes coincidiendo en el mismo par.

Uso:  python3 scripts/c24_analiza.py docs/c24-plantilla.csv
      python3 scripts/c24_analiza.py --demo      (corre con datos sinteticos)
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
UMBRAL_OK, UMBRAL_VIG, MIN_COINCIDENCIA = 90.0, 75.0, 3


def lee_csv(ruta):
    """Devuelve (hablantes, respuestas). Tolerante al formato de la plantilla."""
    hablantes, respuestas = [], []
    with open(ruta, newline="", encoding="utf-8") as f:
        filas = list(csv.reader(f))
    cab = next((i for i, r in enumerate(filas) if r and r[0] == "hablante_id"), None)
    if cab is None:
        raise SystemExit("no encuentro la cabecera 'hablante_id'")
    if cab + 1 < len(filas) and len(filas[cab + 1]) >= 6:
        h = filas[cab + 1]
        hablantes.append({"id": h[0] or "H1", "edad": h[1], "lengua": h[2],
                          "esperanto": h[3], "fecha": h[4], "minutos": h[5]})
    for r in filas:
        if len(r) >= 5 and r[0] in ("A", "B", "C") and r[1]:
            respuestas.append({"bloque": r[0], "item": r[1], "estimulo": r[2],
                               "dado": r[3].strip().upper() if r[0] == "A" else r[3].strip(),
                               "correcta": r[4].strip().upper() if r[0] == "A" else r[4].strip(),
                               "segundos": r[5] if len(r) > 5 else "",
                               "comentario": r[6] if len(r) > 6 else ""})
    return hablantes, respuestas


def analiza(respuestas, diseno):
    out = {"A": {}, "B": {}, "C": {}}
    # ---- A y B: por item, acierto
    for bloque in ("A", "B"):
        # Bloque A: la unidad de decision es el PAR (A1, A2...), no el item suelto
        # (A1-1 y A1-2 son el mismo par medido dos veces).
        agg = defaultdict(lambda: [0, 0])
        errores = defaultdict(lambda: defaultdict(int))
        for r in respuestas:
            if r["bloque"] != bloque or not r["dado"]:
                continue
            clave = r["item"].split("-")[0] if bloque == "A" else r["item"]
            agg[clave][1] += 1
            if r["dado"] == r["correcta"]:
                agg[clave][0] += 1
            else:
                errores[clave][r["dado"]] += 1
        out[bloque] = {k: {"aciertos": v[0], "total": v[1],
                           "pct": round(100.0 * v[0] / v[1], 1) if v[1] else 0.0,
                           "errores": dict(errores[k])}
                       for k, v in sorted(agg.items())}
    # ---- C: naturalidad
    notas = defaultdict(list)
    for r in respuestas:
        if r["bloque"] != "C" or not r["dado"]:
            continue
        try:
            notas[r["item"]].append(float(str(r["dado"]).replace(",", ".")))
        except ValueError:
            pass
    out["C"] = {k: {"n": len(v), "media": round(sum(v) / len(v), 2),
                    "bajos": sum(1 for x in v if x <= 2),
                    "pct_bajos": round(100.0 * sum(1 for x in v if x <= 2) / len(v), 1)}
                for k, v in sorted(notas.items())}
    # Desglose descriptivo. No cambia el veredicto, que sigue siendo por par.
    mapa = {i["id"]: i for i in diseno["bloques"]["A_colisiones"]["items"]}
    cond = defaultdict(lambda: [0, 0])
    for r in respuestas:
        if r["bloque"] != "A" or not r["dado"]:
            continue
        clave = mapa.get(r["item"], {}).get("condicion", "?")
        cond[clave][1] += 1
        if r["dado"] == r["correcta"]:
            cond[clave][0] += 1
    out["A_condicion"] = {k: {"aciertos": v[0], "total": v[1],
                              "pct": round(100.0 * v[0] / v[1], 1) if v[1] else 0.0}
                          for k, v in sorted(cond.items())}
    return out


def veredicto(analisis, diseno):
    """Aplica los umbrales fijados en el protocolo."""
    problemas, vigilancia = [], []
    mapa_A = {i["id"]: i for i in diseno["bloques"]["A_colisiones"]["items"]}
    mapa_B = {i["id"]: i for i in diseno["bloques"]["B_cluster_hV"]["items"]}

    for bloque, mapa in (("A", mapa_A), ("B", mapa_B)):
        for item, v in analisis[bloque].items():
            if v["total"] < MIN_COINCIDENCIA:
                continue
            d = mapa.get(item, {})
            etq = d.get("par") or d.get("estimulo") or item
            if v["pct"] < UMBRAL_VIG:
                problemas.append(f"{bloque}/{etq}: {v['pct']}% -> RENOMBRAR "
                                 f"(errores hacia {v['errores'] or 'varios'})")
            elif v["pct"] < UMBRAL_OK:
                vigilancia.append(f"{bloque}/{etq}: {v['pct']}% -> vigilar")

    for item, v in analisis["C"].items():
        if v["n"] >= MIN_COINCIDENCIA and v["pct_bajos"] >= 60.0:
            problemas.append(f"C/{item}: {v['pct_bajos']}% le pone <=2 "
                             f"(media {v['media']}) -> candidata a renombrar")
    return problemas, vigilancia


def demo(diseño, n_hablantes=10):
    """Datos sinteticos de N hablantes: demuestra que el analisis discrimina.

    Se inyectan dos fallos conocidos para comprobar que el analizador los ve:
      - el par A3 va al 50% (debe disparar RENOMBRAR)
      - la forma C03 recibe <=2 de casi todos (debe salir como candidata)
    El resto acierta siempre. Si el informe señala otra cosa, el analizador
    no sirve. (Un 95% con N chico cae en vigilancia por azar; aqui no.)
    """
    import random
    random.seed(7)
    filas = []
    for h in range(n_hablantes):
        for bloque, key, corr in (("A", "A_colisiones", "respuesta_correcta"),
                                  ("B", "B_cluster_hV", "respuesta_correcta")):
            for it in diseño["bloques"][key]["items"]:
                malo = bloque == "A" and it["id"].startswith("A3")
                p = 0.50 if malo else 1.0
                alterna = "X"
                if malo and "estimulo_B" in it:
                    alterna = it["estimulo_B"]
                dado = it[corr] if random.random() < p else alterna
                filas.append({"bloque": bloque, "item": it["id"], "estimulo": "",
                              "dado": dado, "correcta": it[corr],
                              "segundos": "", "comentario": ""})
        for it in diseño["bloques"]["C_naturalidad"]["items"]:
            if it["id"] == "C03":
                nota = random.choice([1, 2, 2, 2])
            else:
                nota = random.choice([3, 4, 4, 5])
            filas.append({"bloque": "C", "item": it["id"], "estimulo": it["forma"],
                          "dado": str(nota), "correcta": "",
                          "segundos": "", "comentario": ""})
    return filas


def main():
    diseno = json.loads((RAIZ / "docs" / "c24-estimulos.json").read_text(encoding="utf-8"))
    if "--demo" in sys.argv:
        respuesta = demo(diseno)
        print("== MODO DEMO (datos sinteticos) ==")
    else:
        ruta = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "docs" / "c24-plantilla.csv"
        if not ruta.exists():
            raise SystemExit(f"no existe {ruta}")
        _, respuesta = lee_csv(ruta)
        if not any(r["dado"] for r in respuesta):
            print("La hoja esta VACIA: rellenala primero (columna 'respuesta_dada').")
            print("Para ver el analisis funcionando: python3 scripts/c24_analiza.py --demo")
            return 0

    an = analiza(respuesta, diseno)
    print("\n== Bloque A — colisiones ==")
    for k, v in an["A"].items():
        print(f"  {k:7} {v['pct']:5.1f}%  ({v['aciertos']}/{v['total']})")
    if an.get("A_condicion"):
        print("\n== Bloque A — por condicion (descriptivo; el umbral sigue siendo el par) ==")
        for k, v in an["A_condicion"].items():
            print(f"  {k:10} {v['pct']:5.1f}%  ({v['aciertos']}/{v['total']})")
    print("\n== Bloque B — racimo hV- ==")
    for k, v in an["B"].items():
        print(f"  {k:7} {v['pct']:5.1f}%  ({v['aciertos']}/{v['total']})")
    print("\n== Bloque C — naturalidad (las 5 mas bajas) ==")
    for k, v in sorted(an["C"].items(), key=lambda x: x[1]["media"])[:5]:
        print(f"  {k:7} media={v['media']}  <=2 en {v['pct_bajos']}% ({v['bajos']}/{v['n']})")

    problemas, vigilancia = veredicto(an, diseno)
    print()
    if problemas:
        print(f"❌ {len(problemas)} requieren accion:")
        for p in problemas:
            print("   " + p)
    if vigilancia:
        print(f"⚠ {len(vigilancia)} en vigilancia:")
        for v in vigilancia:
            print("   " + v)
    if not problemas and not vigilancia:
        print("✅ sin problemas: no se toca el lexico")
    return 0


if __name__ == "__main__":
    sys.exit(main())
