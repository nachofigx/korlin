# Changelog de Korlin

Formato: `vMAYOR.MENOR.PARCHE`. Un cambio de regla gramatical sube el MENOR
(`v0.1` → `v0.2`); una corrección de error tipográfico o aclaración no cambia
la versión. **Documento que manda:** `korlin-spec.md` (generado desde
`data/*.yaml`), seguido de `01-phonology.md`, `02-morphology.md`, `03-syntax.md`.

---

## v0.8.4 — 2026-10-27

Parche. No hay regla gramatical nueva ni raíz nueva. No se renombra nada.
La marca sigue siendo **Korlin**.

La fuente de las reglas es `scripts/generar_ia.py` (emite `korlin-spec.md` y
el campo de `korlin.json`). `02-morphology.md` y `03-syntax.md` son manuales:
siguen al spec.

### A-03 — la regla 12 apunta a la 23

La regla 12 decía que la modalidad no marcada equivale a `to` siempre. La
regla 23 (C-19) dice que eso vale solo con evidencial fuerte (`-ve`, `-di`,
`-sa`); con `-pen` la no marcada es `be`, y `os` si el dato es incompleto.
La 12 pasa a ser un puntero a la 23. `korlin.json` (`modalidad_por_defecto`)
deja de decir «to (certeza)» a secas.

`02-morphology.md` ya estaba alineado en v0.8.3: no repetía la línea vieja.
`03-syntax.md` nombra también el `os` de dato incompleto.

### A-05 — §4.1, cinco filas (16 en total)

Se conservan las once filas correctas. Entran, sin sufijo nuevo:

- identidad / cópula de autoidentificación → `-ve` (`mi e-ve manu`).
  Prohibido `-sa` y, salvo cita ajena, `-di`.
- acción propia en el presente → `-ve` (`mi go-ve`). Prohibido `-di` y `-sa`.
  El pasado propio sin percepción sigue en `-di`.
- hábito o presente genérico → `-sa` solo si es saber común (`le pe man-sa`);
  un hábito que se ve es `-ve` (`li man-ve`). El presente sin marca de tiempo
  no elige `-sa`.
- saber por lectura frente a saber general: documento → `-di`
  (`mi sa-di ki le ho e-di me`); saber común → `-sa`; «yo sé» como estado
  del hablante → `-ve` (regla 20). Leer no sube a `-sa`.
- matices de `-di` (dicho, leído, herramienta): un solo sufijo
  (`li go-di`, `le ho e-di me`, `le kin di-di le nom`). La confianza sigue
  en la modalidad (regla 23).

El traductor no elige evidencial. `--ev` sigue siendo un sello. Los casos
nuevos de la batería son oraciones que ya sabía decir.

### A-06 — C-46-FA

Inventario de falsos amigos del español: [`docs/c46-falsos-amigos.md`](docs/c46-falsos-amigos.md)
(`misa`, `lama`, `bebe`, `pala`, `halo`, …). No es la lista cerrada de la
regla 24c. El spec solo apunta al archivo.

**No se renombra ninguna forma.** El umbral de renombre es solo el dato de
C-24, ya fijado en v0.8: ≥90 % no se toca; 75–90 % vigilancia; <75 % en un
par concreto, con al menos 3 hablantes en ese par, se renombra ese par.
La medición con hablantes sigue pendiente. Este parche no amplía los estímulos.

### TTS

Los white papers (`docs/investigacion.md`, `docs/research.md`) decían que la
voz `es-MX-DaliaNeural` es compatible con la fonología. El dato medido de
C-24 es otro: esa voz deja muda la /h/ (`halo` y `alo` salen idénticos).
La fonología no cambia. El README no hacía esa afirmación.

---

## v0.8.3 — 2026-10-27

Parche. No hay regla gramatical nueva ni raíz nueva. La marca sigue siendo **Korlin**.

### 02 y 03 alineados con el spec

`02-morphology.md` y `03-syntax.md` se quedaban atrás de `korlin-spec.md`:

- Interrogativos con guion: `ki-pe`, `ki-lo`, `ki-ti`, `ki-mo`. `ki tem` y el
  espacio (`ki pe`) no son la forma escrita.
- Regla 23: sin partícula, la modalidad vale `to` solo con evidencial fuerte
  (`-ve`, `-di`, `-sa`). Con `-pen` la no marcada vale `be`. La explícita manda.
- Regla 24: una sola cadena `[modalidad] [actitud] [mo]`. No se encadenan dos
  actitudes ni dos modalidades.
- El futuro esperado no lleva `-sa`. Lo predicho va con `-pen` (§4.1). `-sa`
  sigue siendo conocimiento general.
- Plural nominal en el manual de morfología: `-s` tras vocal, `-es` tras coda.

### Alomorfo `-es`

`data/afijos.yaml` solo listaba `-s`. Entra `-es` (tras coda `m`/`n`/`s`:
`nomes`, `kines`, `temes`). `scripts/generar_ia.py` lo vuelca al §3, al §8 y
a `korlin.json`.

`_cat` quitaba solo la `-s` final: `nomes` buscaba `nome` y perdía la categoría,
así que el adjetivo no pasaba delante (`nomes me`). Ahora prueba `-es` cuando
la coda es `m`/`n`/`s`.

### C-10

La excepción de nombres propios y marcas se dice «excepción a la fonotáctica».
Ya no se llama «excepción a una letra = un sonido». La marca sigue siendo **Korlin**.

---

## v0.8.2 — 2026-10-27

Parche de documentación y de estímulos. No hay regla gramatical nueva ni raíz
nueva. `kilo`, `mega` y `nano` no se renombran. La marca sigue siendo **Korlin**.
v0.8.1 ya está etiquetada en el merge de PR #8 (`c367337`); esta aclaración va
aparte.

### C-05 — sexta colisión: `kilo` ≈ `ki-lo`

La regla 24c listaba cinco colisiones que la prosodia separa (un acento frente
a dos). Bajo la regla 21 el compuesto interrogativo `ki-lo` (*dónde*) es una
palabra fonológica con un solo acento, igual que el numeral `kilo` (×10³):
ambos son /ˈki.lo/. `kilo` ≈ `ki lo` (con espacio) sigue entre las cinco;
`kilo` ≈ `ki-lo` (con guion) es la **sexta**, deuda documentada. C-05 (no hay
tilde que marque el acento) sigue abierta: esta es su colisión concreta, no un
cierre.

Mitigación, escrita en la regla 24c:
- el interrogativo se escribe siempre `ki-lo`;
- `kilo` solo en contexto numérico (numeral suelto o `kilo-met`);
- no coocurren en la misma cláusula: el numeral queda en su marco numérico y
  `ki-lo` abre la pregunta.

### C-24

Par A6 en el bloque A: `kilo` frente a `ki-lo` (los dos /ˈki.lo/). Semilla
`20261024` sin cambio. A1–A5, el bloque B y el bloque C conservan el orden; A6
se añade al final del bloque A. En A6-1 la forma oída es `kilo`; en A6-2 es
`ki-lo`. Ese par no consume la secuencia aleatoria de la semilla.

---

## v0.8.1 — 2026-10-27

Parche. No hay regla nueva ni raíz nueva. La marca sigue siendo **Korlin**.

### Traductor: negación, cópula y coordinación

La negación era un flag de la oración entera, así que un `no` de la subordinada
también negaba la matriz. La cópula negada hacía `verbo_puesto = True` y la
cláusula siguiente lanzaba `TypeError: argument of type 'bool' is not iterable`.
`y` / `o` / `pero` no abrían cláusula (en inglés `and` / `then` sí).

`--ev` sigue siendo un sello uniforme: la misma fuente en cada cláusula finita.
No elige el evidencial según §4.1. Los casos de «yo sé» de abajo usan `--ev=ve`
porque §4.1 no permite `-sa` ahí.

| Español | `--ev` | Korlin |
|---|---|---|
| Él dice que yo no como. | sa | `li di-sa ki mi na man-sa.` |
| Yo sé que él no va. | ve | `mi sa-ve ki li na go-ve.` |
| Yo no sé quién va. | ve | `mi na sa-ve ki-pe go-ve.` |
| Pienso que el agua no es buena. | sa | `pen-sa ki le wa na e-sa gu.` |
| El agua no es buena y él come. | sa | `le wa na e-sa gu ka li man-sa.` |
| Él come y ella bebe. | sa | `li man-sa ka li bi-sa.` |
| Él no come y ella bebe. | sa | `li na man-sa ka li bi-sa.` |
| Él come y ella no bebe. | sa | `li man-sa ka li na bi-sa.` |
| Él come o ella bebe. | sa | `li man-sa o li bi-sa.` |
| Él come pero ella bebe. | sa | `li man-sa ba li bi-sa.` |

Con `--ev=sa`, «Yo sé que él no va.» sale `mi sa-sa ki li na go-sa.` Eso es el
sello pedido, no la lectura de §4.1. `cómo` (interrogativo) sigue abriendo
cláusula; `como` (comer) ya no, para que «no como» no deje el `no` atrás.

### `-sa` = conocimiento general

`data/afijos.yaml`, el generador, el spec, `korlin.json` y los manuales decían
«asumido». La tabla §4 ya decía conocimiento general. Queda una sola glosa:
`go-sa` = va (es sabido).

### Ejemplo de sueño y oráculos `sa-sa`

La fila «sueño o ficción» usaba `mi an-mo-pen le ho`. `mo` es la partícula de
pregunta sí/no y no hay raíz «soñar». El ejemplo legal es `mi an-do-ve ki le ho e-pen`
(dormí, lo viví; la casa en el sueño estaba, lo infiero).

Los oráculos de «yo sé» / C-36 que fijaban `sa-sa` pasan a `-ve`. La lectura
normativa mixta, en la regla 20, es `Mi sa-ve ki-pe go-pen.`

### CI

`.github/workflows/test.yml` corre `test-fonotactica`, `test-regresion-v06` y
`test-traductor` en push y pull request.

### Ya cerrado en v0.8

`generar_ia.py` ya no decía que C-36 fuera deuda. Sigue cerrado: `ki-pe` /
`ki-lo` / `ki-ti` / `ki-mo` abren cláusula y la subordinada lleva verbo finito
y evidencial.

---

## v0.8 — 2026-10-27

**PR #6** (merge `ca44f33`, 2026-10-25): protocolo de prueba con hablantes (C-24).
No hay regla gramatical nueva ni cambio de léxico. Esta entrada deja constancia
del protocolo ya mergeado y alinea los encabezados de versión, que seguían en v0.6.

### C-24 — protocolo listo; medición de campo pendiente
- Protocolo: `docs/c24-protocolo.md` (listo para aplicar). Estímulos con orden
  fijado (semilla `20261024`): `docs/c24-estimulos.json`, hoja
  `docs/c24-hoja-respuestas.md`, plantilla `docs/c24-plantilla.csv`. Scripts:
  `scripts/c24_protocolo.py`, `scripts/c24_estimulos.py`, `scripts/c24_analiza.py`.
- Tres bloques, todos **escritos**: A colisiones canónicas (elección forzada),
  B racimo `hV-` (14 vecinos), C naturalidad (escala 1-5). Umbrales fijados
  antes de medir (≥90 % no se toca; 75-90 % vigilancia; <75 % en un par concreto
  se renombra ese par; bloque C ≤2 en ≥60 % de hablantes es candidata; mínimo
  3 hablantes coincidiendo en el mismo par).
- **El audio TTS no es viable** (medido, no supuesto). `scripts/c24_audio.py`:
  en la voz `es-MX` la /h/ es muda (`halo` y `alo` salen idénticos) y el
  sintetizador no marca 1 acento frente a 2 (`halo` vs `ha lo`). Los mp3 se
  sacaron del repo. El camino de la prueba es el **test escrito**. Medir la
  prosodia en habla exige grabación humana.
- La medición con hablantes **sigue pendiente**. Hasta ese resultado no se
  renombra nada (colisiones C-46/C-47, racimo hV-, naturalidad).

### Documentación alineada (sin cambio de diseño)
- Versión de `data/lexico.yaml` y `data/afijos.yaml`: **0.8**. `korlin-spec.md`
  y `korlin.json` regenerados con `scripts/generar_ia.py`.
- Regla 20: quitado el puntero «deuda C-36, no tiene forma aún». C-36 está
  cerrada desde v0.7: el interrogativo (`ki-pe`, `ki-lo`, `ki-ti`, `ki-mo`) es
  frontera de cláusula y la subordinada lleva verbo finito y evidencial.
- `01-phonology.md`: la excepción C-10 en inglés cubre coda ilegal **y** grupo
  consonántico (`-rl-`). La marca sigue siendo **Korlin**.

### Deuda declarada
C-05 (índice sin tilde), `u me hos`, cluster hV- (el bloque B del protocolo lo
mide; el racimo sigue abierto hasta el resultado). **C-24:** protocolo listo /
medición con hablantes pendiente (no falta el protocolo; las decisiones de
renombre esperan el campo). **C-27:** medir con hablantes, pendiente.

---

## v0.7 — 2026-10-24

**Ronda abierta por Korlin** (v0.7: C-14, Swadesh, C-36, C-47).

### Léxico: cobertura Swadesh 38 → 99/100
- **+60 raíces nuevas** en tres lotes, todas pasadas por `scripts/validar-raices.py`
  (R0 fonotáctica, R1 afijos, R3 derivable, R4 existente, R5 dos partículas, R6
  construcción canónica acotada):
  - Lote 1 (cuerpo y naturaleza, 29): `famu` `manu` `bebe` `tomo` `boku` `nupi`
    `pala` `tapi` `kopa` `kuti` `misa` `kuru` `boni` `tamo` `ore` `nosi` `moka`
    `tino` `pode` `noki` `tumi` `tara` `sumu` `toko` `nubu` `sumo` `sena` `pado` `poki`
  - Lote 2 (propiedades y verbos, 24): `tani` `wida` `tika` `lusa` `kumu` `kuno`
    `kola` `puma` `kabe` `kara` `bela` `peta` `liba` `bita` `kida` `tibu` `waka`
    `sona` `sita` `puka` `buna` `fula` `tima` `tumu`
  - Lote 3 (funcionales, 7): interrogativos por composición con `ki` (regla 17)
    — `ki-pe` (quién), `ki-lo` (dónde), `ki-ti` (cuándo), `ki-mo` (cómo) — y los
    cuantificadores `pamo` (todo), `paki` (mucho), `tuki` (poco).
- El único concepto Swadesh sin raíz propia es *esto*, que ya cubre el
  determinante `se` (este/esta).
- Léxico total: **178 → 238 palabras.**

### Herramienta nueva: `scripts/validar-raices.py`
Valida lotes de raíces contra los seis criterios acordados con el revisor,
**con R6 acotado a construcciones canónicas reales** (R6 literal rechaza todas
las CVCV; ver v0.6). Salida con veredicto y motivo por raíz.

### C-14 — homonimia derivado/frase, documentada
Regla nueva (24b): un derivado en `-i` es legítimo por la regla 17 aunque se lea
como dos palabras; se distinguen por la prosodia (regla 21) y el guion.
**Casos con colisión canónica real**, declarados: `somi` (gris) ≈ `so mi`
(*entonces yo*), `kilo` (mil) ≈ `ki lo` (*qué lugar*). Si al probarlos con
hablantes resultan confusos, se renombran (C-24/C-27).

### C-36 — interrogativa indirecta (cerrada)
**Bug real corregido en el traductor.** El interrogativo (`quién`, `dónde`, `cuándo`,
`cómo`) no abría frontera de cláusula, así que el verbo de la subordinada no se
conjugaba: `Yo sé quién va.` daba `mi sa-sa ki-pe [va?]`. Ahora las formas
interrogativas son frontera de cláusula y la subordinada lleva su verbo finito y su
evidencial (regla 14):

| Español | Korlin |
|---|---|
| Yo sé quién va. | `mi sa-sa ki-pe go-sa.` |
| Yo sé dónde está. | `mi sa-sa ki-lo e-sa.` |
| Yo sé cómo va. | `mi sa-sa ki-mo go-sa.` |
| Yo sé que él va. | `mi sa-sa ki li go-sa.` |
| ¿A quién ves? | `a ki-pe ve mo?` |

La distinción **`ki-pe`** (interrogativo, palabra) vs **`ki`** (complementante) queda
operativa: no hace falta una forma nueva para «sé quién va». 5 casos nuevos en
`test-traductor.py` + 3 anti-regresión.

### C-38 — hiato (cerrada)
No había nada que decidir: el spec ya lo fijaba (1.2.5, **sin diptongos**). Los AFI lo
confirman (`noi` = /ˈno.i/, `sui` = /ˈsu.i/ — dos sílabas). Regla **23b** nueva:
dos vocales seguidas son siempre dos sílabas plenas, dentro de la palabra y en
frontera (`le wa e gu` = /le.wa.e.gu/), sin elisión; el acento cuenta el hiato como
dos.

### C-46 / C-47 — colisiones canónicas declaradas (cerradas como deuda documentada)
Al auditar **todo** el léxico contra R6 aparece un problema mayor que `halo`: son
**cinco** formas del léxico que se segmentan además como dos palabras en una
construcción canónica real. Regla **24c** con la **lista cerrada**:

| Forma | Lectura alterna | Caso |
|---|---|---|
| `halo` (hola) | `ha lo` (*tener lugar*) | C-47 |
| `kilo` (mil, ×10³) | `ki lo` (*qué lugar*) | |
| `mega` (millón, ×10⁶) | `me ga` (*tierra grande*) | |
| `nano` (nano-, ×10⁻⁹) | `na no` (*no [es] noche*) | |
| `somi` (gris) | `so mi` (*entonces yo*) | |

**No son errores**: son homófonos declarados, separados por prosodia (regla 21) y
contexto. Los prefijos SI se conservan (son internacionales y su valor numeral es
inconfundible). Si la prueba con hablantes (C-24) muestra confusión real, se
renombran uno a uno.

### Deuda declarada
C-05 (índice sin tilde), `u me hos`, C-24/C-27 (medir con hablantes), cluster hV-.

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

### C-10 — Nombre
- Se mantiene el autónimo y la marca **Korlin** (no Kolin, no Korolin). Los
  nombres propios y las marcas (mayúscula inicial) pueden conservar una
  ortografía que **viole la fonotáctica** `(C)V{m,n,s}`: coda ilegal **o grupo
  consonántico** (`Korlin` = `-rl-`, que el léxico común no admite). Excepción
  documentada, misma familia que PR-26 (`Mekiko`, `Faransa`, `Yapan`, `Barasila`).
  Afecta solo a nombres; la coda del léxico común no cambia.
- **Acento en compuestos:** corregida la contradicción interna. El spec decía
  «cada segmento conserva el suyo», contra la regla 21 («un solo acento por
  palabra fonológica»). Ahora: el compuesto lleva **un** acento, en su penúltima
  sílaba (`do-lo` → /ˈdo.lo/, `ru-sui` → /ruˈsu.i/).

### Léxico
- 150 → **178 palabras**: 7 reemplazos del lote 1 rechazado, 8 del lote 2, 11
  sobrevivientes del lote 1 y los sustitutos que exige el R6 acotado:
  `duka` por `halu`, `duno` por `dano`, `famo` por `fama` (verbo+objeto),
  `semo` por `nami`, `nubi` por `solo`, `nodu` por `hisu` (Adj-N). Las 28
  raíces del lote pasan limpias el comprobador alineado.

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
