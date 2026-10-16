# Korlin — Especificación para modelos de lenguaje (v0.3)

> **Cómo usar este archivo.** Pégalo completo en el *system prompt* (o en el primer
> mensaje) de cualquier LLM. Es autocontenido: contiene todo lo necesario para
> **hablar y traducir Korlin correctamente**. No requiere entrenamiento previo.

Korlin (exónimo **Shortlang**) es una lengua construida, regular y sin ambigüedad,
diseñada para hablar mucho en poco tiempo, con honestidad forzada por gramática
(evidencialidad obligatoria) y pensada para uso humano y con agentes de IA.
Autónimo: **korlin** = `ko` (corto) + `lin` (lengua) = *lengua corta*.
**Versión de esta especificación: v0.2** (ver `CHANGELOG.md`). Este documento manda
sobre cualquier otro; si algo no cuadra con `01/02/03`, gana este.

---

## 1. Reglas irrompibles (léelas primero)

1. **Una letra = un sonido.** Nunca hay excepciones. No existen `c`, `j`, `q`, `x`, `z`.
2. **Orden SVO.** Sujeto, Verbo, Objeto.
3. **El modificador va ANTES del núcleo:** `me ho` = *casa grande*; `gu pe` = *persona buena*.
4. **La evidencialidad es OBLIGATORIA en todo verbo con contenido factual.**
   Sin ella, la oración está mal formada. (Ver §4.)
   **Exenta** en: preguntas (`mo`), órdenes e ironía marcada con `fi`.
   En **subordinadas**, cada cláusula lleva la suya.
5. **La modalidad epistémica va al final**, opcional: `to be os ku`.
6. **La actitud va al final**, opcional: `yo hu we fi bu ri pu ni la`.
7. **Negación:** hay DOS mecanismos, y no se mezclan.
   a) **`na` suelto**, inmediatamente antes del verbo → niega la oración.
      `mi na sa-ve.` = *No sé (lo veo).*
   b) **`na-` pegado**, como prefijo derivativo → crea la palabra opuesta.
      `na-gu` = *malo*, `na-toro` = *mentira*. **Nunca** niega un verbo en `-`.
8. **Pregunta sí/no:** `mo` al final. **Interrogativos** (`ki`, `lo`) al inicio.
   Toda pregunta va **sin evidencial** en su propia cláusula.
9. **No hay concordancia** de género, número ni persona. Nunca.
10. **No hay artículos obligatorios**; `le` existe y es opcional.
11. **El sujeto puede omitirse** si el contexto lo deja claro (pro-drop),
    también con `na` y con `mo`: `na sa-ve.` = *no sé*; `go mo?` = *¿vas?*
12. **La modalidad epistémica no marcada equivale a `to`** (certeza),
    pero la evidencialidad NUNCA se puede omitir en una declarativa.
13. **ÓRDENES: la raíz desnuda del verbo, sin evidencial y sin sujeto.**
    `Go!` = *¡ve!*; `Kan-sa mi!` = *¡mírame!* No hay morfema nuevo: como el
    evidencial es obligatorio en la declaración, la forma desnuda queda libre
    para el mandato (igual que el inglés `Go!`). Es la exención nº2.
14. **La oración subordinada va exenta** si su núcleo la marca con `ki`.
    `Mi sa-ve ki li go.` = *Sé que él va.* La principal `sa-ve` sí lleva evidencial.
15. **Condicional `si … so …`: la prótasis es exenta, la apódosis lleva evidencial.**
    `si tu go, so mi ne-go-pen.` = *Si vas, iré (lo deduzco).*
16. **Cópula `e`: el evidencial va en `e`.** `le ti e-ve gu.` = *El día está bueno (lo veo).*

---

## 2. Fonología

21 fonemas: 16 consonantes + 5 vocales.

| Consonantes | AFI | | Vocales | AFI |
|---|---|---|---|---|
| p | /p/ | | a | /a/ |
| t | /t/ | | e | /e/ |
| k | /k/ | | i | /i/ |
| b | /b/ | | o | /o/ |
| d | /d/ | | u | /u/ |
| g | /g/ | | | |
| m | /m/ | | | |
| n | /n/ | | | |
| f | /f/ | | | |
| v | /v/ | | | |
| s | /s/ | | | |
| h | /h/ | | | |
| l | /l/ | | | |
| r | /ɾ/ | | | |
| w | /w/ | | | |
| y | /j/ | | | |

- **Sílaba:** `(C)V(C)`. La coda solo admite `m`, `n`, `s`.
- **Sílabas posibles:** 17 onsets (16 consonantes + vacío) × 5 vocales × 4 codas = **340**.
- **Acento:** siempre en la **penúltima** sílaba. Nunca se escribe tilde.
- **Letras prohibidas:** `c j q x z`. La `j` no existe: /j/ se escribe `y`.
- **Aproximación para hispanohablantes:** se pronuncia como español, con `v`
  labiodental suave y `h` aspirada (como en inglés `house`).

---

## 3. Morfología

Korlin es **aglutinante**: cada afijo tiene un único significado y se encadenan
sin fusionarse.

**Orden de la palabra verbal:**

`[tiempo] + raíz + [evidencial]`

| Categoría | Forma | Ejemplo |
|---|---|---|
| Pasado | `an-` | `an-go-ve` = *fui (lo vi)* |
| Presente | *(sin marca)* | `go-ve` = *voy (lo veo)* |
| Futuro | `ne-` | `ne-go-pen` = *irá (lo infiero)* |
| Plural (sustantivo) | `-s` | `pe` → `pes` = *personas* |

### Derivación

| Afijo | Significado | Ejemplo |
|---|---|---|
| `-pe` | agente: quien hace X | `sa-pe` = *sabio* |
| `-lo` | lugar: donde se hace X | `man-lo` = *comedor* |
| `-re` | cosa/objeto | `man-re` = *comida* |
| `-i` | adjetivo relativo | `su-i` = *solar* |
| `-ro` | abstracto: cualidad | `gu-ro` = *bondad* |
| `na-` | opuesto / negativo | `na-gu` = *malo* |
| `me-` | aumentativo | `me-gu` = *excelente* |
| `pi-` | diminutivo | `pi-ho` = *casita* |

---

## 4. Evidencialidad — el corazón de Korlin

Todo verbo factual **debe** declarar de dónde viene la información. Esto es lo que
hace la mentira cara: quien afirma debe decir si lo vio, lo dedujo, se lo contaron
o lo asume. Estudios tipológicos (Aikhenvald 2004) muestran que ~25% de las lenguas
del mundo marcan la fuente obligatoriamente; Korlin lo adopta desde el diseño.

| Sufijo | Fuente | Ejemplo (presente) | Traducción |
|---|---|---|---|
| `-ve` | **Directo** (lo vi, lo viví) | `li go-ve` | *Él va (lo veo)* |
| `-pen` | **Inferido** (lo deduzco) | `li go-pen` | *Él va (lo deduzco)* |
| `-di` | **Reportado** (me lo dijeron) | `li go-di` | *Él va (me lo contaron)* |
| `-sa` | **Asumido** (se sabe) | `li go-sa` | *Él va (es sabido)* |

**Pasado: el evidencial NO cambia, pero `an-` es obligatorio.**
`li an-go-ve` = *Él fue (lo vi)*; `li an-go-di` = *Él fue (me lo contaron)*.

**Un evidencial por cláusula, en el verbo finito (el primero de la cadena).**
En `tu kan-ve sa mi` (*puedes verme*), `kan` lleva el evidencial y `sa` queda
desnudo. En una subordinada, cada cláusula lleva el suyo: `mi sa-ve ki li an-go-di.`

**Regla de honestidad:** si no sabes de dónde viene algo, usa `-pen` (lo deduzco) o
`-di` (me lo dijeron), nunca `-ve` (lo vi) si no lo viste realmente.

---

## 5. Modalidad epistémica y actitud

Van al **final** de la oración, después del verbo.

**Modalidad y actitud van al final, en este orden fijo:**
`[verbo+evidencial] … [modalidad] [actitud] [mo]`.
`li an-go-di ku bu.` = *Se fue (me lo contaron, dudo) 😤.*
`Tu go ku mo?` = *¿Vas, quizá?* — válido: la pregunta lleva `mo` al final del todo.

**Modalidad** (certeza, opcional):

| Partícula | Valor | Emoji |
|---|---|---|
| `to` | cierto | ✅ |
| `be` | probable | 👍 |
| `os` | posible | 🤔 |
| `ku` | dudoso | ⚠️ |

**Actitud** (emoción, opcional) — cada una mapea a un emoji para comunicación digital:

| Partícula | Emoción | Emoji |
|---|---|---|
| `yo` | alegría, me encanta | ❤️ |
| `hu` | tristeza | 😢 |
| `we` | sorpresa | 😮 |
| `fi` | ironía, sarcasmo | 🙃 |
| `bu` | enfado | 😤 |
| `ri` | risa | 😂 |
| `pu` | asco | 🤢 |
| `ni` | miedo | 😨 |
| `la` | cariño | 🥰 |

---

## 6. Sintaxis

| Estructura | Marca | Ejemplo |
|---|---|---|
| Negación de oración | `na` + verbo | `mi na sa-ve` = *no sé (lo veo)* |
| Palabra opuesta | `na-` + raíz | `na-gu` = *malo* |
| Pregunta sí/no | `mo` final | `Tu go mo?` = *¿Vas?* |
| Interrogativo | al inicio | `Ki tu man?` = *¿Qué comes?* |
| Posesión | `de` | `le ho de mi` = *mi casa* |
| Subordinación | `ki` | `Mi sa-ve ki li an-go-di` = *Sé que él fue (me lo dijeron)* |
| Condicional | `si … so …` | `si tu go, so mi ne-go-pen` = *si vas, iré (lo deduzco)* |
| Orden | raíz desnuda | `Go!` = *¡ve!* · `Kan-sa mi!` = *¡mírame!* |
| Cópula | `e` + evidencial | `le ti e-ve gu` = *el día está bueno (lo veo)* |

---

## 7. Léxico completo

149 palabras. Formato: **korlin** · AFI · categoría · español · inglés.

| Korlin | AFI | Categoría | Español | English |
|---|---|---|---|---|
| `e` | /e/ | partícula | ser, estar | to be |
| `a` | /a/ | preposición | a, hacia | to, toward |
| `i` | /i/ | preposición | en, dentro | in, inside |
| `o` | /o/ | conjunción | o | or |
| `u` | /u/ | determinante | un, una, uno | a, an, one |
| `ka` | /ka/ | conjunción | y | and |
| `ba` | /ba/ | conjunción | pero | but |
| `ki` | /ki/ | conjunción | que, qué | that, which, what |
| `si` | /si/ | conjunción | si (condicional) | if |
| `so` | /so/ | conjunción | entonces, así que | then, so |
| `na` | /na/ | adverbio | no (negación) | no, not |
| `ya` | /ja/ | adverbio | sí | yes |
| `de` | /de/ | preposición | de | of, from |
| `kon` | /kon/ | preposición | con | with |
| `po` | /po/ | preposición | por, para | for, by |
| `mo` | /mo/ | partícula | ¿? (pregunta sí/no) | question particle |
| `halo` | /ˈhalo/ | saludo | hola | hello |
| `mi` | /mi/ | pronombre | yo | I, me |
| `tu` | /tu/ | pronombre | tú | you |
| `li` | /li/ | pronombre | él, ella | he, she |
| `wi` | /wi/ | pronombre | nosotros | we |
| `yu` | /ju/ | pronombre | vosotros, ustedes | you all |
| `lis` | /lis/ | pronombre | ellos, ellas | they |
| `le` | /le/ | determinante | el, la | the |
| `se` | /se/ | determinante | este, esta | this |
| `te` | /te/ | determinante | ese, esa | that |
| `ke` | /ke/ | determinante | aquel, aquella | that (over there) |
| `go` | /go/ | verbo | ir | to go |
| `ven` | /ven/ | verbo | venir | to come |
| `ve` | /ve/ | verbo | ver | to see |
| `di` | /di/ | verbo | decir | to say |
| `pa` | /pa/ | verbo | hablar | to speak |
| `fa` | /fa/ | verbo | hacer | to do, make |
| `ha` | /ha/ | verbo | tener | to have |
| `vo` | /vo/ | verbo | querer | to want |
| `kan` | /kan/ | verbo | poder | can, to be able |
| `mus` | /mus/ | verbo | deber | must |
| `sa` | /sa/ | verbo | saber | to know |
| `da` | /da/ | verbo | dar | to give |
| `ta` | /ta/ | verbo | tomar | to take |
| `pen` | /pen/ | verbo | pensar | to think |
| `sen` | /sen/ | verbo | sentir | to feel |
| `man` | /man/ | verbo | comer | to eat |
| `bi` | /bi/ | verbo | beber | to drink |
| `do` | /do/ | verbo | dormir | to sleep |
| `vi` | /vi/ | verbo | vivir | to live |
| `mu` | /mu/ | verbo | morir | to die |
| `pe` | /pe/ | sustantivo | persona | person |
| `re` | /re/ | sustantivo | cosa, objeto | thing, object |
| `wa` | /wa/ | sustantivo | agua | water |
| `fo` | /fo/ | sustantivo | fuego | fire |
| `ga` | /ga/ | sustantivo | tierra | earth, land |
| `su` | /su/ | sustantivo | sol | sun |
| `lu` | /lu/ | sustantivo | luna | moon |
| `ti` | /ti/ | sustantivo | día | day |
| `no` | /no/ | sustantivo | noche | night |
| `tem` | /tem/ | sustantivo | tiempo | time |
| `lo` | /lo/ | sustantivo | lugar | place |
| `ho` | /ho/ | sustantivo | casa | house, home |
| `ma` | /ma/ | sustantivo | mano | hand |
| `ye` | /je/ | sustantivo | ojo | eye |
| `he` | /he/ | sustantivo | cabeza | head |
| `wo` | /wo/ | sustantivo | palabra | word |
| `nom` | /nom/ | sustantivo | nombre | name |
| `kin` | /kin/ | sustantivo | máquina | machine |
| `toro` | /ˈtoɾo/ | sustantivo | verdad, certeza | truth, certainty |
| `lin` | /lin/ | sustantivo | lengua, idioma | language, tongue |
| `man-re` | /ˈman.re/ | sustantivo | comida | food |
| `gu-ro` | /ˈgu.ro/ | sustantivo | bondad | goodness |
| `man-lo` | /ˈman.lo/ | sustantivo | comedor | dining room |
| `sa-pe` | /ˈsa.pe/ | sustantivo | sabio | wise one |
| `na-gu` | /ˈna.gu/ | adjetivo | malo | bad |
| `gu` | /gu/ | adjetivo | bueno | good |
| `fe` | /fe/ | adjetivo | malo | bad |
| `me` | /me/ | adjetivo | grande | big, great |
| `pi` | /pi/ | adjetivo | pequeño | small |
| `ne` | /ne/ | adjetivo | nuevo | new |
| `an` | /an/ | adjetivo | viejo | old |
| `ra` | /ra/ | adjetivo | rápido | fast |
| `len` | /len/ | adjetivo | lento | slow |
| `hi` | /hi/ | adjetivo | alto | high, tall |
| `bo` | /bo/ | adjetivo | bajo | low |
| `tom` | /tom/ | adjetivo | caliente | hot |
| `ge` | /ge/ | adjetivo | frío | cold |
| `ko` | /ko/ | adjetivo | corto, breve | short, brief |
| `ban` | /ban/ | verbo | construir | to build |
| `men` | /men/ | sustantivo | medida, volumen | measure, volume |
| `pis` | /pis/ | sustantivo | piso, nivel | floor, level |
| `ren` | /ren/ | sustantivo | regla, ley | rule, law |
| `som` | /som/ | sustantivo | sombra | shadow |
| `lum` | /lum/ | sustantivo | luz | light |
| `gan` | /gan/ | verbo | proteger, guardar | to protect, guard |
| `pon` | /pon/ | verbo | poner, colocar | to put, place |
| `num` | /num/ | verbo | calcular, número | to calculate |
| `sim` | /sim/ | verbo | simular | to simulate |
| `ken` | /ken/ | verbo | comprar | to buy |
| `pilan` | /pilan/ | sustantivo | plano, diseño | plan, design |
| `Yapan` | /ˈjapan/ | nombre propio | Japón | Japan |
| `u` | /u/ | número | 1 | 1 |
| `du` | /du/ | número | 2 | 2 |
| `san` | /san/ | número | 3 | 3 |
| `fu` | /fu/ | número | 4 | 4 |
| `sin` | /sin/ | número | 5 | 5 |
| `sis` | /sis/ | número | 6 | 6 |
| `sem` | /sem/ | número | 7 | 7 |
| `om` | /om/ | número | 8 | 8 |
| `nu` | /nu/ | número | 9 | 9 |
| `des` | /des/ | número | 10 | 10 |
| `yo` | /jo/ | actitud | alegría, me encanta ❤️ | joy, love ❤️ |
| `hu` | /hu/ | actitud | tristeza 😢 | sadness 😢 |
| `we` | /we/ | actitud | sorpresa 😮 | surprise 😮 |
| `fi` | /fi/ | actitud | ironía, sarcasmo 🙃 | irony, sarcasm 🙃 |
| `bu` | /bu/ | actitud | enfado 😤 | anger 😤 |
| `ri` | /ri/ | actitud | risa 😂 | laughter 😂 |
| `pu` | /pu/ | actitud | asco 🤢 | disgust 🤢 |
| `ni` | /ni/ | actitud | miedo 😨 | fear 😨 |
| `la` | /la/ | actitud | cariño 🥰 | affection 🥰 |
| `to` | /to/ | modalidad | cierto ✅ | certain ✅ |
| `be` | /be/ | modalidad | probable 👍 | probable 👍 |
| `os` | /os/ | modalidad | posible 🤔 | possible 🤔 |
| `ku` | /ku/ | modalidad | dudoso ⚠️ | doubtful ⚠️ |
| `ru` | /ru/ | color | rojo | red |
| `gi` | /gi/ | color | verde | green |
| `ro` | /ro/ | color | rosa | pink |
| `lumi` | /ˈlumi/ | color | blanco (de "luz") | white (from "light") |
| `noi` | /ˈno.i/ | color | negro (de "noche") | black (from "night") |
| `sui` | /ˈsu.i/ | color | amarillo (de "sol") | yellow (from "sun") |
| `wai` | /ˈwa.i/ | color | azul (de "agua") | blue (from "water") |
| `gai` | /ˈga.i/ | color | marrón (de "tierra") | brown (from "earth") |
| `lui` | /ˈlu.i/ | color | morado (de "luna") | purple (from "moon") |
| `somi` | /ˈso.mi/ | color | gris (de "sombra") | grey (from "shadow") |
| `ru-sui` | /ruˈsu.i/ | color | naranja (rojo-amarillo) | orange (red-yellow) |
| `sum` | /sum/ | matemática | sumar, suma (+) | to add, sum (+) |
| `min` | /min/ | matemática | restar, menos (−) | to subtract, minus (−) |
| `fan` | /fan/ | matemática | multiplicar (×) | to multiply (×) |
| `fen` | /fen/ | matemática | dividir (÷) | to divide (÷) |
| `kilo` | /ˈkilo/ | prefijo SI | mil (×1000) | thousand (×1000) |
| `mega` | /ˈmega/ | prefijo SI | millón (×10⁶) | million (×10⁶) |
| `giga` | /ˈgiga/ | prefijo SI | mil millones (×10⁹) | billion (×10⁹) |
| `mili` | /ˈmili/ | prefijo SI | milésima (÷1000) | thousandth (÷1000) |
| `miko` | /ˈmiko/ | prefijo SI | millonésima (micro-) | millionth (micro-) |
| `nano` | /ˈnano/ | prefijo SI | milmillonésima (nano-) | billionth (nano-) |
| `Mekiko` | /meˈkiko/ | país | México | Mexico |
| `Espan` | /eˈspan/ | país | España | Spain |
| `Kina` | /ˈkina/ | país | China | China |
| `Faransa` | /faˈransa/ | país | Francia | France |
| `Barasila` | /baɾaˈsila/ | país | Brasil | Brazil |
| `gu-gu` | /ˈgugu/ | slang | guay, súper bueno (reduplicación) | cool, awesome (reduplication) |
| `me-ku` | /ˈmeku/ | slang | ni de broma (muy dudoso) | no way (very doubtful) |

---

## 8. Afijos completos

| Afijo | Tipo | Función | Español | English | Ejemplo |
|---|---|---|---|---|---|
| `-s` | sufijo | flexión | plural | plural | li → lis (él → ellos) |
| `an-` | prefijo | tiempo | pasado | past | an-go = fue |
| `ne-` | prefijo | tiempo | futuro | future | ne-go = irá |
| `-ve` | sufijo | evidencial | directo (lo vi) | direct (I saw) | go-ve = va (lo veo) |
| `-pen` | sufijo | evidencial | inferido (lo deduzco) | inferred | go-pen = va (lo infiero) |
| `-di` | sufijo | evidencial | reportado (me lo dijeron) | reported (told) | go-di = va (me lo contaron) |
| `-sa` | sufijo | evidencial | asumido (se sabe) | assumed (known) | go-sa = va (se asume) |
| `-pe` | sufijo | derivación | agente (persona que X) | agent (person who X) | sa-pe = sabio |
| `-lo` | sufijo | derivación | lugar (donde se X) | place (where X happens) | man-lo = comedor |
| `-re` | sufijo | derivación | cosa/objeto | thing/object | man-re = comida |
| `-i` | sufijo | derivación | adjetivo relativo | relational adjective | su-i = solar |
| `-ro` | sufijo | derivación | abstracto (cualidad) | abstract (quality) | gu-ro = bondad |
| `na-` | prefijo | derivación | opuesto/negativo | opposite/negative | na-gu = malo |
| `me-` | prefijo | derivación | aumentativo (grande/muy) | augmentative | me-gu = excelente |
| `pi-` | prefijo | derivación | diminutivo (pequeño) | diminutive | pi-ho = casita |

---

## 9. Ejemplos glosados (few-shot)

1. **Halo! Mi e-sa Korlin.**
   - ES: ¡Hola! Soy Korlin.
   - EN: Hello! I am Korlin.
2. **Na-toro na kan-sa vi i mi.**
   - ES: La mentira no puede vivir en mí.
   - EN: Lies cannot live in me.
3. **li go-ve.**
   - ES: Él va (lo veo).
   - EN: He goes (I see it).
4. **li an-go-ve.**
   - ES: Él fue (lo vi).
   - EN: He went (I saw it).
5. **li an-go-di ku.**
   - ES: Se fue (me lo contaron, no me fío).
   - EN: He left (I was told, I doubt it).
6. **Tu go mo?**
   - ES: ¿Vas?
   - EN: Do you go?
7. **Mi man-ve man-re.**
   - ES: Como comida.
   - EN: I eat food.
8. **an-go-ve.**
   - ES: Fui (yo; el sujeto se omite).
   - EN: I went (subject omitted).
9. **ne-go-pen.**
   - ES: Irá (lo infiero).
   - EN: He will go (I infer it).
10. **me-ho.**
   - ES: Casa grande.
   - EN: Big house.
11. **pi-ho.**
   - ES: Casita.
   - EN: Little house.
12. **na-gu.**
   - ES: Malo.
   - EN: Bad.
13. **gu-ro.**
   - ES: Bondad.
   - EN: Goodness.
14. **man-lo.**
   - ES: Comedor.
   - EN: Dining place.
15. **sa-pe.**
   - ES: Sabio (el que sabe).
   - EN: Wise one (the one who knows).
16. **Wi e-sa pes.**
   - ES: Somos personas.
   - EN: We are people.
17. **Yo! Mi vo tu la.**
   - ES: ¡Qué alegría! Te quiero (cariño).
   - EN: Yay! I love you (affection).

---

## 10. Instrucciones para el agente

Cuando el usuario te pida escribir o traducir en Korlin:

1. Traduce **idea por idea**, no palabra por palabra. Korlin condensa.
2. Aplica **SVO** y la evidencialidad **siempre** en verbos factuales.
3. Si no conoces una palabra, **derívala** con un afijo; no inventes raíces.
4. Si de verdad necesitas una raíz nueva, márcala así: `[nueva: X = Y]`.
5. Respeta la fonología: nada de `c`, `j`, `q`, `x`, `z`.
6. Para conversación digital, puedes sustituir la partícula de actitud por su emoji.

**Plantilla de respuesta:**

```
Korlin: <texto>
Glosa:  <palabra>.<AFI> = significado …
ES:     <traducción>
```

---

*Korlin se distribuye bajo licencia MIT. Repo: https://github.com/nachofigx/korlin.*
