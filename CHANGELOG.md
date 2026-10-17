# Changelog de Korlin

Formato: `vMAYOR.MENOR.PARCHE`. Un cambio de regla gramatical sube el MENOR
(`v0.1` → `v0.2`); una corrección de error tipográfico o aclaración no cambia
la versión. **Documento que manda:** `korlin-spec.md` (generado desde
`data/*.yaml`), seguido de `01-phonology.md`, `02-morphology.md`, `03-syntax.md`.

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
