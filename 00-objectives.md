# 00 — Objectives and scope

*[Español disponible en docs/manual-es.md]*

## Purpose
A constructed language ("conlang") that is **"elegant and short but speakable"**:
- **Condenses concepts** into few sounds (inherited from Dutton Speedwords).
- **Easy to pronounce** for speakers of the world's major languages.
- **Future-proof for AI**: minimal ambiguity, 1:1 phonemic orthography,
  regular composable morphology → fewer tokens and deterministic parsing.

## Direct inspiration
**Dutton Speedwords** (Reginald J. G. Dutton, 1922–1951):
- Most frequent words = shortest (information theory).
- Roots of 1–3 letters; ~493 base roots.
- One-letter derivational affixes.
- Verb tense via prefixes (`y-` past, `r-` future).

## Dutton's flaws we avoid
1. Irregular orthography/pronunciation → here **1 letter = 1 sound, always**.
2. Vague, unpredictable affixes → here **each affix has ONE fixed meaning**.
3. Opaque compounds (ky+luf = "picnic") → here **transparent, regular composition**.

## Design principles
1. Concise but speakable (1–2 syllable roots; medium-high density, not extreme).
2. Easy, universal phonology ("neutral-international" system).
3. Perfect phonemic orthography (1 letter = 1 sound, no digraphs, no silent letters).
4. Frequency = brevity (most used is shortest).
5. Compositional derivation (few roots + fixed-meaning affixes).
6. Unambiguous syntax (fixed order + clear marking, machine-parseable).
7. Latin alphabet (max token efficiency, typeable).

## Language type (provisional)
Agglutinative/analytic, tending isolating: short invariable words combined with
regular affixes. Constituent order defined in stage 03.

## Truthfulness: anti-lying (added objective)
Request: make a structure where *lying is impossible*.

**Technical answer:** grammatically impossible (lying is intention/pragmatics, not
form). **But achievable:** make lying *costly, explicit and detectable* via three
mechanisms:
1. **Mandatory evidentiality** — every statement marks its source
   (direct / inferred / reported / assumed), like Quechua, Tariana and Tuyuca.
2. **Epistemic modality** — degree of certainty (certain / probable / possible / doubtful).
3. **Zero ambiguity** — each sentence has a single interpretation (cf. Lojban).

Reference: ~25% of the world's languages mandatorily mark information source
(Aikhenvald 2004). Evidentiality marks the *source*, not the *truth*: a speaker can
lie about the source, but doing so commits and exposes them.

For AI: statements with source + certainty = traceable, verifiable, cross-checkable
(contradiction detection), though not "unfalsifiable".

## Mass adoption and modernity (added objective)
The language must be adopted quickly by the masses, be easy, attractive to young
people, and "super modern".

Resulting principles:
- **Learnability**: total regularity (zero exceptions), minimal grammar,
  mnemonic vocabulary, few roots + composition.
- **Youth appeal**: attitude/emotion particles, informal register by default,
  no politeness hierarchies, creativity/neologisms, humor.
- **Modern/digital**: typeable, no diacritics, emoji/hashtag compatible,
  gender neutrality, AI-ready.

## Emoji-mapping and AI communication (added ideas)

**Emoji-mapping (2 letters → emoji):** Korlin's attitude and modality particles
(all 2 letters) each map to an emoji. Typing them on a phone keyboard
(text shortcuts/expansions) "attracts" the corresponding emoji.
E.g. `yo` → ❤️, `we` → 😮, `fi` → 🙃. Digital-native to the extreme.

**Communication with AI agents:** once learned, Korlin serves to talk to AI agents.
Advantages: fewer tokens (shorter/cheaper prompts), unambiguous syntax (deterministic
parsing), evidentiality + modality (sourced, certain information). Realistic path:
a deterministic Korlin ↔ Spanish translator (feasible due to total regularity),
without fine-tuning.
