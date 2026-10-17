# Korlin (Shortlang) 🗣️

**A short, honest, and modern constructed language** — a spiritual successor to
Dutton Speedwords and a better Esperanto.

## What is Korlin?

Korlin (/ˈkoɾlin/) is a constructed language ("conlang") designed to be:

- **Short** — words of 1–2 syllables condense concepts (~40% shorter than Esperanto, ~44% shorter than Spanish).
- **Honest** — mandatory *evidentiality*: every statement declares its source (I saw / I inferred / I was told / assumed). Lying becomes costly and detectable.
- **Modern** — digital-native (21 letters, zero diacritics), emoji-like attitude particles, and AI-ready (deterministic parsing, fewer tokens).

## Design principles

1. One letter = one sound, always (perfect phonemic orthography).
2. Most frequent words are shortest (information theory).
3. Few roots + regular affixes = thousands of words (derivation).
4. Zero exceptions. Zero ambiguity. Zero grammatical gender.
5. Mandatory evidentiality + optional epistemic modality + attitude particles.

## Repository structure

```
data/           ← single source of truth (lexicon + affixes, bilingual ES/EN)
scripts/        ← generators + rule-based translator + test suite
docs/           ← generated manuals (ES, EN, FR, ZH, JA, AI) + white papers
korlin-spec.md  ← self-contained spec pack, ready for any LLM's system prompt
korlin.json     ← machine-readable lexicon, affixes and rules
llms.txt        ← discovery file for AI agents
index.html      ← interactive website (dictionary, flashcards, translator)
learn.html      ← Duolingo-style learning app
```

## Use Korlin with an AI 🤖

No training needed. Two ways:

1. **Paste the spec.** Copy `korlin-spec.md` (~16 KB) into any LLM's system
   prompt and ask it to translate or chat in Korlin.
2. **Give it the tool.** Let the model call `scripts/traductor-korlin.py`; the
   code produces the Korlin, so it never invents a root word.

```bash
python scripts/traductor-korlin.py es "Yo como comida."     # → mi man-sa man-re.
python scripts/traductor-korlin.py en "He went home." --ev=ve
python scripts/traductor-korlin.py k "Mi man-ve man-re."    # → ES/EN
python scripts/test-traductor.py                            # run the test suite
```

See [`docs/ia-integracion.md`](docs/ia-integracion.md) for the full guide.

## Generate

```bash
uv venv .venv
uv pip install --python .venv/bin/python pyyaml
.venv/bin/python scripts/generar.py        # manuals in 5 languages + web data
.venv/bin/python scripts/generar_ia.py     # spec pack + JSON + llms.txt
.venv/bin/python scripts/generar_pdf.py    # white papers as PDF
```

One change in `data/` → regenerates every manual, the web data and the AI spec.

## Learn

- `docs/manual-es.md` — manual en español
- `docs/manual-en.md` — manual in English
- `docs/manual-ia.md` — manual for AI agents
- `docs/study-manual.md` — study manual (11 lessons)
- **Website:** https://nachofigx.github.io/korlin/
- **Learning app:** https://nachofigx.github.io/korlin/learn.html

## License

- **The language** (grammar + vocabulary) — Creative Commons **CC BY-SA 4.0**.
- **The code/software** — **MIT** (see LICENSE).

## Example

> **Na-toro na kan-sa vi i mi.**
> *The lie cannot live in me.*
> (`na-toro` = "lie" = `na-` not + `toro` truth)

---

## Español

Korlin (/ˈkoɾlin/) es una lengua construida diseñada para ser **corta, honesta y
moderna** — sucesora espiritual del Dutton Speedwords y un Esperanto mejorado.

- **Corta** — palabras de 1–2 sílabas condensan conceptos (~40% más corta que el Esperanto).
- **Honesta** — evidencialidad obligatoria: toda afirmación declara su fuente.
- **Moderna** — digital (21 letras, sin tildes), partículas de emoción tipo emoji, lista para IA.

Documentación en español: `docs/manual-es.md` y `manual-de-estudio.md`.

---

*Created by Ignacio, with Lingua (linguist AI).*
