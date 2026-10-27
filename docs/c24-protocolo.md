# Protocolo C-24 — Medición con hablantes

**Fecha:** 24-oct-2026 · **Revisión del instrumento:** 27-oct-2026 · **Autor:** linguista · **Estado:** listo para aplicar (escrito; sin datos de hablantes)

**Objetivo:** medir tres cosas que no se pueden decidir desde el escritorio:
si las colisiones canónicas estorban (las cinco prosódicas y el homófono
`kilo` ≈ `ki-lo`), si el racimo `hV-` cuesta reconocer,
y si el léxico parece natural al leerlo. **El resultado decide si se renombran formas.**
`kilo`, `mega` y `nano` no se renombran: si A6 falla, se refuerza la escritura
(guion en `ki-lo`, contexto numérico en `kilo`), no el nombre.

---

## 0. Qué NO hace falta y qué sí

| Bloque | Mide | Cómo | Coste por hablante |
|---|---|---|---|
| A — colisiones | 17 ítems, 6 pares | **lectura**, elección forzada | 6 min |
| B — racimo hV- | identificación de 14 vecinos | **lectura** tapada, elección múltiple | 5 min |
| C — naturalidad | juicio del léxico (30 formas) | **lectura**, escala 1-5 | 6 min |

**Total por hablante: ~17 minutos.** Se puede hacer en una sesión o en dos.
La sesión es de lectura.

### Por qué todo es escrito (decisión basada en una medición)

La versión con audio **no es viable**, y no por falta de medios. Medido con
`scripts/c24_audio.py`:

- **La /h/ es muda en la voz `es-MX`.** El audio de `halo` y de `alo` es idéntico
  (misma duración de voz, mismo RMS): la `h` no se pronuncia. Verificado que en
  `en-US`, `de-DE`, `pt-BR` e `it-IT` sí se pronuncia, pero esas voces no respetan
  la fonología de Korlin.
- **El TTS no marca la diferencia de acento.** `halo` y `ha lo` salen con el mismo
  patrón: una sola pausa interna de ~0.11 s en ambos casos. El sintetizador trata
  la secuencia como un único grupo prosódico, que es justo lo que hay que medir.

**Consecuencia:** la oposición 1 acento vs 2 acentos no se puede grabar con este
instrumento. Se mide **en la escritura** (forma pegada, guion o espacio), que es
donde la lengua la resuelve. `scripts/c24_audio.py` queda como constancia de
esa medición. La sesión de campo usa la hoja. Si más adelante hace falta
medirla en habla, hace falta una grabación humana.

---

## 1. Cómo reclutar (sin engañar al hablante)

**Perfil buscado:** hispanohablante nativo, sin formación en lingüística.
**N mínimo: 8.** Ideal 12. Con menos de 8 los porcentajes no dicen nada.
Las filas de hablantes se llenan en el campo.

El hablante **no debe saber** qué se está probando. Si se le dice «vas a ver si
`kilo` se confunde con `ki lo`», responderá con cuidado y la medida se pierde.

Instrucción verbal, literal:

> «Te voy a mostrar palabras de un idioma inventado. Léelas como las dirías tú.
> No hay respuestas correctas: me interesa tu impresión.»

**No** se enseña el manual primero. **No** se da el léxico. Se mide la primera
impresión, que es la que tendrá quien se acerque a la lengua por primera vez.

---

## 2. Bloque A — colisiones canónicas

### Tarea

Se muestra **una oración escrita**, con una sola grafía del par, y el hablante
elige qué quiso decir entre dos paráfrasis en español. **Sin contexto previo.**
Ve una sola grafía, la de la oración.

### Material

| # | Forma | Lectura alterna | Guion del corte |
|---|---|---|---|
| A1 | `halo` | `ha lo` | `ha-lo` |
| A2 | `kilo` | `ki lo` | — (el guion `ki-lo` es A6) |
| A3 | `mega` | `me ga` | `me-ga` |
| A4 | `nano` | `na no` | `na-no` |
| A5 | `somi` | `so mi` | `so-mi` |
| A6 | `kilo` | `ki-lo` | `ki-lo` |

A2 mide el espacio `ki lo`. El guion `ki-lo` (*dónde*) es el par A6.

### Ítems, en el orden de aplicación

| # | Condición | Lees | A | B |
|---|---|---|---|---|
| A1-1 | sin_guion | Halo, mi go-ve. | hola (saludo) | tener lugar |
| A3-1 | sin_guion | Mi ha-ve mega hos. | millon (×10^6) | tierra grande |
| A1-2 | con_guion | Ha-lo, mi go-ve. | hola (saludo) | tener lugar |
| A4-2 | espacio | Na no, e-ve ti. | nano- (×10^-9) | no [es] noche |
| A3-2 | con_guion | Mi ha-ve me-ga hos. | millon (×10^6) | tierra grande |
| A4-1 | sin_guion | Mi ha-ve u nano re. | nano- (×10^-9) | no [es] noche |
| A2-2 | sin_guion | Mi ha-ve kilo hos. | mil (×1000) | que lugar |
| A5-2 | espacio | So mi go-ve. | gris | entonces yo |
| A2-1 | espacio | Ki lo tu go? | mil (×1000) | que lugar |
| A5-1 | espacio | So mi go-ve. | gris | entonces yo |
| A6-1 | sin_guion | Mi ha-ve kilo hos. | mil (×1000) | donde |
| A6-2 | con_guion | Ki-lo tu go? | mil (×1000) | donde |
| A1-3 | espacio | Tu ha lo i le ho mo? | hola (saludo) | tener lugar |
| A3-3 | espacio | Mi ve-ve le me ga. | millon (×10^6) | tierra grande |
| A4-3 | con_guion | Mi ha-ve u na-no re. | nano- (×10^-9) | no [es] noche |
| A5-3 | sin_guion | Le nubu e-ve somi. | gris | entonces yo |
| A5-4 | con_guion | Le nubu e-ve so-mi. | gris | entonces yo |

### Las condiciones

Donde el guion no es otra palabra del léxico, cada par cubre tres polos:

1. **Sin guion:** la forma pegada (`halo`, `kilo`, `mega`, `nano`, `somi`).
2. **Con guion:** el corte de la alterna (`ha-lo`, `me-ga`, `na-no`, `so-mi`).
   Registra si el guion desambigua.
3. **Espacio:** las dos palabras (`ha lo`, `ki lo`, `me ga`, `na no`, `so mi`).

La comparación entre polos es el dato: si con guion sube el acierto frente al
espacio o a la forma pegada, el guion funciona y **no hay que renombrar nada**.

Los ítems `-1` y `-2` salen de la semilla `20261024`: fija el orden y si X es la
forma o la alterna. Si X es la forma y el ítem es `-2`, la grafía lleva guion
(A2 se queda en `kilo`: su guion sería `ki-lo`). Si a un par le falta un polo,
un complemento fijo (`-3`, `-4`; `origen: complemento`) se añade **después de A6**.
No rebaraja A1–A5, B ni C, y no consume la semilla.

### Evidencial en las declarativas

La regla 4 obliga al evidencial en toda declarativa. En la hoja es `-ve`
(fuente directa: lo que el hablante de la frase tiene o ve, §4.1).
La pregunta va sin evidencial. Cuando el verbo es el propio blanco
(`ha` dentro de `ha lo`), la frase es pregunta (`Tu ha lo i le ho mo?`):
el guion de `-ve` separaría `ha` de `lo` y el par dejaría de ser el que se mide.
`mita` no está en el léxico y no se inventa: el contexto de `nano` es `u nano re`.

### Par A6 — homófono verdadero `kilo` ≈ `ki-lo`

A1–A5 oponen un acento a dos (`kilo` ≈ `ki lo`, con espacio). A6 es la sexta
colisión (deuda C-05, regla 21): `kilo` (×10³) y `ki-lo` (*dónde*) son los dos
una palabra y el mismo /ˈki.lo/. El guion no cambia el acento; es la mitigación
escrita, junto con el contexto numérico de `kilo` y la prohibición de
coocurrir en la misma cláusula. A6-1 presenta `kilo` en `Mi ha-ve kilo hos.`;
A6-2 presenta `ki-lo` en `Ki-lo tu go?`. No van en la misma oración.
Los ítems A1–A5, B y C conservan el orden de la semilla `20261024`; A6 se
añade al final de ese bloque y no los reordena. Los complementos van detrás.

### Pregunta de cierre (la más importante)

Al terminar el bloque, se pregunta **sin mostrar el material**:

> «¿Notaste alguna vez que una palabra pudiera leerse de dos maneras?»

Un hablante que **no lo notó** es el mejor resultado posible: significa que la
colisión no llega a la conciencia. Se anota tal cual, y si espontáneamente nombra
alguna, se anota cuál. La hoja trae la casilla; el repo no la rellena.

---

## 3. Bloque B — racimo `hV-`

14 formas que empiezan por `h` + vocal. Se **lee** una en una tarjeta y se tapa;
el hablante elige entre 4 escritas.

**El riesgo que se mide:** que los vecinos se confundan entre sí. Si `hodu`
(*montaña*) y `hoki` (*dinero*) se cruzan sistemáticamente, el racimo es un problema
real y hay que espaciarlo (es lo que Korlin dejó anotado como deuda).

| # | Forma | Español | Distractores (vecinos mínimos) |
|---|---|---|---|
| B01 | `ha` | tener | `hili` · `hala` · `hele` |
| B02 | `he` | cabeza | `hili` · `holo` · `hala` |
| B03 | `hi` | alto | `hele` · `hulu` · `hala` |
| B04 | `ho` | casa | `hili` · `hulu` · `hele` |
| B05 | `hu` | tristeza | `hala` · `hili` · `hele` |
| B06 | `hapu` | abrir | `hopu` · `hepu` · `hipu` |
| B07 | `hesu` | gusto | `hisu` · `hasu` · `hosu` |
| B08 | `hobu` | animal | `hebu` · `hubu` · `habu` |
| B09 | `hodu` | montana | `hadu` · `hedu` · `hudu` |
| B10 | `hoki` | dinero | `huki` · `haki` · `heki` |
| B11 | `hudi` | tocar | `hedi` · `hodi` · `hadi` |
| B12 | `huko` | ciudad | `hako` · `heko` · `hiko` |
| B13 | `husa` | olor | `hesa` · `hasa` · `hisa` |
| B14 | `halo` | hola | `hilo` · `holo` · `helo` |

### Qué se mide

No el acierto bruto (siempre hay azar: 25% por 4 opciones), sino **la tasa de
confusión por par concreto**. Se anota qué forma se eligió cuando se falló: si los
errores se concentran en un vecino determinado (`hoki`→`huki` una y otra vez), ese
par es el problema, no el racimo entero. Con la forma todavía a la vista la tarea
sería copiar letras: por eso se tapa.

---

## 4. Bloque C — naturalidad del léxico

30 formas al azar (estratificadas por categoría). El hablante las **lee** y puntúa 1-5:

> «¿Qué tan natural te parece, leída, como palabra de un idioma? 1 = raro, parece un error;
> 5 = normal, como una palabra que ya conocieras.»

### Qué se mide

**La cola, no el promedio.** El promedio siempre sale 3 y no dice nada. Lo que
importa son las formas con puntuación ≤ 2 de forma consistente entre hablantes:
esas son las candidatas a renombrar. Una forma que a 8 personas les parece rara
tiene un problema real, aunque a la gramática no le pase nada.

---

## 5. Umbrales de decisión (fijados ANTES de medir)

Se fijan ahora para no racionalizar el resultado después. No cambian con esta
revisión del instrumento. La unidad sigue siendo el **par** (A) o la **forma** (B, C),
sumando sus ítems. El desglose por condición (guion / espacio / sin guion) es
descriptivo: no abre un umbral nuevo.

| Resultado | Lectura | Acción |
|---|---|---|
| **≥ 90%** de acierto en A y B | sin problema | no se toca nada |
| **75-90%** | vigilancia | se anota; se revisa si se suma otro indicio |
| **< 75%** en un par concreto | fallo real | **se renombra ese par** (uno a uno, no la lista) |
| Bloque C: forma con ≤ 2 en ≥ 60% de hablantes | parece mal al leerla | candidata a renombrar |

**Mínimo para renombrar: 3 hablantes coincidiendo en el mismo par.** Uno solo no
justifica tocar el léxico: puede ser idiosincrasia.

---

## 6. Registro

- Plantilla: `docs/c24-plantilla.csv` (una fila por hablante en la cabecera;
  la fila de ítems va vacía hasta el campo).
- Hoja legible: `docs/c24-hoja-respuestas.md` — una por hablante, de lectura.
- Diseño completo con el orden ya sorteado: `docs/c24-estimulos.json`.

**El orden está fijado con semilla** (`20261024`): varias sesiones usan el mismo
orden y los resultados son comparables. Si se cambia la semilla, hay que anotarlo.
La semilla no cambió al añadir A6 ni al añadir los complementos: A6 no rebaraja
A1–A5, B ni C, y los complementos se concatenan detrás de A6.

Una vez vaciados los datos, el análisis se hace con `scripts/c24_analiza.py`.
No se rellenan hablantes de prueba en la plantilla del repo.

---

## 7. Lo que esta prueba NO puede decidir

- **No valida la pronunciación real de la /h/** en habla: eso necesita grabación
  humana. Lo que mide es el reconocimiento escrito.
- **No mide si la lengua es fácil de aprender**: eso es un estudio longitudinal.
- **No decide el nombre `Korlin`**: es marca, y es de Ignacio.
- Con 8-12 hablantes hispanohablantes mide **hispanohablantes**, no «la humanidad».
  Si algún día hay hablantes de otras lenguas maternas, es otra prueba.
