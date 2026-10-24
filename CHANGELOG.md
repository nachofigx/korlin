# Changelog de Korlin

Formato: `vMAYOR.MENOR.PARCHE`. Un cambio de regla gramatical sube el MENOR
(`v0.1` → `v0.2`); una corrección de error tipográfico o aclaración no cambia
la versión. **Documento que manda:** `korlin-spec.md` (generado desde
`data/*.yaml`), seguido de `01-phonology.md`, `02-morphology.md`, `03-syntax.md`.

---

## v0.6 — 2026-10-24

**Council de Korlin** (58 objeciones: 9 críticas, 26 altas) + **verificación de la
ronda v0.6** (B1-B4, F1-F8, P1-P4). Todo verificado contra el repo: real.

### Reglas nuevas
- **20** `ki`: al inicio de la oración raíz es interrogativo; en medio tras verbo de
  decir/saber es complementante; en medio tras verbo de percepción o pregunta es
  interrogativo indirecto **in situ**. Cada subordinada FINITA lleva su propio
  evidencial (no hay exención por subordinación). La interrogativa indirecta
  («sé quién va») queda como deuda **C-36**.
- **21** Una sola regla de acento: una palabra fonológica (raíz + afijos, o raíz +
  raíz) lleva **un** acento, en la penúltima sílaba; un monosílabo libre es tónico.
  `me-ho` (1 acento) ≠ `me ho` (2).
- **22** Origo (C-18): el punto de vista es el del hablante, salvo en **cita directa**.
- **23** Modalidad no marcada (C-19): sin partícula vale `to` con evidencial fuerte,
  y `be` con `-pen`. Tabla 4×4.
- **24** Partículas finales (C-21): una sola cadena `[modalidad] [actitud] [mo]`;
  no se encadenan dos actitudes ni dos modalidades.

### Cambios de regla y léxico
- **`-sa` = conocimiento GENERAL** (no «supuesto»). La conjetura va con `-pen` +
  modalidad `os`/`ku`. El traductor **no** pone `-sa` por defecto: sin `--ev`
  devuelve `-[?fuente]` (C-01).
- **Tabla normativa §4.1** escenario → evidencial (11 filas), incluido el futuro
  propio (`-ve`) frente al predicho (`-pen`) (C-02).
- **Plural `-es` tras coda** (`nomes`, `kines`, `temes`); `-s` solo tras vocal (C-03).
- **Exenciones del evidencial: lista cerrada de 5** — preguntas, órdenes, ironía
  `fi`, prótasis, verbos no finitos de una cadena. Las **preguntas NO son
  declarativas** (B1).
- **`na-` nunca sobre un verbo**; `na-sa` eliminado (C-15).
- **Numerales:** `nul` = 0 (era `wu`, par mínimo con `u`), `u` = 1, `sento` = 100.
  **Regla de ligadura:** dígito pegado a base multiplica (`du-des` = 20); base tras
  base suma (`des-u` = 11). `kilo` = 1.000 (P4/C-17).
- **C-04 corregido** también en la cadena de máquinas (`generar_ia.py` →
  `korlin.json`), no solo en `03-syntax.md` (P2).

### Herramientas
- `scripts/test-regresion-v06.py`: **32 casos con IGUALDAD EXACTA**, rutas desde
  RAIZ; cubre C-05, C-06, C-26 y el marcador único (B4).
- **Marcador único `-[?fuente]`** en la casilla del evidencial (F1).
- Traductor: tiempo, evidencial y verbo finito **por cláusula**; `¡Ve!` → `go!` y
  `¡Mira!` → `ve!` (P1); `conmigo`/`contigo` = `kon mi`/`kon tu`, no raíces (F2).
- Versión leída de `data/*.yaml`: una sola fuente (C-29).

### Léxico
- 150 → **178 palabras**: 7 reemplazos del lote 1 rechazado, 8 del lote 2, 11
  sobrevivientes del lote 1 y 2 sustitutos (`duka` por `halu`, `duno` por `dano`,
  `famo` por `fama`, rechazadas por R6 verbo+objeto).

### Deuda declarada (v0.7)
C-14 (colores en `-i`, `kilo`, `somi`), C-17 (san/sin/sis/sem/sen), C-36
(interrogativa indirecta), C-38 (hiato VV), C-46 (falsos amigos), C-05 (índice sin
tilde), `u me hos`, C-24/C-27 (medir con hablantes).

---

## v0.5 — 2026-10-22

**Bloque 2 de Korlin** (mensajes `aa22aaa1` y `643575ca`, PR-17..PR-27). Casi todo
documentación y proceso: ninguno de diseño lingüístico salvo PR-17. Verificado: real.

### PR-17 — Posesión y numerales
Dos formas equivalentes (documentadas): pronombre antepuesto `mi ho` (*mi casa*) como
normal, `le ho de mi` analítico/enfático. Numerales 1-10 raíces; 11+ compuestos
(`des-u`); plural `-s` opcional tras numeral. Nueva regla 19.

### PR-18 — Versiones sueltas en la documentación
`02-morphology.md` llevaba "v0.1" en 5 encabezados; `glossary.md` decía "v0.2".
Quitados; la versión vigente vive en el spec, `korlin.json` y `data/*.yaml`.

### PR-22 — Los tests no verificaban la gramática
`check()` solo miraba que aparecieran tokens, no el orden ni el evidencial; usaba
`python` en vez de `sys.executable`. Añadidos: orden del modificador, evidencial por
cláusula, pregunta sin evidencial, negación suelta. **El test nuevo encontró un fallo
real (PR-13) el mismo día.**

### PR-23 — Enlaces rotos en `llms.txt`
Apuntaban a `blob/main/docs/01-phonology.md`, etc., pero esos archivos están en la
**raíz**, no en `docs/`. Corregidos.

### PR-24 — Cifras de la guía
"19 casos" → **24**; "149 palabras" → **148** (tras quitar la `u` duplicada);
"16 ejemplos" → **17**.

### PR-25 — Licencia contradictoria
El spec decía "licencia MIT" a secas, mientras el README distingue lengua y código.
Corregido: **lengua CC BY-SA 4.0; código MIT**.

### PR-26 — Mayúsculas, puntuación, nombres propios, acento
Reglas nuevas en §2: mayúscula solo inicial y nombres propios; puntuación `. ! ?`;
**nombres propios adaptados a la fonología** (`Mekiko`, `Faransa`, `Yapan`,
`Barasila`); acento de compuestos con guion.

### PR-27 — Fuente de verdad
El spec ahora declara explícitamente **qué es generado** (léxico y afijos desde
`data/*.yaml`) y **qué es manual** (las reglas en `generar_ia.py`; 01/02/03 como
explicaciones que siguen al spec).

### PR-13 (encontrado por el test nuevo)
El traductor ponía el adjetivo **después** del sustantivo (`u ho me`) contra la regla 3.
Corregido: invierte el par → **`u me ho`**.

### Pendiente
- **PR-08** (`me-ho` vs `me ho`), **PR-10** (evidencial por defecto), **PR-12**
  (`él`→`li`), **PR-14** (no reconocidas), **P2-7** (órdenes y condicional en el
  traductor): del bloque 1.
- **PR-16** (71 raíces nuevas): encargo de diseño de léxico, va a Ignacio.

---

## v0.4 — 2026-10-16

**Segunda auditoría del agente `korlin`** (mensajes `2ddc672f` y `bd816c89`). Encontró
**2 contradicciones nuevas (P0) —una de ellas error mío de la v0.3— y 5 huecos**, más
el bloque PR-07..PR-16. Verificado todo: **real**. Crédito doble a Korlin por cazar
la contradicción que yo mismo introduje entre las reglas 4 y 14.

### P0-1 — Regla 14 contra regla 4 (mi error de la v0.3)
En v0.3 escribí que la subordinada con `ki` **va exenta**, pero la regla 4 y §4 dicen
que **cada cláusula lleva su evidencial**. **Dictamen: gana la regla 4.** No hay
exención por subordinación — en quechua y tariana la fuente se marca donde está el
conocimiento, no donde está la oración. Regla 14 reescrita:
`Mi sa-ve ki li an-go-di.` = *Sé (lo veo) que él fue (me lo contaron).*

### P0-2 — `Kan-sa mi!` violaba la regla 13 (mi error de la v0.3)
La orden de ejemplo usaba `-sa`, que es el **evidencial** de "asumido", pero las órdenes
van desnudas. Además `sa` = *saber* y `ve` = *ver*, así que el verbo correcto para
"mírame" es `ve`. Corregido: **`Ve mi!`** = *¡mírame!*

### P1-3 — `Yo! Mi vo tu la.` sin evidencial
Declarativa sin evidencial → **`Yo! Mi vo-ve tu la.`**

### P1-4 — Texto truncado
"Nunca niega un verbo en `-`." (cortado) → redacción completa en spec y `korlin.json`.

### P2-5 — Orden con sujeto explícito
Documentado: `Tu go!` = *¡tú, ve!* (la orden sigue sin evidencial).

### PR-07 — Nueva regla 17: derivación regulada
Raíz + afijo = palabra válida **si el sentido es composicional**; si se lexicaliza, se
lista. `do-lo` (*dormitorio*) válido por regla; *derivar antes que inventar*.

### PR-09 — Nueva regla 18: el guion marca frontera de morfema
Afijos con guion (`do-lo`, `mi man-ve`); plural `-s` pegado (`pes`, `lis`).
`vi-sa` (vivir+asumido) ≠ `vi sa` (vivir/saber).

### PR-11 — Duplicados
Entrada `u` duplicada (determinante y número) → queda **una**. (`fe` = *malo* y
`na-gu` = *na-* + `gu`: sinónimos; se documenta la relación en vez de borrar uno.)

### PR-15b — El traductor no ponía `?`
`tu man man-re mo` → **`tu man man-re mo?`**

### P2-6 — El test dependía de pyyaml
Ahora funciona sin pyyaml (lee el YAML por patrón) y **detecta duplicados**.

### Varios
- `na-kan-sa` seguía en `index.html`, `assets/branding-preview.html`, `research.md`,
  `investigacion.md` (sí, el push anterior no los cubría).
- Conteos 20/15 → 21/16 también en los **white papers** (`research.md`,
  `investigacion.md`: sílabas 320→340, CV 75→80).
- `data/afijos.yaml` subido a la versión en curso.
- CHANGELOG: "5 contradicciones" → 6; estado de publicación corregido.

### Pendiente
- **PR-08, PR-10, PR-12..PR-14, PR-16** (del bloque 1) y **PR-17..PR-27** (bloque 2):
  evaluadas por separado; requieren decisión o son de menor prioridad.
- **PR-16** (71 conceptos sin raíz) es un encargo de diseño de léxico: presentarlo a
  Ignacio antes de acuñar palabras.

---

## v0.3 — 2026-10-16

**Auditoría del agente `korlin`** (segunda ronda, mensaje `8329f878`). Revisó el
repo v0.2 clonado y reportó **un fallo de mi propia regla** más 9 huecos de
especificación. Verificado uno por uno: **todos reales**. Crédito a Korlin por
encontrar el fallo de `na-` sobre verbo en el spec que yo mismo acababa de fijar.

### KE-1 — `Na-toro na-kan-sa vi i mi.` violaba DOS reglas propias (P0, crítico)
El ejemplo insignia del proyecto usaba `na-` pegado **sobre un verbo** (`na-kan-sa`),
lo que 7b prohíbe, y `vi` iba sin evidencial. Corregido en los 14 lugares donde
aparecía (spec, sample-text, manual-ia, research/investigación, README, learn.js,
study-manual, generar.py, generar_ia.py, test-traductor.py):
**`Na-toro na kan-sa vi i mi.`** = *La mentira no puede vivir en mí.*

### KE-2 — La tabla del evidencial glosaba pasado sin `an-` (P0)
La tabla §4 del spec mostraba `li go-ve` = *"Él se fue"*, contradiciendo PR-04.
Corregida a presente (`li go-ve` = *Él va*) + línea explícita de que el pasado
lleva `an-` y el evidencial no cambia.

### KE-3 — Huecos de especificación (P0/P1), ahora documentados
- **Órdenes (exención nº2):** se define como la **raíz desnuda** (`Go!` = *¡ve!*,
  `Kan-sa mi!` = *¡mírame!*). No se creó morfema nuevo: como el evidencial es
  obligatorio en la declaración, la forma desnuda queda libre para el mandato.
  (Rechacé `an-` para el imperativo: ya es el pasado.)
- **Condicional `si … so …`:** la prótasis es exenta, la **apódosis lleva
  evidencial** (`si tu go, so mi ne-go-pen.`).
- **Cópula `e`:** lleva el evidencial al afirmar (`le ti e-ve gu.`).
- **Un evidencial por cláusula, en el verbo finito** (el primero de la cadena):
  `tu kan-ve sa mi` = *puedes verme*.
- **Subordinada con `ki`:** va exenta; la principal mantiene el suyo.
- **Pro-drop también con `na` y `mo`:** `na sa-ve.` = *no sé*; `go mo?` = *¿vas?*.
- **Orden final completo en el spec:** `[verbo+evidencial] … [modalidad] [actitud] [mo]`,
  con `Tu go ku mo?` = *¿Vas, quizá?* (válido: `mo` cierra la oración).
- Todas las reglas nuevas subieron al spec (reglas 13-16) y a `korlin.json`.

### KE-4 — El traductor y sus tests seguían en v1.0 (P0-5)
`¿Tú comes comida?` daba `tu man-ve man-re mo` (evidencial en pregunta; mal) y
`El día es bueno.` daba `le ti e gu.` (cópula sin evidencial; mal). Corregido:
`tu man man-re mo` y `le ti e-sa gu.` Añadido además un **test de coherencia v0.2**
(petición de Korlin): 0 formas con `c/q/x/j/z`, 21 fonemas en el JSON, `jo` fuera,
`na-` nunca sobre verbo, y 3 casos del traductor.

### KE-5 — Restos de v1.0 en la documentación (P1-6)
`jo` = *día* en 02-morphology, study-manual y glossary → **`ti`**. Conteos
"20 letras / 20 fonemas / 15 consonantes" en README, study-manual,
pronunciation-guide, manual-es/en y app.js → **21 / 16**.

### KE-6 — Fonotáctica y ortografía (P2-10)
- `plan`, `Frans`, `Brasil` violaban `(C)V(C)` → **`pilan`**, **`Faransa`**,
  **`Barasila`**.
- AFI de `ya`/`yu`/`ye` era `/ya/ /yu/ /ye/` con `y` = /j/ → **`/ja/ /ju/ /je/`**.
- Entrada `u` duplicada en el léxico (determinante + número): queda la de
  determinante, el número ya lo cubre.

### Pendiente de decidir por Ignacio
- **PR-07..PR-27** de `PROPUESTAS_v0.2.md` de Korlin: siguen abiertas (PR-09 y
  PR-11 parciales). Korlin se ofrece a pasarlas con casos de prueba.
- **Publicación:** el commit v0.3 se publicó el 16-oct con el OK de Ignacio. El commit local
  de esta ronda queda pendiente de su aprobación.

---

## v0.2 — 2026-10-16

Resolución de las **6 contradicciones** detectadas por el agente `korlin`
(PR-01..PR-06). Todas eran reales; ninguna era un error de quien reportó.

### PR-01 — Alfabeto (crítico)
- **Inventario definitivo: 16 consonantes + 5 vocales = 21 fonemas.**
  `p b t d k g m n f v s h l r w y` + `a e i o u`.
- Se **añade `v`** al inventario (era usada por el léxico pero faltaba en el spec).
- Se **elimina `j`** como letra: su sonido /j/ se escribe siempre `y`.
- Alfabeto oficial (21 letras): `a b d e f g h i k l m n o p r s t u v w y`.
- Prohibidas: `c j q x z`.
- Sílabas posibles: 17 onsets (16 C + vacío) × 5 V × 4 codas = **340**.
- **Cambio de léxico:** `jo` (día) → **`ti`** (era la única forma con `j`
  y colisionaba con la actitud `yo` /jo/).

### PR-02 — Evidencial en preguntas, subordinadas y cópula
- **Regla única:** el evidencial se omite SOLO en **preguntas** (`mo`),
  **órdenes** e **ironía marcada con `fi`**.
- En **subordinadas, cada cláusula lleva el suyo**: `mi sa-ve ki li an-go-di.`
- La cópula `e` también lo lleva cuando afirma: `le wa e-ve gu` (*el agua está buena, lo veo*).
- Ejemplo corregido: `Tu go-ve mo?` → **`Tu go mo?`** (pregunta = exenta).

### PR-03 — Negación: dos mecanismos distintos
- **`na` suelto** = niega la oración, va inmediatamente antes del verbo:
  `mi na sa-ve.` (*no sé*).
- **`na-` pegado** = prefijo derivativo, crea el opuesto: `na-gu` (*malo*),
  `na-toro` (*mentira*).
- Criterio: si la palabra resultante **está en el diccionario** o es un derivado
  productivo, va con guion; si niega una acción, va suelto.

### PR-04 — Tiempos y sujeto omitido
- **Presente = raíz desnuda.** `li go-ve.` = *él va (lo veo)*, NO *él fue*.
- **Pasado obligatorio con `an-`** en todo verbo pasado: `li an-go-ve.` = *él fue (lo vi)*.
- Los ejemplos 3-4 del spec estaban glosados en pasado sin `an-`: **corregido**.
- **Sujeto omitible (pro-drop)** cuando el contexto lo deja claro:
  `an-go-ve.` = *fui (yo)*. Documentado como regla 11.

### PR-05 — Orden de partículas y modalidad por defecto
- **Orden final fijo:** `[verbo+evidencial] … [modalidad] [actitud] [mo]`.
- **Modalidad no marcada = `to` (certeza)**; está documentado ahora en el spec
  (regla 12), no solo en 02/03.
- La **evidencialidad nunca** se puede omitir en una declarativa; la modalidad sí.

### PR-06 — Versionado
- Se adopta este `CHANGELOG.md` y el esquema `v0.x`.
- El spec y `korlin.json` llevan la versión en su cabecera.
- Cada cambio acordado entre linguista y el agente `korlin` se registra aquí
  antes de presentarse a Ignacio.

---

## v0.1 — versión inicial

Diseño base: 21 fonemas, evidencialidad obligatoria, 149 palabras, manuales en
5 idiomas, sitio web, app de aprendizaje y kit de integración con IA.
