#!/usr/bin/env python3
"""
Generador de documentación de Korlin (Shortlang).

Lee la fuente de verdad única (data/lexico.yaml, data/afijos.yaml) y genera:
  - docs/manual-es.md      → manual en español
  - docs/manual-en.md      → manual en inglés
  - docs/manual-ia.md      → manual para agentes de IA
  - web/lexico.js          → datos para el sitio web interactivo

Un cambio en data/ se refleja automáticamente en los 4 archivos al re-ejecutar.
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
# Contenido fijo (gramática / pronunciación) — también editable aquí.
# En una iteración futura puede moverse a data/gramatica.yaml.
# ---------------------------------------------------------------------------

PRONUNCIACION = {
    "es": """## Pronunciación

20 sonidos, 20 letras. **Una letra = un sonido, siempre.**

| Letra | Sonido (AFI) | Como en español |
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

**Reglas de oro**: vocales puras · p/t/k sin soplo · r siempre suave · s siempre [s] · h siempre sonora.""",
    "en": """## Pronunciation

20 sounds, 20 letters. **One letter = one sound, always.**

| Letter | Sound (IPA) | Like in English |
|---|---|---|
| a | /a/ | f**a**ther |
| e | /e/ | b**e**d |
| i | /i/ | s**ee** |
| o | /o/ | g**o** (pure, no glide) |
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
| s | /s/ | **s**ee (always /s/) |
| h | /h/ | **h**ouse |
| l | /l/ | **l**ow |
| r | /ɾ/ | Spanish "pe**r**o" (tapped) |
| w | /w/ | **w**ater |
| y | /j/ | **y**es |

**Golden rules**: pure vowels · no aspiration on p/t/k · r always tapped · s always /s/ · h always voiced.""",
}

GRAMATICA = {
    "es": """## Gramática esencial

- **Orden**: Sujeto-Verbo-Objeto (SVO). `mi go a le ho` = "voy a la casa".
- **Modificador antes del núcleo**: `me ho` = "casa grande".
- **Plural**: sufijo `-s`. `li` → `lis` (él → ellos).
- **Tiempos**: prefijos `an-` (pasado) y `ne-` (futuro); presente sin marca.
- **Evidencialidad (obligatoria)**: sufijos `-ve` (directo), `-pen` (inferido), `-di` (reportado), `-sa` (asumido). Toda afirmación declara su fuente.
- **Modalidad epistémica**: partículas `to` (cierto), `be` (probable), `os` (posible), `ku` (dudoso).
- **Negación**: `na` antes del verbo. `mi na sa` = "no sé".
- **Pregunta sí/no**: partícula `mo` al final. `tu go mo?` = "¿vas?".
- **Posesión**: `de`. `le ho de mi` = "mi casa".
- **Subordinación**: `ki`. Cada cláusula lleva su propio evidencial.""",
    "en": """## Essential grammar

- **Order**: Subject-Verb-Object (SVO). `mi go a le ho` = "I go to the house".
- **Modifier before head**: `me ho` = "big house".
- **Plural**: suffix `-s`. `li` → `lis` (he → they).
- **Tense**: prefixes `an-` (past) and `ne-` (future); present unmarked.
- **Evidentiality (mandatory)**: suffixes `-ve` (direct), `-pen` (inferred), `-di` (reported), `-sa` (assumed). Every statement declares its source.
- **Epistemic modality**: particles `to` (certain), `be` (probable), `os` (possible), `ku` (doubtful).
- **Negation**: `na` before the verb. `mi na sa` = "I don't know".
- **Yes/no question**: particle `mo` at the end. `tu go mo?` = "do you go?".
- **Possession**: `de`. `le ho de mi` = "my house".
- **Subordination**: `ki`. Each clause carries its own evidential.""",
}

GRUPOS = [
    (["partícula", "preposición", "conjunción", "adverbio", "saludo"], "Palabras funcionales", "Function words"),
    (["pronombre"], "Pronombres", "Pronouns"),
    (["determinante"], "Determinantes", "Determiners"),
    (["verbo"], "Verbos", "Verbs"),
    (["sustantivo", "nombre propio"], "Sustantivos", "Nouns"),
    (["adjetivo"], "Adjetivos", "Adjectives"),
    (["color"], "Colores", "Colors"),
    (["número"], "Números", "Numbers"),
    (["matemática"], "Matemáticas", "Mathematics"),
    (["prefijo SI"], "Prefijos SI", "SI prefixes"),
    (["país"], "Países", "Countries"),
    (["slang"], "Slang", "Slang"),
    (["actitud"], "Partículas de actitud", "Attitude particles"),
    (["modalidad"], "Modalidad epistémica", "Epistemic modality"),
]


def agrupar_por_categoria(palabras):
    d = defaultdict(list)
    for p in palabras:
        d[p["categoria"]].append(p)
    return d


def tabla_lexico(palabras, idioma):
    lineas = ["| Korlin | AFI | Significado |", "|---|---|---|"]
    for p in palabras:
        lineas.append(f"| **{p['forma']}** | {p['afi']} | {p[idioma]} |")
    return "\n".join(lineas)


def generar_manual(idioma, titulo, lexico, afijos):
    por_cat = agrupar_por_categoria(lexico["palabras"])
    partes = [f"# {titulo}", "", "**Korlin** (/ˈkoɾlin/) es una lengua construida *corta, honesta y moderna*.",
              "", PRONUNCIACION[idioma], "", GRAMATICA[idioma], ""]

    for cats, tit_es, tit_en in GRUPOS:
        tit = tit_es if idioma == "es" else tit_en
        palabras = [p for c in cats for p in por_cat.get(c, [])]
        if not palabras:
            continue
        partes.append(f"## {tit}")
        partes.append("")
        partes.append(tabla_lexico(palabras, idioma))
        partes.append("")

    # Afijos
    partes.append("## Afijos")
    partes.append("")
    cab = "| Afijo | Tipo | Función | Ejemplo |" if idioma == "es" else "| Affix | Type | Function | Example |"
    partes.append(cab)
    partes.append("|---|---|---|---|")
    for a in afijos["afijos"]:
        funcion = a["es"] if idioma == "es" else a["en"]
        partes.append(f"| `{a['forma']}` | {a['tipo']} | {funcion} | `{a['ejemplo']}` |")
    partes.append("")
    return "\n".join(partes)


def generar_manual_ia(lexico, afijos):
    """Manual pensado para que un agente de IA (o un LLM) aprenda Korlin."""
    lineas = [
        "# Manual de Korlin para agentes de IA",
        "",
        "Korlin (Shortlang) es una lengua construida regular y sin ambigüedad.",
        "Reglas de uso para un agente:",
        "",
        "1. **Orden**: SVO. Modificador antes del núcleo.",
        "2. **Plural**: sufijo `-s`.",
        "3. **Tiempo**: `an-` (pasado), `ne-` (futuro), presente sin marca.",
        "4. **Evidencialidad OBLIGATORIA**: todo verbo declarativo lleva `-ve` (directo), `-pen` (inferido), `-di` (reportado) o `-sa` (asumido).",
        "5. **Modalidad epistémica** (opcional, al final): `to` cierto, `be` probable, `os` posible, `ku` dudoso.",
        "6. **Negación**: `na` antes del verbo.",
        "7. **Pregunta sí/no**: `mo` al final. Interrogativos al inicio.",
        "8. **Posesión**: `de`. **Subordinación**: `ki`.",
        "9. **Derivación**: `-pe` agente, `-lo` lugar, `-re` cosa, `-i` adjetivo, `-ro` abstracto, `na-` opuesto, `me-` aumentativo, `pi-` diminutivo.",
        "",
        "## Vocabulario (korlin | categoría | es | en)",
        "```",
    ]
    for p in lexico["palabras"]:
        lineas.append(f"{p['forma']:<8} | {p['categoria']:<12} | {p['es']} | {p['en']}")
    lineas.append("```")
    lineas.append("")
    lineas.append("## Pares de ejemplo (traducción)")
    lineas.append("```")
    ejemplos = [
        ("Halo! Mi e-sa Korlin.", "¡Hola! Soy Korlin.", "Hello! I am Korlin."),
        ("Mi e-sa u ko lin.", "Soy una lengua corta.", "I am a short language."),
        ("Na-toro na-kan-sa vi i mi.", "La mentira no puede vivir en mí.", "Lies cannot live in me."),
        ("li go-ve.", "Él se fue (lo vi).", "He left (I saw it)."),
        ("li go-di ku.", "Se fue (me lo contaron, no me fío).", "He left (I was told, I doubt it)."),
        ("Tu go mo?", "¿Vas?", "Do you go?"),
    ]
    for k, es, en in ejemplos:
        lineas.append(f"{k}")
        lineas.append(f"  ES: {es}")
        lineas.append(f"  EN: {en}")
    lineas.append("```")
    return "\n".join(lineas)


def generar_lexico_js(lexico):
    data = [{"f": p["forma"], "a": p["afi"], "c": p["categoria"], "es": p["es"], "en": p["en"]} for p in lexico["palabras"]]
    return "window.KORLIN_LEXICO = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"


def main():
    lexico = cargar("lexico.yaml")
    afijos = cargar("afijos.yaml")

    docs = ROOT / "docs"
    web = ROOT / "web"
    docs.mkdir(exist_ok=True)
    web.mkdir(exist_ok=True)

    manual_es = generar_manual("es", "Manual de Korlin (español)", lexico, afijos)
    manual_en = generar_manual("en", "Korlin Manual (English)", lexico, afijos)
    manual_ia = generar_manual_ia(lexico, afijos)
    lexico_js = generar_lexico_js(lexico)

    (docs / "manual-es.md").write_text(manual_es, encoding="utf-8")
    (docs / "manual-en.md").write_text(manual_en, encoding="utf-8")
    (docs / "manual-ia.md").write_text(manual_ia, encoding="utf-8")
    (web / "lexico.js").write_text(lexico_js, encoding="utf-8")

    n_pal = len(lexico["palabras"])
    n_af = len(afijos["afijos"])
    print(f"✓ Generados {n_pal} palabras y {n_af} afijos →")
    print(f"  docs/manual-es.md")
    print(f"  docs/manual-en.md")
    print(f"  docs/manual-ia.md")
    print(f"  web/lexico.js")


if __name__ == "__main__":
    main()
