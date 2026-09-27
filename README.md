# Korlin (Shortlang) 🗣️

**A short, honest, and modern constructed language** — a spiritual successor to
Dutton Speedwords and a better Esperanto.

## What is Korlin?

Korlin (/ˈkoɾlin/) is a constructed language ("conlang") designed to be:

- **Short** — words of 1–2 syllables condense concepts (~40% shorter than Esperanto, ~44% shorter than Spanish).
- **Honest** — mandatory *evidentiality*: every statement declares its source (I saw / I inferred / I was told / assumed). Lying becomes costly and detectable.
- **Modern** — digital-native (20 letters, zero diacritics), emoji-like attitude particles, and AI-ready (deterministic parsing, fewer tokens).

## Design principles

1. One letter = one sound, always (perfect phonemic orthography).
2. Most frequent words are shortest (information theory).
3. Few roots + regular affixes = thousands of words (derivation).
4. Zero exceptions. Zero ambiguity. Zero grammatical gender.
5. Mandatory evidentiality + optional epistemic modality + attitude particles.

## Repository structure

```
data/           ← single source of truth (lexicon + affixes, bilingual ES/EN)
scripts/        ← generator (produces everything from data/)
docs/           ← generated manuals (ES, EN, IA)
web/            ← web data (interactive site)
```

## Generate

```bash
uv venv .venv
uv pip install --python .venv/bin/python pyyaml
.venv/bin/python scripts/generar.py
```

One change in `data/` → regenerates the ES/EN/IA manuals and web data automatically.

## Learn

- `docs/manual-es.md` — manual en español
- `docs/manual-en.md` — manual in English
- `docs/manual-ia.md` — manual for AI agents
- `manual-de-estudio.md` — study manual (11 lessons)

## License

- **The language** (grammar + vocabulary) — Creative Commons **CC BY-SA 4.0**.
- **The code/software** — **MIT** (see LICENSE).

## Example

> **Na-toro na-kan-sa vi i mi.**
> *The lie cannot live in me.*
> (`na-toro` = "lie" = `na-` not + `toro` truth)

---

## Español

Korlin (/ˈkoɾlin/) es una lengua construida diseñada para ser **corta, honesta y
moderna** — sucesora espiritual del Dutton Speedwords y un Esperanto mejorado.

- **Corta** — palabras de 1–2 sílabas condensan conceptos (~40% más corta que el Esperanto).
- **Honesta** — evidencialidad obligatoria: toda afirmación declara su fuente.
- **Moderna** — digital (20 letras, sin tildes), partículas de emoción tipo emoji, lista para IA.

Documentación en español: `docs/manual-es.md` y `manual-de-estudio.md`.

---

*Created by Ignacio, with Lingua (linguist AI).*
