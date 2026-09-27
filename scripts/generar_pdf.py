#!/usr/bin/env python3
"""
Genera versiones PDF de los white papers de Korlin con estilo de paper académico profesional.

Usa markdown (MD -> HTML) + weasyprint (HTML+CSS -> PDF).
"""

import markdown
from pathlib import Path
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

CSS = """
@page {
  size: A4;
  margin: 2.3cm 2cm 2.5cm 2cm;
  @bottom-center {
    content: counter(page);
    font-size: 8.5pt;
    color: #555;
    font-family: "DejaVu Sans", sans-serif;
  }
  @top-center {
    content: "Korlin (Shortlang) — White Paper";
    font-size: 7.5pt;
    color: #888;
    font-family: "DejaVu Sans", sans-serif;
  }
}

html { font-size: 10pt; }

body {
  font-family: "DejaVu Serif", "Liberation Serif", Georgia, "Times New Roman", serif;
  font-size: 10pt;
  line-height: 1.52;
  color: #111;
  text-align: justify;
  hyphens: auto;
}

/* ===== Portada ===== */
.portada {
  text-align: center;
  page-break-after: always;
  padding-top: 22%;
}
.portada .tipo {
  font-family: "DejaVu Sans", sans-serif;
  font-size: 9pt;
  letter-spacing: 3pt;
  text-transform: uppercase;
  color: #666;
  margin-bottom: 2.5em;
}
.portada h1 {
  font-size: 30pt;
  border: none;
  margin: 0 0 0.3em;
  letter-spacing: -0.5pt;
}
.portada .subtitulo {
  font-size: 13pt;
  color: #444;
  font-style: italic;
  margin-bottom: 3em;
  text-align: center;
}
.portada .meta {
  display: inline-block;
  text-align: left;
  font-family: "DejaVu Sans", sans-serif;
  font-size: 9.5pt;
  color: #333;
  border-top: 1pt solid #999;
  border-bottom: 1pt solid #999;
  padding: 1em 2em;
  line-height: 1.9;
}
.portada .meta b { color: #111; }

/* ===== Encabezados ===== */
h1 {
  font-size: 17pt;
  text-align: center;
  margin: 0 0 1em;
  border: none;
  page-break-after: avoid;
}
h2 {
  font-size: 13pt;
  border-bottom: 0.8pt solid #bbb;
  padding-bottom: 3pt;
  margin: 1.6em 0 0.6em;
  page-break-after: avoid;
  text-align: left;
}
h3 {
  font-size: 10.5pt;
  margin: 1.2em 0 0.4em;
  page-break-after: avoid;
  text-align: left;
}

/* ===== Texto ===== */
p { margin: 0 0 0.55em; }
strong { color: #000; }
em { font-style: italic; }

ul, ol { margin: 0.4em 0 0.7em 1.4em; padding: 0; }
li { margin-bottom: 0.2em; }

/* ===== Tablas ===== */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.7em 0 1em;
  font-size: 8.2pt;
  page-break-inside: avoid;
}
th, td {
  border: 0.5pt solid #999;
  padding: 3pt 5pt;
  text-align: left;
  vertical-align: top;
}
th {
  background: #eef0f3;
  font-weight: bold;
  font-family: "DejaVu Sans", sans-serif;
  font-size: 7.6pt;
}

/* ===== Código ===== */
code {
  font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
  font-size: 8.2pt;
  background: #f4f4f4;
  padding: 0.5pt 2pt;
  border-radius: 2pt;
}
pre {
  background: #f6f7f9;
  border: 0.5pt solid #ddd;
  padding: 8pt;
  overflow-x: auto;
  page-break-inside: avoid;
}
pre code { background: none; padding: 0; }

blockquote {
  border-left: 3pt solid #999;
  margin: 0.8em 0;
  padding: 0.2em 1em;
  font-style: italic;
  color: #333;
}

hr { border: none; border-top: 0.5pt solid #ccc; margin: 1.5em 0; }
"""


def md_a_html(texto: str) -> str:
    return markdown.markdown(
        texto,
        extensions=["tables", "fenced_code", "sane_lists"],
    )


def generar(nombre_md: str, titulo: str, subtitulo: str, tipo: str, marcador_resumen: str):
    texto = (DOCS / nombre_md).read_text(encoding="utf-8")

    # Separar el cuerpo (desde el resumen ejecutivo) del encabezado del MD
    idx = texto.find(marcador_resumen)
    cuerpo_md = texto[idx:] if idx != -1 else texto
    cuerpo = md_a_html(cuerpo_md)

    portada = f"""
    <div class="portada">
      <div class="tipo">{tipo}</div>
      <h1>{titulo}</h1>
      <p class="subtitulo">{subtitulo}</p>
      <div class="meta">
        <b>Versión:</b> 1.1<br>
        <b>Fecha:</b> 27 de septiembre de 2026<br>
        <b>Autoría:</b> Lingua (lingüista) · Ignacio (creador)<br>
        <b>Repositorio:</b> github.com/nachofigx/korlin<br>
        <b>Licencia:</b> CC BY-SA 4.0 (idioma) · MIT (código)
      </div>
    </div>
    """

    html_completo = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <style>{CSS}</style>
</head>
<body>
  {portada}
  {cuerpo}
</body>
</html>"""

    salida = DOCS / nombre_md.replace(".md", ".pdf")
    HTML(string=html_completo, base_url=str(DOCS)).write_pdf(str(salida))
    print(f"✓ {salida.name}")


if __name__ == "__main__":
    generar(
        "investigacion.md",
        "Korlin (Shortlang)",
        "Diseño, investigación y fundamentación de una lengua construida para la era digital",
        "White paper científico",
        "## Resumen ejecutivo",
    )
    generar(
        "research.md",
        "Korlin (Shortlang)",
        "Design, research and rationale of a constructed language for the digital era",
        "Scientific White Paper",
        "## Executive summary",
    )
