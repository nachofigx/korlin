# Korlin (Shortlang) 🗣️

**Korlin** /ˈkoɾlin/ is a constructed language ("conlang") designed to be
**short, honest, and modern** — a spiritual successor to Dutton Speedwords and
a better Esperanto.

*Korlin es una lengua construida diseñada para ser **corta, honesta y moderna** —
sucesora espiritual del Dutton Speedwords y un Esperanto mejorado.*

## ✨ What makes it special / Qué lo hace especial

- **Short / Corta** — words of 1–2 syllables condense concepts (~40% shorter than Esperanto, ~44% shorter than Spanish).
- **Honest / Honesta** — mandatory *evidentiality*: every statement declares its source (I saw / I inferred / I was told / assumed). Lying becomes costly and detectable.
- **Modern / Moderna** — digital-native (no diacritics, 20 letters), emoji-like attitude particles, and designed for AI (deterministic parsing, fewer tokens).

## 🧬 Design principles / Principios de diseño

1. One letter = one sound, always (perfect phonemic orthography).
2. Most frequent words are shortest (information theory).
3. Few roots + regular affixes = thousands of words (derivation).
4. Zero exceptions. Zero ambiguity. Zero gender.
5. Mandatory evidentiality + optional epistemic modality + attitude particles.

## 📁 Repository structure / Estructura

```
data/           ← single source of truth (lexicon + affixes, bilingual ES/EN)
scripts/        ← generator (produces everything from data/)
docs/           ← generated manuals (ES, EN, IA)
web/            ← web data (interactive site)
```

## 🚀 Generate / Generar

```bash
uv venv .venv
uv pip install --python .venv/bin/python pyyaml
.venv/bin/python scripts/generar.py
```

One change in `data/` → regenerates the ES/EN/IA manuals and web data
automatically. *Single source of truth.*

## 📖 Learn / Aprende

- `docs/manual-es.md` — manual en español
- `docs/manual-en.md` — manual in English
- `docs/manual-ia.md` — manual for AI agents
- `manual-de-estudio.md` — study manual (11 lessons)

## 📜 License / Licencia

- **The language** (grammar + vocabulary, in `data/` and `docs/`) — Creative Commons **CC BY-SA 4.0**.
- **The code/software** — **MIT** (see LICENSE).

## 🎯 Example / Ejemplo

> **Na-toro na-kan-sa vi i mi.**
> *The lie cannot live in me. / La mentira no puede vivir en mí.*
> (`na-toro` = "lie" = `na-` not + `toro` truth)

---

*Created by Ignacio, with Lingua (linguist AI).*
