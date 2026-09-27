# Korlin (Shortlang) — Investigación completa

> Documento de investigación y decisiones del proyecto Korlin, desde el origen de la idea hasta el estado actual.
> **Cómo pegarlo en Coda:** copia este documento completo y pégalo en una página de Coda. Los títulos `##` se convierten en encabezados, las tablas `|` en tablas reales, las listas `-` en viñetas y el texto `**en negrita**` se conserva.

---

## 1. Origen de la idea

La idea nace de una pregunta: **¿existen lenguajes creados con la finalidad de acortar las palabras?** — algo así como una *taquigrafía hablada*, pero que además sea un idioma completo.

Objetivos definidos desde el inicio:

- **Elegante y corto, pero hablable** (no un código de máquina).
- **Condensar el concepto** en pocas sílabas.
- **Future-proof para la IA** — que las máquinas y agentes se expresen de forma más eficiente.
- Fácil de pronunciar para todo el mundo (asiáticos, africanos, europeos).

La inspiración directa fue **Dutton Speedwords**, un sistema de taquigrafía internacional de los años 1930–1940.

---

## 2. Lenguas construidas para condensar (taquigrafía hablada)

Investigamos los principales intentos históricos de "decir mucho en poco":

| Lengua | Autor / Año | Enfoque | Resultado |
|---|---|---|---|
| **Speedtalk** | Heinlein, 1949 (novela *Gulf*) | Lengua densa ficticia | Concepto literario, no hablable |
| **Ithkuil** | John Quijada, 2004/2023 | Máxima densidad morfológica | Una frase puede valer por un párrafo, pero es casi imposible de hablar |
| **aUI** | W. John Weilgart | 31 morfemas primitivos | Muy compacto, poco natural |
| **Sona** | Kenneth Searight, 1935 | ~360 radicales | Interesante pero incompleto |
| **Toki Pona** | Sonja Lang, 2001 | ~120 palabras (minimalismo) | Lo contrario: no acorta, simplifica |
| **Dutton Speedwords** | Reginald Dutton, 1930s | ~493 raíces + palabras de 1 letra | La inspiración directa de Korlin |

**Conclusión:** existen muchos intentos de condensar, pero ninguno logró ser a la vez **corto, hablable y moderno**. Ese es el hueco que Korlin ocupa.

---

## 3. ¿Se puede hacer "imposible mentir"?

Ignacio lanzó un reto: **¿se puede construir una lengua donde sea estructuralmente imposible mentir?**

**Respuesta técnica (honesta):** No. La mentira es una **intención pragmática**, no una estructura gramatical. Ninguna gramática puede impedir que alguien diga algo falso a propósito.

**Pero sí se puede lograr un efecto muy cercano** mediante tres mecanismos combinados:

1. **Evidencialidad obligatoria** — marcar la fuente de toda afirmación.
2. **Modalidad epistémica** — marcar el grado de certeza.
3. **Actos de habla marcados** — distinguir ironía, broma, rumor, etc.

Con esto, mentir se vuelve **costoso y detectable**: quien miente debe elegir deliberadamente una marca falsa, y queda expuesto al ser verificado.

---

## 4. La evidencialidad en las lenguas naturales

La evidencialidad no es una invención de Korlin: existe en muchas lenguas del mundo.

| Lengua | Sistema | Ejemplo |
|---|---|---|
| **Quechua** | Sufijos obligatorios | `-mi` (directo), `-shi` (reportado), `-chi` (inferido) |
| **Tariana** (Amazonia) | Evidencialidad obligatoria en cada frase | No se puede decir "llovió" sin decir *cómo lo sabes* |
| **Tuyuca** (Amazonia) | 5 categorías evidenciales | Visual, no-visual, aparente, de segunda mano, asumido |

Dato clave: **~25% de las lenguas del mundo marcan la fuente de forma obligatoria** (Aikhenvald, 2004). Es un fenómeno natural, no un artificio.

**Korlin adopta 4 marcas evidenciales:**

| Marca | Significado |
|---|---|
| `-ve` | directo (lo vi/lo viví) |
| `-pen` | inferido (lo deduzco) |
| `-di` | reportado (me lo contaron) |
| `-sa` | asumido (se asume por convención) |

---

## 5. Estudio Pellegrino 2011 (tasa de información)

Investigamos la ciencia detrás de "hablar rápido y condensar".

**Hallazgo principal:** las lenguas transmiten información a una tasa casi constante de **~39 bits por segundo** (Pellegrino et al., 2011).

- Las lenguas "lentas" (con muchas sílabas) transmiten **más información por sílaba**.
- Las lenguas "rápidas" (pocas sílabas por segundo) transmiten **menos información por sílaba**.
- Se compensan mutuamente: hay un **cuello de botella cognitivo** humano, no lingüístico.

**Implicación para Korlin:** la ventaja no es "hablar más rápido", sino **usar menos caracteres y sílabas para el mismo mensaje** — lo que importa para escribir, tokenizar y transmitir (clave para la IA).

---

## 6. Dutton Speedwords (la inspiración)

Sistema creado por Reginald Dutton en los años 1930 como taquigrafía internacional.

**Características:**
- ~493 raíces cortas.
- Palabras gramaticales de **1 letra**.
- Sufijos derivacionales.

**Comparativa directa (mismo texto):**

| Métrica | Dutton | Korlin |
|---|---|---|
| Caracteres | 338 | 388 |
| Palabras | 90 | 89 |
| Sílabas | 83 | 117 |

Dutton es **13% más corto en bruto**, pero tiene problemas que lo hacen inviable:

- ❌ **No es pronunciable** (consonantes sueltas, "vocales fantasma").
- ❌ **Irregular** (excepciones por todas partes).
- ❌ **Sin vocabulario técnico** moderno.
- ❌ **Sin evidencialidad** ni sistema anti-mentira.

**Relación Korlin ↔ Dutton:** Korlin es su **sucesor espiritual**, no descendiente directo. Aproximadamente **30% del "ADN" conceptual** proviene de Dutton (filosofía de condensación, raíces cortas, palabras de 1 letra); el **70% restante es original** (fonología hablable, regularidad total, evidencialidad, emojis, enfoque IA).

---

## 7. Esperanto (por qué no conquistó el mundo)

Korlin se posiciona como "la competencia del Esperanto, 100 veces mejor". Para ello estudiamos **por qué el Esperanto fracasó** en su objetivo de lengua universal:

| Problema del Esperanto | Detalle |
|---|---|
| Diacríticos raros | ĉ, ĝ, ĥ, ĵ, ŝ, ŭ — difíciles de teclear y de escribir |
| Eurocentrismo | Vocabulario y estructura casi exclusivamente europeos |
| Acusativo `-n` | Una regla extraña que confunde a los aprendices |
| Concordancia | Los adjetivos y sustantivos deben concordar en caso y número |
| Sexismo | Sufijos femeninos derivados del masculino |
| Grupos difíciles | `knabino`, `scii` — combinaciones de letras incómodas |
| Diseño del siglo XIX | No pensado para internet, móviles ni IA |

**Korlin corrige todo esto:** sin diacríticos, sin casos, sin concordancia, neutro, inclusivo y nativo digital.

---

## 8. Comparativas de longitud

Medimos el mismo texto en varios idiomas para comprobar la condensación real.

### 8.1 Texto largo (un enunciado técnico sobre un arquitecto japonés)

| Idioma | Caracteres | Ahorro vs Korlin |
|---|---|---|
| **Korlin** | **388** | — |
| Dutton (estilo) | 338 | +15% (Dutton más corto) |
| Japonés (romaji) | 565 | −31% |
| Inglés | 603 | −36% |
| Chino (pinyin) | 616 | −37% |
| Esperanto | 660 | −41% |
| Español | 690 | −44% |
| Francés | 729 | −47% |
| Alemán | 759 | −49% |

### 8.2 Frase corta — "La mentira no puede vivir en mí"

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

### 8.3 Resumen de ahorros

- **−44%** caracteres vs español
- **−36%** caracteres vs inglés
- **−31%** caracteres vs japonés (romaji)
- **−41%** caracteres y **−50%** sílabas vs Esperanto
- **−49%** caracteres vs alemán

---

## 9. Fonología de Korlin

Diseñada para ser **neutra, simple y universal** (fácil para asiáticos, africanos y europeos).

### Inventario (20 fonemas)

**Consonantes (15):** `p b t d k g m n f s h l r w y`

**Vocales (5):** `a e i o u`

### Reglas

- **1 letra = 1 sonido** (siempre, sin excepciones).
- Sílaba: **(C)V(C)** — la coda solo puede ser `m`, `n` o `s`.
- **Sin grupos consonánticos** (nada de "str", "pr", etc.).
- Acento en la **penúltima** sílaba.
- Sin las letras `c, j, q, v, x, z` (redundan con otras).
- `r` siempre suave [ɾ] (como en español "pero").
- `h` siempre sonora [h] (como en inglés "house").

### Por qué estas decisiones

- La **pronunciación neutra tipo español/latín** es la más fácil para el mayor número de hablantes.
- Evitar sonidos difíciles (aspiradas, tonos, guturales) maximiza la adopción.

---

## 10. Nombre del idioma

- **Exónimo (nombre internacional):** Shortlang — "lengua corta".
- **Endónimo (nombre propio):** **Korlin** /ˈkoɾlin/ = `ko` (corto) + `lin` (lengua).

Se verificó que el nombre no colisionara con marcas registradas relevantes (existe un lenguaje de programación llamado *Kotlin*, pero es un riesgo bajo para un proyecto open source de distinta naturaleza).

---

## 11. Gramática y morfología

### Orden y estructura

- Orden básico: **SVO** (Sujeto–Verbo–Objeto).
- Modificadores **antes** del núcleo (adjetivo antes del sustantivo).

### Palabras funcionales (1 letra)

| Palabra | Significado |
|---|---|
| `e` | ser |
| `a` | a / hacia |
| `i` | en |
| `o` | o |
| `u` | un / uno |

### Categorías gramaticales

| Categoría | Sistema | Ejemplos |
|---|---|---|
| Plural | `-s` | `pe` (persona) → `pes` (personas) |
| Pregunta sí/no | `mo` al final | `Tu go mo?` (¿Vas?) |
| Pasado | prefijo `an-` (de "viejo") | `an-go` (fui) |
| Futuro | prefijo `ne-` (de "nuevo") | `ne-go` (iré) |
| Evidencialidad | `-ve` `-pen` `-di` `-sa` | `go-ve` (voy, lo sé por mí) |
| Modalidad epistémica | `to` `be` `os` `ku` | `to` = cierto, `be` = probable, `os` = posible, `ku` = dudoso |

### Derivación (afijos)

| Afijo | Función | Ejemplo |
|---|---|---|
| `-pe` | agente (persona) | `ban` (construir) → `ban-pe` (constructor) |
| `-lo` | lugar | `man` (comer) → `man-lo` (comedor) |
| `-re` | cosa | `gu` (bueno) → `gu-re` (cosa buena) |
| `-i` | adjetivo | `lum` (luz) → `lum-i` (luminoso) |
| `-ro` | abstracto | `gu` → `gu-ro` (bondad) |
| `na-` | opuesto | `toro` (verdad) → `na-toro` (mentira) |
| `me-` | aumentativo | `ho` (casa) → `me-ho` (mansión) |
| `pi-` | diminutivo | `ho` → `pi-ho` (casita) |

---

## 12. Léxico

Actualmente **143 palabras núcleo**, organizadas por categorías y almacenadas en `data/lexico.yaml`.

### Categorías

- **Números:** `u` (1), `du` (2), `san` (3), `fu` (4), `sin` (5), `sis` (6), `sem` (7), `om` (8), `nu` (9), `des` (10).
- **Pronombres:** `mi` (yo), `tu` (tú), `li` (él/ella), `wi` (nosotros), `yu` (vosotros), `lis` (ellos).
- **Verbos, sustantivos, adjetivos** de alta frecuencia.
- **Matemáticas:** `sum` (+), `min` (−), `fan` (×), `fen` (÷); prefijos SI: kilo, mega, giga, mili, miko, nano.
- **Países:** Mekiko, Espan, Kina, Frans, Brasil, Yapan (gentilicio con `-i`).

### Colores (economía máxima)

Solo **3 raíces primarias**, el resto derivado:

- `ru` rojo · `gi` verde · `ro` rosa
- Derivados: `lum-i` blanco, `no-i` negro, `su-i` amarillo, `wa-i` azul, `ga-i` marrón, `lu-i` morado, `som-i` gris, `ru-su-i` naranja.

---

## 13. Emojis y modernidad

Idea de Ignacio: **dos letras de Korlin disparan el emoji correspondiente en el teclado del móvil.**

| Partícula | Emoji | Emoción |
|---|---|---|
| `yo` | ❤️ | alegría |
| `we` | 😮 | sorpresa |
| `fi` | 🙃 | ironía |
| `ri` | 😂 | risa |
| `hu` | 😢 | tristeza |
| `bu` | 😤 | enfado |
| `la` | 🥰 | cariño |
| `pu` | 🤢 | asco |
| `ni` | 😨 | miedo |

Esto hace a Korlin **nativo digital**: informal, expresivo y perfecto para jóvenes.

---

## 14. Korlin y la IA

Un objetivo clave: **usar Korlin para hablar con agentes de IA**.

Ventajas:

- **Menos tokens** → textos más cortos = menos coste de procesamiento.
- **Parseo determinista** → gramática 100% regular, sin ambigüedades.
- **Evidencialidad obligatoria** → la IA declara la fuente de su información.
- **Traducción por reglas** Korlin ↔ español/inglés (viable sin ML).

La idea es un traductor por reglas que permita a humanos y agentes comunicarse en Korlin de forma eficiente.

---

## 15. Adopción masiva y posicionamiento

### Posicionamiento

> **"La competencia del Esperanto, 100 veces mejor."**

### Pilares de adopción

1. **Facilidad total** — regularidad sin excepciones.
2. **Juventud** — emojis, informal, digital.
3. **Modernidad** — sin diacríticos, listo para chat y móviles.
4. **Honestidad** — evidencialidad obligatoria (valor diferencial ético).
5. **IA** — eficiencia de tokens y parseo determinista.

### Métricas de marketing (reales, verificadas)

- **~41% más corto** que el Esperanto (caracteres).
- **~44% más corto** que el español.
- **~30% del "DNA"** conceptual de Dutton Speedwords.

---

## 16. Decisiones de proyecto (docs as code, open source)

### Arquitectura de fuente única

```
data/lexico.yaml        ← vocabulario (fuente de verdad)
data/traducciones.yaml  ← traducciones fr/zh/ja
data/afijos.yaml        ← afijos
        ↓
scripts/generar.py      ← generador
        ↓
5 manuales (ES/EN/FR/ZH/JA) + manual IA + lexico.js
```

**Un cambio en la fuente → se refleja automáticamente en todos los idiomas y en la web.**

### Open source

- **Repositorio público:** https://github.com/nachofigx/korlin
- **Licencias:** MIT (código) · CC BY-SA 4.0 (el idioma).
- **Control de evolución:** Lingua es la mantenedora; la comunidad propone vía PR/issues.

### Idiomas de documentación

- **Inglés (principal)** — audiencia de GitHub.
- **Español, Francés, Chino, Japonés** — para alcance global.
- **Manual para IA** — para que agentes aprendan Korlin.

---

## 17. Estado actual del proyecto

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

*Documento generado a partir de la investigación del proyecto Korlin. Se actualiza conforme el idioma evoluciona.*
