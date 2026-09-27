// Korlin (Shortlang) — interactive app with language selector
// Uses window.KORLIN_LEXICO (generated from data/lexico.yaml + data/traducciones.yaml)

const LEXICO = window.KORLIN_LEXICO || [];
let LANG = 'en';

// ===== i18n: interface strings =====
const I18N = {
  en: {
    tagline: "A short, honest, modern constructed language",
    tab_inicio: "🏠 Home", tab_diccionario: "📖 Dictionary", tab_flashcards: "🎴 Flashcards", tab_traductor: "🔄 Translator",
    inicio_titulo: "Welcome to Korlin 🗣️",
    inicio_desc: "Korlin is a constructed language designed to be <strong>short</strong>, <strong>honest</strong> and <strong>modern</strong> — a spiritual successor to Dutton Speedwords and a better Esperanto.",
    card_corta_t: "✂️ Short", card_corta_d: "Words of 1–2 syllables condense concepts. ~40% shorter than Esperanto.",
    card_honesta_t: "🛡️ Honest", card_honesta_d: "Mandatory evidentiality: every statement declares its source. Lying is costly and detectable.",
    card_moderna_t: "📱 Modern", card_moderna_d: "20 letters, no diacritics, emoji particles, and AI-ready.",
    ejemplo_titulo: "Example",
    ejemplo_gloss: '"The lie cannot live in me." · <code>na-toro</code> = lie (<code>na-</code> not + <code>toro</code> truth)',
    diccionario_titulo: "Dictionary 📖",
    busqueda_ph: "Search in Korlin, Spanish or English…",
    flashcards_titulo: "Flashcards 🎴",
    flashcards_desc: "Guess the meaning. Click the card to reveal.",
    flash_no: "🙈 Didn't know it", flash_si: "✅ Knew it",
    traductor_titulo: "Translator (word by word) 🔄",
    traductor_desc: "Translates Korlin → selected language, word by word (demo).",
    traductor_ph: "Type in Korlin… e.g. mi go a le ho",
    btn_traducir: "Translate →"
  },
  es: {
    tagline: "Una lengua corta, honesta y moderna",
    tab_inicio: "🏠 Inicio", tab_diccionario: "📖 Diccionario", tab_flashcards: "🎴 Flashcards", tab_traductor: "🔄 Traductor",
    inicio_titulo: "Bienvenido a Korlin 🗣️",
    inicio_desc: "Korlin es una lengua construida diseñada para ser <strong>corta</strong>, <strong>honesta</strong> y <strong>moderna</strong> — sucesora del Dutton Speedwords y un Esperanto mejorado.",
    card_corta_t: "✂️ Corta", card_corta_d: "Palabras de 1–2 sílabas condensan conceptos. ~40% más corta que el Esperanto.",
    card_honesta_t: "🛡️ Honesta", card_honesta_d: "Evidencialidad obligatoria: toda afirmación declara su fuente. Mentir es costoso y detectable.",
    card_moderna_t: "📱 Moderna", card_moderna_d: "20 letras, sin tildes, partículas emoji y lista para IA.",
    ejemplo_titulo: "Ejemplo",
    ejemplo_gloss: '"La mentira no puede vivir en mí." · <code>na-toro</code> = mentira (<code>na-</code> no + <code>toro</code> verdad)',
    diccionario_titulo: "Diccionario 📖",
    busqueda_ph: "Busca en Korlin, español o inglés…",
    flashcards_titulo: "Flashcards 🎴",
    flashcards_desc: "Adivina el significado. Haz clic para revelar.",
    flash_no: "🙈 No la sabía", flash_si: "✅ La sabía",
    traductor_titulo: "Traductor (palabra por palabra) 🔄",
    traductor_desc: "Traduce Korlin → idioma seleccionado, palabra por palabra (demo).",
    traductor_ph: "Escribe en Korlin… ej. mi go a le ho",
    btn_traducir: "Traducir →"
  },
  fr: {
    tagline: "Une langue construite courte, honnête et moderne",
    tab_inicio: "🏠 Accueil", tab_diccionario: "📖 Dictionnaire", tab_flashcards: "🎴 Flashcards", tab_traductor: "🔄 Traducteur",
    inicio_titulo: "Bienvenue à Korlin 🗣️",
    inicio_desc: "Korlin est une langue construite conçue pour être <strong>courte</strong>, <strong>honnête</strong> et <strong>moderne</strong> — successeur du Dutton Speedwords et un meilleur espéranto.",
    card_corta_t: "✂️ Courte", card_corta_d: "Des mots de 1–2 syllabes condensent les concepts. ~40 % plus courte que l'espéranto.",
    card_honesta_t: "🛡️ Honnête", card_honesta_d: "Évidentialité obligatoire : chaque affirmation déclare sa source. Mentir est coûteux et détectable.",
    card_moderna_t: "📱 Moderne", card_moderna_d: "20 lettres, sans diacritiques, particules emoji, et prête pour l'IA.",
    ejemplo_titulo: "Exemple",
    ejemplo_gloss: '« Le mensonge ne peut pas vivre en moi. » · <code>na-toro</code> = mensonge (<code>na-</code> non + <code>toro</code> vérité)',
    diccionario_titulo: "Dictionnaire 📖",
    busqueda_ph: "Cherchez en korlin, espagnol ou anglais…",
    flashcards_titulo: "Flashcards 🎴",
    flashcards_desc: "Devinez le sens. Cliquez sur la carte pour révéler.",
    flash_no: "🙈 Je ne savais pas", flash_si: "✅ Je savais",
    traductor_titulo: "Traducteur (mot à mot) 🔄",
    traductor_desc: "Traduit korlin → langue choisie, mot à mot (démo).",
    traductor_ph: "Écrivez en korlin… ex. mi go a le ho",
    btn_traducir: "Traduire →"
  },
  zh: {
    tagline: "一种简短、诚实、现代的人造语言",
    tab_inicio: "🏠 首页", tab_diccionario: "📖 词典", tab_flashcards: "🎴 闪卡", tab_traductor: "🔄 翻译器",
    inicio_titulo: "欢迎来到 Korlin 🗣️",
    inicio_desc: "Korlin 是一种人造语言，旨在<strong>简短</strong>、<strong>诚实</strong>、<strong>现代</strong>——是 Dutton Speedwords 的继承者，也是更好的世界语。",
    card_corta_t: "✂️ 简短", card_corta_d: "1–2 个音节的单词浓缩概念，比世界语短约 40%。",
    card_honesta_t: "🛡️ 诚实", card_honesta_d: "强制示证：每句话都声明其来源。说谎代价高昂且可被察觉。",
    card_moderna_t: "📱 现代", card_moderna_d: "20 个字母，无变音符，表情符号助词，为 AI 就绪。",
    ejemplo_titulo: "示例",
    ejemplo_gloss: '「谎言无法活在我之中。」· <code>na-toro</code> = 谎言（<code>na-</code> 非 + <code>toro</code> 真相）',
    diccionario_titulo: "词典 📖",
    busqueda_ph: "用 Korlin、西班牙语或英语搜索…",
    flashcards_titulo: "闪卡 🎴",
    flashcards_desc: "猜猜意思。点击卡片揭晓。",
    flash_no: "🙈 不知道", flash_si: "✅ 知道",
    traductor_titulo: "翻译器（逐词）🔄",
    traductor_desc: "将 Korlin 逐词翻译为所选语言（演示）。",
    traductor_ph: "用 Korlin 输入…例如 mi go a le ho",
    btn_traducir: "翻译 →"
  },
  ja: {
    tagline: "短く、誠実で、現代的に作られた言語",
    tab_inicio: "🏠 ホーム", tab_diccionario: "📖 辞書", tab_flashcards: "🎴 フラッシュカード", tab_traductor: "🔄 翻訳",
    inicio_titulo: "Korlin へようこそ 🗣️",
    inicio_desc: "Korlin は<strong>短く</strong>、<strong>誠実で</strong>、<strong>現代的</strong>に設計された人工言語です——Dutton Speedwords の後継であり、より優れたエスペラントです。",
    card_corta_t: "✂️ 短い", card_corta_d: "1～2 音節の単語が概念を凝縮。エスペラントより約 40% 短い。",
    card_honesta_t: "🛡️ 誠実", card_honesta_d: "証拠性が必須：すべての発言が情報源を宣言。嘘はコストが高く、検出可能。",
    card_moderna_t: "📱 現代的", card_moderna_d: "20 文字、発音区別符号なし、絵文字助詞、AI 対応。",
    ejemplo_titulo: "例",
    ejemplo_gloss: '「嘘は私の中に生きられない。」· <code>na-toro</code> = 嘘（<code>na-</code> 非 + <code>toro</code> 真実）',
    diccionario_titulo: "辞書 📖",
    busqueda_ph: "Korlin・スペイン語・英語で検索…",
    flashcards_titulo: "フラッシュカード 🎴",
    flashcards_desc: "意味を当ててください。カードをクリックして表示。",
    flash_no: "🙈 知らなかった", flash_si: "✅ 知っていた",
    traductor_titulo: "翻訳（単語ごと）🔄",
    traductor_desc: "Korlin を選択した言語へ単語ごとに翻訳（デモ）。",
    traductor_ph: "Korlin で入力…例 mi go a le ho",
    btn_traducir: "翻訳 →"
  }
};

// ===== Language selector =====
function setIdioma(lang) {
  LANG = lang;
  document.querySelectorAll('.lang').forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
  const t = I18N[lang] || I18N.en;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const k = el.dataset.i18n;
    if (t[k] !== undefined) el.innerHTML = t[k];
  });
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    const k = el.dataset.i18nPh;
    if (t[k] !== undefined) el.placeholder = t[k];
  });
  // Re-render dynamic parts
  renderDiccionario(document.getElementById('busqueda').value);
  actualizarFlashSignificado();
  if (document.getElementById('traduccion').textContent) traducir();
}

document.querySelectorAll('.lang').forEach(btn => {
  btn.addEventListener('click', () => setIdioma(btn.dataset.lang));
});

// ===== Tabs =====
document.querySelectorAll('.tab').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.tab).classList.add('active');
  });
});

// ===== Dictionary =====
const busqueda = document.getElementById('busqueda');
const resultados = document.getElementById('resultados');
const countEl = document.getElementById('resultado-count');

function traduccionDe(p) {
  return p[LANG] || p.es;
}

function renderDiccionario(q) {
  q = (q || '').trim().toLowerCase();
  const filtradas = LEXICO.filter(p =>
    !q || p.f.toLowerCase().includes(q) ||
    (p.es || '').toLowerCase().includes(q) ||
    (p.en || '').toLowerCase().includes(q)
  );
  countEl.textContent = filtradas.length + ' results';
  resultados.innerHTML = filtradas.slice(0, 100).map(p => `
    <div class="item">
      <div>
        <span class="f">${p.f}</span>
        <span class="cat"> [${p.c}] ${p.a || ''}</span>
      </div>
      <div class="t">${traduccionDe(p)}</div>
    </div>
  `).join('') || '<p class="gloss">No results.</p>';
}

if (busqueda) {
  busqueda.addEventListener('input', () => renderDiccionario(busqueda.value));
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
  actualizarFlashSignificado();
}

function actualizarFlashSignificado() {
  const sig = document.getElementById('flash-significado');
  if (flashActual) {
    sig.textContent = traduccionDe(flashActual);
    sig.classList.add('hidden');
  }
}

function revelar() {
  document.getElementById('flash-significado').classList.remove('hidden');
}

function siguiente(r) {
  if (r === 'si') aciertos++;
  total++;
  const t = I18N[LANG] || I18N.en;
  document.getElementById('flash-score').textContent = (LANG === 'es' ? 'Aciertos' : 'Score') + `: ${aciertos} / ${total}`;
  nuevaFlash();
}

if (document.getElementById('flashcard')) nuevaFlash();

// ===== Translator (word by word, demo) =====
function buscarPalabra(tok) {
  let p = LEXICO.find(x => x.f === tok);
  if (p) return p;
  const base = tok.replace(/-(ve|pen|di|sa)$/, '').replace(/^(an|ne|na|me|pi)-/, '').replace(/-s$/, '');
  p = LEXICO.find(x => x.f === base);
  return p || null;
}

function traducir() {
  const texto = document.getElementById('texto-origen').value.trim();
  const out = document.getElementById('traduccion');
  if (!texto) { out.innerHTML = '<p class="gloss">…</p>'; return; }
  const tokens = texto.split(/\s+/);
  out.innerHTML = tokens.map(tok => {
    const p = buscarPalabra(tok);
    if (!p) return `<span class="gloss" title="not found">${tok}?</span>`;
    return `<span title="${p.c}">${traduccionDe(p)}</span>`;
  }).join(' ');
}

// ===== Init =====
setIdioma('en');
