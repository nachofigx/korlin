# 01 — Phonology

*[Español disponible en docs/manual-es.md]*

## 1. Phoneme inventory (21 total)

### 1.1 Consonants (16)

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
| v | /v/ | labiodental fricative | voiced | "v" (English *van*) |
| s | /s/ | alveolar fricative | voiceless | "s" |
| h | /h/ | glottal fricative | voiceless | "h" as in *house* |
| l | /l/ | alveolar lateral | voiced | "l" |
| r | /ɾ/ | alveolar tap | voiced | "r" as in Spanish *pero* |
| w | /w/ | labiovelar approximant | voiced | "w" as in *water* |
| y | /j/ | palatal approximant | voiced | "y" as in *yes* |

### 1.2 Vowels (5)

| Letter | IPA | Description |
|---|---|---|
| a | /a/ | open (central/low) |
| e | /e/ | close-mid front |
| i | /i/ | close front |
| o | /o/ | close-mid back |
| u | /u/ | close back |

### 1.3 Sounds that DON'T exist (avoid interference)
- No /x/ (Spanish jota), /θ/, /ʃ/ ("sh"), /tʃ/ ("ch"), /v/, /z/, /ŋ/ ("ng"), /ʒ/.
- **h** is always [h] (as in *house*); never silent.
- **r** is always [ɾ] (tap); never [r] trill nor English [ɹ].
- **y** is always consonant /j/ (semivowel); never a vowel.
- **w** is always /w/; never /v/ nor /b/.

## 2. Phonotactics (allowed syllables)

Syllable structure: **(C) V (C)**, where coda C may only be {m, n, s}.

Rules:
1. **Onset** optional: any consonant, or empty.
2. **Nucleus** mandatory: a single vowel.
3. **Coda** optional: only /m/, /n/ or /s/.
4. **No consonant clusters** (no "pr", "st", "kt", etc.).
5. **No diphthongs**: /j/ and /w/ are onset-only; each vowel is its own syllable
   (e.g. "ai" is read /a.i/, two syllables).

Valid: `a`, `e`, `ka`, `te`, `mi`, `so`, `lu`, `kan`, `sen`, `los`, `nam`, `sis`, `tan`, `wan`.
Invalid: `stra` (cluster), `kri` (cluster), `ek` (coda /k/), `kast` (double coda).

**Possible syllables** = 17 onsets (16 consonants + empty) × 5 vowels × 4 codas = **340**.

**Documented exception (C-10).** Proper names and brand names (initial capital) may
keep orthography that violates `(C)V{m,n,s}`: an illegal coda **or a consonant
cluster**. The language autonym and brand is **Korlin**: `-rl-` is a consonant
cluster the common lexicon does not admit, and it is kept. Same family as
Mekiko, Faransa, Yapan, Barasila (PR-26). The coda rule for the common lexicon
does not change.

## 3. Stress
- One phonological word (root + affixes, or root + root in a compound) carries
  **exactly one** accent, on its **penultimate syllable**.
- A free monosyllable is always stressed.
- `me-ho` (one word, one accent: /ˈme.ho/) ≠ `me ho` (two words, two accents:
  /ˈme ˈho/); `do-lo` → /ˈdo.lo/, `ru-sui` → /ruˈsu.i/. Compound segments do
  **not** keep an accent of their own.
- Predictable → **never written** (no accent marks).

## 4. Orthography (official romanization)
- **1 letter = 1 phoneme, always.** No digraphs, no silent letters, no accents.
- Alphabet (21 letters, in order):
  `a b d e f g h i k l m n o p r s t u v w y`
- Unused Latin letters: c, j, q, x, z.

**Inventario consonántico (16):** `p b t d k g m n f s h l r w y v`.
`v` y `y` son fonemas plenos (`v` = /v/ labiodental, `y` = /j/ palatal); `j` no
existe como letra: su sonido /j/ se escribe siempre `y`.

## 5. Typological notes
- 5-vowel system /a e i o u/: the most common worldwide (Spanish, Italian,
  Japanese, Greek, Swahili, Hawaiian…).
- No voicing contrast in fricatives: only voiceless /f s h/ plus a single voiced
  /v/ (kept because it is extremely frequent in the world's languages).
- Tap /ɾ/ instead of trill /r/: /ɾ/ is typologically far more frequent.
- All chosen consonants rank among the world's most frequent.
- 16 consonants + 5 vowels compares to Spanish (~18 C + 5 V), Italian (~21 C + 7 V)
  and Japanese (~14 C + 5 V); simpler than most.
