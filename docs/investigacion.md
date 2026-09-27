# Korlin (Shortlang)

## White paper científico — Diseño, investigación y fundamentación de una lengua construida para la era digital

| | |
|---|---|
| **Versión** | 1.1 |
| **Fecha** | 27 de septiembre de 2026 |
| **Autoría** | Lingua (lingüista del proyecto) · Ignacio (creador del concepto) |
| **Repositorio** | https://github.com/nachofigx/korlin |
| **Licencia** | Idioma: CC BY-SA 4.0 · Código: MIT |
| **Estado** | Documento vivo — se actualiza conforme la lengua evoluciona |

---

## Resumen ejecutivo

Korlin (exónimo internacional: *Shortlang*) es una lengua construida (*conlang*) diseñada desde cero para resolver un problema concreto: **condensar la máxima información en el mínimo número de caracteres, sílabas y fonemas, sin sacrificar la pronunciabilidad, la regularidad ni la honestidad epistémica**.

El proyecto nace de la observación de que existen sistemas históricos de "taquigrafía hablada" —principalmente el **Dutton Speedwords** (Dutton, 1943)— que lograron una alta densidad de información, pero fracasaron como lenguas hablables por su irregularidad, su imposibilidad de pronunciación y su obsolescencia técnica. Korlin se posiciona como el **sucesor espiritual** de esa tradición, tomando aproximadamente el **30 % de su "ADN" conceptual** (filosofía de condensación, raíces cortas, palabras funcionales de una letra) y aportando un **70 % original** (fonología universalmente pronunciable, regularidad total, evidencialidad obligatoria, partículas emoji y un enfoque nativo-digital orientado a la inteligencia artificial).

Este documento presenta la **investigación completa** que sustenta el diseño: el estado del arte de las lenguas condensantes, los fundamentos teóricos (tasa de información del habla, evidencialidad, modalidad epistémica), el diseño fonológico, morfológico, sintáctico y léxico, las comparativas cuantitativas de longitud frente a lenguas naturales y artificiales, el análisis del fracaso histórico del Esperanto, y la arquitectura técnica del proyecto (fuente única de verdad, generación automática y open source).

**Resultado principal:** en un texto técnico de referencia, Korlin produce **388 caracteres** frente a los 660 del Esperanto (−41 %), los 690 del español (−44 %) y los 603 del inglés (−36 %), manteniendo una fonología de 20 fonemas universalmente accesible y una gramática sin excepciones.

---

## Palabras clave

lengua construida · conlang · condensación de información · evidencialidad · modalidad epistémica · Dutton Speedwords · Esperanto · fonología · morfología · sintaxis · inteligencia artificial · tokenización · adopción lingüística

---

## Índice

1. Introducción
2. Estado del arte: lenguas construidas para condensar información
3. Fundamentos teóricos
4. Fonología
5. Morfología
6. Sintaxis
7. Léxico y derivación
8. Escritura y sistema digital
9. Comparativas de longitud
10. Análisis del Esperanto y estrategia de adopción
11. Korlin y la inteligencia artificial
12. Arquitectura del proyecto (docs as code)
13. Conclusiones
14. Trabajo futuro
Referencias
Apéndice A — Vocabulario completo
Apéndice B — Afijos
Apéndice C — Texto de muestra

---

## 1. Introducción

### 1.1 Motivación y origen de la idea

La pregunta que originó el proyecto fue directa: **¿existen lenguajes creados específicamente para acortar las palabras?** — algo análogo a una *taquigrafía hablada*, pero que constituyera, además, una lengua completa y funcional.

La intuición subyacente es que la escritura y la comunicación humana contienen una redundancia significativa que podría eliminarse mediante un diseño deliberado. Si una lengua se construye desde cero con el objetivo explícito de minimizar la longitud de los mensajes, es teóricamente posible superar en densidad de información a cualquier lengua natural, cuyas formas son el producto de siglos de deriva histórica y no de optimización.

La inspiración directa fue el sistema **Dutton Speedwords**, una taquigrafía internacional creada por Reginald Dutton en las décadas de 1930 y 1940, que empleaba raíces muy cortas y palabras gramaticales de una sola letra.

### 1.2 Objetivos

Los objetivos del proyecto, definidos en su fase inicial, son los siguientes:

1. **Condensación extrema.** Palabras de una a dos sílabas que expresen conceptos completos.
2. **Pronunciabilidad universal.** Que cualquier hablante —europeo, asiático o africano— pueda articularla sin dificultad.
3. **Regularidad total.** Cero excepciones gramaticales, ortográficas o fonológicas.
4. **Honestidad epistémica.** Evidencialidad obligatoria y modalidad de certeza, de modo que mentir sea costoso y detectable.
5. **Nativo digital.** Sin signos diacríticos, compatible con emojis y diseñado para chat, móviles y agentes de IA.
6. **Future-proof para la IA.** Menos tokens por mensaje, parseo determinista y traducción por reglas.

### 1.3 Alcance y metodología

Este white paper documenta el proceso completo de investigación y diseño. La metodología combinó:

- **Revisión del estado del arte** en lenguas construidas condensantes y en evidencialidad lingüística.
- **Análisis tipológico** de fonologías, morfologías y sintaxis de lenguas naturales y artificiales.
- **Medición cuantitativa** de la longitud de textos idénticos traducidos a múltiples idiomas.
- **Iteración de diseño** con el creador del concepto, validando cada decisión contra los objetivos.

---

## 2. Estado del arte: lenguas construidas para condensar información

La idea de comprimir el lenguaje no es nueva. Este capítulo revisa los principales intentos históricos y sus resultados.

### 2.1 Speedtalk (Heinlein, 1949)

En la novela de ciencia ficción *Gulf* (1949), Robert A. Heinlein imaginó un lenguaje hipotético llamado **Speedtalk**, en el que cada fonema representaría un concepto y la combinación de fonemas construiría oraciones con una densidad de información extrema. Es un concepto puramente literario: no existe una gramática completa ni es pronunciable por humanos, pero estableció la idea cultural de "pensar y comunicarse a velocidad máxima".

### 2.2 Ithkuil (Quijada, 2004–2023)

**Ithkuil**, creado por John Quijada, es el intento más radical de **máxima densidad morfológica**. Una sola palabra de Ithkuil puede codificar lo que en una lengua natural requiere una oración completa o incluso un párrafo. Su ejemplo más célebre es la frase *Tram-mļöi hhâsmařpţuktôx* ("Por el contrario, creo que puede resultar que este áspero grupo montañoso vacila en algún momento…"). Sin embargo, su complejidad morfofonológica es tal que es **prácticamente imposible de hablar de forma espontánea**. Es un límite teórico, no una lengua de uso.

### 2.3 aUI (Weilgart, 1979)

**aUI** ("lengua del espacio"), de W. John Weilgart, intenta construir toda la semántica a partir de **31 morfemas primitivos** (por ejemplo, una vocal o una consonante representa una categoría básica como "luz", "vida", "movimiento"). Es extremadamente compacto, pero su naturaleza altamente abstracta lo hace **poco natural e inaccesible** para el aprendizaje humano.

### 2.4 Sona (Searight, 1935)

**Sona**, de Kenneth Searight, emplea unos **360 radicales** monosilábicos que se combinan para formar palabras compuestas. Es un sistema elegante y más natural que aUI, pero quedó **incompleto** y nunca alcanzó una comunidad de hablantes.

### 2.5 Toki Pona (Lang, 2001)

**Toki Pona**, de Sonja Lang, representa el extremo opuesto: con apenas **~120 palabras**, busca el **minimalismo semántico**. Su objetivo no es condensar información, sino simplificar el pensamiento reduciendo el vocabulario. Una oración en Toki Pona suele ser *más larga* que en español o inglés, porque los conceptos complejos deben descomponerse en combinaciones de palabras básicas. Es relevante aquí como contraejemplo: **menos palabras no implica menos caracteres**.

### 2.6 Dutton Speedwords (Dutton, 1943)

El sistema que inspiró directamente a Korlin. Reginald Dutton diseñó **Dutton Speedwords** como una taquigrafía internacional basada en la raíz etimológica de las palabras (principalmente latín y lenguas germánicas). Sus características clave:

- ~**493 raíces** cortas.
- **Palabras gramaticales de una letra** (por ejemplo, una sola letra para "el", "de", "y").
- **Sufijos derivacionales** sistemáticos.

Dutton logró una densidad de información muy alta. Sin embargo, adolece de limitaciones que lo hacen inviable como lengua hablada moderna:

- ❌ **No es pronunciable**: muchas palabras son consonantes sueltas sin vocal, lo que obliga a "vocales fantasma" arbitrarias.
- ❌ **Irregular**: contiene excepciones que contradicen su propia lógica.
- ❌ **Sin vocabulario técnico**: creado antes de la era digital, carece de términos para computación, internet o IA.
- ❌ **Sin evidencialidad** ni mecanismos de honestidad epistémica.

### 2.7 Lojban (Logical Language Group, 1987)

**Lojban**, descendiente del Loglan, es una lengua **lógicamente no ambigua** diseñada para la interacción humano-máquina. Su gramática es un predicado lógico formal. Aunque es sintácticamente inequívoca, **no está optimizada para la brevedad** y su aprendizaje es considerablemente más difícil que el de una lengua natural. Es un precedente del objetivo "IA-friendly", pero con un enfoque distinto al de Korlin.

### 2.8 Análisis comparativo

| Lengua | Densidad | Pronunciable | Regular | Moderna | Hablable |
|---|---|---|---|---|---|
| Speedtalk | Muy alta | No | — | No | No |
| Ithkuil | Máxima | No | Sí | No | No |
| aUI | Alta | Parcial | Sí | No | Difícil |
| Sona | Media | Sí | Parcial | No | Incompleta |
| Toki Pona | Baja | Sí | Sí | Sí | Sí |
| Dutton Speedwords | Alta | No | No | No | No |
| Lojban | Media | Sí | Sí | Parcial | Difícil |
| **Korlin** | **Alta** | **Sí** | **Sí** | **Sí** | **Sí** |

**Conclusión:** el espacio de diseño de una lengua que sea simultáneamente *corta, pronunciable, regular, moderna y hablable* estaba vacío. Korlin lo ocupa.

---

## 3. Fundamentos teóricos

### 3.1 La tasa de información del habla (Pellegrino et al., 2011)

Un hallazgo central de la psicolingüística contemporánea es que las lenguas humanas transmiten información a una **tasa casi constante de ~39 bits por segundo** (Pellegrino, Coupé & Marsico, 2011).

El estudio midió dos magnitudes contrapuestas:

- La **densidad de información por sílaba** (cuánta información codifica cada sílaba).
- La **velocidad de articulación** (cuántas sílabas se pronuncian por segundo).

Los resultados muestran una **compensación** sistemática: las lenguas con sílabas muy densas (como el mandarín) se hablan con menos sílabas por segundo, mientras que las lenguas con sílabas ligeras (como el español o el japonés) se hablan con más sílabas por segundo. El producto de ambas magnitudes converge en ~39 bits/s.

**Implicación para Korlin:** existe un **cuello de botella cognitivo** humano, no lingüístico, que limita la velocidad de transmisión *hablada*. La ventaja de Korlin, por tanto, no reside en "hablar más rápido" (imposible, por el límite cognitivo), sino en **usar menos caracteres, menos sílabas y menos tokens para el mismo mensaje**. Esto es decisivo en los canales donde el límite cognitivo no opera: la **escritura**, la **transmisión digital** y la **tokenización** para modelos de lenguaje.

### 3.2 Evidencialidad y modalidad epistémica

La **evidencialidad** es la categoría gramatical que codifica la **fuente de la información** de una afirmación. Es un fenómeno bien documentado en la tipología lingüística.

| Lengua | Sistema evidencial | Ejemplo |
|---|---|---|
| **Quechua** | Sufijos obligatorios | `-mi` (directo), `-shi` (reportado), `-chi` (inferido) |
| **Tariana** (Amazonia) | Evidencialidad obligatoria en cada oración | No se puede afirmar "llovió" sin indicar *cómo se sabe* |
| **Tuyuca** (Amazonia) | Cinco categorías evidenciales | Visual, no visual, aparente, de segunda mano, asumido |

El dato clave: **aproximadamente el 25 % de las lenguas del mundo marcan la fuente de forma obligatoria** (Aikhenvald, 2004). La evidencialidad no es, por tanto, un artificio de Korlin, sino un rasgo natural que la mayoría de las lenguas europeas simplemente perdieron.

La **modalidad epistémica**, por su parte, codifica el **grado de certeza** del hablante (cierto, probable, posible, dudoso). Es distinta de la evidencialidad (que indica *fuente*) y complementaria a ella (indica *confianza*).

### 3.3 ¿Es posible hacer "imposible mentir"?

Una de las aspiraciones originales del proyecto fue diseñar una lengua donde **mentir fuera estructuralmente imposible**.

**Respuesta técnica (honesta):** No. La mentira es una **intención pragmática** —decir deliberadamente algo que se sabe falso—, no una propiedad de la estructura gramatical. Ninguna gramática puede impedir que un hablante articule una proposición falsa con conocimiento de causa.

**Lo que sí es alcanzable** es hacer la mentira **costosa, explícita y detectable**, mediante tres mecanismos combinados:

1. **Evidencialidad obligatoria** (`-ve` directo, `-pen` inferido, `-di` reportado, `-sa` asumido): toda afirmación debe declarar su fuente.
2. **Modalidad epistémica** (`to` cierto, `be` probable, `os` posible, `ku` dudoso): toda afirmación debe declarar su grado de certeza.
3. **Actos de habla marcados** (partículas de actitud, incluida `fi` para la ironía): la intención comunicativa se hace explícita.

Con este sistema, un hablante que desee mentir debe **elegir deliberadamente una marca falsa** (por ejemplo, marcar como "directo" algo que solo conoce de oídas). Esa elección deja un rastro gramatical que puede ser verificado y refutado. La mentira deja de ser "gratuita" y se vuelve **responsabilizable**.

---

## 4. Fonología

La fonología de Korlin está diseñada para maximizar la **facilidad de pronunciación universal** y minimizar la interferencia con las lenguas maternas de los hablantes.

### 4.1 Inventario fonémico (20 fonemas)

**Consonantes (15):**

| Letra | AFI | Punto/modo | Sonoridad | Referencia aproximada |
|---|---|---|---|---|
| p | /p/ | bilabial oclusiva | sorda | "p" |
| b | /b/ | bilabial oclusiva | sonora | "b" |
| t | /t/ | alveolar oclusiva | sorda | "t" |
| d | /d/ | alveolar oclusiva | sonora | "d" |
| k | /k/ | velar oclusiva | sorda | "k" |
| g | /g/ | velar oclusiva | sonora | "g" |
| m | /m/ | bilabial nasal | sonora | "m" |
| n | /n/ | alveolar nasal | sonora | "n" |
| f | /f/ | labiodental fricativa | sorda | "f" |
| s | /s/ | alveolar fricativa | sorda | "s" |
| h | /h/ | glotal fricativa | sorda | "h" (inglés *house*) |
| l | /l/ | alveolar lateral | sonora | "l" |
| r | /ɾ/ | alveolar vibrante simple | sonora | "r" (español *pero*) |
| w | /w/ | labiovelar aproximante | sonora | "w" (inglés *water*) |
| y | /j/ | palatal aproximante | sonora | "y" (inglés *yes*) |

**Vocales (5):**

| Letra | AFI | Descripción |
|---|---|---|
| a | /a/ | abierta (central/baja) |
| e | /e/ | semicerrada anterior |
| i | /i/ | cerrada anterior |
| o | /o/ | semicerrada posterior |
| u | /u/ | cerrada posterior |

**Sonidos que NO existen en Korlin** (para evitar interferencias): /x/ (jota española), /θ/, /ʃ/ ("sh"), /tʃ/ ("ch"), /v/, /z/, /ŋ/ ("ng"), /ʒ/.

### 4.2 Fonotáctica (sílabas permitidas)

La estructura silábica es **(C) V (C)**, donde la coda consonántica solo puede ser {m, n, s}.

Reglas:

1. **Ataque (onset) opcional**: cualquier consonante, o vacío.
2. **Núcleo obligatorio**: una única vocal.
3. **Coda opcional**: solo /m/, /n/ o /s/.
4. **Sin grupos consonánticos** (prohibidos "pr", "st", "kt", etc.).
5. **Sin diptongos**: /j/ y /w/ solo aparecen como ataque; cada vocal forma su propia sílaba (p. ej. "ai" se lee /a.i/, dos sílabas).

Sílabas válidas: `a`, `e`, `ka`, `te`, `mi`, `so`, `lu`, `kan`, `sen`, `los`, `nam`, `sis`, `tan`, `wan`.
Sílabas inválidas: `stra` (grupo), `kri` (grupo), `ek` (coda /k/), `kast` (doble coda).

**Total de sílabas posibles** = 16 ataques × 5 vocales × 4 codas = **320 sílabas**. De ellas, las **75 sílabas CV** (15 consonantes × 5 vocales) forman la base de la guía de pronunciación para estudiantes.

### 4.3 Acento

- El acento recae **siempre en la penúltima sílaba**.
- Las palabras monosílabas no llevan acento especial.
- Al ser predecible, **nunca se escribe** (no se usan tildes).

### 4.4 Ortografía (romanización oficial)

- **1 letra = 1 fonema, siempre.** Sin dígrafos, sin letras mudas, sin tildes.
- Alfabeto (20 letras, en orden): `a b d e f g h i k l m n o p r s t u w y`.
- Letras latinas no utilizadas: `c, j, q, v, x, z` (redundantes con otras letras de Korlin).

### 4.5 Justificación tipológica

- El sistema de **5 vocales** /a e i o u/ es el más común del mundo (español, italiano, japonés, griego, suajili, hawaiano…).
- **Sin contraste de sonoridad en las fricativas** (solo /f s h/ sordas): el español y el japonés también carecen del par /s/–/z/, simplificación que maximiza la facilidad.
- **Vibrante simple /ɾ/** en lugar de vibrante múltiple /r/: la /ɾ/ es tipológicamente mucho más frecuente y fácil.
- Todas las consonantes elegidas figuran entre las más frecuentes del mundo.
- 15 consonantes + 5 vocales se compara con el español (~18 C + 5 V), el italiano (~21 C + 7 V) y el japonés (~14 C + 5 V): **más simple que la mayoría**.

La **pronunciación neutra tipo español/latín** se eligió deliberadamente por ser la más accesible para el mayor número de hablantes, evitando sonidos difíciles (aspiradas, tonos, guturales) que dificultarían la adopción por hablantes de Asia y África.

---

## 5. Morfología

### 5.1 Tipo morfológico

Korlin es una lengua de tipo **aglutinante-aislante**: las palabras raíz son cortas e invariables, y los afijos se añaden de forma regular y transparente, sin fusión (cada afijo conserva una única forma y un único significado). No hay flexión de género, número obligatorio en el adjetivo ni concordancia.

### 5.2 Flexión gramatical

| Categoría | Sistema | Ejemplo |
|---|---|---|
| Plural | sufijo `-s` | `pe` (persona) → `pes` (personas) |
| Pasado | prefijo `an-` (de *an* "viejo") | `go` (ir) → `an-go` (fue) |
| Futuro | prefijo `ne-` (de *ne* "nuevo") | `go` → `ne-go` (irá) |
| Presente | sin marca | `go` = va (presente) |

### 5.3 Evidencialidad obligatoria

| Marca | Significado | Ejemplo |
|---|---|---|
| `-ve` | directo (lo vi/lo viví) | `go-ve` = "va (lo veo)" |
| `-pen` | inferido (lo deduzco) | `go-pen` = "va (lo infiero)" |
| `-di` | reportado (me lo contaron) | `go-di` = "va (me lo dijeron)" |
| `-sa` | asumido (se sabe por convención) | `go-sa` = "va (se asume)" |

La evidencialidad es **obligatoria** en toda oración declarativa: no se puede afirmar un hecho sin declarar su fuente.

### 5.4 Modalidad epistémica

| Partícula | Significado |
|---|---|
| `to` | cierto ✅ |
| `be` | probable 👍 |
| `os` | posible 🤔 |
| `ku` | dudoso ⚠️ |

### 5.5 Derivación (afijos productivos)

| Afijo | Función | Ejemplo |
|---|---|---|
| `-pe` | agente (persona que X) | `sa` (saber) → `sa-pe` (sabio) |
| `-lo` | lugar (donde se X) | `man` (comer) → `man-lo` (comedor) |
| `-re` | cosa/objeto | `man` → `man-re` (comida) |
| `-i` | adjetivo relacional | `su` (sol) → `su-i` (solar) |
| `-ro` | abstracto (cualidad) | `gu` (bueno) → `gu-ro` (bondad) |
| `na-` | opuesto/negativo | `toro` (verdad) → `na-toro` (mentira) |
| `me-` | aumentativo | `ho` (casa) → `me-ho` (mansión) |
| `pi-` | diminutivo | `ho` → `pi-ho` (casita) |

La derivación es el mecanismo central de expansión del léxico: a partir de un núcleo reducido de raíces, los afijos generan sistemáticamente nuevas palabras sin inflar el diccionario.

---

## 6. Sintaxis

### 6.1 Orden de constituyentes: SVO

Korlin usa el orden **Sujeto–Verbo–Objeto (SVO)**, el más común y fácil del mundo (español, inglés, chino…).

- `mi go a le ho.` — "Voy a la casa."
- Glosado: `mi` (yo) `go` (ir) `a` (a) `le` (el) `ho` (casa).

### 6.2 Frase nominal: modificador antes del núcleo

Los adjetivos y determinantes van **antes** del sustantivo (como en inglés y chino).

- `le gu pe` = "la buena persona" (`le` el + `gu` bueno + `pe` persona).
- `me ho` = "casa grande" (`me` grande + `ho` casa).

Orden canónico: `[determinante] [adjetivo] [sustantivo]`.

### 6.3 Preposiciones

Las preposiciones van **antes** del sustantivo: `a` (a/hacia), `i` (en), `de` (de/desde), `kon` (con), `po` (por/para).

### 6.4 Negación

La partícula `na` va **antes** del verbo (o de la cópula).

- `mi na sa.` — "No sé."

### 6.5 Interrogación

- **Pregunta sí/no**: partícula `mo` al final. `tu go mo?` = "¿Vas?"
- **Interrogativas**: la palabra interrogativa (`ki pe` quién, `ki lo` dónde, `ki tem` cuándo…) va **al inicio**. `ki pe e i le ho?` = "¿Quién está en la casa?"

### 6.6 Subordinación

`ki` introduce oraciones subordinadas y relativas. **Cada cláusula lleva su propio evidencial** (cada afirmación declara su fuente).

- `mi sa-ve ki li an-go-di.` — "Sé que él se fue (me lo contaron)."
- Glosado: `mi` yo `sa-ve` saber-DIRECTO `ki` que `li` él `an-go-di` PASADO-ir-REPORTADO.

### 6.7 Posesión

Con `de`: `le ho de mi` = "mi casa" (literalmente "la casa de mí").

### 6.8 Alineamiento

**Nominativo-acusativo sin casos**: el sujeto y el objeto se distinguen por el orden SVO (sujeto antes del verbo, objeto después). No hay marcación de caso.

### 6.9 Orden de partículas finales

`[verbo + evidencial] … [modalidad epistémica] [actitud] [mo]`

- `li go-di ku bu.` — "Él se fue (me lo contaron, dudoso) 😤."

**Resumen de reglas sintácticas:** (1) orden SVO; (2) modificador antes del núcleo; (3) preposición antes del sustantivo; (4) negación `na` antes del verbo; (5) `mo` al final para sí/no, interrogativas al inicio; (6) subordinación con `ki` y evidencial en cada cláusula; (7) posesión con `de`; (8) sin casos; (9) partículas finales en orden fijo.

---

## 7. Léxico y derivación

### 7.1 Estrategia de construcción del léxico

El léxico de Korlin se construye sobre un **núcleo reducido de raíces monosilábicas y bisilábicas** de alta frecuencia, que se expanden mediante los afijos derivacionales (sección 5.5) y la composición. Esta economía radical permite un vocabulario funcional con un número mínimo de formas.

Actualmente el diccionario contiene **143 palabras núcleo**, organizadas por categorías y almacenadas en `data/lexico.yaml` (fuente de verdad única). El vocabulario completo, con su transcripción AFI, se reproduce en el **Apéndice A**.

### 7.2 Economía de los colores

Un ejemplo de la filosofía de condensación: en lugar de raíces independientes para cada color, Korlin define solo **3 colores primarios** y deriva el resto de raíces ya existentes:

| Color | Raíz | Origen |
|---|---|---|
| rojo | `ru` | raíz propia |
| verde | `gi` | raíz propia |
| rosa | `ro` | raíz propia |
| blanco | `lum-i` | de `lum` (luz) |
| negro | `no-i` | de `no` (noche) |
| amarillo | `su-i` | de `su` (sol) |
| azul | `wa-i` | de `wa` (agua) |
| marrón | `ga-i` | de `ga` (tierra) |
| morado | `lu-i` | de `lu` (luna) |
| gris | `som-i` | de `som` (sombra) |
| naranja | `ru-su-i` | rojo-amarillo (compuesto) |

### 7.3 Matemáticas y prefijos SI

| Operación | Korlin | | Prefijo | Valor |
|---|---|---|---|---|
| sumar | `sum` (+) | | kilo | ×1000 |
| restar | `min` (−) | | mega | ×10⁶ |
| multiplicar | `fan` (×) | | giga | ×10⁹ |
| dividir | `fen` (÷) | | mili | ÷1000 |
| | | | miko | micro- |
| | | | nano | nano- |

### 7.4 Países (nombres propios adaptados)

`Mekiko` (México) · `Espan` (España) · `Kina` (China) · `Frans` (Francia) · `Brasil` (Brasil) · `Yapan` (Japón). El gentilicio se forma con `-i`.

### 7.5 Slang (mecanismos iniciales)

El slang de Korlin se construye mediante mecanismos productivos:

- **Reduplicación**: `gu-gu` = "guay, súper bueno" (de `gu`, bueno).
- **Derivación coloquial**: `me-ku` = "ni de broma" (de `me-` aumentativo + `ku` dudoso).
- **Partículas de actitud** (sección 8.2) para el tono emocional.

---

## 8. Escritura y sistema digital

### 8.1 Romanización

Korlin se escribe con el alfabeto latino de 20 letras, sin diacríticos ni dígrafos. La romanización es biunívoca: **cada letra corresponde a exactamente un sonido y viceversa**, lo que elimina toda ambigüedad de lectura.

### 8.2 Partículas de actitud → emojis

Una innovación clave, propuesta por Ignacio: **dos letras de Korlin disparan el emoji correspondiente** en el teclado del móvil. Las partículas de actitud son morfemas que expresan emoción y se mapean directamente a emojis:

| Partícula | Emoji | Emoción |
|---|---|---|
| `yo` | ❤️ | alegría |
| `we` | 😮 | sorpresa |
| `fi` | 🙃 | ironía/sarcasmo |
| `ri` | 😂 | risa |
| `hu` | 😢 | tristeza |
| `bu` | 😤 | enfado |
| `la` | 🥰 | cariño |
| `pu` | 🤢 | asco |
| `ni` | 😨 | miedo |

Esto convierte a Korlin en una lengua **nativo-digital**: expresiva, informal y perfecta para la comunicación en chat y móviles.

### 8.3 Compatibilidad con la IA

El diseño biunívoco (1 letra = 1 sonido), la ausencia de diacríticos y la gramática sin excepciones hacen que Korlin sea **óptimo para el procesamiento por máquinas**: no hay ambigüedad ortográfica, el parseo es determinista y la tokenización es mínima.

---

## 9. Comparativas de longitud

### 9.1 Metodología

Para cuantificar la ventaja de condensación de Korlin, se tradujo un texto técnico de referencia a múltiples idiomas y se midió su longitud en **caracteres** (y, secundariamente, en sílabas y palabras). El texto de referencia describe a un arquitecto japonés y su herramienta de estudio volumétrico, e incluye terminología técnica (planos, volúmenes, sombras, regulaciones, IA).

### 9.2 Resultados (texto largo)

| Idioma | Caracteres | Diferencia vs Korlin |
|---|---|---|
| **Korlin** | **388** | — |
| Dutton (estilo) | 338 | +15 % (Dutton más corto) |
| Japonés (romaji) | 565 | −31 % |
| Inglés | 603 | −36 % |
| Chino (pinyin) | 616 | −37 % |
| Esperanto | 660 | −41 % |
| Español | 690 | −44 % |
| Francés | 729 | −47 % |
| Alemán | 759 | −49 % |

### 9.3 Resultados (frase corta)

Frase de ejemplo: **"La mentira no puede vivir en mí."**

| Idioma | Caracteres |
|---|---|
| Dutton (estilo) | 21 |
| **Korlin** | **26** |
| Inglés | 26 |
| Esperanto | 31 |
| Español | 32 |
| Alemán | 33 |
| Japonés (romaji) | 37 |
| Francés | 37 |
| Chino (pinyin) | 38 |

### 9.4 Resumen de ahorros

- **−44 %** caracteres frente al español.
- **−36 %** caracteres frente al inglés.
- **−31 %** caracteres frente al japonés (romaji).
- **−41 %** caracteres y **−50 %** sílabas frente al Esperanto.
- **−49 %** caracteres frente al alemán.

**Nota sobre Dutton:** Dutton es un 13 % más corto en bruto, pero esa ventaja es un **espejismo**: no es pronunciable (consonantes sueltas y "vocales fantasma"), es irregular, carece de vocabulario técnico y de evidencialidad. Korlin es la versión **funcional** de esa idea.

---

## 10. Análisis del Esperanto y estrategia de adopción

### 10.1 Por qué el Esperanto no conquistó el mundo

Korlin se posiciona como "la competencia del Esperanto, 100 veces mejor". Para sustentar esta afirmación, se analizaron las causas del fracaso histórico del Esperanto (Zamenhof, 1887) como lengua universal:

| Problema | Detalle |
|---|---|
| Diacríticos raros | ĉ, ĝ, ĥ, ĵ, ŝ, ŭ — difíciles de teclear y escribir |
| Eurocentrismo | Vocabulario y estructura casi exclusivamente europeos |
| Acusativo `-n` | Regla extraña que confunde a los aprendices |
| Concordancia | Adjetivos y sustantivos deben concordar en caso y número |
| Sexismo | Sufijos femeninos derivados del masculino |
| Grupos consonánticos incómodos | `knabino`, `scii` |
| Diseño del siglo XIX | No pensado para internet, móviles ni IA |

Korlin corrige **todas** estas carencias: sin diacríticos, sin casos, sin concordancia, neutro, inclusivo y nativo digital.

### 10.2 Estrategia de adopción

La dirección de adopción definida para Korlin es: **rápida por las masas, fácil, atractiva para los jóvenes, "super moderna", con una idea de mejora**. Los pilares son:

1. **Facilidad total** — regularidad sin excepciones.
2. **Juventud** — emojis, informal, digital.
3. **Modernidad** — sin diacríticos, listo para chat y móviles.
4. **Honestidad** — evidencialidad obligatoria (valor diferencial ético).
5. **IA** — eficiencia de tokens y parseo determinista.

### 10.3 Métricas de posicionamiento (reales, verificadas)

- **~41 % más corto** que el Esperanto (caracteres).
- **~44 % más corto** que el español.
- **~30 % del "ADN"** conceptual de Dutton Speedwords.

---

## 11. Korlin y la inteligencia artificial

Un objetivo central del proyecto es **usar Korlin para comunicarse con agentes de IA**.

### 11.1 Ventajas para la IA

- **Menos tokens** → textos más cortos = menor coste de procesamiento por mensaje.
- **Parseo determinista** → gramática 100 % regular y sin ambigüedades.
- **Evidencialidad obligatoria** → la IA declara la fuente de su información (trazabilidad).
- **Modalidad epistémica** → la IA declara su grado de certeza (mejor calibración).
- **Traducción por reglas** Korlin ↔ español/inglés (viable sin aprendizaje automático).

### 11.2 Visión

La visión es un **traductor por reglas** que permita a humanos y agentes comunicarse en Korlin de forma eficiente, reduciendo el coste computacional y aumentando la transparencia epistémica de las respuestas de la IA.

---

## 12. Arquitectura del proyecto (docs as code)

### 12.1 Fuente única de verdad

El proyecto sigue una arquitectura de **"docs as code"**: todo el contenido (vocabulario, afijos, gramática) vive en archivos YAML que actúan como fuente única de verdad.

```
data/lexico.yaml        ← vocabulario (fuente de verdad)
data/traducciones.yaml  ← traducciones fr/zh/ja
data/afijos.yaml        ← afijos
        ↓
scripts/generar.py      ← generador
        ↓
5 manuales (ES/EN/FR/ZH/JA) + manual IA + lexico.js
```

**Un cambio en la fuente se refleja automáticamente en todos los idiomas y en el sitio web.**

### 12.2 Idiomas de documentación

- **Inglés (principal)** — audiencia de GitHub.
- **Español, francés, chino y japonés** — alcance global.
- **Manual para IA** — para que agentes aprendan Korlin.

### 12.3 Open source y gobernanza

- **Repositorio público:** https://github.com/nachofigx/korlin
- **Licencias:** MIT (código) · CC BY-SA 4.0 (el idioma).
- **Control de evolución:** Lingua es la mantenedora; la comunidad propone mediante PR/issues.

### 12.4 Detalles técnicos de implementación

- **Nombre:** Shortlang (exónimo) / **Korlin** (endónimo) /ˈkoɾlin/ = `ko` (corto) + `lin` (lengua). Se verificó que no colisionara con marcas relevantes (existe el lenguaje de programación *Kotlin*, riesgo bajo para un proyecto de distinta naturaleza).
- **Síntesis de voz (TTS):** configurada con voz neutra `es-MX-DaliaNeural` (español neutro con seseo), compatible con la fonología Korlin (solo /s/, sin /θ/).
- **Publicación:** el repositorio se publicó en GitHub autenticando con token almacenado en `~/.git-credentials` (sin exponer credenciales en comandos).

---

## 13. Conclusiones

1. El espacio de diseño de una lengua **corta, pronunciable, regular, moderna y hablable** estaba vacío; Korlin lo ocupa, tomando lo mejor del Dutton Speedwords (condensación) y corrigiendo sus defectos.
2. La **condensación** de Korlin es cuantificable: −44 % caracteres vs español, −36 % vs inglés, −41 % vs Esperanto.
3. La ventaja real no está en "hablar más rápido" (limitado por el cuello de botella cognitivo de ~39 bits/s), sino en **usar menos caracteres, sílabas y tokens** — decisivo para la escritura y la IA.
4. **"Hacer imposible mentir"** no es gramaticalmente alcanzable, pero la **evidencialidad obligatoria + modalidad epistémica + actos de habla marcados** hacen la mentira costosa, explícita y detectable — un valor diferencial único.
5. La **arquitectura docs-as-code** garantiza coherencia entre idiomas y soporta la evolución controlada del idioma.

---

## 14. Trabajo futuro

| Componente | Estado |
|---|---|
| Fonología (20 fonemas) | ✅ Definida |
| Gramática y morfología | ✅ Definida |
| Léxico (143 palabras) | ✅ Creciendo |
| Documentación en 5 idiomas + IA | ✅ |
| Open source en GitHub | ✅ Publicado |
| Sitio web interactivo (5 idiomas) | ✅ En vivo |
| CI/CD (despliegue automático) | ⬜ Pendiente |
| Traductor/parser real para IA | ⬜ Pendiente |
| Lanzamiento a la comunidad | ⬜ Pendiente |

---

## Referencias

1. Aikhenvald, A. Y. (2004). *Evidentiality*. Oxford: Oxford University Press.
2. Pellegrino, F., Coupé, C., & Marsico, E. (2011). A cross-language perspective on speech information rate. *Language*, 87(3), 539–558.
3. Dutton, R. (1943). *Dutton Speedwords*. London: Dutton Publications.
4. Quijada, J. (2004). *Ithkuil: A Philosophical Design for a Hypothetical Language*.
5. Lang, S. (2014). *Toki Pona: The Language of Good*.
6. Searight, K. (1935). *Sona: An Auxiliary Neutral Language*.
7. Weilgart, W. J. (1979). *aUI: The Language of Space*.
8. Zamenhof, L. L. (1887). *Lingvo Internacia* (Esperanto).

---

## Apéndice A — Vocabulario completo (143 palabras)

> Transcripción fonémica en AFI entre barras. Categorías tal como se almacenan en `data/lexico.yaml`.

### A.1 Partículas y funcionales

| Forma | AFI | Categoría | Español | Inglés |
|---|---|---|---|---|
| e | /e/ | partícula | ser, estar | to be |
| a | /a/ | preposición | a, hacia | to, toward |
| i | /i/ | preposición | en, dentro | in, inside |
| o | /o/ | conjunción | o | or |
| u | /u/ | determinante | un, una, uno | a, an, one |
| ka | /ka/ | conjunción | y | and |
| ba | /ba/ | conjunción | pero | but |
| ki | /ki/ | conjunción | que, qué | that, which, what |
| si | /si/ | conjunción | si (condicional) | if |
| so | /so/ | conjunción | entonces, así que | then, so |
| na | /na/ | adverbio | no (negación) | no, not |
| ya | /ya/ | adverbio | sí | yes |
| de | /de/ | preposición | de | of, from |
| kon | /kon/ | preposición | con | with |
| po | /po/ | preposición | por, para | for, by |
| mo | /mo/ | partícula | ¿? (pregunta sí/no) | question particle |
| halo | /ˈhalo/ | saludo | hola | hello |

### A.2 Pronombres

| Forma | AFI | Español | Inglés |
|---|---|---|---|
| mi | /mi/ | yo | I, me |
| tu | /tu/ | tú | you |
| li | /li/ | él, ella | he, she |
| wi | /wi/ | nosotros | we |
| yu | /yu/ | vosotros, ustedes | you all |
| lis | /lis/ | ellos, ellas | they |

### A.3 Determinantes

| Forma | AFI | Español | Inglés |
|---|---|---|---|
| le | /le/ | el, la | the |
| se | /se/ | este, esta | this |
| te | /te/ | ese, esa | that |
| ke | /ke/ | aquel, aquella | that (over there) |

### A.4 Verbos

| Forma | AFI | Español | Inglés |
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

### A.5 Sustantivos

| Forma | AFI | Español | Inglés |
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

### A.6 Adjetivos

| Forma | AFI | Español | Inglés |
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

### A.7 Técnicas

| Forma | AFI | Español | Inglés |
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

### A.8 Números

| Forma | AFI | Valor |
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

### A.9 Partículas de actitud (emoji)

| Forma | AFI | Emoción |
|---|---|---|
| yo | /jo/ | alegría ❤️ |
| hu | /hu/ | tristeza 😢 |
| we | /we/ | sorpresa 😮 |
| fi | /fi/ | ironía 🙃 |
| bu | /bu/ | enfado 😤 |
| ri | /ri/ | risa 😂 |
| pu | /pu/ | asco 🤢 |
| ni | /ni/ | miedo 😨 |
| la | /la/ | cariño 🥰 |

### A.10 Modalidad epistémica

| Forma | AFI | Certeza |
|---|---|---|
| to | /to/ | cierto ✅ |
| be | /be/ | probable 👍 |
| os | /os/ | posible 🤔 |
| ku | /ku/ | dudoso ⚠️ |

### A.11 Colores

| Forma | AFI | Español | Inglés |
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

### A.12 Matemáticas y prefijos SI

| Forma | AFI | Función |
|---|---|---|
| sum | /sum/ | sumar (+) |
| min | /min/ | restar (−) |
| fan | /fan/ | multiplicar (×) |
| fen | /fen/ | dividir (÷) |
| kilo | /ˈkilo/ | ×1000 |
| mega | /ˈmega/ | ×10⁶ |
| giga | /ˈgiga/ | ×10⁹ |
| mili | /ˈmili/ | ÷1000 |
| miko | /ˈmiko/ | micro- |
| nano | /ˈnano/ | nano- |

### A.13 Países y slang

| Forma | AFI | Español | Inglés |
|---|---|---|---|
| Mekiko | /meˈkiko/ | México | Mexico |
| Espan | /eˈspan/ | España | Spain |
| Kina | /ˈkina/ | China | China |
| Frans | /frans/ | Francia | France |
| Brasil | /bɾaˈsil/ | Brasil | Brazil |
| gu-gu | /ˈgugu/ | guay (reduplicación) | cool |
| me-ku | /ˈmeku/ | ni de broma | no way |

---

## Apéndice B — Afijos

### B.1 Flexivos (gramaticales)

| Afijo | Tipo | Función | Ejemplo |
|---|---|---|---|
| -s | sufijo | plural | `li → lis` (él → ellos) |
| an- | prefijo | pasado | `an-go` = fue |
| ne- | prefijo | futuro | `ne-go` = irá |
| -ve | sufijo | evidencial directo | `go-ve` = va (lo veo) |
| -pen | sufijo | evidencial inferido | `go-pen` = va (lo infiero) |
| -di | sufijo | evidencial reportado | `go-di` = va (me lo contaron) |
| -sa | sufijo | evidencial asumido | `go-sa` = va (se asume) |

### B.2 Derivacionales

| Afijo | Tipo | Función | Ejemplo |
|---|---|---|---|
| -pe | sufijo | agente | `sa-pe` = sabio |
| -lo | sufijo | lugar | `man-lo` = comedor |
| -re | sufijo | cosa | `man-re` = comida |
| -i | sufijo | adjetivo relacional | `su-i` = solar |
| -ro | sufijo | abstracto | `gu-ro` = bondad |
| na- | prefijo | opuesto/negativo | `na-gu` = malo |
| me- | prefijo | aumentativo | `me-gu` = excelente |
| pi- | prefijo | diminutivo | `pi-ho` = casita |

---

## Apéndice C — Texto de muestra

Texto de presentación de Korlin, con glosado y traducción:

**Korlin:** `Halo! Mi e-sa Korlin. Mi e-sa u ko lin. Mi e-sa ra ka gu. Na-toro na-kan-sa vi i mi. Mi pa-ve kon pe ka kon kin. Tu kan-ve sa mi. Ven kon mi yo!`

**Glosado (morfema por morfema):**

| Segmento | Análisis |
|---|---|
| Halo | hola |
| Mi e-sa Korlin | yo ser-ASUMIDO Korlin → "yo soy Korlin" |
| Mi e-sa u ko lin | yo ser-ASUMIDO una corta lengua → "soy una lengua corta" |
| Mi e-sa ra ka gu | yo ser-ASUMIDO rápida y buena → "soy rápida y buena" |
| Na-toro na-kan-sa vi i mi | mentira no-poder-ASUMIDO vivir en mí → "la mentira no puede vivir en mí" |
| Mi pa-ve kon pe ka kon kin | yo hablar-DIRECTO con persona y con máquina → "hablo con personas y con máquinas" |
| Tu kan-ve sa mi | tú poder-DIRECTO saber yo → "puedes aprenderme" |
| Ven kon mi yo | ven con yo ALEGRÍA → "¡ven conmigo! ❤️" |

**Traducción:** "¡Hola! Yo soy Korlin. Soy una lengua corta. Soy rápida y buena. La mentira no puede vivir en mí. Hablo con personas y con máquinas. Puedes aprenderme. ¡Ven conmigo! ❤️"

---

*Documento generado a partir de la investigación completa del proyecto Korlin. Es un documento vivo y se actualiza conforme la lengua evoluciona.*
