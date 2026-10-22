#!/usr/bin/env python3
"""
Genera el paquete de integración para IA de Korlin:
  - korlin-spec.md   (spec pack LLM-ready, autocontenido)
  - korlin.json      (léxico + afijos + reglas legibles por máquina)
  - llms.txt         (descubrimiento para agentes)

Fuente de verdad: data/lexico.yaml, data/afijos.yaml
Uso:  python scripts/generar_ia.py
"""
import json
import unicodedata
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DATA = RAIZ / "data"

# ---------------------------------------------------------------- carga

def carga():
    lex = yaml.safe_load((DATA / "lexico.yaml").read_text(encoding="utf-8"))
    afi = yaml.safe_load((DATA / "afijos.yaml").read_text(encoding="utf-8"))
    palabras = lex["palabras"]
    afijos = afi["afijos"]
    # normaliza 'forma' booleana si alguien vuelve a escribir `no:` sin comillas
    for p in palabras:
        if not isinstance(p["forma"], str):
            p["forma"] = {False: "no", True: "ya"}.get(p["forma"], str(p["forma"]))
        for campo in ("es", "en", "categoria", "afi"):
            if not isinstance(p.get(campo), str):
                p[campo] = {True: "yes", False: "no"}.get(p.get(campo), str(p.get(campo, "")))
    return palabras, afijos


# ---------------------------------------------------------------- korlin.json

REGLAS = {
    "tipologia": {
        "orden": "SVO",
        "alineamiento": "nominativo-acusativo",
        "modificadores": "antes del nucleo (Adj-N, Det-N, Gen-N)",
        "tipo_morfologico": "aglutinante, altamente regular",
    },
    "fonologia": {
        "fonemas": 21,
        "consonantes": ["p", "b", "t", "d", "k", "g", "m", "n", "f", "v", "s", "h", "l", "r", "w", "y"],
        "vocales": ["a", "e", "i", "o", "u"],
        "silaba": "(C)V(C)",
        "coda_permitida": ["m", "n", "s"],
        "acento": "penultima silaba",
        "letras_prohibidas": ["c", "j", "q", "x", "z"],
        "regla_oro": "una letra = un sonido, siempre",
    },
    "morfologia": {
        "plural": "-s",
        "pasado": "an-",
        "futuro": "ne-",
        "presente": "sin marca",
        "evidencialidad": {
            "obligatoria": True,
            "sufijos": {
                "-ve": "directo / lo vi",
                "-pen": "inferido / lo deduzco",
                "-di": "reportado / me lo dijeron",
                "-sa": "asumido / se sabe",
            },
        },
        "modalidad_epistemica": {
            "posicion": "final de la oracion",
            "opciones": {"to": "cierto", "be": "probable", "os": "posible", "ku": "dudoso"},
        },
        "actitud": {
            "posicion": "final, opcional, emotiva",
            "particulas": {
                "yo": "alegria ❤️", "hu": "tristeza 😢", "we": "sorpresa 😮",
                "fi": "ironia 🙃", "bu": "enfado 😤", "ri": "risa 😂",
                "pu": "asco 🤢", "ni": "miedo 😨", "la": "carino 🥰",
            },
        },
    },
    "sintaxis": {
        "negacion": {"oracion": "na suelto antes del verbo", "derivacion": "prefijo na- = opuesto (nunca sobre un verbo: para negar la accion se usa na suelto)"},
        "pregunta_si_no": "mo al final (la pregunta exime el evidencial)",
        "interrogativo": "al inicio",
        "pro_drop": "el sujeto se omite si el contexto basta (tambien con na y mo)",
        "orden_final": "[verbo+evidencial] ... [modalidad] [actitud] [mo]",
        "modalidad_por_defecto": "to (certeza)",
        "ordenes": "raiz desnuda, sin evidencial ni sujeto (Go!)",
        "condicional": "si ... so ...: protasis exenta, apodosis con evidencial",
        "copula": "e lleva el evidencial en la declarativa (le ti e-ve gu)",
        "subordinacion": "ki (la subordinada va exenta; cada clausula puede llevar el suyo)",
        "posesion": "de (X de Y = Y posee X)",
        "derivacion": {
            "-pe": "agente (persona que X)",
            "-lo": "lugar (donde se X)",
            "-re": "cosa/objeto",
            "-i": "adjetivo relativo",
            "-ro": "abstracto (cualidad)",
            "na-": "opuesto/negativo",
            "me-": "aumentativo (grande/muy)",
            "pi-": "diminutivo (pequeno)",
        },
    },
}


def genera_json(palabras, afijos):
    doc = {
        "nombre": "Korlin",
        "exonimo": "Shortlang",
        "autonimo": "korlin",
        "significado": "ko (corto) + lin (lengua) = lengua corta",
        "version": "0.5",
        "licencia": "MIT",
        "sitio": "https://nachofigx.github.io/korlin/",
        "repo": "https://github.com/nachofigx/korlin",
        "reglas": REGLAS,
        "lexico": [
            {
                "forma": p["forma"],
                "afi": p.get("afi", ""),
                "categoria": p.get("categoria", ""),
                "es": p.get("es", ""),
                "en": p.get("en", ""),
            }
            for p in palabras
        ],
        "afijos": [
            {
                "forma": a["forma"],
                "tipo": a.get("tipo", ""),
                "funcion": a.get("funcion", ""),
                "es": a.get("es", ""),
                "en": a.get("en", ""),
                "ejemplo": a.get("ejemplo", ""),
            }
            for a in afijos
        ],
    }
    (RAIZ / "korlin.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return len(doc["lexico"]), len(doc["afijos"])


# ---------------------------------------------------------------- spec pack

EJEMPLOS = [
    ("Halo! Mi e-sa Korlin.", "¡Hola! Soy Korlin.", "Hello! I am Korlin."),
    ("Na-toro na kan-sa vi i mi.", "La mentira no puede vivir en mí.", "Lies cannot live in me."),
    ("li go-ve.", "Él va (lo veo).", "He goes (I see it)."),
    ("li an-go-ve.", "Él fue (lo vi).", "He went (I saw it)."),
    ("li an-go-di ku.", "Se fue (me lo contaron, no me fío).", "He left (I was told, I doubt it)."),
    ("Tu go mo?", "¿Vas?", "Do you go?"),
    ("Mi man-ve man-re.", "Como comida.", "I eat food."),
    ("an-go-ve.", "Fui (yo; el sujeto se omite).", "I went (subject omitted)."),
    ("ne-go-pen.", "Irá (lo infiero).", "He will go (I infer it)."),
    ("me-ho.", "Casa grande.", "Big house."),
    ("pi-ho.", "Casita.", "Little house."),
    ("na-gu.", "Malo.", "Bad."),
    ("gu-ro.", "Bondad.", "Goodness."),
    ("man-lo.", "Comedor.", "Dining place."),
    ("sa-pe.", "Sabio (el que sabe).", "Wise one (the one who knows)."),
    ("Wi e-sa pes.", "Somos personas.", "We are people."),
    ("Yo! Mi vo-ve tu la.", "¡Qué alegría! Te quiero (cariño).", "Yay! I love you (affection)."),
]


def genera_spec(palabras, afijos):
    L = []
    A = L.append
    A("# Korlin — Especificación para modelos de lenguaje (v0.5)")
    A("")
    A("> **Cómo usar este archivo.** Pégalo completo en el *system prompt* (o en el primer")
    A("> mensaje) de cualquier LLM. Es autocontenido: contiene todo lo necesario para")
    A("> **hablar y traducir Korlin correctamente**. No requiere entrenamiento previo.")
    A("")
    A("Korlin (exónimo **Shortlang**) es una lengua construida, regular y sin ambigüedad,")
    A("diseñada para hablar mucho en poco tiempo, con honestidad forzada por gramática")
    A("(evidencialidad obligatoria) y pensada para uso humano y con agentes de IA.")
    A("Autónimo: **korlin** = `ko` (corto) + `lin` (lengua) = *lengua corta*.")
    A("**Versión de esta especificación: v0.4** (ver `CHANGELOG.md`). Este documento manda")
    A("sobre cualquier otro; si algo no cuadra con `01/02/03`, gana este.")
    A("")
    A("**Fuente de verdad y qué es generado.** `data/lexico.yaml`, `data/afijos.yaml` y")
    A("`data/traducciones.yaml` son la fuente única del **léxico y los afijos**; de ahí")
    A("salen este spec, `korlin.json`, `llms.txt`, los manuales y `lexico.js`. Las")
    A("**reglas gramaticales** (1-19) viven por ahora en `scripts/generar_ia.py` y en este")
    A("spec; `01-phonology.md`, `02-morphology.md` y `03-syntax.md` son explicaciones")
    A("manuales que deben seguir al spec, no al revés.")
    A("")
    A("---")
    A("")
    A("## 1. Reglas irrompibles (léelas primero)")
    A("")
    A("1. **Una letra = un sonido.** Nunca hay excepciones. No existen `c`, `j`, `q`, `x`, `z`.")
    A("2. **Orden SVO.** Sujeto, Verbo, Objeto.")
    A("3. **El modificador va ANTES del núcleo:** `me ho` = *casa grande*; `gu pe` = *persona buena*.")
    A("4. **La evidencialidad es OBLIGATORIA en todo verbo con contenido factual.**")
    A("   Sin ella, la oración está mal formada. (Ver §4.)")
    A("   **Exenta** en: preguntas (`mo`), órdenes e ironía marcada con `fi`.")
    A("   En **subordinadas**, cada cláusula lleva la suya.")
    A("5. **La modalidad epistémica va al final**, opcional: `to be os ku`.")
    A("6. **La actitud va al final**, opcional: `yo hu we fi bu ri pu ni la`.")
    A("7. **Negación:** hay DOS mecanismos, y no se mezclan.")
    A("   a) **`na` suelto**, inmediatamente antes del verbo → niega la oración.")
    A("      `mi na sa-ve.` = *No sé (lo veo).*")
    A("   b) **`na-` pegado**, como prefijo derivativo → crea la palabra opuesta.")
    A("      `na-gu` = *malo*, `na-toro` = *mentira*. **Nunca** niega un verbo: para")
    A("      negar la acción se usa siempre `na` suelto.")
    A("8. **Pregunta sí/no:** `mo` al final. **Interrogativos** al inicio:")
    A("    `ki` + sustantivo = qué/cuál (`ki lo` = *qué lugar, dónde*); se antepone.")
    A("   Toda pregunta va **sin evidencial** en su propia cláusula.")
    A("9. **No hay concordancia** de género, número ni persona. Nunca.")
    A("10. **No hay artículos obligatorios**; `le` existe y es opcional.")
    A("11. **El sujeto puede omitirse** si el contexto lo deja claro (pro-drop),")
    A("    también con `na` y con `mo`: `na sa-ve.` = *no sé*; `go mo?` = *¿vas?*")
    A("12. **La modalidad epistémica no marcada equivale a `to`** (certeza),")
    A("    pero la evidencialidad NUNCA se puede omitir en una declarativa.")
    A("13. **ÓRDENES: la raíz desnuda del verbo, sin evidencial.**")
    A("    `Go!` = *¡ve!*; `Ve mi!` = *¡mírame!* No hay morfema nuevo: como el")
    A("    evidencial es obligatorio en la declaración, la forma desnuda queda libre")
    A("    para el mandato (igual que el inglés `Go!`). Es la exención nº2.")
    A("    El sujeto se omite por defecto; si va explícito, tampoco lleva evidencial:")
    A("    `Tu go!` = *¡tú, ve!*")
    A("14. **NO hay exención por subordinación.** En una subordinada, **cada cláusula")
    A("    lleva su propio evidencial** (cf. quechua, tariana; la fuente se marca donde")
    A("    está el conocimiento, no donde está la oración).")
    A("    `Mi sa-ve ki li an-go-di.` = *Sé (lo veo) que él fue (me lo contaron).*")
    A("15. **Condicional `si … so …`: la prótasis es exenta, la apódosis lleva evidencial.**")
    A("    `si tu go, so mi ne-go-pen.` = *Si vas, iré (lo deduzco).*")
    A("16. **Cópula `e`: el evidencial va en `e`.** `le ti e-ve gu.` = *El día está bueno (lo veo).*")
    A("17. **DERIVACIÓN: una raíz + un afijo derivacional válido es palabra legítima**")
    A("    si el sentido es composicional (el afijo aporta lo suyo sin sorpresa).")
    A("    `do` (dormir) + `-lo` (lugar) = `do-lo` (*dormitorio*) es válido por regla.")
    A("    Si el sentido se lexicaliza (deja de ser predecible), se LISTA en el léxico.")
    A("    Regla de oro: **derivar antes que inventar**; inventar solo si ningún afijo sirve.")
    A("18. **El guion marca frontera de morfema.** Los afijos derivacionales y flexivos")
    A("    van con guion (`do-lo`, `mi man-ve`); el plural `-s` se escribe pegado")
    A("    (`pes`, `lis`). Sin guion, dos raíces seguidas son dos palabras.")
    A("    `vi-sa` (vivir+asumido) ≠ `vi sa` (vivir/saber).")
    A("19. **Posesión: dos formas equivalentes.** El pronombre antepuesto es la normal")
    A("    (`mi ho` = *mi casa*); `de` da la forma analítica o enfática (`le ho de mi`).")
    A("    **Numerales:** del 1 al 10 son raíces; 11+ se componen (`des-u` = *once*).")
    A("    El plural `-s` es opcional tras un numeral (`du ho` = *dos casas*).")
    A("")
    A("---")
    A("")
    A("## 2. Fonología")
    A("")
    A("21 fonemas: 16 consonantes + 5 vocales.")
    A("")
    A("| Consonantes | AFI | | Vocales | AFI |")
    A("|---|---|---|---|---|")
    A("| p | /p/ | | a | /a/ |")
    A("| t | /t/ | | e | /e/ |")
    A("| k | /k/ | | i | /i/ |")
    A("| b | /b/ | | o | /o/ |")
    A("| d | /d/ | | u | /u/ |")
    A("| g | /g/ | | | |")
    A("| m | /m/ | | | |")
    A("| n | /n/ | | | |")
    A("| f | /f/ | | | |")
    A("| v | /v/ | | | |")
    A("| s | /s/ | | | |")
    A("| h | /h/ | | | |")
    A("| l | /l/ | | | |")
    A("| r | /ɾ/ | | | |")
    A("| w | /w/ | | | |")
    A("| y | /j/ | | | |")
    A("")
    A("- **Sílaba:** `(C)V(C)`. La coda solo admite `m`, `n`, `s`.")
    A("- **Sílabas posibles:** 17 onsets (16 consonantes + vacío) × 5 vocales × 4 codas = **340**.")
    A("- **Acento:** siempre en la **penúltima** sílaba. Nunca se escribe tilde.")
    A("- **Letras prohibidas:** `c j q x z`. La `j` no existe: /j/ se escribe `y`.")
    A("- **Aproximación para hispanohablantes:** se pronuncia como español, con `v`")
    A("  labiodental suave y `h` aspirada (como en inglés `house`).")
    A("- **Mayúscula:** solo en la primera letra de la oración y en los nombres")
    A("  propios. Nunca en medio de una palabra ni para marcar énfasis.")
    A("- **Puntuación:** `.` `!` `?` como en español; `?` cierra toda pregunta.")
    A("- **Nombres propios:** se adaptan a la fonología, no se dejan en su grafía")
    A("  original: `Mekiko` (México), `Faransa` (Francia), `Yapan` (Japón),")
    A("  `Barasila` (Brasil), `Alemania` (Alemania). Si violan `(C)V(C)`, se adaptan")
    A("  (`Frans` → `Faransa`, `Brasil` → `Barasila`).")
    A("- **Acento en compuestos con guion:** cada segmento conserva el suyo; se cuenta")
    A("  la penúltima **dentro de la palabra principal** (`do-lo` → /do.lo/).")
    A("")
    A("---")
    A("")
    A("## 3. Morfología")
    A("")
    A("Korlin es **aglutinante**: cada afijo tiene un único significado y se encadenan")
    A("sin fusionarse.")
    A("")
    A("**Orden de la palabra verbal:**")
    A("")
    A("`[tiempo] + raíz + [evidencial]`")
    A("")
    A("| Categoría | Forma | Ejemplo |")
    A("|---|---|---|")
    A("| Pasado | `an-` | `an-go-ve` = *fui (lo vi)* |")
    A("| Presente | *(sin marca)* | `go-ve` = *voy (lo veo)* |")
    A("| Futuro | `ne-` | `ne-go-pen` = *irá (lo infiero)* |")
    A("| Plural (sustantivo) | `-s` | `pe` → `pes` = *personas* |")
    A("")
    A("### Derivación")
    A("")
    A("| Afijo | Significado | Ejemplo |")
    A("|---|---|---|")
    A("| `-pe` | agente: quien hace X | `sa-pe` = *sabio* |")
    A("| `-lo` | lugar: donde se hace X | `man-lo` = *comedor* |")
    A("| `-re` | cosa/objeto | `man-re` = *comida* |")
    A("| `-i` | adjetivo relativo | `su-i` = *solar* |")
    A("| `-ro` | abstracto: cualidad | `gu-ro` = *bondad* |")
    A("| `na-` | opuesto / negativo | `na-gu` = *malo* |")
    A("| `me-` | aumentativo | `me-gu` = *excelente* |")
    A("| `pi-` | diminutivo | `pi-ho` = *casita* |")
    A("")
    A("---")
    A("")
    A("## 4. Evidencialidad — el corazón de Korlin")
    A("")
    A("Todo verbo factual **debe** declarar de dónde viene la información. Esto es lo que")
    A("hace la mentira cara: quien afirma debe decir si lo vio, lo dedujo, se lo contaron")
    A("o lo asume. Estudios tipológicos (Aikhenvald 2004) muestran que ~25% de las lenguas")
    A("del mundo marcan la fuente obligatoriamente; Korlin lo adopta desde el diseño.")
    A("")
    A("| Sufijo | Fuente | Ejemplo (presente) | Traducción |")
    A("|---|---|---|---|")
    A("| `-ve` | **Directo** (lo vi, lo viví) | `li go-ve` | *Él va (lo veo)* |")
    A("| `-pen` | **Inferido** (lo deduzco) | `li go-pen` | *Él va (lo deduzco)* |")
    A("| `-di` | **Reportado** (me lo dijeron) | `li go-di` | *Él va (me lo contaron)* |")
    A("| `-sa` | **Asumido** (se sabe) | `li go-sa` | *Él va (es sabido)* |")
    A("")
    A("**Pasado: el evidencial NO cambia, pero `an-` es obligatorio.**")
    A("`li an-go-ve` = *Él fue (lo vi)*; `li an-go-di` = *Él fue (me lo contaron)*.")
    A("")
    A("**Un evidencial por cláusula, en el verbo finito (el primero de la cadena).**")
    A("En `tu kan-ve sa mi` (*puedes verme*), `kan` lleva el evidencial y `sa` queda")
    A("desnudo. En una subordinada, cada cláusula lleva el suyo: `mi sa-ve ki li an-go-di.`")
    A("")
    A("**Regla de honestidad:** si no sabes de dónde viene algo, usa `-pen` (lo deduzco) o")
    A("`-di` (me lo dijeron), nunca `-ve` (lo vi) si no lo viste realmente.")
    A("")
    A("---")
    A("")
    A("## 5. Modalidad epistémica y actitud")
    A("")
    A("Van al **final** de la oración, después del verbo.")
    A("")
    A("**Modalidad y actitud van al final, en este orden fijo:**")
    A("`[verbo+evidencial] … [modalidad] [actitud] [mo]`.")
    A("`li an-go-di ku bu.` = *Se fue (me lo contaron, dudo) 😤.*")
    A("`Tu go ku mo?` = *¿Vas, quizá?* — válido: la pregunta lleva `mo` al final del todo.")
    A("")
    A("**Modalidad** (certeza, opcional):")
    A("")
    A("| Partícula | Valor | Emoji |")
    A("|---|---|---|")
    A("| `to` | cierto | ✅ |")
    A("| `be` | probable | 👍 |")
    A("| `os` | posible | 🤔 |")
    A("| `ku` | dudoso | ⚠️ |")
    A("")
    A("**Actitud** (emoción, opcional) — cada una mapea a un emoji para comunicación digital:")
    A("")
    A("| Partícula | Emoción | Emoji |")
    A("|---|---|---|")
    A("| `yo` | alegría, me encanta | ❤️ |")
    A("| `hu` | tristeza | 😢 |")
    A("| `we` | sorpresa | 😮 |")
    A("| `fi` | ironía, sarcasmo | 🙃 |")
    A("| `bu` | enfado | 😤 |")
    A("| `ri` | risa | 😂 |")
    A("| `pu` | asco | 🤢 |")
    A("| `ni` | miedo | 😨 |")
    A("| `la` | cariño | 🥰 |")
    A("")
    A("---")
    A("")
    A("## 6. Sintaxis")
    A("")
    A("| Estructura | Marca | Ejemplo |")
    A("|---|---|---|")
    A("| Negación de oración | `na` + verbo | `mi na sa-ve` = *no sé (lo veo)* |")
    A("| Palabra opuesta | `na-` + raíz | `na-gu` = *malo* |")
    A("| Pregunta sí/no | `mo` final | `Tu go mo?` = *¿Vas?* |")
    A("| Interrogativo | al inicio | `Ki tu man?` = *¿Qué comes?* |")
    A("| Posesión | `de` (o pronombre antepuesto) | `le ho de mi` = *mi casa* · `mi ho` |")
    A("| Subordinación | `ki` | `Mi sa-ve ki li an-go-di` = *Sé que él fue (me lo dijeron)* |")
    A("| Condicional | `si … so …` | `si tu go, so mi ne-go-pen` = *si vas, iré (lo deduzco)* |")
    A("| Orden | raíz desnuda | `Go!` = *¡ve!* · `Ve mi!` = *¡mírame!* |")
    A("| Cópula | `e` + evidencial | `le ti e-ve gu` = *el día está bueno (lo veo)* |")
    A("")
    A("---")
    A("")
    A("## 7. Léxico completo")
    A("")
    A(f"{len(palabras)} palabras. Formato: **korlin** · AFI · categoría · español · inglés.")
    A("")
    A("| Korlin | AFI | Categoría | Español | English |")
    A("|---|---|---|---|---|")
    for p in palabras:
        A(f"| `{p['forma']}` | {p.get('afi','')} | {p.get('categoria','')} | {p.get('es','')} | {p.get('en','')} |")
    A("")
    A("---")
    A("")
    A("## 8. Afijos completos")
    A("")
    A("| Afijo | Tipo | Función | Español | English | Ejemplo |")
    A("|---|---|---|---|---|---|")
    for a in afijos:
        A(f"| `{a['forma']}` | {a.get('tipo','')} | {a.get('funcion','')} | {a.get('es','')} | {a.get('en','')} | {a.get('ejemplo','')} |")
    A("")
    A("---")
    A("")
    A("## 9. Ejemplos glosados (few-shot)")
    A("")
    for i, (k, es, en) in enumerate(EJEMPLOS, 1):
        A(f"{i}. **{k}**")
        A(f"   - ES: {es}")
        A(f"   - EN: {en}")
    A("")
    A("---")
    A("")
    A("## 10. Instrucciones para el agente")
    A("")
    A("Cuando el usuario te pida escribir o traducir en Korlin:")
    A("")
    A("1. Traduce **idea por idea**, no palabra por palabra. Korlin condensa.")
    A("2. Aplica **SVO** y la evidencialidad **siempre** en verbos factuales.")
    A("3. Si no conoces una palabra, **derívala** con un afijo; no inventes raíces.")
    A("4. Si de verdad necesitas una raíz nueva, márcala así: `[nueva: X = Y]`.")
    A("5. Respeta la fonología: nada de `c`, `j`, `q`, `x`, `z`.")
    A("6. Para conversación digital, puedes sustituir la partícula de actitud por su emoji.")
    A("")
    A("**Plantilla de respuesta:**")
    A("")
    A("```")
    A("Korlin: <texto>")
    A("Glosa:  <palabra>.<AFI> = significado …")
    A("ES:     <traducción>")
    A("```")
    A("")
    A("---")
    A("")
    A(f"*Korlin se distribuye bajo licencia MIT. Repo: {REGLAS and 'https://github.com/nachofigx/korlin'}.*")
    A("")

    (RAIZ / "korlin-spec.md").write_text("\n".join(L), encoding="utf-8")
    return len("\n".join(L))


# ---------------------------------------------------------------- llms.txt

def genera_llms():
    txt = """# Korlin (Shortlang)

> Lengua construida corta, regular y honesta (evidencialidad obligatoria).
> Diseñada para hablar rápido, ser hablable y ser usable por humanos y agentes de IA.

## Especificación para IA
- [korlin-spec.md](https://raw.githubusercontent.com/nachofigx/korlin/main/korlin-spec.md): spec pack autocontenido. Pégalo en tu system prompt para hablar Korlin.
- [korlin.json](https://raw.githubusercontent.com/nachofigx/korlin/main/korlin.json): léxico + afijos + reglas en JSON.

## Gramática
- [01-phonology.md](https://github.com/nachofigx/korlin/blob/main/01-phonology.md): fonología
- [02-morphology.md](https://github.com/nachofigx/korlin/blob/main/02-morphology.md): morfología
- [03-syntax.md](https://github.com/nachofigx/korlin/blob/main/03-syntax.md): sintaxis
- [glossary.md](https://github.com/nachofigx/korlin/blob/main/glossary.md): glosario

## Herramientas
- [traductor-korlin.py](https://github.com/nachofigx/korlin/blob/main/scripts/traductor-korlin.py): traductor por reglas ES/EN <-> Korlin

## Web
- [Sitio](https://nachofigx.github.io/korlin/): diccionario, comparativas, flashcards
- [App de aprendizaje](https://nachofigx.github.io/korlin/learn.html): tipo Duolingo, con voz

## Investigación
- [research.md](https://github.com/nachofigx/korlin/blob/main/docs/research.md): white paper (EN)
- [investigacion.md](https://github.com/nachofigx/korlin/blob/main/docs/investigacion.md): white paper (ES)
"""
    (RAIZ / "llms.txt").write_text(txt, encoding="utf-8")
    return len(txt)


# ---------------------------------------------------------------- main

def main():
    palabras, afijos = carga()
    n_lex, n_afi = genera_json(palabras, afijos)
    n_spec = genera_spec(palabras, afijos)
    n_llms = genera_llms()
    print(f"korlin.json    → {n_lex} palabras, {n_afi} afijos")
    print(f"korlin-spec.md → {n_spec:,} caracteres")
    print(f"llms.txt       → {n_llms:,} caracteres")


if __name__ == "__main__":
    main()
