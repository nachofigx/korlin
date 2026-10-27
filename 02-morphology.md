# 02 — Morphology

*[Español disponible en docs/manual-es.md]*

## 1. Attitude particles (attitudinals)

**Optional** particles marking the speaker's emotion/attitude.
Position: in the final chain, **after** epistemic modality and **before** `mo`
(`[modality] [attitude] [mo]`, rules 23–24).
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
- **One attitude** per sentence. Two attitudes do not chain (rule 24). For two
  nuances, one stays at the end and the other is expressed in the verb.
- One attitude may follow one modality: `li go-di ku bu.`
- **Usable alone**: `we!` = "wow!".

### Examples
- `le ti e-ve gu yo!` — "The day is good (I see it), I love it!"
- `we! le su e-ve hi.` — "Wow! The sun is high (I see it)."
- `mi go a le ho fi.` — "I go to the house (irony)." Irony marked with `fi` is
  one of the five evidential exemptions (rule 4).

### Anti-lying note
The particle `fi` (irony) explicitly marks the "playful lie" of sarcasm, separating
it from factual assertion. Thus irony does **not contaminate** the evidentiality
system: a joke is declared a joke.

## 2. Evidentiality (mandatory)

Evidentiality forces marking the **source** of information of every statement.
It is Korlin's "anti-lying" layer.

### Categories (4)
| Suffix | IPA | Category | Meaning | Derives from |
|---|---|---|---|---|
| `-ve` | /ve/ | Direct (DIR) | "I perceived it with my senses" | `ve` = see |
| `-pen` | /pen/ | Inferred (INF) | "I deduce it from evidence" | `pen` = think |
| `-di` | /di/ | Reported (REP) | "I was told" | `di` = say |
| `-sa` | /sa/ | General (GEN) | "general knowledge" | `sa` = know |

### Rules
1. **Mandatory**: every declarative sentence carries an evidential on its verb
   (or copula `e`). One cannot assert a fact without declaring its source.
2. **Position**: suffix immediately after the verb.
3. **Exemptions** — closed list of five (rule 4). Questions are not declaratives.
   The evidential is omitted only in:
   (a) **questions** (`mo`, or an interrogative at the start);
   (b) **orders** (bare root);
   (c) **irony marked with `fi`**;
   (d) the **protasis** of a conditional (`si …`);
   (e) **non-finite verbs in a chain** (the auxiliary carries the evidential;
   the supporting verb stays bare: `tu kan-ve ve mi` = "you can see me").
   It is NOT optional elsewhere.
   In subordinate clauses, **each finite clause carries its own** evidential:
   `mi sa-ve ki li an-go-di.` = "I know-DIR that he left-REP."
4. **No overlap.** Each suffix has one value. `-sa` is general knowledge, never
   a conjecture. A guess uses **`-pen` + modality `os`/`ku`**:
   `li ne-go-pen os` = "he may go (I infer it)". How sure the speaker is belongs
   to modality (section 3), not to the evidential.

### Examples
- `li go-ve.` — "He goes (I see it)."
- `li an-go-di.` — "He went (I was told)."
- `li go-pen.` — "He goes (I infer it)."
- `li go-sa.` — "He goes (it is general knowledge)."
- `le lu e-ve i le no.` — "The moon is in the night (I see it)."

### Anti-lying effect
Asserting "li go" without evidential is **ungrammatical**. The speaker MUST choose
a source; marking "I saw it" commits and exposes them. Lying requires an explicit,
traceable, refutable commitment.

## 3. Epistemic modality (degree of certainty)

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
1. **Optional.** With no final particle, modality is `to` (certain) **only** if
   the evidential is strong (`-ve`, `-di`, `-sa`). With `-pen`, the unmarked
   value is `be` (probable); with `-pen` and incomplete data, `os`. The explicit
   particle always wins (rule 23).
2. **Position**: end of the sentence, in the fixed chain
   `[verb+evidential] … [modality] [attitude] [mo]`.
3. **One modality.** Two modalities do not chain (rule 24). One modality may
   combine with one attitude, in that order.

| evidential \ explicit | (none) | `to` | `be` | `os` | `ku` |
|---|---|---|---|---|---|
| `-ve` (I saw it) | to | to | be | os | os |
| `-di` (I was told) | to | — | be | os | ku |
| `-sa` (general knowledge) | to | to | be | os | ku |
| `-pen` (I infer it) | be | to | be | os | ku |

(`—` = unused: if you were told, explicit certainty adds nothing.)

### Combining source × certainty (the anti-lying power)
- `li go-ve.` — "He left (I saw it)." — direct source, certainty by default
- `li go-di be.` — "He left (I was told), probably."
- `li go-pen os.` — "He left (I infer it), possibly."
- `li go-di ku.` — "He left (I was told), doubtful (I don't trust it)."
- `li go-di ku bu.` — "He left (I was told, doubtful) 😤."

## 4. Verb tense

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
- `wi ne-go-ve a le ho.` — "We will go to the house (we've decided)."

### Note: evidentiality in the future
In the future, the evidential marks the source of the *prediction* (§4.1):
`mi ne-go-ve` = "I'll go (I've decided)"; `li ne-go-pen` = "he'll go (I infer it,
or it is expected)". `-sa` is not a future and not a guess: it only marks
general knowledge.

## 5. Derivation (affixes)

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
3. `na-` never attaches to a verb (rule 7b), inflected or bare. `na-sa-ve` and
   `na-sa` are ungrammatical. Sentence negation is free `na`: `mi na sa-ve`.
   "An ignorant person" is `pe ki na sa-ve`, not `na-sa-pe`.

### Examples (the power of derivation)
- `sa` (know) → `sa-pe` sage · `sa-re` knowledge (na- NO va sobre verbos: regla 7b)
- `man` (eat) → `man-pe` diner · `man-re` food · `man-lo` dining room
- `do` (sleep) → `do-pe` sleeper · `do-lo` bedroom · `do-re` dream
- `gu` (good) → `gu-ro` goodness · `na-gu` bad · `me-gu` excellent
- `su` (sun) → `su-i` solar
- `ho` (house) → `pi-ho` cottage · `me-ho` mansion

### Note
With ~100 roots and these 8 affixes, Korlin generates a vocabulary of several
thousand words. Deriving is trivial and predictable.

## 6. Nominal plural

Number is a suffix **glued** to the noun, with no hyphen (rule 18).

| Allomorph | When | Example |
|---|---|---|
| `-s` | after a vowel | `pe` → `pes`, `li` → `lis` |
| `-es` | after a coda `m`, `n` or `s` | `nom` → `nomes`, `kin` → `kines`, `tem` → `temes` |

Never two codas in a row. After a numeral, plural `-s` is optional.
