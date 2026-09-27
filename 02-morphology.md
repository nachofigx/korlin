# 02 — Morphology

*[Español disponible en docs/manual-es.md]*

## 1. Attitude particles (attitudinals) — v0.1

**Optional** particles marking the speaker's emotion/attitude.
Position: **at the end of the sentence** (like the question particle `mo`).
Can also be used **alone** as an interjection.

| Particle | IPA | Emotion / attitude | Emoji |
|---|---|---|---|
| `yo` | /jo/ | joy, love, awesome! | ❤️ |
| `hu` | /hu/ | sadness, sorrow | 😢 |
| `we` | /we/ | surprise, wow! | 😮 |
| `fi` | /fi/ | irony, sarcasm | 🙃 |
| `bu` | /bu/ | anger, frustration | 😤 |
| `ri` | /ri/ | laughter, humor | 😂 |
| `pu` | /pu/ | disgust | 🤢 |
| `ni` | /ni/ | fear, worry | 😨 |
| `la` | /la/ | affection, tenderness | 🥰 |

### Rules
- **Optional** (unlike evidentiality, which is mandatory).
- Placed at the **end** of the sentence.
- **Combinable**: `yo la` = "I love it and it's tender".
- **Usable alone**: `we!` = "wow!".

### Examples
- `le jo e gu yo!` — "The day is good, I love it!"
- `we! le su e hi.` — "Wow! The sun is high."
- `mi go a le ho fi.` — "I go to the house (irony)."

### Anti-lying note
The particle `fi` (irony) explicitly marks the "playful lie" of sarcasm, separating
it from factual assertion. Thus irony does **not contaminate** the evidentiality
system: a joke is declared a joke.

## 2. Evidentiality (mandatory) — v0.1

Evidentiality forces marking the **source** of information of every statement.
It is Korlin's "anti-lying" layer.

### Categories (4)
| Suffix | IPA | Category | Meaning | Derives from |
|---|---|---|---|---|
| `-ve` | /ve/ | Direct (DIR) | "I perceived it with my senses" | `ve` = see |
| `-pen` | /pen/ | Inferred (INF) | "I deduce it from evidence" | `pen` = think |
| `-di` | /di/ | Reported (REP) | "I was told" | `di` = say |
| `-sa` | /sa/ | Assumed (ASU) | "known / assumed" | `sa` = know |

### Rules
1. **Mandatory**: every declarative sentence carries an evidential on its verb
   (or copula `e`). One cannot assert a fact without declaring its source.
2. **Position**: suffix immediately after the verb.
3. **Exemptions**: questions, orders and irony marked with `fi` carry no evidential.
4. **Hierarchy**: with several sources, mark the strongest
   (direct > inferred > reported > assumed; cf. Barnes 1984, Faller 2002).

### Examples
- `li go-ve.` — "He left (I saw it)."
- `li go-di.` — "He left (I was told)."
- `li go-pen.` — "He left (I infer it)."
- `li go-sa.` — "He left (it's assumed)."
- `le lu e-ve i le no.` — "The moon is in the night (I see it)."

### Anti-lying effect
Asserting "li go" without evidential is **ungrammatical**. The speaker MUST choose
a source; marking "I saw it" commits and exposes them. Lying requires an explicit,
traceable, refutable commitment.

## 3. Epistemic modality (degree of certainty) — v0.1

Epistemic modality marks **how certain** the speaker is of the statement.
It complements evidentiality: evidentiality says *how* you know (source);
modality says *how sure* you are (certainty).

### Categories (4)
| Particle | IPA | Degree | Equivalent |
|---|---|---|---|
| `to` | /to/ | Certain (I guarantee) | ✅ "for sure" |
| `be` | /be/ | Probable (I think so) | 👍 "pro**ba**bly" |
| `os` | /os/ | Possible (maybe) | 🤔 "p**os**sible" |
| `ku` | /ku/ | Doubtful (I don't trust it) | ⚠️ |

### Rules
1. **Optional**, default = `to` (certain). If no particle, certainty is implied.
2. **Position**: at the end of the sentence, after the verb with its evidential.
3. **Combinable** with evidentiality and attitude particles.
   Order: `[verb+evidential] … epistemic … attitude`.

### Combining source × certainty (the anti-lying power)
- `li go-ve.` — "He left (I saw it)." — direct source, certainty by default
- `li go-di be.` — "He left (I was told), probably."
- `li go-pen os.` — "He left (I infer it), possibly."
- `li go-di ku.` — "He left (I was told), doubtful (I don't trust it)."
- `li go-di ku bu.` — "He left (I was told, doubtful) 😤."

## 4. Verb tense — v0.1

Tense is marked with **prefixes** on the verbal root.
Present is unmarked.

### Categories (3)
| Prefix | IPA | Tense | Derives from |
|---|---|---|---|
| (none) | — | Present | — |
| `an-` | /an/ | Past | `an` = old |
| `ne-` | /ne/ | Future | `ne` = new |

### Rules
1. **Present** = bare root.
2. **Past** = prefix `an-` ("old" → past).
3. **Future** = prefix `ne-` ("new" → future).
4. **Order**: `[tense-] + root + [-evidential]`.
5. The mandatory evidential applies in all tenses.

### Examples
- `li go-ve.` — "He goes (I see it)."
- `li an-go-ve.` — "He went (I saw it)."
- `li ne-go-ve.` — "He will go (I'll see it)."
- `li an-vi-di.` — "He lived (I was told)."
- `wi ne-go a le ho.` — "We will go to the house."

### Note: evidentiality in the future
In the future, the evidential marks the source of the *prediction*: `ne-go-ve` = "I'll
go (by my plan/will)"; `ne-go-pen` = "I'll go (I infer)"; `ne-go-sa` = "I'll go (expected)".

## 5. Derivation (affixes) — v0.1

Derivation multiplies vocabulary: few roots + regular affixes = thousands of words
without extra memorization. This is Dutton's conciseness key, done cleanly.

### Derivational affixes (8)
| Affix | Type | Meaning | Derives from |
|---|---|---|---|
| `-pe` | suffix | agent (person who X) | `pe` = person |
| `-lo` | suffix | place (where X happens) | `lo` = place |
| `-re` | suffix | thing/object (derived noun) | `re` = thing |
| `-i` | suffix | relational adjective (relative to X) | — |
| `-ro` | suffix | abstract (quality of X) | — |
| `na-` | prefix | opposite/negative | `na` = no |
| `me-` | prefix | augmentative (big/very) | `me` = big |
| `pi-` | prefix | diminutive (small) | `pi` = small |

### Rules
1. Suffixes attach to the root; prefixes precede it.
2. One affix = one fixed meaning (no exceptions).
3. Combinable: `na-sa-pe` = "ignorant" (person who doesn't know).

### Examples (the power of derivation)
- `sa` (know) → `sa-pe` sage · `sa-re` knowledge · `na-sa` ignore
- `man` (eat) → `man-pe` diner · `man-re` food · `man-lo` dining room
- `do` (sleep) → `do-pe` sleeper · `do-lo` bedroom · `do-re` dream
- `gu` (good) → `gu-ro` goodness · `na-gu` bad · `me-gu` excellent
- `su` (sun) → `su-i` solar
- `ho` (house) → `pi-ho` cottage · `me-ho` mansion

### Note
With ~100 roots and these 8 affixes, Korlin generates a vocabulary of several
thousand words. Deriving is trivial and predictable.
