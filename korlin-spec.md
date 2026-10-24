# Korlin — Especificación para modelos de lenguaje (v0.6)

> **Cómo usar este archivo.** Pégalo completo en el *system prompt* (o en el primer
> mensaje) de cualquier LLM. Es autocontenido: contiene todo lo necesario para
> **hablar y traducir Korlin correctamente**. No requiere entrenamiento previo.

Korlin (exónimo **Shortlang**) es una lengua construida, regular y sin ambigüedad,
diseñada para hablar mucho en poco tiempo, con honestidad forzada por gramática
(evidencialidad obligatoria) y pensada para uso humano y con agentes de IA.
Autónimo: **korlin** = `ko` (corto) + `lin` (lengua) = *lengua corta*.
**Versión de esta especificación: v0.6** (ver `CHANGELOG.md`). Este documento manda
sobre cualquier otro; si algo no cuadra con `01/02/03`, gana este.

**Fuente de verdad y qué es generado.** `data/lexico.yaml`, `data/afijos.yaml` y
`data/traducciones.yaml` son la fuente única del **léxico y los afijos**; de ahí
salen este spec, `korlin.json`, `llms.txt`, los manuales y `lexico.js`. Las
**reglas gramaticales** (1-19) viven por ahora en `scripts/generar_ia.py` y en este
spec; `01-phonology.md`, `02-morphology.md` y `03-syntax.md` son explicaciones
manuales que deben seguir al spec, no al revés.

---

## 1. Reglas irrompibles (léelas primero)

1. **Una letra = un sonido.** Nunca hay excepciones. No existen `c`, `j`, `q`, `x`, `z`.
2. **Orden SVO.** Sujeto, Verbo, Objeto.
3. **El modificador va ANTES del núcleo:** `me ho` = *casa grande*; `gu pe` = *persona buena*.
4. **La evidencialidad es OBLIGATORIA en el verbo finito de toda oración factual.**
   (Declarativa = afirmar un hecho. **Las preguntas NO son declarativas**: no
   afirman nada, así que quedan exentas por (a).)
   **Exenciones — lista CERRADA, solo estas cinco:**
   (a) **preguntas** (`mo`, o interrogativo al inicio);
   (b) **órdenes** (raíz desnuda); (c) **ironía marcada con `fi`**;
   (d) la **prótasis** del condicional (`si …`);
   (e) los **verbos no finitos de una cadena** (el auxiliar o modal lleva el
   evidencial; el verbo de apoyo va desnudo: `tu kan-ve ve mi` = *puedes verme*).
   **No hay ninguna otra exención.**
5. **La modalidad epistémica va al final**, opcional: `to be os ku`.
6. **La actitud va al final**, opcional: `yo hu we fi bu ri pu ni la`.
7. **Negación:** hay DOS mecanismos, y no se mezclan.
   a) **`na` suelto**, inmediatamente antes del verbo → niega la oración.
      `mi na sa-ve.` = *No sé (lo veo).*
   b) **`na-` pegado**, como prefijo derivativo → crea la palabra opuesta.
      `na-gu` = *malo*, `na-toro` = *mentira* (**derivado enfático**; `fe` = *malo*
      simple). **`na-` NUNCA va sobre un verbo**, ni flexionado ni en su forma de
      diccionario: `na-sa-ve` y `na-sa` son incorrectos. Para negar una acción se
      usa siempre `na` suelto (`mi na sa-ve`), y `na sa` ≠ `na-sa-ve` porque en la
      segunda hay una palabra fonológica y el acento cae distinto.
8. **Pregunta sí/no:** `mo` al final. **Interrogativos** al inicio:
    `ki` + sustantivo = qué/cuál (`ki lo` = *qué lugar, dónde*); se antepone.
   Toda pregunta va **sin evidencial** en su propia cláusula.
9. **No hay concordancia** de género, número ni persona. Nunca.
10. **No hay artículos obligatorios**; `le` existe y es opcional.
11. **El sujeto puede omitirse** si el contexto lo deja claro (pro-drop),
    también con `na` y con `mo`: `na sa-ve.` = *no sé*; `go mo?` = *¿vas?*
12. **La modalidad epistémica no marcada equivale a `to`** (certeza),
    pero la evidencialidad NUNCA se puede omitir en una declarativa.
13. **ÓRDENES: la raíz desnuda del verbo, sin evidencial.**
    `Go!` = *¡ve!*; `Ve mi!` = *¡mírame!* No hay morfema nuevo: como el
    evidencial es obligatorio en la declaración, la forma desnuda queda libre
    para el mandato (igual que el inglés `Go!`). Es la exención nº2.
    El sujeto se omite por defecto; si va explícito, tampoco lleva evidencial:
    `Tu go!` = *¡tú, ve!*
14. **NO hay exención por subordinación.** En una subordinada, **cada cláusula
    lleva su propio evidencial** (cf. quechua, tariana; la fuente se marca donde
    está el conocimiento, no donde está la oración).
    `Mi sa-ve ki li an-go-di.` = *Sé (lo veo) que él fue (me lo contaron).*
15. **Condicional `si … so …`: la prótasis es exenta, la apódosis lleva evidencial.**
    `si tu go, so mi ne-go-pen.` = *Si vas, iré (lo deduzco).*
16. **Cópula `e`: el evidencial va en `e`.** `le ti e-ve gu.` = *El día está bueno (lo veo).*
17. **DERIVACIÓN: una raíz + un afijo derivacional válido es palabra legítima**
    si el sentido es composicional (el afijo aporta lo suyo sin sorpresa).
    `do` (dormir) + `-lo` (lugar) = `do-lo` (*dormitorio*) es válido por regla.
    Si el sentido se lexicaliza (deja de ser predecible), se LISTA en el léxico.
    Regla de oro: **derivar antes que inventar**; inventar solo si ningún afijo sirve.
18. **El guion marca frontera de morfema.** Los afijos derivacionales y flexivos
    van con guion (`do-lo`, `mi man-ve`). El plural va **pegado**: `-s` tras
    vocal (`pes`, `lis`) y **`-es` tras coda** (`nom` → `nomes`, `kin` → `kines`,
    `tem` → `temes`). Nunca dos codas seguidas. Sin guion, dos raíces seguidas
    son dos palabras: `vi-sa` (vivir+asumido) ≠ `vi sa` (vivir/saber).
19. **Posesión y numerales.** El pronombre antepuesto es la forma normal
    (`mi ho` = *mi casa*); `de` da la analítica o enfática (`le ho de mi`).
    **Numerales:** `nul` = 0, `u` = 1; 2-10 son raíces (`du san fu sin sis sem om nu des`).
    **Composición — regla de ligadura (corrige C-17):** un dígito pegado a una base
    la MULTIPLICA; una base tras otra base solo SUMA. Se escribe de mayor a menor.
    `du-des` = 20 · `des-u` = 11 · `du-des-u` = 21 · `sento` = 100 · `sento-u` = 101 ·
    `sento-des` = 110 · `du-sento` = 200 · `nu-des-nu` = 99 · `nu-sento-nu-des-nu` = 999.
    `kilo` = 1.000 como numeral suelto; como prefijo del SI va con guion a una
    unidad (`kilo-met` = *kilómetro*). El plural `-s` es opcional tras numeral.
20. **`ki` tiene dos funciones; decide la posición Y el verbo que la precede.**
    (corrige C-12 vs C-13)
    - `ki` **al inicio de la oración raíz** = interrogativo (`Ki pe go?` = *¿quién va?*).
    - `ki` **en medio tras un verbo de decir/saber** = complementante de una
      declarativa: `Mi sa-ve ki li go-ve.` = *Sé que él va.* (la subordinada FINITA
      lleva su propio evidencial, regla 14).
    - `ki` **en medio tras un verbo de percepción o pregunta** (`ve`, `ari`, `mo`) =
      interrogativo indirecto, **in situ**: `Tu ve ki pe?` = *¿a quién ves?*
    **Interrogativa indirecta («sé quién va») = deuda C-36, no tiene forma aún.**
    **Interrogativo con pro-drop:** el sujeto se omite solo si el interrogativo es
    el sujeto; si es el objeto, va **in situ**.
21. **Acento: una palabra fonológica lleva UN solo acento, en la penúltima sílaba.**
    (corrige C-14 y C-16) Una palabra fonológica = raíz + sus afijos, o raíz + raíz
    en un compuesto. Un monosílabo libre es siempre tónico.
    - `me-ho` (1 palabra, 1 acento: /ˈme.ho/) ≠ `me ho` (2 palabras, 2 acentos: /ˈme ˈho/).
    - `gu-gu` = /ˈgu.gu/ (1 acento) y `ru-sui` = /ruˈsu.i/ (1 acento).
    - `na-gu` = /ˈna.gu/ y `pi-ho` = /ˈpi.ho`: el acento cae en el prefijo, pero sigue
      siendo UN solo acento. Por eso la escritura con guion sí distingue derivado de frase.
22. **Origo (C-18):** el punto de vista del evidencial es SIEMPRE el hablante que
    emite la oración, salvo en **cita directa**, donde es el hablante citado.
    - Creencia ajena (= cita indirecta): `Li sa-ve ki le wa e-di wa.` = *Él sabe que el
      agua moja* — el `-di` es MÍO (me lo dijo él), no suyo.
    - Cita directa (dos origos): `Li di-an: «Mi ve-ve le ho.»` = *Él dijo: «Veo la casa».*
      El `-ve` es del hablante citado; `di-an` lleva el evidencial del que cita.
23. **Modalidad no marcada (C-19):** sin partícula final, la modalidad vale `to`
    (certeza) SOLO si el evidencial es fuerte (`-ve`, `-di`, `-sa`).
    Con `-pen` (deducción) la no marcada vale `be` (probable); con `-pen` + dato
    incompleto, `os`. La partícula explícita siempre manda.

    | evidencial \ explícita | (ninguna) | `to` | `be` | `os` | `ku` |
    |---|---|---|---|---|---|
    | `-ve` (vi) | to | to | be | os | os |
    | `-di` (me dijeron) | to | — | be | os | ku |
    | `-sa` (sabido) | to | to | be | os | ku |
    | `-pen` (deduzco) | be | to | be | os | ku |

    (`—` = combinación no usada: si me lo dijeron, la certeza explícita no aporta.)
24. **Partículas finales (nota C-21, mínima en v0.6):** la oración admite una sola
    cadena final en orden fijo `[modalidad] [actitud] [mo]`. **No se encadenan dos
    actitudes** ni dos modalidades: para dos matices, una va al final y la otra se
    expresa en el verbo. Estudio completo (qué matices merecen partícula propia) = v0.7.

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
- **Acento:** la **penúltima sílaba de la palabra fonológica** (raíz + afijos).
  Coincide con el AFI del léxico (`na-gu` /ˈna.gu/, `ru-sui` /ruˈsu.i/).
  Nunca se escribe tilde.
- **Prosodia afijo/raíz (corrige C-14):** un **afijo es átono** dentro de la
  palabra fonológica; un **monosílabo libre es tónico**. Por eso `vi-sa` (una
  palabra, acento en `vi`) ≠ `vi sa` (dos palabras, dos acentos). El guion
  marca la frontera y la fonología la distingue **al hablar**; «sin ambigüedad»
  se limita a la **escritura**.
- **Letras prohibidas:** `c j q x z`. La `j` no existe: /j/ se escribe `y`.
- **Aproximación para hispanohablantes:** se pronuncia como español, con `v`
  labiodental suave y `h` aspirada (como en inglés `house`).
- **Mayúscula:** solo en la primera letra de la oración y en los nombres
  propios. Nunca en medio de una palabra ni para marcar énfasis.
- **Puntuación:** `.` `!` `?` como en español; `?` cierra toda pregunta.
- **Nombres propios:** se adaptan a la fonología, no se dejan en su grafía
  original: `Mekiko` (México), `Faransa` (Francia), `Yapan` (Japón),
  `Barasila` (Brasil), `Alemania` (Alemania). Si violan `(C)V(C)`, se adaptan
  (`Frans` → `Faransa`, `Brasil` → `Barasila`).
- **Acento en compuestos con guion:** cada segmento conserva el suyo; se cuenta
  la penúltima **dentro de la palabra principal** (`do-lo` → /do.lo/).

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

Todo verbo finito factual **debe** declarar de dónde viene la información. Esto es lo que
hace la mentira cara: quien afirma debe decir si lo vio, lo dedujo, se lo contaron
o lo asume. Estudios tipológicos (Aikhenvald 2004) muestran que ~25% de las lenguas
del mundo marcan la fuente obligatoriamente; Korlin lo adopta desde el diseño.

**Cada sufijo tiene UN valor, sin solapes (corrige C-01):**

| Sufijo | Valor ÚNICO | Ejemplo (presente) | Traducción |
|---|---|---|---|
| `-ve` | **Directo**: lo percibí con cualquier sentido, incluidos los estados internos | `li go-ve` | *Él va (lo veo)* |
| `-pen` | **Inferido**: lo deduzco o lo calculo | `li go-pen` | *Él va (lo deduzco)* |
| `-di` | **Reportado**: me lo dijeron, lo leí o lo devolvió una herramienta | `li go-di` | *Él va (me lo dijeron)* |
| `-sa` | **Conocimiento GENERAL**: es sabido por todos, no de una fuente concreta | `le su e-sa me` | *El sol es grande (hecho general)* |

**`-sa` NO es «supuesto».** Para lo conjetural se usa **`-pen` + modalidad `os`/`ku`**:
`li ne-go-pen os` = *quizá vaya (lo deduzco)*. Nunca `-sa` para una conjetura.

**Pasado: el evidencial NO cambia, pero `an-` es obligatorio.**
`li an-go-ve` = *Él fue (lo vi)*; `li an-go-di` = *Él fue (me lo contaron)*.

**Un evidencial por cláusula, en el verbo finito (el primero de la cadena).**
En `tu kan-ve ve mi` (*puedes verme*), `kan` lleva el evidencial y `ve` queda
desnudo. En una subordinada, cada cláusula finita lleva el suyo:
`mi sa-ve ki li an-go-di.`

**El emisor nunca decide «cuánto se fía» con el evidencial: eso es la modalidad.**

### 4.1 Tabla normativa: escenario → evidencial (corrige C-02)

| Escenario | Evidencial | Ejemplo |
|---|---|---|
| Percibido con cualquier sentido (vista, oído, tacto, gusto, olfato) | `-ve` | `mi ve-ve le ho` = *veo la casa* |
| Estado interno (dolor, emoción, sueño, hambre) | `-ve` | `mi sen-ve tom` = *tengo calor (lo siento)* |
| Deducido, calculado, medido | `-pen` | `le nom e-pen me` = *el número es grande (lo calculo)* |
| Dicho, leído, o devuelto por un documento, API o herramienta | `-di` | `le ho e-di me` = *la casa es grande (lo leí)* |
| Conocimiento general, saber común | `-sa` | `le wa e-sa wa` = *el agua moja (es sabido)* |
| Memoria de algo vivido | `-ve` | `mi an-ve-ve le ho` = *vi la casa (la recuerdo)* |
| Sueño o ficción (contenido) | `-pen` | `mi an-mo-pen le ho` = *soñé la casa* |
| Matemáticas y lo que uno mismo construye | `-pen` | `du ka du e-pen fu` = *2+2 es 4* |
| **Futuro** que uno mismo da por hecho | `-ve` | `mi ne-go-ve` = *iré (decidido)* |
| **Futuro** planeado por otros, predicho o esperado | `-pen` | `li ne-go-pen` = *irá (lo deduzco)* |
| Acción propia pasada sin percepción directa | `-di` | `mi an-go-di` = *fui (consta)* |

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
| Posesión | `de` (o pronombre antepuesto) | `le ho de mi` = *mi casa* · `mi ho` |
| Subordinación | `ki` | `Mi sa-ve ki li an-go-di` = *Sé que él fue (me lo dijeron)* |
| Condicional | `si … so …` | `si tu go, so mi ne-go-pen` = *si vas, iré (lo deduzco)* |
| Orden | raíz desnuda | `Go!` = *¡ve!* · `Ve mi!` = *¡mírame!* |
| Cópula | `e` + evidencial | `le ti e-ve gu` = *el día está bueno (lo veo)* |

---

## 7. Léxico completo

178 palabras. Formato: **korlin** · AFI · categoría · español · inglés.

| Korlin | AFI | Categoría | Español | English |
|---|---|---|---|---|
| `e` | /e/ | partícula | ser, estar | to be |
| `a` | /a/ | preposición | a, hacia | to, toward |
| `i` | /i/ | preposición | en, dentro | in, inside |
| `o` | /o/ | conjunción | o | or |
| `nul` | /nul/ | número | 0 | 0 |
| `u` | /u/ | determinante, número | un, una, uno; 1 | a, an, one; 1 |
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
| `kotu` | /kotu/ | verbo | cerrar | close |
| `hapu` | /hapu/ | verbo | abrir | open |
| `kubi` | /kubi/ | verbo | correr | run |
| `dula` | /dula/ | sustantivo | amigo | friend |
| `hobu` | /hobu/ | sustantivo | animal | animal |
| `tusi` | /tusi/ | sustantivo | pájaro | bird |
| `tuni` | /tuni/ | sustantivo | brillo | brightness |
| `husa` | /husa/ | sustantivo | olor | smell |
| `hudi` | /hudi/ | verbo | tocar | touch |
| `hesu` | /hesu/ | sustantivo | gusto | taste |
| `huko` | /huko/ | sustantivo | ciudad | city |
| `duka` | /duka/ | sustantivo | mar | sea |
| `hisu` | /hisu/ | sustantivo | río | river |
| `hodu` | /hodu/ | sustantivo | montaña | mountain |
| `hoki` | /hoki/ | sustantivo | dinero | money |
| `tapa` | /tapa/ | verbo | trabajar | work |
| `ari` | /ari/ | verbo | oír | hear |
| `lama` | /lama/ | verbo | amar | love |
| `reme` | /reme/ | verbo | recordar | remember |
| `resi` | /resi/ | verbo | escribir | write |
| `nami` | /nami/ | verbo | nadar | swim |
| `solo` | /solo/ | adjetivo | solo | alone |
| `mama` | /mama/ | sustantivo | madre | mother |
| `papa` | /papa/ | sustantivo | padre | father |
| `poko` | /poko/ | sustantivo | comercio | trade |
| `peke` | /peke/ | sustantivo | pez | fish |
| `duno` | /duno/ | adjetivo | oscuro | dark |
| `famo` | /famo/ | sustantivo | familia | family |
| `sento` | /ˈsento/ | número | 100 | 100 |
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
17. **Yo! Mi vo-ve tu la.**
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

*Korlin: la **lengua** se distribuye bajo CC BY-SA 4.0; el **código** bajo MIT. Repo: https://github.com/nachofigx/korlin.*
