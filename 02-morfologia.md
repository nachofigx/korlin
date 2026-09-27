# 02 — Morfología

## 1. Partículas de actitud (attitudinals) — v0.1

Partículas **opcionales** que marcan la emoción/actitud del hablante.
Posición: **al final de la oración** (igual que la partícula de pregunta `mo`).
También pueden usarse **solas** como interjección.

| Partícula | AFI | Emoción / actitud | Emoji |
|---|---|---|---|
| `yo` | /jo/ | alegría, amor, ¡genial! | ❤️ |
| `hu` | /hu/ | tristeza, pena | 😢 |
| `we` | /we/ | sorpresa, ¡wow! | 😮 |
| `fi` | /fi/ | ironía, sarcasmo | 🙃 |
| `bu` | /bu/ | enfado, frustración | 😤 |
| `ri` | /ri/ | risa, humor | 😂 |
| `pu` | /pu/ | asco, desagrado | 🤢 |
| `ni` | /ni/ | miedo, preocupación | 😨 |
| `la` | /la/ | cariño, ternura | 🥰 |

### Reglas
- **Opcionales** (a diferencia de la evidencialidad, que es obligatoria).
- Se colocan **al final** de la oración.
- **Combinables**: `yo la` = "me encanta y es tierno".
- **Usables solas**: `we!` = "¡wow!".

### Ejemplos
- `le jo e gu yo!` — "¡El día es bueno, me encanta!"
- `we! le su e hi.` — "¡Wow! El sol está alto."
- `mi go a le ho fi.` — "Voy a la casa (ironía)."

### Nota anti-mentira
La partícula `fi` (ironía) marca explícitamente la "mentira juguetona" del
sarcasmo, separándola de la afirmación factual. Así la ironía **no contamina**
el sistema de evidencialidad: lo que es broma se declara broma.

## 2. Evidencialidad (obligatoria) — v0.1

La evidencialidad obliga a marcar la **fuente** de información de cada afirmación.
Es la capa "anti-mentira" de Korlin.

### Categorías (4)
| Sufijo | AFI | Categoría | Significado | Deriva de |
|---|---|---|---|---|
| `-ve` | /ve/ | Directo (DIR) | "lo percibí con mis sentidos" | `ve` = ver |
| `-pen` | /pen/ | Inferido (INF) | "lo deduzco de la evidencia" | `pen` = pensar |
| `-di` | /di/ | Reportado (REP) | "me lo dijeron" | `di` = decir |
| `-sa` | /sa/ | Asumido (ASU) | "se sabe / se asume" | `sa` = saber |

### Reglas
1. **Obligatorio**: toda oración declarativa lleva un evidencial en su verbo
   (o en la cópula `e`). No se puede afirmar un hecho sin declarar su fuente.
2. **Posición**: sufijo inmediatamente después del verbo.
3. **Exenciones**: preguntas, órdenes y la ironía marcada con `fi` no llevan evidencial.
4. **Jerarquía**: si hay varias fuentes, se marca la más fuerte
   (directo > inferido > reportado > asumido; cf. Barnes 1984, Faller 2002).

### Ejemplos
- `li go-ve.` — "Él se fue (lo vi)."
- `li go-di.` — "Él se fue (me lo contaron)."
- `li go-pen.` — "Él se fue (lo infiero)."
- `li go-sa.` — "Él se fue (se asume)."
- `le lu e-ve i le no.` — "La luna está en la noche (lo veo)."

### Efecto anti-mentira
Afirmar "li go" sin evidencial es **agramatical**. El hablante DEBE elegir una
fuente; al marcar "lo vi" se compromete y se expone. Mentir exige un
compromiso explícito, rastreable y desmontable.

## 3. Modalidad epistémica (grado de certeza) — v0.1

La modalidad epistémica marca **cuán seguro** está el hablante de la afirmación.
Complementa la evidencialidad: la evidencialidad dice *cómo* lo sabes (fuente);
la modalidad dice *cuán seguro* estás (certeza).

### Categorías (4)
| Partícula | AFI | Grado de certeza | Equivalente |
|---|---|---|---|
| `to` | /to/ | Cierto (lo garantizo) | ✅ "en serio" |
| `be` | /be/ | Probable (creo que sí) | 👍 "pro**ba**ble" |
| `os` | /os/ | Posible (quizás) | 🤔 "p**os**ible" |
| `ku` | /ku/ | Dudoso (no me fío) | ⚠️ "¿cuestionable?" |

### Reglas
1. **Opcional**, con valor por defecto = `to` (cierto). Si no pones partícula,
   se entiende que afirmas con certeza.
2. **Posición**: al final de la oración, después del verbo con su evidencial.
3. **Combinable** con evidencialidad y con partículas de actitud.
   Orden: `[verbo+evidencial] … epistémica … actitud`.

### Combinación fuente × certeza (el poder anti-mentira)
- `li go-ve.` — "Él se fue (lo vi)." — fuente directa, certeza por defecto
- `li go-di be.` — "Él se fue (me lo contaron), probablemente."
- `li go-pen os.` — "Él se fue (lo infiero), posiblemente."
- `li go-di ku.` — "Él se fue (me lo contaron), dudoso (no me fío)."
- `li go-di ku bu.` — "Él se fue (me lo contaron, dudoso) 😤."

## 4. Tiempo verbal — v0.1

El tiempo se marca con **prefijos** pegados a la raíz verbal.
El presente es la forma no marcada (sin prefijo).

### Categorías (3)
| Prefijo | AFI | Tiempo | Deriva de |
|---|---|---|---|
| (ninguno) | — | Presente | — |
| `an-` | /an/ | Pasado | `an` = viejo |
| `ne-` | /ne/ | Futuro | `ne` = nuevo |

### Reglas
1. **Presente** = raíz sin prefijo.
2. **Pasado** = prefijo `an-` ("viejo" → pasado).
3. **Futuro** = prefijo `ne-` ("nuevo" → futuro).
4. **Orden**: `[tiempo-] + raíz + [-evidencial]`.
5. El evidencial obligatorio sigue aplicando en todos los tiempos.

### Ejemplos
- `li go-ve.` — "Él va (lo veo)."
- `li an-go-ve.` — "Él fue (lo vi)."
- `li ne-go-ve.` — "Él irá (lo veré)."
- `li an-vi-di.` — "Él vivió (me lo contaron)."
- `wi ne-go a le ho.` — "Iremos a la casa."

### Nota: evidencialidad en el futuro
En futuro, el evidencial marca la fuente de la *predicción*: `ne-go-ve` = "iré
(por mi plan/voluntad)"; `ne-go-pen` = "iré (lo infiero)"; `ne-go-sa` = "iré
(se espera)".

## 5. Derivación (afijos) — v0.1

La derivación multiplica el vocabulario: pocas raíces + afijos regulares = miles
de palabras sin memorización extra. Es la clave de la concisión de Dutton,
pero con reglas limpias y predecibles.

### Afijos derivacionales (8)
| Afijo | Tipo | Significado | Deriva de |
|---|---|---|---|
| `-pe` | sufijo | agente (persona que X) | `pe` = persona |
| `-lo` | sufijo | lugar (donde se X) | `lo` = lugar |
| `-re` | sufijo | cosa/objeto (sustantivo derivado) | `re` = cosa |
| `-i` | sufijo | adjetivo relativo (relativo a X) | — |
| `-ro` | sufijo | abstracto (cualidad de X) | — |
| `na-` | prefijo | opuesto/negativo | `na` = no |
| `me-` | prefijo | aumentativo (grande/muy) | `me` = grande |
| `pi-` | prefijo | diminutivo (pequeño) | `pi` = pequeño |

### Reglas
1. Los sufijos se pegan a la raíz; los prefijos se anteponen.
2. Un afijo = un significado fijo (sin excepciones).
3. Se pueden combinar: `na-sa-pe` = "ignorante" (persona que no sabe).

### Ejemplos (el poder de la derivación)
- `sa` (saber) → `sa-pe` sabio · `sa-re` conocimiento · `na-sa` ignorar
- `man` (comer) → `man-pe` comensal · `man-re` comida · `man-lo` comedor
- `do` (dormir) → `do-pe` durmiente · `do-lo` dormitorio · `do-re` sueño
- `gu` (bueno) → `gu-ro` bondad · `na-gu` malo · `me-gu` excelente
- `su` (sol) → `su-i` solar
- `ho` (casa) → `pi-ho` casita · `me-ho` mansión

### Nota
Con ~100 raíces y estos 8 afijos, Korlin genera un vocabulario de varios miles
de palabras. Derivar es trivial y predecible.
