#!/usr/bin/env python3
"""
Generador de documentación de Korlin (multi-idioma: es, en, fr, zh, ja).

Lee la fuente de verdad única (data/lexico.yaml, data/afijos.yaml,
data/traducciones.yaml) y genera manuales en 5 idiomas + manual IA + datos web.
"""

import json
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def cargar(nombre: str) -> dict:
    with open(ROOT / "data" / nombre, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Metadatos por idioma
# ---------------------------------------------------------------------------
IDIOMAS = {
    "es": {"titulo": "Manual de Korlin (español)", "tagline": "**Korlin** (/ˈkoɾlin/) es una lengua construida *corta, honesta y moderna*."},
    "en": {"titulo": "Korlin Manual (English)", "tagline": "**Korlin** (/ˈkoɾlin/) is a constructed language: *short, honest and modern*."},
    "fr": {"titulo": "Manuel de Korlin (français)", "tagline": "**Korlin** (/ˈkoɾlin/) est une langue construite *courte, honnête et moderne*."},
    "zh": {"titulo": "Korlin 手册（中文）", "tagline": "**Korlin**（/ˈkoɾlin/）是一种*简短、诚实、现代*的人造语言。"},
    "ja": {"titulo": "Korlin マニュアル（日本語）", "tagline": "**Korlin**（/ˈkoɾlin/）は*短く、誠実で、現代的*な人工言語です。"},
}


# ---------------------------------------------------------------------------
# Pronunciación por idioma
# ---------------------------------------------------------------------------
PRONUNCIACION = {
    "es": """## Pronunciación

20 sonidos, 20 letras. **Una letra = un sonido, siempre.**

| Letra | AFI | Como en español |
|---|---|---|
| a | /a/ | c**a**sa |
| e | /e/ | m**e**sa |
| i | /i/ | s**í** |
| o | /o/ | n**o** |
| u | /u/ | t**ú** |
| p | /p/ | **p**an |
| b | /b/ | **b**ar |
| t | /t/ | **t**an |
| d | /d/ | **d**ar |
| k | /k/ | **c**asa |
| g | /g/ | **g**ato |
| m | /m/ | **m**ano |
| n | /n/ | **n**o |
| f | /f/ | **f**e |
| s | /s/ | **s**ol |
| h | /h/ | **h**ouse (inglesa) |
| l | /l/ | **l**uz |
| r | /ɾ/ | pe**r**o (suave) |
| w | /w/ | **w**ater (inglesa) |
| y | /j/ | **y**o |

**Reglas de oro**: vocales puras · p/t/k sin soplo · r suave · s siempre [s] · h siempre sonora.""",
    "en": """## Pronunciation

20 sounds, 20 letters. **One letter = one sound, always.**

| Letter | IPA | Like in English |
|---|---|---|
| a | /a/ | f**a**ther |
| e | /e/ | b**e**d |
| i | /i/ | s**ee** |
| o | /o/ | g**o** (pure) |
| u | /u/ | f**oo**d |
| p | /p/ | s**p**in (no puff) |
| b | /b/ | **b**ed |
| t | /t/ | s**t**op (no puff) |
| d | /d/ | **d**og |
| k | /k/ | s**k**ip (no puff) |
| g | /g/ | **g**o |
| m | /m/ | **m**an |
| n | /n/ | **n**o |
| f | /f/ | **f**an |
| s | /s/ | **s**ee |
| h | /h/ | **h**ouse |
| l | /l/ | **l**ow |
| r | /ɾ/ | Spanish "pe**r**o" |
| w | /w/ | **w**ater |
| y | /j/ | **y**es |

**Golden rules**: pure vowels · no aspiration · r tapped · s always /s/ · h voiced.""",
    "fr": """## Prononciation

20 sons, 20 lettres. **Une lettre = un son, toujours.**

| Lettre | API | Comme en français |
|---|---|---|
| a | /a/ | p**a**tte |
| e | /e/ | bl**é** |
| i | /i/ | s**i** |
| o | /o/ | m**o**t |
| u | /u/ | f**ou** |
| p | /p/ | **p**as (sans souffle) |
| b | /b/ | **b**as |
| t | /t/ | **t**as (sans souffle) |
| d | /d/ | **d**as |
| k | /k/ | **k**as (sans souffle) |
| g | /g/ | **g**are |
| m | /m/ | **m**ain |
| n | /n/ | **n**on |
| f | /f/ | **f**ou |
| s | /s/ | **s**ol (jamais [z]) |
| h | /h/ | **h**ouse (anglais) |
| l | /l/ | **l**ait |
| r | /ɾ/ | «r» de pe**r**o (espagnol) |
| w | /w/ | **w**att |
| y | /j/ | **y**eux |

**Règles d'or** : voyelles pures · pas d'aspiration · r battu · s toujours [s] · h sonore.""",
    "zh": """## 发音

20 个音，20 个字母。**一个字母 = 一个音，永远如此。**

| 字母 | 国际音标 | 近似发音（中文） |
|---|---|---|
| a | /a/ | 啊 |
| e | /e/ | 诶 |
| i | /i/ | 衣 |
| o | /o/ | 哦 |
| u | /u/ | 乌 |
| p | /p/ | 巴（不送气） |
| b | /b/ | 吧（浊音） |
| t | /t/ | 达（不送气） |
| d | /d/ | 大（浊音） |
| k | /k/ | 嘎（不送气） |
| g | /g/ | 嘎（浊音） |
| m | /m/ | 妈 |
| n | /n/ | 拿 |
| f | /f/ | 发 |
| s | /s/ | 撒 |
| h | /h/ | 哈（声门音） |
| l | /l/ | 拉 |
| r | /ɾ/ | 闪音（如日语「ら」） |
| w | /w/ | 哇 |
| y | /j/ | 呀 |

**黄金法则**：元音纯正 · p/t/k 不送气 · r 为闪音 · s 始终 [s] · h 始终有声。""",
    "ja": """## 発音

20 の音、20 の文字。**一文字 = 一音、常に。**

| 文字 | IPA | 日本語の近似 |
|---|---|---|
| a | /a/ | あ |
| e | /e/ | え |
| i | /i/ | い |
| o | /o/ | お |
| u | /u/ | う |
| p | /p/ | ぱ（気音なし） |
| b | /b/ | ば |
| t | /t/ | た（気音なし） |
| d | /d/ | だ |
| k | /k/ | か（気音なし） |
| g | /g/ | が |
| m | /m/ | ま |
| n | /n/ | な |
| f | /f/ | ふぁ |
| s | /s/ | さ |
| h | /h/ | は |
| l | /l/ | ら（舌端音） |
| r | /ɾ/ | ら（はじき音） |
| w | /w/ | わ |
| y | /j/ | や |

**黄金律**：純粋な母音 · 気音なし · r ははじき音 · s は常に [s] · h は常に有声音。""",
}


# ---------------------------------------------------------------------------
# Gramática por idioma
# ---------------------------------------------------------------------------
GRAMATICA = {
    "es": """## Gramática esencial

- **Orden**: Sujeto-Verbo-Objeto (SVO). `mi go a le ho` = "voy a la casa".
- **Modificador antes del núcleo**: `me ho` = "casa grande".
- **Plural**: sufijo `-s`. `li` → `lis`.
- **Tiempos**: `an-` (pasado), `ne-` (futuro); presente sin marca.
- **Evidencialidad (obligatoria)**: `-ve` (directo), `-pen` (inferido), `-di` (reportado), `-sa` (asumido).
- **Modalidad epistémica**: `to` (cierto), `be` (probable), `os` (posible), `ku` (dudoso).
- **Negación**: `na` antes del verbo.
- **Pregunta sí/no**: `mo` al final.
- **Posesión**: `de`. **Subordinación**: `ki`.""",
    "en": """## Essential grammar

- **Order**: Subject-Verb-Object (SVO). `mi go a le ho` = "I go to the house".
- **Modifier before head**: `me ho` = "big house".
- **Plural**: suffix `-s`. `li` → `lis`.
- **Tense**: `an-` (past), `ne-` (future); present unmarked.
- **Evidentiality (mandatory)**: `-ve` (direct), `-pen` (inferred), `-di` (reported), `-sa` (assumed).
- **Epistemic modality**: `to` (certain), `be` (probable), `os` (possible), `ku` (doubtful).
- **Negation**: `na` before the verb.
- **Yes/no question**: `mo` at the end.
- **Possession**: `de`. **Subordination**: `ki`.""",
    "fr": """## Grammaire essentielle

- **Ordre** : Sujet-Verbe-Objet (SVO). `mi go a le ho` = « je vais à la maison ».
- **Modificateur avant le noyau** : `me ho` = « grande maison ».
- **Pluriel** : suffixe `-s`. `li` → `lis`.
- **Temps** : `an-` (passé), `ne-` (futur) ; présent non marqué.
- **Évidentialité (obligatoire)** : `-ve` (direct), `-pen` (inféré), `-di` (rapporté), `-sa` (supposé).
- **Modalité épistémique** : `to` (certain), `be` (probable), `os` (possible), `ku` (douteux).
- **Négation** : `na` avant le verbe.
- **Question oui/non** : `mo` à la fin.
- **Possession** : `de`. **Subordination** : `ki`.""",
    "zh": """## 基本语法

- **语序**：主-谓-宾（SVO）。`mi go a le ho` =「我去房子」。
- **修饰语在核心词之前**：`me ho` =「大房子」。
- **复数**：后缀 `-s`。`li` → `lis`。
- **时态**：`an-`（过去）、`ne-`（将来）；现在时无标记。
- **示证（强制）**：`-ve`（直接）、`-pen`（推断）、`-di`（转述）、`-sa`（假定）。
- **认识情态**：`to`（确定）、`be`（可能）、`os`（也许）、`ku`（存疑）。
- **否定**：`na` 置于动词前。
- **是非疑问句**：`mo` 置于句末。
- **所有格**：`de`。**从句**：`ki`。""",
    "ja": """## 基本文法

- **語順**：主語-動詞-目的語（SVO）。`mi go a le ho` =「私は家に行く」。
- **修飾語は主要部の前**：`me ho` =「大きな家」。
- **複数**：接尾辞 `-s`。`li` → `lis`。
- **時制**：`an-`（過去）、`ne-`（未来）；現在は無標。
- **証拠性（必須）**：`-ve`（直接）、`-pen`（推論）、`-di`（伝聞）、`-sa`（想定）。
- **認識モダリティ**：`to`（確実）、`be`（多分）、`os`（可能）、`ku`（疑わしい）。
- **否定**：`na` を動詞の前に。
- **Yes/No 疑問**：`mo` を文末に。
- **所有**：`de`。**従属節**：`ki`。""",
}


# ---------------------------------------------------------------------------
# Grupos (categorías) con títulos en 5 idiomas
# ---------------------------------------------------------------------------
GRUPOS = [
    (["partícula", "preposición", "conjunción", "adverbio", "saludo"],
     {"es": "Palabras funcionales", "en": "Function words", "fr": "Mots fonctionnels", "zh": "功能词", "ja": "機能語"}),
    (["pronombre"], {"es": "Pronombres", "en": "Pronouns", "fr": "Pronoms", "zh": "代词", "ja": "代名詞"}),
    (["determinante"], {"es": "Determinantes", "en": "Determiners", "fr": "Déterminants", "zh": "限定词", "ja": "限定詞"}),
    (["verbo"], {"es": "Verbos", "en": "Verbs", "fr": "Verbes", "zh": "动词", "ja": "動詞"}),
    (["sustantivo", "nombre propio"], {"es": "Sustantivos", "en": "Nouns", "fr": "Noms", "zh": "名词", "ja": "名詞"}),
    (["adjetivo"], {"es": "Adjetivos", "en": "Adjectives", "fr": "Adjectifs", "zh": "形容词", "ja": "形容詞"}),
    (["color"], {"es": "Colores", "en": "Colors", "fr": "Couleurs", "zh": "颜色", "ja": "色"}),
    (["número"], {"es": "Números", "en": "Numbers", "fr": "Nombres", "zh": "数字", "ja": "数字"}),
    (["matemática"], {"es": "Matemáticas", "en": "Mathematics", "fr": "Mathématiques", "zh": "数学", "ja": "数学"}),
    (["prefijo SI"], {"es": "Prefijos SI", "en": "SI prefixes", "fr": "Préfixes SI", "zh": "国际单位制前缀", "ja": "SI接頭辞"}),
    (["país"], {"es": "Países", "en": "Countries", "fr": "Pays", "zh": "国家", "ja": "国"}),
    (["slang"], {"es": "Slang", "en": "Slang", "fr": "Argot", "zh": "俚语", "ja": "俗語"}),
    (["actitud"], {"es": "Partículas de actitud", "en": "Attitude particles", "fr": "Particules d'attitude", "zh": "态度助词", "ja": "態度助詞"}),
    (["modalidad"], {"es": "Modalidad epistémica", "en": "Epistemic modality", "fr": "Modalité épistémique", "zh": "认识情态", "ja": "認識モダリティ"}),
]


def agrupar(palabras):
    d = defaultdict(list)
    for p in palabras:
        d[p["categoria"]].append(p)
    return d


def generar_manual(idioma, lexico, afijos, traducciones):
    meta = IDIOMAS[idioma]
    trad = traducciones.get(idioma, {})
    por_cat = agrupar(lexico["palabras"])
    partes = [f"# {meta['titulo']}", "", meta["tagline"], "", PRONUNCIACION[idioma], "", GRAMATICA[idioma], ""]

    for cats, titulos in GRUPOS:
        titulo = titulos[idioma]
        palabras = [p for c in cats for p in por_cat.get(c, [])]
        if not palabras:
            continue
        partes.append(f"## {titulo}")
        partes.append("")
        partes.append(f"| Korlin | AFI | {'Significado' if idioma=='es' else 'Meaning' if idioma=='en' else 'Sens' if idioma=='fr' else '含义' if idioma=='zh' else '意味'} |")
        partes.append("|---|---|---|")
        for p in palabras:
            # Usar la traducción del idioma si existe, si no el campo es/en
            significado = trad.get(p["forma"], p.get(idioma, p["es"]))
            partes.append(f"| **{p['forma']}** | {p['afi']} | {significado} |")
        partes.append("")

    return "\n".join(partes)


def generar_manual_ia(lexico, afijos):
    lineas = [
        "# Manual de Korlin para agentes de IA", "",
        "Korlin (Shortlang) es una lengua construida regular y sin ambigüedad.",
        "Reglas de uso para un agente:", "",
        "1. **Orden**: SVO. Modificador antes del núcleo.",
        "2. **Plural**: sufijo `-s`.",
        "3. **Tiempo**: `an-` (pasado), `ne-` (futuro), presente sin marca.",
        "4. **Evidencialidad OBLIGATORIA**: `-ve` (directo), `-pen` (inferido), `-di` (reportado), `-sa` (asumido).",
        "5. **Modalidad epistémica** (opcional, al final): `to` cierto, `be` probable, `os` posible, `ku` dudoso.",
        "6. **Negación**: `na` antes del verbo.",
        "7. **Pregunta sí/no**: `mo` al final. Interrogativos al inicio.",
        "8. **Posesión**: `de`. **Subordinación**: `ki`.",
        "9. **Derivación**: `-pe` agente, `-lo` lugar, `-re` cosa, `-i` adjetivo, `-ro` abstracto, `na-` opuesto, `me-` aumentativo, `pi-` diminutivo.", "",
        "## Vocabulario (korlin | categoría | es | en)", "```",
    ]
    for p in lexico["palabras"]:
        lineas.append(f"{p['forma']:<8} | {p['categoria']:<12} | {p['es']} | {p['en']}")
    lineas.append("```")
    lineas.append("")
    lineas.append("## Pares de ejemplo")
    lineas.append("```")
    ejemplos = [
        ("Halo! Mi e-sa Korlin.", "¡Hola! Soy Korlin.", "Hello! I am Korlin."),
        ("Na-toro na-kan-sa vi i mi.", "La mentira no puede vivir en mí.", "Lies cannot live in me."),
        ("li go-ve.", "Él se fue (lo vi).", "He left (I saw it)."),
        ("li go-di ku.", "Se fue (me lo contaron, no me fío).", "He left (I was told, I doubt it)."),
        ("Tu go mo?", "¿Vas?", "Do you go?"),
    ]
    for k, es, en in ejemplos:
        lineas.append(k)
        lineas.append(f"  ES: {es}")
        lineas.append(f"  EN: {en}")
    lineas.append("```")
    return "\n".join(lineas)


def generar_lexico_js(lexico, traducciones):
    data = []
    for p in lexico["palabras"]:
        f = p["forma"]
        item = {"f": f, "a": p["afi"], "c": p["categoria"], "es": p["es"], "en": p["en"]}
        for lang in ("fr", "zh", "ja"):
            trad = traducciones.get(lang, {}).get(f)
            if trad:
                item[lang] = trad
        data.append(item)
    return "window.KORLIN_LEXICO = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"


def main():
    lexico = cargar("lexico.yaml")
    afijos = cargar("afijos.yaml")
    traducciones = cargar("traducciones.yaml")

    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)

    # Manuales ES/EN (desde lexico.yaml) + FR/ZH/JA (desde traducciones.yaml)
    for idioma in ["es", "en", "fr", "zh", "ja"]:
        manual = generar_manual(idioma, lexico, afijos, traducciones)
        (docs / f"manual-{idioma}.md").write_text(manual, encoding="utf-8")

    (docs / "manual-ia.md").write_text(generar_manual_ia(lexico, afijos), encoding="utf-8")
    (ROOT / "lexico.js").write_text(generar_lexico_js(lexico, traducciones), encoding="utf-8")

    n_pal = len(lexico["palabras"])
    print(f"✓ {n_pal} palabras →")
    for idioma in ["es", "en", "fr", "zh", "ja"]:
        print(f"  docs/manual-{idioma}.md")
    print(f"  docs/manual-ia.md")
    print(f"  web/lexico.js")


if __name__ == "__main__":
    main()
