# C-46-FA — Falsos amigos del español

Inventario de **v0.8.4**. No es una regla nueva y no es un renombre.

Una forma del léxico es falso amigo cuando un lector de español puede leerla
como una palabra española (grafía exacta, con tilde, o con `k` donde el
español escribe `c`) y el sentido no es el de Korlin. La comprobación fue
forma por forma contra `data/lexico.yaml`. No es un estudio de corpus.

**No es la regla 24c.** Esa lista (cinco colisiones, más el homófono
`kilo` ≈ `ki-lo`) son dos lecturas *dentro* de Korlin. Aquí la otra lectura
es española. `halo` está en las dos: en 24c porque `halo` ≈ `ha lo`, y aquí
porque el español *halo* es la aureola, no el saludo.

## Umbral de renombre = solo C-24

Los umbrales se fijaron en v0.8, antes de medir, y no se reabren aquí:

- ≥90 % en el par: no se toca.
- 75–90 %: vigilancia.
- <75 % en un par concreto, y al menos 3 hablantes coincidiendo en ese par:
  se renombra **ese** par.
- Bloque C: ≤2 en ≥60 % de hablantes hace candidata la frase.

**No se renombra** ninguna forma de este archivo en v0.8.4. La medición con
hablantes sigue pendiente. Este parche no añade estímulos a
`docs/c24-estimulos.json` ni cambia la semilla `20261024`. Una forma que no
esté en el protocolo no tiene dato de campo: el inventario no autoriza a
tocarla.

## A. Grafía exacta

La forma korlin es también una palabra española, con otro sentido.

| Forma | Korlin | Lectura española que estorba |
|---|---|---|
| `misa` | carne | misa (liturgia) |
| `lama` | amar | lama (lodo; también el préstamo «lama») |
| `bebe` | niño | bebe (3.ª de *beber*). *Bebé* (infante) tampoco es «niño». El verbo beber es `bi` |
| `pala` | hoja | pala (herramienta) |
| `halo` | hola | halo (aureola). El saludo español es *hola*, otra grafía. Colisión 24c aparte |
| `toro` | verdad, certeza | toro (animal) |
| `no` | noche | no (negación). La negación korlin es `na` |
| `ya` | sí | ya (*already*) |
| `yo` | alegría (actitud) | yo (pronombre). El pronombre es `mi` |
| `mi` | yo | mi / mí (posesivo u objeto) |
| `me` | grande | me (objeto) |
| `su` | sol | su (posesivo) |
| `se` | este, esta | se (reflexivo) |
| `te` | ese, esa | te (objeto) |
| `le` | el, la | le (objeto indirecto) |
| `la` | cariño (actitud) | la (artículo) |
| `ti` | día | ti (pronombre) |
| `lo` | lugar | lo (artículo neutro / objeto) |
| `he` | cabeza | he (1.ª de *haber*) |
| `ha` | tener | ha (3.ª de *haber*). No es el auxiliar |
| `vi` | vivir | vi (pretérito de *ver*) |
| `ni` | miedo (actitud) | ni (conjunción) |
| `os` | posible (modalidad) | os (objeto de *vosotros*) |
| `san` | 3 | san (título: San…) |
| `sin` | 5 | sin (preposición) |
| `des` | 10 | des (subjuntivo de *dar*) |
| `pis` | piso, nivel | pis (orina, coloquial) |
| `tomo` | esposo | tomo (volumen de un libro; 1.ª de *tomar*) |
| `tapa` | trabajar | tapa (tapadera; alimento) |
| `puma` | pluma | puma (felino) |
| `tara` | estrella | tara (defecto; peso que se rebaja) |
| `tino` | diente | tino (puntería, tacto) |
| `sumo` | humo | sumo (supremo; el deporte) |
| `moka` | boca | moka / moca (café) |
| `mili` | milésima (÷1000) | la mili (servicio militar). El prefijo SI «mili-» sí coincide: ese sentido no es falso amigo |
| `tamo` | huevo | tamo (paja menuda). Poco frecuente |
| `ve` | ver | ¡ve! (imperativo de *ir*). En Korlin «¡ve!» es `go`. La 3.ª de *ver* sí coincide |
| `di` | decir | di (pretérito de *dar*). El imperativo «di» de *decir* sí coincide |
| `ven` | venir | ven (3.ª plural de *ver*). El imperativo «ven» sí coincide |
| `pi` | pequeño | pi (el número) |
| `fan` | multiplicar | fan (admirador, préstamo) |
| `min` | restar | min (abreviatura de minuto) |

`do` (dormir), `re` (cosa) y `fa` (hacer) coinciden además con notas musicales.
La trampa fuerte de `mi`, `la` y `si` es la de la tabla, no el solfeo.

## B. Tilde

Sin tilde, la forma korlin se lee como otra palabra. Con tilde, a veces el
sentido sí coincide: por eso no se toca el léxico a ciegas.

| Forma | Korlin | Sin tilde | Con tilde |
|---|---|---|---|
| `tu` | tú | tu (posesivo) | tú (pronombre) sí coincide |
| `si` | si (condicional) | si (condicional) sí coincide | sí (afirmación) es `ya`, no `si` |
| `mama` | madre | mama (pecho) | mamá (madre) sí coincide |
| `papa` | padre | papa (patata) | papá (padre) sí coincide |
| `sento` | 100 | — | sentó (pretérito de *sentar*) |

## C. `k` donde el español escribe `c`, o una letra de diferencia

Korlin no tiene `c`. El lector restituye la palabra española.

| Forma | Korlin | Lectura española |
|---|---|---|
| `kara` | garra | cara (rostro) |
| `kopa` | corteza | copa (vaso) |
| `kabe` | pelo | cabe (3.ª de *caber*) |
| `poko` | comercio | poco. En Korlin «poco» es `tuki` |
| `famo` | familia | fama |
| `peke` | pez | peque (niño, coloquial) |

## No son falsos amigos

No entran en el umbral de renombre por este inventario:

- Misma función: `de`, `a`, `o`. `kon` es *con* con otra grafía.
- Cognados de verbo: `pon` (imperativo de *poner*), `da` (3.ª de *dar*).
- `kola` (cola del animal) coincide con *cola* en ese sentido. *Cola* también
  es pegamento y fila: no basta para un renombre.
- Prefijos SI `kilo`, `mega`, `giga`, `nano`: el valor numeral es el mismo.
  El español *kilo* a menudo es el kilogramo. La regla 24c ya dice que no se
  renombran `kilo`, `mega` ni `nano`. `mili` solo es falso amigo de «la mili»
  (tabla A), no del prefijo.

## Qué no hacer con esta lista

No sustituir una forma por otra «más española». No añadir raíces para esquivar
el choque. No mover un par al protocolo C-24 dentro de un parche de
documentación: el orden de los estímulos ya está fijado. Si más adelante se
mide un par de esta lista, el único criterio de renombre es el dato de C-24
de arriba.
