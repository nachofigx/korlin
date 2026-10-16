# Changelog de Korlin

Formato: `vMAYOR.MENOR.PARCHE`. Un cambio de regla gramatical sube el MENOR
(`v0.1` → `v0.2`); una corrección de error tipográfico o aclaración no cambia
la versión. **Documento que manda:** `korlin-spec.md` (generado desde
`data/*.yaml`), seguido de `01-phonology.md`, `02-morphology.md`, `03-syntax.md`.

---

## v0.2 — 2026-10-16

Resolución de las **5 contradicciones** detectadas por el agente `korlin`
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

Diseño base: 20 fonemas, evidencialidad obligatoria, 143 palabras, manuales en
5 idiomas, sitio web, app de aprendizaje y kit de integración con IA.
