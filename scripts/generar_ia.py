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
    global VERSION
    VERSION = str(lex.get("version", "0.0")).strip('"')
    # normaliza 'forma' booleana si alguien vuelve a escribir `no:` sin comillas
    for p in palabras:
        if not isinstance(p["forma"], str):
            p["forma"] = {False: "no", True: "ya"}.get(p["forma"], str(p["forma"]))
        for campo in ("es", "en", "categoria", "afi"):
            if not isinstance(p.get(campo), str):
                p[campo] = {True: "yes", False: "no"}.get(p.get(campo), str(p.get(campo, "")))
    va = str(afi.get("version", "")).strip('"')
    if va and va != VERSION:
        print(f"  AVISO: afijos.yaml v{va} != lexico.yaml v{VERSION}")
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
        "subordinacion": "ki; cada clausula FINITA lleva su propio evidencial (no hay exencion por subordinacion; la protasis es la excepcion de la regla 15)",
        "posesion": "pronombre antepuesto (mi ho) normal; de = analitica/enfatica",
        "numerales": "non=0, u=1; raices 2-10; ligadura: digito+base multiplica (du-des=20), base+base suma (des-u=11). sento=100, kilo=1000",
        "ortografia": "mayuscula solo inicial y nombres propios; . ! ? ; nombres propios adaptados (Mekiko, Faransa)",
        "ki": "al inicio = interrogativo; en medio tras verbo de decir/saber = complementante",
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
        "version": VERSION,
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
    A(f"# Korlin — Especificación para modelos de lenguaje (v{VERSION})")
    A("")
    A("> **Cómo usar este archivo.** Pégalo completo en el *system prompt* (o en el primer")
    A("> mensaje) de cualquier LLM. Es autocontenido: contiene todo lo necesario para")
    A("> **hablar y traducir Korlin correctamente**. No requiere entrenamiento previo.")
    A("")
    A("Korlin (exónimo **Shortlang**) es una lengua construida, regular y sin ambigüedad,")
    A("diseñada para hablar mucho en poco tiempo, con honestidad forzada por gramática")
    A("(evidencialidad obligatoria) y pensada para uso humano y con agentes de IA.")
    A("Autónimo: **korlin** = `ko` (corto) + `lin` (lengua) = *lengua corta*.")
    A(f"**Versión de esta especificación: v{VERSION}** (ver `CHANGELOG.md`). Este documento manda")
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
    A("4. **La evidencialidad es OBLIGATORIA en el verbo finito de toda oración factual.**")
    A("   (Declarativa = afirmar un hecho. **Las preguntas NO son declarativas**: no")
    A("   afirman nada, así que quedan exentas por (a).)")
    A("   **Exenciones — lista CERRADA, solo estas cinco:**")
    A("   (a) **preguntas** (`mo`, o interrogativo al inicio);")
    A("   (b) **órdenes** (raíz desnuda); (c) **ironía marcada con `fi`**;")
    A("   (d) la **prótasis** del condicional (`si …`);")
    A("   (e) los **verbos no finitos de una cadena** (el auxiliar o modal lleva el")
    A("   evidencial; el verbo de apoyo va desnudo: `tu kan-ve ve mi` = *puedes verme*).")
    A("   **No hay ninguna otra exención.**")
    A("5. **La modalidad epistémica va al final**, opcional: `to be os ku`.")
    A("6. **La actitud va al final**, opcional: `yo hu we fi bu ri pu ni la`.")
    A("7. **Negación:** hay DOS mecanismos, y no se mezclan.")
    A("   a) **`na` suelto**, inmediatamente antes del verbo → niega la oración.")
    A("      `mi na sa-ve.` = *No sé (lo veo).*")
    A("   b) **`na-` pegado**, como prefijo derivativo → crea la palabra opuesta.")
    A("      `na-gu` = *malo*, `na-toro` = *mentira* (**derivado enfático**; `fe` = *malo*")
    A("      simple). **`na-` NUNCA va sobre un verbo**, ni flexionado ni en su forma de")
    A("      diccionario: `na-sa-ve` y `na-sa` son incorrectos. Para negar una acción se")
    A("      usa siempre `na` suelto (`mi na sa-ve`), y `na sa` ≠ `na-sa-ve` porque en la")
    A("      segunda hay una palabra fonológica y el acento cae distinto.")
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
    A("    van con guion (`do-lo`, `mi man-ve`). El plural va **pegado**: `-s` tras")
    A("    vocal (`pes`, `lis`) y **`-es` tras coda** (`nom` → `nomes`, `kin` → `kines`,")
    A("    `tem` → `temes`). Nunca dos codas seguidas. Sin guion, dos raíces seguidas")
    A("    son dos palabras: `vi-sa` (vivir+asumido) ≠ `vi sa` (vivir/saber).")
    A("19. **Posesión y numerales.** El pronombre antepuesto es la forma normal")
    A("    (`mi ho` = *mi casa*); `de` da la analítica o enfática (`le ho de mi`).")
    A("    **Numerales:** `non` = 0, `u` = 1; 2-10 son raíces (`du san fu sin sis sem om nu des`).")
    A("    **Composición — regla de ligadura (corrige C-17):** un dígito pegado a una base")
    A("    la MULTIPLICA; una base tras otra base solo SUMA. Se escribe de mayor a menor.")
    A("    `du-des` = 20 · `des-u` = 11 · `du-des-u` = 21 · `sento` = 100 · `sento-u` = 101 ·")
    A("    `sento-des` = 110 · `du-sento` = 200 · `nu-des-nu` = 99 · `nu-sento-nu-des-nu` = 999.")
    A("    `kilo` = 1.000 como numeral suelto; como prefijo del SI va con guion a una")
    A("    unidad (`kilo-met` = *kilómetro*). El plural `-s` es opcional tras numeral.")
    A("20. **`ki` tiene dos funciones; decide la posición Y el verbo que la precede.**")
    A("    (corrige C-12 vs C-13)")
    A("    - `ki` **al inicio de la oración raíz** = interrogativo (`Ki pe go?` = *¿quién va?*).")
    A("    - `ki` **en medio tras un verbo de decir/saber** = complementante de una")
    A("      declarativa: `Mi sa-ve ki li go-ve.` = *Sé que él va.* (la subordinada FINITA")
    A("      lleva su propio evidencial, regla 14).")
    A("    - `ki` **en medio tras un verbo de percepción o pregunta** (`ve`, `ari`, `mo`) =")
    A("      interrogativo indirecto, **in situ**: `Tu ve ki pe?` = *¿a quién ves?*")
    A("    **Interrogativa indirecta («sé quién va») — C-36 cerrada en v0.7.** El")
    A("    interrogativo (`ki-pe` quién, `ki-lo` dónde, `ki-ti` cuándo, `ki-mo` cómo)")
    A("    es frontera de cláusula: la subordinada lleva su verbo finito y su")
    A("    evidencial (regla 14). No hace falta una forma nueva. `ki-pe`")
    A("    (interrogativo, palabra) ≠ `ki` (complementante): `Mi sa-sa ki-pe go-sa.`")
    A("    = *Sé quién va.* · `Mi sa-sa ki li go-sa.` = *Sé que él va.*")
    A("    **Interrogativo con pro-drop:** el sujeto se omite solo si el interrogativo es")
    A("    el sujeto; si es el objeto, va **in situ**.")
    A("21. **Acento: una palabra fonológica lleva UN solo acento, en la penúltima sílaba.**")
    A("    (corrige C-14 y C-16) Una palabra fonológica = raíz + sus afijos, o raíz + raíz")
    A("    en un compuesto. Un monosílabo libre es siempre tónico.")
    A("    - `me-ho` (1 palabra, 1 acento: /ˈme.ho/) ≠ `me ho` (2 palabras, 2 acentos: /ˈme ˈho/).")
    A("    - `gu-gu` = /ˈgu.gu/ (1 acento) y `ru-sui` = /ruˈsu.i/ (1 acento).")
    A("    - `na-gu` = /ˈna.gu/ y `pi-ho` = /ˈpi.ho`: el acento cae en el prefijo, pero sigue")
    A("      siendo UN solo acento. Por eso la escritura con guion sí distingue derivado de frase.")
    A("22. **Origo (C-18):** el punto de vista del evidencial es SIEMPRE el hablante que")
    A("    emite la oración, salvo en **cita directa**, donde es el hablante citado.")
    A("    - Creencia ajena (= cita indirecta): `Li sa-ve ki le wa e-di wa.` = *Él sabe que el")
    A("      agua moja* — el `-di` es MÍO (me lo dijo él), no suyo.")
    A("    - Cita directa (dos origos): `Li di-an: «Mi ve-ve le ho.»` = *Él dijo: «Veo la casa».*")
    A("      El `-ve` es del hablante citado; `di-an` lleva el evidencial del que cita.")
    A("23. **Modalidad no marcada (C-19):** sin partícula final, la modalidad vale `to`")
    A("    (certeza) SOLO si el evidencial es fuerte (`-ve`, `-di`, `-sa`).")
    A("    Con `-pen` (deducción) la no marcada vale `be` (probable); con `-pen` + dato")
    A("    incompleto, `os`. La partícula explícita siempre manda.")
    A("")
    A("    | evidencial \\ explícita | (ninguna) | `to` | `be` | `os` | `ku` |")
    A("    |---|---|---|---|---|---|")
    A("    | `-ve` (vi) | to | to | be | os | os |")
    A("    | `-di` (me dijeron) | to | — | be | os | ku |")
    A("    | `-sa` (sabido) | to | to | be | os | ku |")
    A("    | `-pen` (deduzco) | be | to | be | os | ku |")
    A("")
    A("    (`—` = combinación no usada: si me lo dijeron, la certeza explícita no aporta.)")
    A("23b. **Hiato (C-38, v0.7):** no hay diptongos (1.2.5): dos vocales seguidas son")
    A("    SIEMPRE dos sílabas plenas, dentro de la palabra (`noi` = /ˈno.i/, `sui` = /ˈsu.i/)")
    A("    y en frontera de palabra (`le wa e gu` = /le.wa.e.gu/). No hay elisión ni")
    A("    coalescencia: el hiato se mantiene. El acento (regla 21) recae en la penúltima")
    A("    sílaba, contando el hiato como dos.")
    A("24b. **Homonimia derivado/frase (C-14, v0.7):** un derivado en `-i` (colores y")
    A("    relativos: `wa`→`wai`, `su`→`sui`, `som`→`somi`) es **legítimo** por la regla 17,")
    A("    aunque al escribir se lea también como dos palabras (`wai` = `wa i`). Se")
    A("    distinguen por la **prosodia** (regla 21: 1 acento vs 2) y en la escritura por")
    A("    el guion. **Casos con colisión canónica real** (la frase sí es una oración")
    A("    posible), declarados: `somi` (gris) ≈ `so mi` (*entonces yo*), `kilo` (mil) ≈")
    A("    `ki lo` (*qué lugar*). El contexto y el acento los separan; si resultan")
    A("    confusos al probarlos con hablantes, se renombran (C-24).")
    A("24c. **Colisiones canónicas declaradas (C-46/C-47, v0.7):** lista CERRADA de formas")
    A("    del léxico que se segmentan además como dos palabras en una construcción")
    A("    canónica. **No son errores**: son homófonos declarados, y los separan la")
    A("    prosodia (regla 21) y el contexto. Son **cinco**:")
    A("      · `halo` (hola) ≈ `ha lo` (*tener lugar*) — C-47, saludo de alta frecuencia")
    A("      · `kilo` (mil, ×10³) ≈ `ki lo` (*qué lugar*)")
    A("      · `mega` (millón, ×10⁶) ≈ `me ga` (*tierra grande*)")
    A("      · `nano` (nano-, ×10⁻⁹) ≈ `na no` (*no [es] noche*)")
    A("      · `somi` (gris) ≈ `so mi` (*entonces yo*)")
    A("    Los prefijos SI (`kilo`, `mega`, `nano`) se conservan: son internacionales y")
    A("    su valor numeral es inconfundible en contexto numérico. Si la prueba con")
    A("    hablantes (C-24) muestra confusión real, se renombran uno a uno.")
    A("24. **Partículas finales (nota C-21, mínima en v0.6):** la oración admite una sola")
    A("    cadena final en orden fijo `[modalidad] [actitud] [mo]`. **No se encadenan dos")
    A("    actitudes** ni dos modalidades: para dos matices, una va al final y la otra se")
    A("    expresa en el verbo. Estudio completo (qué matices merecen partícula propia) = v0.7.")
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
    A("- **Acento:** la **penúltima sílaba de la palabra fonológica** (raíz + afijos).")
    A("  Coincide con el AFI del léxico (`na-gu` /ˈna.gu/, `ru-sui` /ruˈsu.i/).")
    A("  Nunca se escribe tilde.")
    A("- **Prosodia afijo/raíz (corrige C-14):** un **afijo es átono** dentro de la")
    A("  palabra fonológica; un **monosílabo libre es tónico**. Por eso `vi-sa` (una")
    A("  palabra, acento en `vi`) ≠ `vi sa` (dos palabras, dos acentos). El guion")
    A("  marca la frontera y la fonología la distingue **al hablar**; «sin ambigüedad»")
    A("  se limita a la **escritura**.")
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
    A("- **Excepción documentada (C-10):** los **nombres propios y las marcas**, con")
    A("  mayúscula inicial, pueden conservar una ortografía que **viole la fonotáctica**")
    A("  `(C)V{m,n,s}`: coda ilegal **o grupo consonántico**. Es la única excepción a")
    A("  «una letra = un sonido» y afecta solo a nombres, nunca al léxico común. El")
    A("  autónimo y la marca del idioma es **Korlin**: `-rl-` es un grupo consonántico")
    A("  que el léxico común no admite (ninguna partición encaja en `(C)V(C)`), pero es")
    A("  marca y se conserva. Misma familia que `Mekiko`, `Faransa`, `Yapan`, `Barasila`.")
    A("- **Acento en compuestos con guion (regla 21):** el compuesto es UNA palabra")
    A("  fonológica y lleva **un solo** acento, en su penúltima sílaba: `do-lo` →")
    A("  /ˈdo.lo/, `ru-sui` → /ruˈsu.i/. Los segmentos **no** conservan acento propio.")
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
    A("Todo verbo finito factual **debe** declarar de dónde viene la información. Esto es lo que")
    A("hace la mentira cara: quien afirma debe decir si lo vio, lo dedujo, se lo contaron")
    A("o lo asume. Estudios tipológicos (Aikhenvald 2004) muestran que ~25% de las lenguas")
    A("del mundo marcan la fuente obligatoriamente; Korlin lo adopta desde el diseño.")
    A("")
    A("**Cada sufijo tiene UN valor, sin solapes (corrige C-01):**")
    A("")
    A("| Sufijo | Valor ÚNICO | Ejemplo (presente) | Traducción |")
    A("|---|---|---|---|")
    A("| `-ve` | **Directo**: lo percibí con cualquier sentido, incluidos los estados internos | `li go-ve` | *Él va (lo veo)* |")
    A("| `-pen` | **Inferido**: lo deduzco o lo calculo | `li go-pen` | *Él va (lo deduzco)* |")
    A("| `-di` | **Reportado**: me lo dijeron, lo leí o lo devolvió una herramienta | `li go-di` | *Él va (me lo dijeron)* |")
    A("| `-sa` | **Conocimiento GENERAL**: es sabido por todos, no de una fuente concreta | `le su e-sa me` | *El sol es grande (hecho general)* |")
    A("")
    A("**`-sa` NO es «supuesto».** Para lo conjetural se usa **`-pen` + modalidad `os`/`ku`**:")
    A("`li ne-go-pen os` = *quizá vaya (lo deduzco)*. Nunca `-sa` para una conjetura.")
    A("")
    A("**Pasado: el evidencial NO cambia, pero `an-` es obligatorio.**")
    A("`li an-go-ve` = *Él fue (lo vi)*; `li an-go-di` = *Él fue (me lo contaron)*.")
    A("")
    A("**Un evidencial por cláusula, en el verbo finito (el primero de la cadena).**")
    A("En `tu kan-ve ve mi` (*puedes verme*), `kan` lleva el evidencial y `ve` queda")
    A("desnudo. En una subordinada, cada cláusula finita lleva el suyo:")
    A("`mi sa-ve ki li an-go-di.`")
    A("")
    A("**El emisor nunca decide «cuánto se fía» con el evidencial: eso es la modalidad.**")
    A("")
    A("### 4.1 Tabla normativa: escenario → evidencial (corrige C-02)")
    A("")
    A("| Escenario | Evidencial | Ejemplo |")
    A("|---|---|---|")
    A("| Percibido con cualquier sentido (vista, oído, tacto, gusto, olfato) | `-ve` | `mi ve-ve le ho` = *veo la casa* |")
    A("| Estado interno (dolor, emoción, sueño, hambre) | `-ve` | `mi sen-ve tom` = *tengo calor (lo siento)* |")
    A("| Deducido, calculado, medido | `-pen` | `le nom e-pen me` = *el número es grande (lo calculo)* |")
    A("| Dicho, leído, o devuelto por un documento, API o herramienta | `-di` | `le ho e-di me` = *la casa es grande (lo leí)* |")
    A("| Conocimiento general, saber común | `-sa` | `le wa e-sa wa` = *el agua moja (es sabido)* |")
    A("| Memoria de algo vivido | `-ve` | `mi an-ve-ve le ho` = *vi la casa (la recuerdo)* |")
    A("| Sueño o ficción (contenido) | `-pen` | `mi an-mo-pen le ho` = *soñé la casa* |")
    A("| Matemáticas y lo que uno mismo construye | `-pen` | `du ka du e-pen fu` = *2+2 es 4* |")
    A("| **Futuro** que uno mismo da por hecho | `-ve` | `mi ne-go-ve` = *iré (decidido)* |")
    A("| **Futuro** planeado por otros, predicho o esperado | `-pen` | `li ne-go-pen` = *irá (lo deduzco)* |")
    A("| Acción propia pasada sin percepción directa | `-di` | `mi an-go-di` = *fui (consta)* |")
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
    A("*Korlin: la **lengua** se distribuye bajo CC BY-SA 4.0; el **código** bajo MIT. "
      "Repo: https://github.com/nachofigx/korlin.*")
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
