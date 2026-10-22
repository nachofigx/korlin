# Cómo enseñarle Korlin a una IA

Esta guía explica cómo hacer que **cualquier modelo de lenguaje** (ChatGPT, Claude, Gemini, un agente Hermes, un modelo local) hable Korlin correctamente.

La idea central:

> **No le pidas a la IA que "sepa" Korlin. Dale la especificación y una herramienta.**
> El modelo decide *qué* decir; la herramienta sabe *cómo* decirlo en Korlin.

---

## 1. Por qué no funciona solo con un manual

| Enfoque | ¿Sirve? | Motivo |
|---|---|---|
| Darle un PDF del manual | ⚠️ Poco | El modelo no lo lee si no lo pegas, y no lo retiene entre sesiones |
| Fine-tuning | ❌ Todavía no | Requiere ~1.000+ pares glosados; con 148 palabras generaliza mal |
| **Spec pack en el system prompt** | ✅ **Sí** | Es el estándar de facto: 7-8k tokens con fonología + gramática + léxico |
| **Traductor por reglas como herramienta** | ✅ **Sí** | El Korlin lo produce el código, no el modelo → cero alucinación |
| **Benchmark de frases** | ✅ Sí | Sin medir, no sabes si "aprendió" |

---

## 2. Los tres archivos

### `korlin-spec.md` — el paquete de contexto
Autocontenido y denso: reglas irrompibles, fonología, morfología, evidencialidad, sintaxis, las 149 palabras en tabla, los 15 afijos, 17 ejemplos glosados e instrucciones de agente.

**Cómo usarlo:** pégalo completo en el *system prompt* (o en el primer mensaje) y pídele al modelo que hable Korlin. No requiere entrenamiento.

### `korlin.json` — la versión para máquinas
Léxico + afijos + reglas en JSON. Un agente lo consulta en lugar de adivinar.

### `scripts/traductor-korlin.py` — el traductor determinista
No usa estadística: aplica la gramática con reglas explícitas.

```bash
python scripts/traductor-korlin.py es "Yo como comida."
# → mi man-sa man-re.

python scripts/traductor-korlin.py en "He went to the house." --ev=ve
# → li an-go-ve a le ho.

python scripts/traductor-korlin.py k "Mi man-ve man-re."
# → ES: yo comer (lo vi) comida.
# → EN: I to eat (I saw it) food.
```

Opciones: `--ev=ve|pen|di|sa` (evidencial), `--time=an|ne` (tiempo), `--gloss` (glosa morfema a morfema), `--stdin`.

### `llms.txt` — descubrimiento
Estándar para que los agentes encuentren la especificación desde el sitio.

---

## 3. Recetas de integración

### a) Chat manual (ChatGPT / Claude / Gemini)
1. Abre `korlin-spec.md` y copia todo.
2. Pégalo al inicio de la conversación (o en "instrucciones personalizadas").
3. Pide: *"Traduce al Korlin: …"* o *"Conversemos en Korlin"*.

### b) Agente con herramientas
Dale al agente dos herramientas:
- `korlin_lookup(palabra)` → consulta `korlin.json`
- `korlin_traducir(texto, direccion, evidencial)` → llama al traductor

Así el agente nunca inventa una raíz: consulta.

### c) System prompt mínimo (si el contexto es corto)
Pega solo §1 (reglas) + §4 (evidenciales) + §7 (léxico). Con eso ya produce Korlin aceptable; el traductor corrige el resto.

### d) Flujo híbrido (recomendado)
1. El modelo redacta la idea en español/inglés.
2. Llama al traductor para convertirla.
3. El modelo revisa la salida y ajusta la evidencialidad según la fuente real.

---

## 4. Cómo medir que "aprendió"

Usa el banco de pruebas como referencia y evalúa al modelo con frases nuevas:

```bash
python scripts/test-traductor.py     # verifica el traductor (24 casos)
```

Para el modelo, pídele que traduzca 10 frases y comprueba tres cosas:
1. ¿Respetó **SVO**?
2. ¿Puso **evidencial** en todo verbo factual?
3. ¿Usó solo **fonemas válidos** (sin c, j, q, x, z)?

Aciertos ≥ 8/10 con la spec = el modelo "habla Korlin".

---

## 5. Regenerar todo

```bash
python scripts/generar_ia.py     # spec + json + llms.txt
python scripts/generar.py        # manuales en 5 idiomas
python scripts/generar_pdf.py    # PDFs
python scripts/test-traductor.py # pruebas
```

Fuente de verdad única: `data/lexico.yaml` y `data/afijos.yaml`. Un cambio ahí se propaga a todo.
