# Korlin (Shortlang)

## Scientific White Paper — Design, research and rationale of a constructed language for the digital era

| | |
|---|---|
| **Version** | 1.1 |
| **Date** | September 27, 2026 |
| **Authorship** | Lingua (project linguist) · Ignacio (concept creator) |
| **Repository** | https://github.com/nachofigx/korlin |
| **License** | Language: CC BY-SA 4.0 · Code: MIT |
| **Status** | Living document — updated as the language evolves |

---

## Executive summary

Korlin (international exonym: *Shortlang*) is a constructed language (*conlang*) designed from scratch to solve a specific problem: **condensing the maximum information into the minimum number of characters, syllables and phonemes, without sacrificing pronounceability, regularity or epistemic honesty**.

The project stems from the observation that historical "spoken shorthand" systems exist — chiefly **Dutton Speedwords** (Dutton, 1943) — which achieved high information density but failed as speakable languages due to their irregularity, unpronounceability and technical obsolescence. Korlin positions itself as the **spiritual successor** of that tradition, taking approximately **30 % of its conceptual "DNA"** (condensation philosophy, short roots, one-letter function words) and contributing an original **70 %** (universally pronounceable phonology, total regularity, mandatory evidentiality, emoji particles and a digital-native, AI-oriented approach).

This document presents the **complete research** underpinning the design: the state of the art of condensing languages, the theoretical foundations (speech information rate, evidentiality, epistemic modality), the phonological, morphological, syntactic and lexical design, the quantitative length comparisons against natural and constructed languages, the analysis of Esperanto's historical failure, and the technical architecture of the project (single source of truth, automatic generation and open source).

**Main result:** on a reference technical text, Korlin produces **388 characters** versus 660 for Esperanto (−41 %), 690 for Spanish (−44 %) and 603 for English (−36 %), while maintaining a 20-phoneme, universally accessible phonology and an exception-free grammar.

---

## Keywords

constructed language · conlang · information condensation · evidentiality · epistemic modality · Dutton Speedwords · Esperanto · phonology · morphology · syntax · artificial intelligence · tokenization · language adoption

---

## Table of contents

1. Introduction
2. State of the art: constructed languages for condensing information
3. Theoretical foundations
4. Phonology
5. Morphology
6. Syntax
7. Lexicon and derivation
8. Writing and digital system
9. Length comparisons
10. Esperanto analysis and adoption strategy
11. Korlin and artificial intelligence
12. Project architecture (docs as code)
13. Conclusions
14. Future work
References
Appendix A — Complete vocabulary
Appendix B — Affixes
Appendix C — Sample text

---

## 1. Introduction

### 1.1 Motivation and origin of the idea

The question that originated the project was direct: **do languages exist that were created specifically to shorten words?** — something analogous to a *spoken shorthand*, but which also constituted a complete, functional language.

The underlying intuition is that human writing and speech contain significant redundancy that could be eliminated through deliberate design. If a language is built from scratch with the explicit goal of minimizing message length, it is theoretically possible to surpass any natural language in information density, since natural forms are the product of centuries of historical drift rather than optimization.

The direct inspiration was the **Dutton Speedwords** system, an international shorthand created by Reginald Dutton in the 1930s and 1940s, which used very short roots and one-letter grammatical words.

### 1.2 Objectives

The project's objectives, defined in its initial phase, are:

1. **Extreme condensation.** One- to two-syllable words that express complete concepts.
2. **Universal pronounceability.** Any speaker — European, Asian or African — can articulate it without difficulty.
3. **Total regularity.** Zero grammatical, orthographic or phonological exceptions.
4. **Epistemic honesty.** Mandatory evidentiality and certainty modality, making lying costly and detectable.
5. **Digital native.** No diacritics, emoji-compatible, designed for chat, mobile and AI agents.
6. **Future-proof for AI.** Fewer tokens per message, deterministic parsing and rule-based translation.

### 1.3 Scope and methodology

This white paper documents the complete research and design process. The methodology combined:

- **State-of-the-art review** of condensing constructed languages and linguistic evidentiality.
- **Typological analysis** of phonologies, morphologies and syntaxes of natural and constructed languages.
- **Quantitative measurement** of the length of identical texts translated into multiple languages.
- **Iterative design** with the concept creator, validating each decision against the objectives.

---

## 2. State of the art: constructed languages for condensing information

The idea of compressing language is not new. This chapter reviews the main historical attempts and their outcomes.

### 2.1 Speedtalk (Heinlein, 1949)

In the science-fiction novel *Gulf* (1949), Robert A. Heinlein imagined a hypothetical language called **Speedtalk**, in which each phoneme would represent a concept and phoneme combinations would build sentences with extreme information density. It is a purely literary concept: there is no complete grammar and it is not pronounceable by humans, but it established the cultural idea of "thinking and communicating at maximum speed".

### 2.2 Ithkuil (Quijada, 2004–2023)

**Ithkuil**, created by John Quijada, is the most radical attempt at **maximum morphological density**. A single Ithkuil word can encode what a natural language requires a whole sentence or even a paragraph to express. Its most famous example is *Tram-mļöi hhâsmařpţuktôx* ("On the contrary, I think it may turn out that this rugged mountain range trails off at some point…"). However, its morphophonological complexity is such that it is **practically impossible to speak spontaneously**. It is a theoretical limit, not a usable language.

### 2.3 aUI (Weilgart, 1979)

**aUI** ("the language of space"), by W. John Weilgart, attempts to build all semantics from **31 primitive morphemes** (a vowel or consonant represents a basic category such as "light", "life", "motion"). It is extremely compact, but its highly abstract nature makes it **unnatural and inaccessible** for human learning.

### 2.4 Sona (Searight, 1935)

**Sona**, by Kenneth Searight, uses about **360 monosyllabic radicals** that combine into compound words. It is an elegant system, more natural than aUI, but it remained **incomplete** and never achieved a community of speakers.

### 2.5 Toki Pona (Lang, 2001)

**Toki Pona**, by Sonja Lang, represents the opposite extreme: with barely **~120 words**, it seeks **semantic minimalism**. Its goal is not to condense information but to simplify thought by reducing vocabulary. A Toki Pona sentence is usually *longer* than in Spanish or English, because complex concepts must be decomposed into combinations of basic words. It is relevant here as a counterexample: **fewer words does not imply fewer characters**.

### 2.6 Dutton Speedwords (Dutton, 1943)

The system that directly inspired Korlin. Reginald Dutton designed **Dutton Speedwords** as an international shorthand based on the etymological root of words (mainly Latin and Germanic languages). Its key features:

- ~**493 short roots**.
- **One-letter grammatical words** (e.g. a single letter for "the", "of", "and").
- **Systematic derivational suffixes**.

Dutton achieved very high information density. However, it suffers from limitations that make it unviable as a modern spoken language:

- ❌ **Not pronounceable**: many words are bare consonants without a vowel, forcing arbitrary "ghost vowels".
- ❌ **Irregular**: it contains exceptions that contradict its own logic.
- ❌ **No technical vocabulary**: created before the digital era, it lacks terms for computing, internet or AI.
- ❌ **No evidentiality** or epistemic-honesty mechanisms.

### 2.7 Lojban (Logical Language Group, 1987)

**Lojban**, a descendant of Loglan, is a **logically unambiguous** language designed for human-machine interaction. Its grammar is a formal logical predicate. Although it is syntactically unequivocal, it is **not optimized for brevity** and its learning is considerably harder than a natural language. It is a precedent for the "AI-friendly" goal, but with a different approach from Korlin.

### 2.8 Comparative analysis

| Language | Density | Pronounceable | Regular | Modern | Speakable |
|---|---|---|---|---|---|
| Speedtalk | Very high | No | — | No | No |
| Ithkuil | Maximum | No | Yes | No | No |
| aUI | High | Partial | Yes | No | Hard |
| Sona | Medium | Yes | Partial | No | Incomplete |
| Toki Pona | Low | Yes | Yes | Yes | Yes |
| Dutton Speedwords | High | No | No | No | No |
| Lojban | Medium | Yes | Yes | Partial | Hard |
| **Korlin** | **High** | **Yes** | **Yes** | **Yes** | **Yes** |

**Conclusion:** the design space of a language that is simultaneously *short, pronounceable, regular, modern and speakable* was empty. Korlin fills it.

---

## 3. Theoretical foundations

### 3.1 Speech information rate (Pellegrino et al., 2011)

A central finding of contemporary psycholinguistics is that human languages transmit information at a nearly constant rate of **~39 bits per second** (Pellegrino, Coupé & Marsico, 2011).

The study measured two opposing magnitudes:

- The **information density per syllable** (how much information each syllable encodes).
- The **articulation rate** (how many syllables are pronounced per second).

The results show a systematic **compensation**: languages with very dense syllables (such as Mandarin) are spoken with fewer syllables per second, while languages with light syllables (such as Spanish or Japanese) are spoken with more syllables per second. The product of both magnitudes converges at ~39 bits/s.

**Implication for Korlin:** there is a human **cognitive bottleneck**, not a linguistic one, that limits the rate of *spoken* transmission. Korlin's advantage, therefore, lies not in "speaking faster" (impossible, due to the cognitive limit), but in **using fewer characters, fewer syllables and fewer tokens for the same message**. This is decisive in channels where the cognitive limit does not operate: **writing**, **digital transmission** and **tokenization** for language models.

### 3.2 Evidentiality and epistemic modality

**Evidentiality** is the grammatical category encoding the **source of information** of a statement. It is a well-documented phenomenon in linguistic typology.

| Language | Evidential system | Example |
|---|---|---|
| **Quechua** | Mandatory suffixes | `-mi` (direct), `-shi` (reported), `-chi` (inferred) |
| **Tariana** (Amazonia) | Mandatory evidentiality in every sentence | You cannot state "it rained" without saying *how you know* |
| **Tuyuca** (Amazonia) | Five evidential categories | Visual, non-visual, apparent, secondhand, assumed |

The key fact: **approximately 25 % of the world's languages mark source obligatorily** (Aikhenvald, 2004). Evidentiality is therefore not a Korlin artifice, but a natural feature that most European languages simply lost.

**Epistemic modality**, in turn, encodes the speaker's **degree of certainty** (certain, probable, possible, doubtful). It is distinct from evidentiality (which indicates *source*) and complementary to it (it indicates *confidence*).

### 3.3 Can you make "lying impossible"?

One of the project's original aspirations was to design a language where **lying would be structurally impossible**.

**Technical (honest) answer:** No. Lying is a **pragmatic intention** — deliberately saying something known to be false — not a property of grammatical structure. No grammar can prevent a speaker from knowingly articulating a false proposition.

**What is achievable** is making lying **costly, explicit and detectable**, through three combined mechanisms:

1. **Mandatory evidentiality** (`-ve` direct, `-pen` inferred, `-di` reported, `-sa` assumed): every statement must declare its source.
2. **Epistemic modality** (`to` certain, `be` probable, `os` possible, `ku` doubtful): every statement must declare its degree of certainty.
3. **Marked speech acts** (attitude particles, including `fi` for irony): communicative intention is made explicit.

With this system, a speaker who wishes to lie must **deliberately choose a false marker** (e.g. mark as "direct" something only known by hearsay). That choice leaves a grammatical trace that can be verified and refuted. Lying ceases to be "free" and becomes **accountable**.

---

## 4. Phonology

Korlin's phonology is designed to maximize **universal ease of pronunciation** and minimize interference with speakers' native languages.

### 4.1 Phoneme inventory (20 phonemes)

**Consonants (15):**

| Letter | IPA | Place/manner | Voicing | Approximate reference |
|---|---|---|---|---|
| p | /p/ | bilabial plosive | voiceless | "p" |
| b | /b/ | bilabial plosive | voiced | "b" |
| t | /t/ | alveolar plosive | voiceless | "t" |
| d | /d/ | alveolar plosive | voiced | "d" |
| k | /k/ | velar plosive | voiceless | "k" |
| g | /g/ | velar plosive | voiced | "g" |
| m | /m/ | bilabial nasal | voiced | "m" |
| n | /n/ | alveolar nasal | voiced | "n" |
| f | /f/ | labiodental fricative | voiceless | "f" |
| s | /s/ | alveolar fricative | voiceless | "s" |
| h | /h/ | glottal fricative | voiceless | "h" as in *house* |
| l | /l/ | alveolar lateral | voiced | "l" |
| r | /ɾ/ | alveolar tap | voiced | "r" as in Spanish *pero* |
| w | /w/ | labiovelar approximant | voiced | "w" as in *water* |
| y | /j/ | palatal approximant | voiced | "y" as in *yes* |

**Vowels (5):**

| Letter | IPA | Description |
|---|---|---|
| a | /a/ | open (central/low) |
| e | /e/ | close-mid front |
| i | /i/ | close front |
| o | /o/ | close-mid back |
| u | /u/ | close back |

**Sounds that DON'T exist in Korlin** (to avoid interference): /x/ (Spanish jota), /θ/, /ʃ/ ("sh"), /tʃ/ ("ch"), /v/, /z/, /ŋ/ ("ng"), /ʒ/.

### 4.2 Phonotactics (allowed syllables)

The syllable structure is **(C) V (C)**, where the consonantal coda may only be {m, n, s}.

Rules:

1. **Onset optional**: any consonant, or empty.
2. **Nucleus mandatory**: a single vowel.
3. **Coda optional**: only /m/, /n/ or /s/.
4. **No consonant clusters** ("pr", "st", "kt", etc. are forbidden).
5. **No diphthongs**: /j/ and /w/ are onset-only; each vowel forms its own syllable (e.g. "ai" is read /a.i/, two syllables).

Valid syllables: `a`, `e`, `ka`, `te`, `mi`, `so`, `lu`, `kan`, `sen`, `los`, `nam`, `sis`, `tan`, `wan`.
Invalid syllables: `stra` (cluster), `kri` (cluster), `ek` (coda /k/), `kast` (double coda).

**Total possible syllables** = 16 onsets × 5 vowels × 4 codas = **320 syllables**. Of these, the **75 CV syllables** (15 consonants × 5 vowels) form the basis of the pronunciation guide for students.

### 4.3 Stress

- Stress falls **always on the penultimate syllable**.
- Monosyllabic words carry no special stress.
- Being predictable, it is **never written** (no accent marks).

### 4.4 Orthography (official romanization)

- **1 letter = 1 phoneme, always.** No digraphs, no silent letters, no accents.
- Alphabet (20 letters, in order): `a b d e f g h i k l m n o p r s t u w y`.
- Unused Latin letters: `c, j, q, v, x, z` (redundant with other Korlin letters).

### 4.5 Typological justification

- The **5-vowel** system /a e i o u/ is the most common worldwide (Spanish, Italian, Japanese, Greek, Swahili, Hawaiian…).
- **No voicing contrast in fricatives** (only voiceless /f s h/): Spanish and Japanese also lack the /s/–/z/ pair, a simplification for maximal ease.
- **Tap /ɾ/** instead of trill /r/: /ɾ/ is typologically far more frequent and easy.
- All chosen consonants rank among the world's most frequent.
- 15 consonants + 5 vowels compares to Spanish (~18 C + 5 V), Italian (~21 C + 7 V) and Japanese (~14 C + 5 V): **simpler than most**.

The **neutral Spanish/Latin-style pronunciation** was deliberately chosen as the most accessible for the greatest number of speakers, avoiding difficult sounds (aspiration, tones, gutturals) that would hinder adoption by Asian and African speakers.

---

## 5. Morphology

### 5.1 Morphological type

Korlin is an **agglutinative-isolating** language: root words are short and invariable, and affixes are added regularly and transparently, without fusion (each affix keeps a single form and a single meaning). There is no gender inflection, no obligatory adjective agreement and no concordance.

### 5.2 Grammatical inflection

| Category | System | Example |
|---|---|---|
| Plural | suffix `-s` | `pe` (person) → `pes` (people) |
| Past | prefix `an-` (from *an* "old") | `go` (go) → `an-go` (went) |
| Future | prefix `ne-` (from *ne* "new") | `go` → `ne-go` (will go) |
| Present | unmarked | `go` = goes (present) |

### 5.3 Mandatory evidentiality

| Marker | Meaning | Example |
|---|---|---|
| `-ve` | direct (I saw/lived it) | `go-ve` = "goes (I see it)" |
| `-pen` | inferred (I deduce it) | `go-pen` = "goes (I infer it)" |
| `-di` | reported (I was told) | `go-di` = "goes (I was told)" |
| `-sa` | assumed (known by convention) | `go-sa` = "goes (it is assumed)" |

Evidentiality is **mandatory** in every declarative sentence: a fact cannot be asserted without declaring its source.

### 5.4 Epistemic modality

| Particle | Meaning |
|---|---|
| `to` | certain ✅ |
| `be` | probable 👍 |
| `os` | possible 🤔 |
| `ku` | doubtful ⚠️ |

### 5.5 Derivation (productive affixes)

| Affix | Function | Example |
|---|---|---|
| `-pe` | agent (person who X) | `sa` (know) → `sa-pe` (sage) |
| `-lo` | place (where X happens) | `man` (eat) → `man-lo` (dining room) |
| `-re` | thing/object | `man` → `man-re` (food) |
| `-i` | relational adjective | `su` (sun) → `su-i` (solar) |
| `-ro` | abstract (quality) | `gu` (good) → `gu-ro` (goodness) |
| `na-` | opposite/negative | `toro` (truth) → `na-toro` (lie) |
| `me-` | augmentative | `ho` (house) → `me-ho` (mansion) |
| `pi-` | diminutive | `ho` → `pi-ho` (little house) |

Derivation is the central mechanism of lexicon expansion: from a reduced core of roots, the affixes systematically generate new words without inflating the dictionary.

---

## 6. Syntax

### 6.1 Constituent order: SVO

Korlin uses **Subject–Verb–Object (SVO)** order, the most common and easiest worldwide (Spanish, English, Chinese…).

- `mi go a le ho.` — "I go to the house."
- Gloss: `mi` (I) `go` (go) `a` (to) `le` (the) `ho` (house).

### 6.2 Noun phrase: modifier before head

Adjectives and determiners come **before** the noun (as in English and Chinese).

- `le gu pe` = "the good person" (`le` the + `gu` good + `pe` person).
- `me ho` = "big house" (`me` big + `ho` house).

Canonical order: `[determiner] [adjective] [noun]`.

### 6.3 Prepositions

Prepositions come **before** the noun: `a` (to/towards), `i` (in), `de` (of/from), `kon` (with), `po` (for/by).

### 6.4 Negation

The particle `na` goes **before** the verb (or copula).

- `mi na sa.` — "I don't know."

### 6.5 Interrogation

- **Yes/no question**: particle `mo` at the end. `tu go mo?` = "Are you going?"
- **Interrogatives**: the question word (`ki pe` who, `ki lo` where, `ki tem` when…) goes **first**. `ki pe e i le ho?` = "Who is in the house?"

### 6.6 Subordination

`ki` introduces subordinate and relative clauses. **Each clause carries its own evidential** (each statement declares its source).

- `mi sa-ve ki li an-go-di.` — "I know that he left (I was told)."
- Gloss: `mi` I `sa-ve` know-DIRECT `ki` that `li` he `an-go-di` PAST-go-REPORTED.

### 6.7 Possession

With `de`: `le ho de mi` = "my house" (literally "the house of me").

### 6.8 Alignment

**Nominative-accusative without cases**: subject and object are distinguished by SVO order (subject before verb, object after). No case marking.

### 6.9 Final particle order

`[verb + evidential] … [epistemic modality] [attitude] [mo]`

- `li go-di ku bu.` — "He left (I was told, doubtful) 😤."

**Summary of syntactic rules:** (1) SVO order; (2) modifier before head; (3) preposition before noun; (4) negation `na` before verb; (5) `mo` at the end for yes/no, interrogatives first; (6) subordination with `ki` and evidential in each clause; (7) possession with `de`; (8) no cases; (9) final particles in fixed order.

---

## 7. Lexicon and derivation

### 7.1 Lexicon construction strategy

Korlin's lexicon is built on a **reduced core of monosyllabic and bisyllabic high-frequency roots**, expanded through derivational affixes (section 5.5) and compounding. This radical economy allows a functional vocabulary with a minimal number of forms.

The dictionary currently contains **143 core words**, organized by category and stored in `data/lexico.yaml` (single source of truth). The complete vocabulary, with IPA transcription, is reproduced in **Appendix A**.

### 7.2 Color economy

An example of the condensation philosophy: instead of independent roots for each color, Korlin defines only **3 primary colors** and derives the rest from existing roots:

| Color | Root | Origin |
|---|---|---|
| red | `ru` | own root |
| green | `gi` | own root |
| pink | `ro` | own root |
| white | `lum-i` | from `lum` (light) |
| black | `no-i` | from `no` (night) |
| yellow | `su-i` | from `su` (sun) |
| blue | `wa-i` | from `wa` (water) |
| brown | `ga-i` | from `ga` (earth) |
| purple | `lu-i` | from `lu` (moon) |
| grey | `som-i` | from `som` (shadow) |
| orange | `ru-su-i` | red-yellow (compound) |

### 7.3 Mathematics and SI prefixes

| Operation | Korlin | | Prefix | Value |
|---|---|---|---|---|
| add | `sum` (+) | | kilo | ×1000 |
| subtract | `min` (−) | | mega | ×10⁶ |
| multiply | `fan` (×) | | giga | ×10⁹ |
| divide | `fen` (÷) | | mili | ÷1000 |
| | | | miko | micro- |
| | | | nano | nano- |

### 7.4 Countries (adapted proper nouns)

`Mekiko` (Mexico) · `Espan` (Spain) · `Kina` (China) · `Frans` (France) · `Brasil` (Brazil) · `Yapan` (Japan). The gentilic is formed with `-i`.

### 7.5 Slang (initial mechanisms)

Korlin slang is built through productive mechanisms:

- **Reduplication**: `gu-gu` = "cool, awesome" (from `gu`, good).
- **Colloquial derivation**: `me-ku` = "no way" (from `me-` augmentative + `ku` doubtful).
- **Attitude particles** (section 8.2) for emotional tone.

---

## 8. Writing and digital system

### 8.1 Romanization

Korlin is written with the 20-letter Latin alphabet, without diacritics or digraphs. The romanization is biunique: **each letter corresponds to exactly one sound and vice versa**, eliminating all reading ambiguity.

### 8.2 Attitude particles → emojis

A key innovation, proposed by Ignacio: **two Korlin letters trigger the matching emoji** on the phone keyboard. Attitude particles are morphemes that express emotion and map directly to emojis:

| Particle | Emoji | Emotion |
|---|---|---|
| `yo` | ❤️ | joy |
| `we` | 😮 | surprise |
| `fi` | 🙃 | irony/sarcasm |
| `ri` | 😂 | laughter |
| `hu` | 😢 | sadness |
| `bu` | 😤 | anger |
| `la` | 🥰 | affection |
| `pu` | 🤢 | disgust |
| `ni` | 😨 | fear |

This makes Korlin a **digital-native** language: expressive, informal and perfect for chat and mobile communication.

### 8.3 AI compatibility

The biunique design (1 letter = 1 sound), the absence of diacritics and the exception-free grammar make Korlin **optimal for machine processing**: no orthographic ambiguity, deterministic parsing and minimal tokenization.

---

## 9. Length comparisons

### 9.1 Methodology

To quantify Korlin's condensation advantage, a reference technical text was translated into multiple languages and its length measured in **characters** (and, secondarily, in syllables and words). The reference text describes a Japanese architect and their volumetric-study tool, and includes technical terminology (plans, volumes, shadows, regulations, AI).

### 9.2 Results (long text)

| Language | Characters | Difference vs Korlin |
|---|---|---|
| **Korlin** | **388** | — |
| Dutton (style) | 338 | +15 % (Dutton shorter) |
| Japanese (romaji) | 565 | −31 % |
| English | 603 | −36 % |
| Chinese (pinyin) | 616 | −37 % |
| Esperanto | 660 | −41 % |
| Spanish | 690 | −44 % |
| French | 729 | −47 % |
| German | 759 | −49 % |

### 9.3 Results (short sentence)

Example sentence: **"The lie cannot live in me."**

| Language | Characters |
|---|---|
| Dutton (style) | 21 |
| **Korlin** | **26** |
| English | 26 |
| Esperanto | 31 |
| Spanish | 32 |
| German | 33 |
| Japanese (romaji) | 37 |
| French | 37 |
| Chinese (pinyin) | 38 |

### 9.4 Summary of savings

- **−44 %** characters vs Spanish.
- **−36 %** characters vs English.
- **−31 %** characters vs Japanese (romaji).
- **−41 %** characters and **−50 %** syllables vs Esperanto.
- **−49 %** characters vs German.

**Note on Dutton:** Dutton is 13 % shorter in raw terms, but that advantage is a **mirage**: it is not pronounceable (bare consonants and "ghost vowels"), it is irregular, and it lacks technical vocabulary and evidentiality. Korlin is the **functional** version of that idea.

---

## 10. Esperanto analysis and adoption strategy

### 10.1 Why Esperanto didn't conquer the world

Korlin positions itself as "Esperanto's competitor, 100 times better". To support this claim, we analyzed the causes of Esperanto's historical failure (Zamenhof, 1887) as a universal language:

| Problem | Detail |
|---|---|
| Rare diacritics | ĉ, ĝ, ĥ, ĵ, ŝ, ŭ — hard to type and write |
| Eurocentrism | Vocabulary and structure almost exclusively European |
| Accusative `-n` | A strange rule that confuses learners |
| Agreement | Adjectives and nouns must agree in case and number |
| Sexism | Feminine suffixes derived from the masculine |
| Awkward consonant clusters | `knabino`, `scii` |
| 19th-century design | Not built for internet, mobile or AI |

Korlin fixes **all** of these: no diacritics, no cases, no agreement, neutral, inclusive and digital-native.

### 10.2 Adoption strategy

The adoption direction defined for Korlin is: **rapid mass adoption, easy, attractive to youth, "super modern", with an idea of improvement**. The pillars are:

1. **Total ease** — regularity with no exceptions.
2. **Youth** — emojis, informal, digital.
3. **Modernity** — no diacritics, ready for chat and mobile.
4. **Honesty** — mandatory evidentiality (ethical differentiator).
5. **AI** — token efficiency and deterministic parsing.

### 10.3 Positioning metrics (real, verified)

- **~41 % shorter** than Esperanto (characters).
- **~44 % shorter** than Spanish.
- **~30 % of the conceptual "DNA"** from Dutton Speedwords.

---

## 11. Korlin and artificial intelligence

A central goal of the project is **using Korlin to communicate with AI agents**.

### 11.1 Advantages for AI

- **Fewer tokens** → shorter texts = lower processing cost per message.
- **Deterministic parsing** → 100 % regular grammar with no ambiguities.
- **Mandatory evidentiality** → the AI declares the source of its information (traceability).
- **Epistemic modality** → the AI declares its degree of certainty (better calibration).
- **Rule-based translation** Korlin ↔ Spanish/English (viable without machine learning).

### 11.2 Vision

The vision is a **rule-based translator** that lets humans and agents communicate in Korlin efficiently, reducing computational cost and increasing the epistemic transparency of AI responses.

---

## 12. Project architecture (docs as code)

### 12.1 Single source of truth

The project follows a **"docs as code"** architecture: all content (vocabulary, affixes, grammar) lives in YAML files acting as the single source of truth.

```
data/lexico.yaml        ← vocabulary (source of truth)
data/traducciones.yaml  ← fr/zh/ja translations
data/afijos.yaml        ← affixes
        ↓
scripts/generar.py      ← generator
        ↓
5 manuals (ES/EN/FR/ZH/JA) + AI manual + lexico.js
```

**A change in the source is automatically reflected in all languages and on the website.**

### 12.2 Documentation languages

- **English (primary)** — GitHub audience.
- **Spanish, French, Chinese and Japanese** — global reach.
- **AI manual** — so agents can learn Korlin.

### 12.3 Open source and governance

- **Public repository:** https://github.com/nachofigx/korlin
- **Licenses:** MIT (code) · CC BY-SA 4.0 (the language).
- **Evolution control:** Lingua is the maintainer; the community proposes via PR/issues.

### 12.4 Technical implementation details

- **Name:** Shortlang (exonym) / **Korlin** (endonym) /ˈkoɾlin/ = `ko` (short) + `lin` (language). We verified it didn't collide with relevant trademarks (there is a programming language called *Kotlin*, a low risk for a project of a different nature).
- **Text-to-speech (TTS):** configured with the neutral `es-MX-DaliaNeural` voice (neutral Spanish with seseo), compatible with Korlin phonology (only /s/, no /θ/).
- **Publication:** the repository was published on GitHub authenticating with a token stored in `~/.git-credentials` (without exposing credentials in commands).

---

## 13. Conclusions

1. The design space of a language that is **short, pronounceable, regular, modern and speakable** was empty; Korlin fills it, taking the best of Dutton Speedwords (condensation) and fixing its flaws.
2. Korlin's **condensation** is quantifiable: −44 % characters vs Spanish, −36 % vs English, −41 % vs Esperanto.
3. The real advantage is not "speaking faster" (limited by the ~39 bits/s cognitive bottleneck), but **using fewer characters, syllables and tokens** — decisive for writing and AI.
4. **"Making lying impossible"** is not grammatically achievable, but **mandatory evidentiality + epistemic modality + marked speech acts** make lying costly, explicit and detectable — a unique differentiator.
5. The **docs-as-code architecture** guarantees coherence across languages and supports the controlled evolution of the language.

---

## 14. Future work

| Component | Status |
|---|---|
| Phonology (20 phonemes) | ✅ Defined |
| Grammar and morphology | ✅ Defined |
| Lexicon (143 words) | ✅ Growing |
| Documentation in 5 languages + AI | ✅ |
| Open source on GitHub | ✅ Published |
| Interactive website (5 languages) | ✅ Live |
| CI/CD (automatic deployment) | ⬜ Pending |
| Real translator/parser for AI | ⬜ Pending |
| Community launch | ⬜ Pending |

---

## References

1. Aikhenvald, A. Y. (2004). *Evidentiality*. Oxford: Oxford University Press.
2. Pellegrino, F., Coupé, C., & Marsico, E. (2011). A cross-language perspective on speech information rate. *Language*, 87(3), 539–558.
3. Dutton, R. (1943). *Dutton Speedwords*. London: Dutton Publications.
4. Quijada, J. (2004). *Ithkuil: A Philosophical Design for a Hypothetical Language*.
5. Lang, S. (2014). *Toki Pona: The Language of Good*.
6. Searight, K. (1935). *Sona: An Auxiliary Neutral Language*.
7. Weilgart, W. J. (1979). *aUI: The Language of Space*.
8. Zamenhof, L. L. (1887). *Lingvo Internacia* (Esperanto).

---

## Appendix A — Complete vocabulary (143 words)

> Phonemic transcription in IPA between slashes. Categories as stored in `data/lexico.yaml`.

### A.1 Particles and function words

| Form | IPA | Category | Spanish | English |
|---|---|---|---|---|
| e | /e/ | particle | ser, estar | to be |
| a | /a/ | preposition | a, hacia | to, toward |
| i | /i/ | preposition | en, dentro | in, inside |
| o | /o/ | conjunction | o | or |
| u | /u/ | determiner | un, una, uno | a, an, one |
| ka | /ka/ | conjunction | y | and |
| ba | /ba/ | conjunction | pero | but |
| ki | /ki/ | conjunction | que, qué | that, which, what |
| si | /si/ | conjunction | si (conditional) | if |
| so | /so/ | conjunction | entonces, así que | then, so |
| na | /na/ | adverb | no (negation) | no, not |
| ya | /ya/ | adverb | sí | yes |
| de | /de/ | preposition | de | of, from |
| kon | /kon/ | preposition | con | with |
| po | /po/ | preposition | por, para | for, by |
| mo | /mo/ | particle | ¿? (yes/no question) | question particle |
| halo | /ˈhalo/ | greeting | hola | hello |

### A.2 Pronouns

| Form | IPA | Spanish | English |
|---|---|---|---|
| mi | /mi/ | yo | I, me |
| tu | /tu/ | tú | you |
| li | /li/ | él, ella | he, she |
| wi | /wi/ | nosotros | we |
| yu | /yu/ | vosotros, ustedes | you all |
| lis | /lis/ | ellos, ellas | they |

### A.3 Determiners

| Form | IPA | Spanish | English |
|---|---|---|---|
| le | /le/ | el, la | the |
| se | /se/ | este, esta | this |
| te | /te/ | ese, esa | that |
| ke | /ke/ | aquel, aquella | that (over there) |

### A.4 Verbs

| Form | IPA | Spanish | English |
|---|---|---|---|
| go | /go/ | ir | to go |
| ven | /ven/ | venir | to come |
| ve | /ve/ | ver | to see |
| di | /di/ | decir | to say |
| pa | /pa/ | hablar | to speak |
| fa | /fa/ | hacer | to do, make |
| ha | /ha/ | tener | to have |
| vo | /vo/ | querer | to want |
| kan | /kan/ | poder | can, to be able |
| mus | /mus/ | deber | must |
| sa | /sa/ | saber | to know |
| da | /da/ | dar | to give |
| ta | /ta/ | tomar | to take |
| pen | /pen/ | pensar | to think |
| sen | /sen/ | sentir | to feel |
| man | /man/ | comer | to eat |
| bi | /bi/ | beber | to drink |
| do | /do/ | dormir | to sleep |
| vi | /vi/ | vivir | to live |
| mu | /mu/ | morir | to die |

### A.5 Nouns

| Form | IPA | Spanish | English |
|---|---|---|---|
| pe | /pe/ | persona | person |
| re | /re/ | cosa, objeto | thing, object |
| wa | /wa/ | agua | water |
| fo | /fo/ | fuego | fire |
| ga | /ga/ | tierra | earth, land |
| su | /su/ | sol | sun |
| lu | /lu/ | luna | moon |
| jo | /jo/ | día | day |
| no | /no/ | noche | night |
| tem | /tem/ | tiempo | time |
| lo | /lo/ | lugar | place |
| ho | /ho/ | casa | house, home |
| ma | /ma/ | mano | hand |
| ye | /ye/ | ojo | eye |
| he | /he/ | cabeza | head |
| wo | /wo/ | palabra | word |
| nom | /nom/ | nombre | name |
| kin | /kin/ | máquina | machine |
| toro | /ˈtoɾo/ | verdad, certeza | truth, certainty |

### A.6 Adjectives

| Form | IPA | Spanish | English |
|---|---|---|---|
| gu | /gu/ | bueno | good |
| fe | /fe/ | malo | bad |
| me | /me/ | grande | big, great |
| pi | /pi/ | pequeño | small |
| ne | /ne/ | nuevo | new |
| an | /an/ | viejo | old |
| ra | /ra/ | rápido | fast |
| len | /len/ | lento | slow |
| hi | /hi/ | alto | high, tall |
| bo | /bo/ | bajo | low |
| tom | /tom/ | caliente | hot |
| ge | /ge/ | frío | cold |
| ko | /ko/ | corto, breve | short, brief |

### A.7 Technical

| Form | IPA | Spanish | English |
|---|---|---|---|
| ban | /ban/ | construir | to build |
| men | /men/ | medida, volumen | measure, volume |
| pis | /pis/ | piso, nivel | floor, level |
| ren | /ren/ | regla, ley | rule, law |
| som | /som/ | sombra | shadow |
| lum | /lum/ | luz | light |
| gan | /gan/ | proteger, guardar | to protect, guard |
| pon | /pon/ | poner, colocar | to put, place |
| num | /num/ | calcular, número | to calculate |
| sim | /sim/ | simular | to simulate |
| ken | /ken/ | comprar | to buy |
| plan | /plan/ | plano, diseño | plan, design |
| Yapan | /ˈjapan/ | Japón | Japan |

### A.8 Numbers

| Form | IPA | Value |
|---|---|---|
| u | /u/ | 1 |
| du | /du/ | 2 |
| san | /san/ | 3 |
| fu | /fu/ | 4 |
| sin | /sin/ | 5 |
| sis | /sis/ | 6 |
| sem | /sem/ | 7 |
| om | /om/ | 8 |
| nu | /nu/ | 9 |
| des | /des/ | 10 |

### A.9 Attitude particles (emoji)

| Form | IPA | Emotion |
|---|---|---|
| yo | /jo/ | joy ❤️ |
| hu | /hu/ | sadness 😢 |
| we | /we/ | surprise 😮 |
| fi | /fi/ | irony 🙃 |
| bu | /bu/ | anger 😤 |
| ri | /ri/ | laughter 😂 |
| pu | /pu/ | disgust 🤢 |
| ni | /ni/ | fear 😨 |
| la | /la/ | affection 🥰 |

### A.10 Epistemic modality

| Form | IPA | Certainty |
|---|---|---|
| to | /to/ | certain ✅ |
| be | /be/ | probable 👍 |
| os | /os/ | possible 🤔 |
| ku | /ku/ | doubtful ⚠️ |

### A.11 Colors

| Form | IPA | Spanish | English |
|---|---|---|---|
| ru | /ru/ | rojo | red |
| gi | /gi/ | verde | green |
| ro | /ro/ | rosa | pink |
| lumi | /ˈlumi/ | blanco (de "luz") | white |
| noi | /ˈno.i/ | negro (de "noche") | black |
| sui | /ˈsu.i/ | amarillo (de "sol") | yellow |
| wai | /ˈwa.i/ | azul (de "agua") | blue |
| gai | /ˈga.i/ | marrón (de "tierra") | brown |
| lui | /ˈlu.i/ | morado (de "luna") | purple |
| somi | /ˈso.mi/ | gris (de "sombra") | grey |
| ru-sui | /ruˈsu.i/ | naranja (rojo-amarillo) | orange |

### A.12 Mathematics and SI prefixes

| Form | IPA | Function |
|---|---|---|
| sum | /sum/ | add (+) |
| min | /min/ | subtract (−) |
| fan | /fan/ | multiply (×) |
| fen | /fen/ | divide (÷) |
| kilo | /ˈkilo/ | ×1000 |
| mega | /ˈmega/ | ×10⁶ |
| giga | /ˈgiga/ | ×10⁹ |
| mili | /ˈmili/ | ÷1000 |
| miko | /ˈmiko/ | micro- |
| nano | /ˈnano/ | nano- |

### A.13 Countries and slang

| Form | IPA | Spanish | English |
|---|---|---|---|
| Mekiko | /meˈkiko/ | México | Mexico |
| Espan | /eˈspan/ | España | Spain |
| Kina | /ˈkina/ | China | China |
| Frans | /frans/ | Francia | France |
| Brasil | /bɾaˈsil/ | Brasil | Brazil |
| gu-gu | /ˈgugu/ | guay (reduplication) | cool |
| me-ku | /ˈmeku/ | ni de broma | no way |

---

## Appendix B — Affixes

### B.1 Inflectional (grammatical)

| Affix | Type | Function | Example |
|---|---|---|---|
| -s | suffix | plural | `li → lis` (he → they) |
| an- | prefix | past | `an-go` = went |
| ne- | prefix | future | `ne-go` = will go |
| -ve | suffix | direct evidential | `go-ve` = goes (I see it) |
| -pen | suffix | inferred evidential | `go-pen` = goes (I infer it) |
| -di | suffix | reported evidential | `go-di` = goes (I was told) |
| -sa | suffix | assumed evidential | `go-sa` = goes (assumed) |

### B.2 Derivational

| Affix | Type | Function | Example |
|---|---|---|---|
| -pe | suffix | agent | `sa-pe` = sage |
| -lo | suffix | place | `man-lo` = dining room |
| -re | suffix | thing | `man-re` = food |
| -i | suffix | relational adjective | `su-i` = solar |
| -ro | suffix | abstract | `gu-ro` = goodness |
| na- | prefix | opposite/negative | `na-gu` = bad |
| me- | prefix | augmentative | `me-gu` = excellent |
| pi- | prefix | diminutive | `pi-ho` = little house |

---

## Appendix C — Sample text

Korlin's presentation text, with gloss and translation:

**Korlin:** `Halo! Mi e-sa Korlin. Mi e-sa u ko lin. Mi e-sa ra ka gu. Na-toro na-kan-sa vi i mi. Mi pa-ve kon pe ka kon kin. Tu kan-ve sa mi. Ven kon mi yo!`

**Gloss (morpheme by morpheme):**

| Segment | Analysis |
|---|---|
| Halo | hello |
| Mi e-sa Korlin | I be-ASSUMED Korlin → "I am Korlin" |
| Mi e-sa u ko lin | I be-ASSUMED a short language → "I am a short language" |
| Mi e-sa ra ka gu | I be-ASSUMED fast and good → "I am fast and good" |
| Na-toro na-kan-sa vi i mi | lie not-can-ASSUMED live in me → "the lie cannot live in me" |
| Mi pa-ve kon pe ka kon kin | I speak-DIRECT with person and with machine → "I speak with people and with machines" |
| Tu kan-ve sa mi | you can-DIRECT know me → "you can learn me" |
| Ven kon mi yo | come with me JOY → "come with me! ❤️" |

**Translation:** "Hello! I am Korlin. I am a short language. I am fast and good. The lie cannot live in me. I speak with people and with machines. You can learn me. Come with me! ❤️"

---

*Document generated from the complete research of the Korlin project. It is a living document and is updated as the language evolves.*
