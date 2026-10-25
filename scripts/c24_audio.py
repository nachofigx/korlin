#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
c24_audio.py — Genera y VERIFICA los audios del Bloque A (pares minimos).

Dos problemas del instrumento, medidos, no supuestos:

1. PISO DE SILENCIO. `edge-tts` rellena toda locucion corta hasta ~1.872 s:
   `halo` y `ha lo` salian con duracion IDENTICA y el par minimo no se podia
   distinguir en el archivo. Se resuelve con FRASE PORTADORA (el estimulo va
   en medio); asi la duracion si varia.

2. LA /h/ ES MUDA EN ESPANOL. En `es-MX-DaliaNeural` el audio de `halo` y de
   `alo` es identico (misma duracion de voz y mismo RMS): la h no se pronuncia.
   Verificado que en en-US, de-DE, pt-BR e it-IT SI se pronuncia.
   CONSECUENCIA: con la voz es-MX, el audio NO puede medir la oposicion
   /h/ vs cero. Si puede medir (a) la PROSODIA de los pares del Bloque A y
   (b) el esqueleto vocalico/consonantico del Bloque B. Se documenta y se
   resuelve el bloque B tambien en ESCRITO.

Uso:  python3 scripts/c24_audio.py            genera + verifica
      python3 scripts/c24_audio.py --lista     solo lista
      python3 scripts/c24_audio.py --verifica  solo verifica lo ya generado
"""
import asyncio
import hashlib
import json
import math
import struct
import subprocess
import sys
import wave
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "docs" / "c24-audio"
VOZ = "es-MX-DaliaNeural"          # voz del proyecto
PORTADORA = "mi sa-ve {} a ti"     # el estimulo va en medio
UMBRAL_DIF = 0.06                  # s: por debajo, los estimulos son el mismo audio


def carga():
    return json.loads((RAIZ / "docs" / "c24-estimulos.json").read_text(encoding="utf-8"))


def tareas():
    """[(nombre, texto_a_decir)] — un audio por estimulo, con frase portadora."""
    d = carga()
    vistos, t = set(), []
    for it in d["bloques"]["A_colisiones"]["items"]:
        for cual, clave in (("A", "estimulo_A"), ("B", "estimulo_B")):
            nombre = f"{it['par']}-{cual}.mp3"
            if nombre in vistos:
                continue
            vistos.add(nombre)
            t.append((nombre, PORTADORA.format(it[clave])))
    return t


def voz_util(mp3):
    """(duracion_de_voz_sin_silencio, rms) — mide SOLO el tramo con voz."""
    wav = mp3.with_suffix(".wav")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), str(wav)], check=True)
    w = wave.open(str(wav))
    n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
    xs = struct.unpack(f"<{n*ch}h", w.readframes(n))
    w.close()
    ws = int(sr * 0.01)                      # ventanas de 10 ms
    env = [math.sqrt(sum(x * x for x in xs[i:i + ws]) / ws)
           for i in range(0, len(xs) - ws, ws)]
    mx = max(env) or 1
    idx = [i for i, e in enumerate(env) if e / mx > 0.08]
    if not idx:
        return 0.0, 0.0
    seg = xs[idx[0] * ws:(idx[-1] + 1) * ws]
    return len(seg) / sr, math.sqrt(sum(x * x for x in seg) / len(seg))


async def genera(t):
    import edge_tts
    SALIDA.mkdir(parents=True, exist_ok=True)
    for nombre, texto in t:
        await edge_tts.Communicate(texto, VOZ).save(str(SALIDA / nombre))
    print(f"  {len(t)} audios generados con la voz {VOZ}")


def verifica():
    """Comprueba que A y B de cada par NO son el mismo audio."""
    d = carga()
    pares = {it["par"]: (it["estimulo_A"], it["estimulo_B"])
             for it in d["bloques"]["A_colisiones"]["items"]}
    print("\n  par   A / B                    dur_A    dur_B    veredicto")
    fallos = []
    for par, (fa, fb) in sorted(pares.items()):
        a, b = SALIDA / f"{par}-A.mp3", SALIDA / f"{par}-B.mp3"
        if not (a.exists() and b.exists()):
            fallos.append(f"{par}: falta un audio")
            continue
        da, ra = voz_util(a)
        db, rb = voz_util(b)
        dif = abs(da - db)
        ok = dif >= UMBRAL_DIF
        print(f"  {par:5} {fa+' / '+fb:24} {da:.3f}s  {db:.3f}s  "
              f"{'OK (distinguibles)' if ok else 'IGUALES -> par no medible'}")
        if not ok:
            fallos.append(f"{par}: A y B duran casi lo mismo ({da:.3f} vs {db:.3f})")
    return fallos


def main():
    t = tareas()
    if "--lista" in sys.argv:
        for n, x in t:
            print(f"  {n:12} «{x}»")
        return 0
    if "--verifica" not in sys.argv:
        print(f"{len(t)} audios, voz {VOZ}")
        asyncio.run(genera(t))
    print("\n== VERIFICACION: ¿los pares minimos son audibles? ==")
    fallos = verifica()
    print()
    if fallos:
        print(f"❌ {len(fallos)} problemas:")
        for f in fallos:
            print("   " + f)
        return 1
    print("✅ los 5 pares son auditivamente distinguibles (prosodia)")
    print("   NOTA: la /h/ es muda en esta voz; ver docstring del modulo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
