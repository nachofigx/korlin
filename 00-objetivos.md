# 00 — Objetivos y alcance

## Finalidad
Lengua construida (*conlang*) "elegante y corta pero hablable":
- **Condensa conceptos** en pocos sonidos (herencia de Dutton Speedwords).
- **Fácil de pronunciar** para hablantes de las grandes lenguas del mundo.
- **Future-proof para IA**: mínima ambigüedad, ortografía fonémica 1:1,
  morfología regular y compositiva → menos tokens y parseo determinista.

## Inspiración directa
**Dutton Speedwords** (Reginald J. G. Dutton, 1922–1951):
- Palabras más frecuentes = más cortas (teoría de la información).
- Raíces de 1–3 letras; ~493 raíces base.
- Afijos derivacionales de una letra.
- Tiempo verbal con prefijos (`y-` pasado, `r-` futuro).

## Defectos de Dutton que evitamos
1. Ortografía/pronunciación irregular → aquí **1 letra = 1 sonido, siempre**.
2. Afijos vagos e impredecibles → aquí **cada afijo tiene UN significado fijo**.
3. Compuestos opacos (ky+luf = "picnic") → aquí **composición transparente y regular**.

## Principios de diseño
1. Conciso pero hablable (raíces de 1–2 sílabas; densidad media-alta, no extrema).
2. Fonología fácil y universal (sistema "neutro-internacional").
3. Ortografía fonémica perfecta (1 letra = 1 sonido, sin dígrafos ni letras mudas).
4. Frecuencia = brevedad (lo más usado es lo más corto).
5. Derivación compositiva (pocas raíces + afijos de significado fijo).
6. Sintaxis sin ambigüedad (orden fijo + marcado claro, parseable por máquina).
7. Alfabeto latino (máxima eficiencia de tokens, tecleable).

## Tipo de lengua (previsión)
Aglutinante/analítica, con tendencia aislante: palabras cortas e invariables
combinadas con afijos regulares. Orden de constituyentes por definir (etapa 03).

## Veracidad: anti-mentira (objetivo añadido)
Petición de Ignacio: ¿se puede hacer una estructura donde sea *imposible* mentir?

**Respuesta técnica:** imposible gramaticalmente (la mentira es intención/pragmática,
no forma). **Pero sí alcanzable:** hacer la mentira *costosa, explícita y detectable*
mediante tres mecanismos:
1. **Evidencialidad obligatoria** — toda afirmación debe marcar su fuente
   (directo / inferido / reportado / asumido), como el quechua, tariana y tuyuca.
2. **Modalidad epistémica** — grado de certeza (cierto / probable / posible / dudoso).
3. **Ambigüedad cero** — cada oración con una única interpretación (cf. Lojban).

Referencia: ~25% de las lenguas del mundo marcan obligatoriamente la fuente de
información (Aikhenvald 2004). La evidencialidad marca la *fuente*, no la *verdad*:
el hablante puede mentir sobre la fuente, pero al hacerlo se compromete y se expone.

Para IA: afirmaciones con fuente + certeza = trazables, verificables y contrastables
(detección de contradicciones), aunque no "infalsificables".

## Adopción masiva y modernidad (objetivo añadido)
Dirección de Ignacio: el idioma debe ser adoptado rápido por las masas, fácil,
atractivo para jóvenes, con idea de mejora, y "super moderno".

Principios resultantes:
- **Aprendibilidad**: regularidad total (cero excepciones), gramática mínima,
  vocabulario mnemotécnico, pocas raíces + composición.
- **Atractivo juvenil**: partículas de actitud/emoción, registro informal por
  defecto, sin jerarquías de cortesía, creatividad/neologismos, humor.
- **Moderno/digital**: tecleable, sin diacríticos, compatible con emoji/hashtags,
  neutralidad de género, diseño para IA.

## Emoji-mapping y comunicación con IA (ideas añadidas)

**Emoji-mapping (2 letras → emoji):** las partículas de actitud y modalidad de
Korlin (todas de 2 letras) tienen un emoji asociado. Al escribirlas en el teclado
del celular (atajos/expansiones de texto), "atraen" el emoji correspondiente.
Ej.: `yo` → ❤️, `we` → 😮, `fi` → 🙃. Digital-native al extremo.

**Comunicación con agentes de IA:** una vez aprendido, Korlin servirá para hablar
con agentes de IA. Ventajas: menos tokens (prompts más cortos/baratos), sintaxis
sin ambigüedad (parseo determinista), evidencialidad + modalidad (información con
fuente y certeza). Camino realista: traductor determinista Korlin ↔ español
(factible por la regularidad total), sin necesidad de fine-tuning.
