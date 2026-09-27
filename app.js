// Korlin (Shortlang) — app interactiva
// Usa window.KORLIN_LEXICO (generado desde data/lexico.yaml)

let LEXICO = window.KORLIN_LEXICO || [];

// ===== Pestañas =====
document.querySelectorAll('.tab').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.tab).classList.add('active');
  });
});

// ===== Diccionario =====
const busqueda = document.getElementById('busqueda');
const resultados = document.getElementById('resultados');
const countEl = document.getElementById('resultado-count');

function renderDiccionario(q) {
  q = (q || '').trim().toLowerCase();
  const filtradas = LEXICO.filter(p =>
    !q ||
    p.f.toLowerCase().includes(q) ||
    (p.es || '').toLowerCase().includes(q) ||
    (p.en || '').toLowerCase().includes(q)
  );
  countEl.textContent = filtradas.length + ' resultados';
  resultados.innerHTML = filtradas.slice(0, 100).map(p => `
    <div class="item">
      <div>
        <span class="f">${p.f}</span>
        <span class="cat"> [${p.c}] ${p.a || ''}</span>
      </div>
      <div class="t">${p.es} · ${p.en}</div>
    </div>
  `).join('') || '<p class="gloss">Sin resultados.</p>';
}

if (busqueda) {
  busqueda.addEventListener('input', () => renderDiccionario(busqueda.value));
  renderDiccionario('');
}

// ===== Flashcards =====
let flashActual = null;
let aciertos = 0;
let total = 0;

function palabraAleatoria() {
  return LEXICO[Math.floor(Math.random() * LEXICO.length)];
}

function nuevaFlash() {
  flashActual = palabraAleatoria();
  document.getElementById('flash-palabra').textContent = flashActual.f;
  const sig = document.getElementById('flash-significado');
  sig.textContent = flashActual.es + ' · ' + flashActual.en;
  sig.classList.add('hidden');
}

function revelar() {
  document.getElementById('flash-significado').classList.remove('hidden');
}

function siguiente(r) {
  if (r === 'si') aciertos++;
  total++;
  document.getElementById('flash-score').textContent = `Aciertos: ${aciertos} / ${total}`;
  nuevaFlash();
}

if (document.getElementById('flashcard')) nuevaFlash();

// ===== Traductor (palabra por palabra, demo) =====
function buscarPalabra(tok) {
  // exacto
  let p = LEXICO.find(x => x.f === tok);
  if (p) return p;
  // por raíz (quitar sufijos/afijos simples)
  const base = tok.replace(/-(ve|pen|di|sa)$/, '').replace(/^(an|ne|na|me|pi)-/, '').replace(/-s$/, '');
  p = LEXICO.find(x => x.f === base);
  return p || null;
}

function traducir(idioma) {
  const texto = document.getElementById('texto-origen').value.trim();
  if (!texto) { document.getElementById('traduccion').innerHTML = '<p class="gloss">Escribe algo en Korlin.</p>'; return; }
  const tokens = texto.split(/\s+/);
  const out = tokens.map(tok => {
    const p = buscarPalabra(tok);
    if (!p) return `<span class="gloss" title="no encontrada">${tok}?</span>`;
    return `<span title="${p.c}">${idioma === 'es' ? p.es : p.en}</span>`;
  });
  document.getElementById('traduccion').innerHTML = out.join(' ');
}
