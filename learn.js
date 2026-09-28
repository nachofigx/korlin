// Korlin — app de aprendizaje tipo Duolingo (v3: interfaz bilingüe ES/EN)
// Usa window.KORLIN_LEXICO (generado desde data/lexico.yaml)

const LEXICO = window.KORLIN_LEXICO || [];
let LANG = 'es';

// ===== Traducciones de la interfaz =====
const I18N = {
  es: {
    titulo: 'Aprende Korlin', subtitulo: 'La lengua corta, honesta y moderna.',
    disponible: 'disponible', nivel: 'nivel', dominada: 'dominada 🏆',
    palabras: 'palabras', frases: 'frases completas', completada: 'completada ✓',
    vamos: '¡Vamos! 🚀', significa: '¿Qué significa?', comoSeDice: '¿Cómo se dice en Korlin?',
    ordena: 'Ordena la frase:', tocaOrden: 'Toca las palabras en orden…', comprobar: 'Comprobar',
    empareja: 'Empareja cada palabra con su significado',
    escuchaEscribe: 'Escucha y escribe lo que oyes en Korlin', escuchaDeNuevo: '(pulsa para escuchar de nuevo)',
    escribePalabra: 'Escribe la palabra…', completa: 'Completa la frase:',
    perfecto: '¡Perfecto!', leccionCompletada: '¡Lección completada!', continuar: 'Continuar',
    sinVidas: 'Sin vidas... 💔', sinVidasAlert: 'Sin vidas ❤️. Vuelve mañana o reinicia tu progreso.',
    era: 'Era:', error: 'error', errores: 'errores',
    conversar: '🗣️ Conversar en Korlin', escuchar: '🔊 Escuchar',
    tuRespuesta: 'Tu respuesta aparecerá aquí…', escuchando: 'Escuchando… 🎙️',
    noTeEscuche: 'No te escuché. Intenta de nuevo.', pista: 'Pista: intenta decir',
    convCompletada: 'Conversación completada. ¡Enhorabuena!', yaSabesKorlin: '¡Bien! ¡Ya sabes Korlin!',
    sinSoporte: 'Tu navegador no soporta reconocimiento de voz. Usa Chrome o Edge.',
    flashcards: '🎴 Repasar con flashcards', noLaSabia: '🙈 No la sabía', laSabia: '✅ La sabía', gramatica: 'gramática',
  },
  en: {
    titulo: 'Learn Korlin', subtitulo: 'The short, honest, modern language.',
    disponible: 'available', nivel: 'level', dominada: 'mastered 🏆',
    palabras: 'words', frases: 'phrases', completada: 'completed ✓',
    vamos: "Let's go! 🚀", significa: 'What does it mean?', comoSeDice: 'How do you say it in Korlin?',
    ordena: 'Order the sentence:', tocaOrden: 'Tap the words in order…', comprobar: 'Check',
    empareja: 'Match each word with its meaning',
    escuchaEscribe: 'Listen and type what you hear in Korlin', escuchaDeNuevo: '(tap to listen again)',
    escribePalabra: 'Type the word…', completa: 'Complete the sentence:',
    perfecto: 'Perfect!', leccionCompletada: 'Lesson completed!', continuar: 'Continue',
    sinVidas: 'No lives... 💔', sinVidasAlert: 'No lives ❤️. Come back tomorrow or reset your progress.',
    era: 'It was:', error: 'error', errores: 'errors',
    conversar: '🗣️ Chat in Korlin', escuchar: '🔊 Listen',
    tuRespuesta: 'Your answer will appear here…', escuchando: 'Listening… 🎙️',
    noTeEscuche: "I didn't hear you. Try again.", pista: 'Hint: try saying',
    convCompletada: 'Conversation completed. Congratulations!', yaSabesKorlin: 'Great! You know Korlin!',
    sinSoporte: "Your browser doesn't support speech recognition. Use Chrome or Edge.",
    flashcards: '🎴 Review with flashcards', noLaSabia: "🙈 Didn't know it", laSabia: '✅ Knew it', gramatica: 'grammar',
  },
};
function t(clave) { return (I18N[LANG] || I18N.es)[clave] || clave; }

// ===== Lecciones =====
const LECCIONES = [
  { id: 'saludos', nombre: 'Saludos', nombre_en: 'Greetings', icono: '👋', mascota: 'assets/personajes/pez.jpg', palabras: ['halo','mi','tu','e','ya','na'] },
  { id: 'verbos', nombre: 'Verbos', nombre_en: 'Verbs', icono: '🏃', mascota: 'assets/personajes/monstruo.jpg', palabras: ['go','ven','ve','man','bi','do','pa','di'] },
  { id: 'cosas', nombre: 'Personas y cosas', nombre_en: 'People & things', icono: '📦', mascota: 'assets/personajes/cocodrilo.jpg', palabras: ['pe','re','ho','wa','fo','kin'] },
  { id: 'adjetivos', nombre: 'Adjetivos', nombre_en: 'Adjectives', icono: '✨', mascota: 'assets/personajes/ovoide.jpg', palabras: ['gu','fe','me','pi','ko','ne','an'] },
  { id: 'numeros', nombre: 'Números', nombre_en: 'Numbers', icono: '🔢', mascota: 'assets/personajes/cocodrilo2.jpg', palabras: ['u','du','san','fu','sin'] },
  { id: 'colores', nombre: 'Colores', nombre_en: 'Colors', icono: '🎨', mascota: 'assets/personajes/pez.jpg', palabras: ['ru','gi','ro','lumi','noi','sui'] },
  { id: 'actitud', nombre: 'Emociones', nombre_en: 'Emotions', icono: '💖', mascota: 'assets/personajes/monstruo.jpg', palabras: ['yo','we','fi','ri','hu','bu','la'] },
  { id: 'frases', nombre: 'Frases', nombre_en: 'Phrases', icono: '💬', mascota: 'assets/personajes/ovoide.jpg', tipo: 'frases' },
  { id: 'evidenciales', nombre: 'Evidenciales', nombre_en: 'Evidentials', icono: '🛡️', mascota: 'assets/personajes/monstruo.jpg', tipo: 'gramatica',
    explicacion: { es: 'Toda afirmación declara su fuente: -ve directo, -pen inferido, -di reportado, -sa asumido.', en: 'Every statement declares its source: -ve direct, -pen inferred, -di reported, -sa assumed.' },
    pares: [
      { f: 'go-ve', es: 'va (lo vi)', en: 'goes (I saw)' },
      { f: 'go-pen', es: 'va (lo deduzco)', en: 'goes (I infer)' },
      { f: 'go-di', es: 'va (me lo contaron)', en: 'goes (told)' },
      { f: 'go-sa', es: 'va (se asume)', en: 'goes (assumed)' },
      { f: 've-ve', es: 've (lo veo)', en: 'sees (direct)' },
      { f: 've-di', es: 've (me lo dijeron)', en: 'sees (reported)' },
    ] },
  { id: 'tiempos', nombre: 'Tiempos', nombre_en: 'Tenses', icono: '⏰', mascota: 'assets/personajes/pez.jpg', tipo: 'gramatica',
    explicacion: { es: 'an- indica pasado, ne- indica futuro. El presente no lleva marca.', en: 'an- marks past, ne- marks future. Present is unmarked.' },
    pares: [
      { f: 'an-go', es: 'fue', en: 'went' },
      { f: 'ne-go', es: 'irá', en: 'will go' },
      { f: 'an-man', es: 'comió', en: 'ate' },
      { f: 'ne-man', es: 'comerá', en: 'will eat' },
      { f: 'an-vi', es: 'vivió', en: 'lived' },
      { f: 'ne-vi', es: 'vivirá', en: 'will live' },
    ] },
  { id: 'derivacion', nombre: 'Derivación', nombre_en: 'Derivation', icono: '🧩', mascota: 'assets/personajes/cocodrilo.jpg', tipo: 'gramatica',
    explicacion: { es: 'Los afijos crean palabras: -pe agente, -lo lugar, -re cosa, na- opuesto, me- aumentativo, pi- diminutivo.', en: 'Affixes build words: -pe agent, -lo place, -re thing, na- opposite, me- augmentative, pi- diminutive.' },
    pares: [
      { f: 'ban-pe', es: 'constructor', en: 'builder' },
      { f: 'man-lo', es: 'comedor', en: 'dining room' },
      { f: 'man-re', es: 'comida', en: 'food' },
      { f: 'na-toro', es: 'mentira', en: 'lie' },
      { f: 'me-ho', es: 'mansión', en: 'mansion' },
      { f: 'pi-ho', es: 'casita', en: 'little house' },
    ] },
];

const FRASES = [
  { k: 'mi go a le ho', es: 'voy a la casa', en: 'I go to the house' },
  { k: 'le gu pe', es: 'la buena persona', en: 'the good person' },
  { k: 'mi na sa', es: 'no sé', en: "I don't know" },
  { k: 'tu go mo', es: '¿vas?', en: 'are you going?' },
  { k: 'le ho de mi', es: 'mi casa', en: 'my house' },
  { k: 'na-toro na-kan-sa vi i mi', es: 'la mentira no puede vivir en mí', en: 'the lie cannot live in me' },
  { k: 'mi e-sa Korlin', es: 'yo soy Korlin', en: 'I am Korlin' },
];

// ===== Estado (localStorage) =====
const CLAVE = 'korlin_estado';
function cargarEstado() {
  try {
    return JSON.parse(localStorage.getItem(CLAVE)) || { xp: 0, racha: 0, vidas: 3, ultima: null, completadas: {} };
  } catch (e) {
    return { xp: 0, racha: 0, vidas: 3, ultima: null, completadas: {} };
  }
}
let estado = cargarEstado();
function guardar() { localStorage.setItem(CLAVE, JSON.stringify(estado)); }

// ===== DOM =====
const $ = (id) => document.getElementById(id);
const vistaLecciones = $('vista-lecciones');
const vistaLeccion = $('vista-leccion');
const vistaResultado = $('vista-resultado');
const vistaConversar = $('vista-conversar');
const vistaFlashcards = $('vista-flashcards');

// ===== Utilidades =====
function getPalabra(f) { return LEXICO.find(p => p.f === f); }
function sig(p) { return p[LANG] || p.es; }
function nom(l) { return LANG === 'en' ? (l.nombre_en || l.nombre) : l.nombre; }
function barajar(arr) { const a = [...arr]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

const MSG_OK = ['Gu! 👍', 'To! ✅', 'Ra! ⚡', 'Gu-gu! 🎉'];
const MSG_NO = ['Na... 😅', 'Ku... ⚠️', 'Os... 🤔', 'Ba... 🙃'];

function hablar(texto) {
  if (!('speechSynthesis' in window)) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(texto);
  u.lang = 'es-ES';
  u.rate = 0.8;
  speechSynthesis.speak(u);
}

// ===== Motor de lección =====
let leccionActual = null;
let ejercicios = [];
let idxEjercicio = 0;
let errores = 0;
let respondiendo = false;

function mostrarVista(v) {
  [vistaLecciones, vistaLeccion, vistaResultado, vistaConversar, vistaFlashcards].forEach(x => x.classList.remove('active'));
  if (v === 'lecciones') vistaLecciones.classList.add('active');
  if (v === 'leccion') vistaLeccion.classList.add('active');
  if (v === 'resultado') vistaResultado.classList.add('active');
  if (v === 'conversar') vistaConversar.classList.add('active');
  if (v === 'flashcards') vistaFlashcards.classList.add('active');
  actualizarHUD();
}

function actualizarHUD() {
  $('racha').textContent = estado.racha;
  $('xp').textContent = estado.xp;
  $('vidas').textContent = estado.vidas;
  $('vidas-mini').textContent = '❤️'.repeat(Math.max(0, estado.vidas)) || '💔';
}

// ===== Render lecciones =====
function renderLecciones() {
  const lista = $('lista-lecciones');
  $('titulo-app').textContent = t('titulo');
  $('subtitulo-app').textContent = t('subtitulo');
  lista.innerHTML = LECCIONES.map((l, i) => {
    const nivel = Math.min(estado.completadas[l.id] || 0, 5);
    const completada = nivel > 0;
    const dominada = nivel >= 5;
    const bloqueada = i > 0 && (estado.completadas[LECCIONES[i - 1].id] || 0) === 0;
    const detalle = l.tipo === 'frases' ? t('frases') : (l.tipo === 'gramatica' ? t('gramatica') : (l.palabras.length + ' ' + t('palabras')));
    const estadoTxt = dominada ? t('dominada') : (completada ? t('nivel') + ' ' + nivel + '/5' : t('disponible'));
    return `
      <div class="leccion-card ${completada ? 'completada' : ''} ${bloqueada ? 'bloqueada' : ''}" onclick="${bloqueada ? '' : "iniciarLeccion('" + l.id + "')"}">
        <div class="ico">${l.icono}</div>
        <div class="info">
          <b>${nom(l)}</b>
          <span>${detalle} · ${estadoTxt}</span>
        </div>
        <div class="estado">${dominada ? '🏆' : completada ? '✅' : bloqueada ? '🔒' : '▶️'}</div>
      </div>`;
  }).join('');
}

// ===== Iniciar lección =====
function iniciarLeccion(id) {
  if (estado.vidas <= 0) { alert(t('sinVidasAlert')); return; }
  leccionActual = LECCIONES.find(l => l.id === id);

  if (leccionActual.tipo === 'frases') {
    ejercicios = barajar(FRASES.slice(0, 6)).map((f, i) => i % 2 === 0 ? { tipo: 'ordenar', frase: f } : crearFill(f));
  } else if (leccionActual.tipo === 'gramatica') {
    ejercicios = barajar(leccionActual.pares).map(p => crearChoice(p, leccionActual.pares));
  } else {
    const palabras = leccionActual.palabras.map(getPalabra).filter(Boolean);
    ejercicios = [];
    for (let i = 0; i < 7; i++) {
      if (i % 4 === 3) ejercicios.push(crearDictado(palabras[i % palabras.length]));
      else ejercicios.push(crearChoice(palabras[i % palabras.length]));
    }
    ejercicios.push(crearEmparejar(barajar(palabras).slice(0, 5)));
  }

  idxEjercicio = 0;
  errores = 0;
  respondiendo = false;
  $('mascota-img').src = leccionActual.mascota;
  mostrarVista('leccion');
  $('bocadillo').textContent = leccionActual.explicacion
    ? (leccionActual.explicacion[LANG] || leccionActual.explicacion.es)
    : t('vamos');
  renderEjercicio();
}

function crearChoice(objetivo, pool) {
  const tipo = Math.random() < 0.5 ? 'k2s' : 's2k';
  const base = pool || LEXICO;
  const distractores = barajar(base.filter(p => p.f !== objetivo.f)).slice(0, 3);
  const opciones = barajar([objetivo, ...distractores]);
  const correcta = opciones.indexOf(objetivo);
  return { tipo, objetivo, opciones, correcta };
}

function crearEmparejar(palabras) {
  return { tipo: 'emparejar', pares: palabras.map(p => ({ f: p.f, s: sig(p) })) };
}

// ===== Render ejercicio =====
function renderEjercicio() {
  const e = ejercicios[idxEjercicio];
  $('barra-fill').style.width = ((idxEjercicio) / ejercicios.length * 100) + '%';
  respondiendo = false;

  if (e.tipo === 'k2s' || e.tipo === 's2k') renderChoice(e);
  else if (e.tipo === 'ordenar') renderOrdenar(e);
  else if (e.tipo === 'emparejar') renderEmparejar(e);
  else if (e.tipo === 'fill') renderFill(e);
  else if (e.tipo === 'dictado') renderDictado(e);
}

function renderChoice(e) {
  const prompt = e.tipo === 'k2s' ? `<span class="korlin">${e.objetivo.f}</span>` : `"${sig(e.objetivo)}"`;
  const pregunta = e.tipo === 'k2s' ? t('significa') : t('comoSeDice');
  const audioBtn = e.tipo === 'k2s' ? `<button class="btn-audio" onclick="hablar('${e.objetivo.f}')">🔊</button>` : '';
  const opciones = e.opciones.map((p, i) => {
    const texto = e.tipo === 'k2s' ? sig(p) : `<span class="korlin">${p.f}</span>`;
    return `<button class="opcion" onclick="responderChoice(${i})">${texto}</button>`;
  }).join('');
  $('ejercicio').innerHTML = `
    <div class="palabra-grande">${prompt} ${audioBtn}</div>
    <p class="prompt">${pregunta}</p>
    <div class="opciones">${opciones}</div>`;
}

function responderChoice(i) {
  if (respondiendo) return;
  respondiendo = true;
  const e = ejercicios[idxEjercicio];
  const botones = document.querySelectorAll('#ejercicio .opcion');
  botones.forEach((b, idx) => {
    b.disabled = true;
    if (idx === e.correcta) b.classList.add('correcta');
    if (idx === i && i !== e.correcta) b.classList.add('incorrecta');
  });
  if (i === e.correcta) {
    $('bocadillo').textContent = MSG_OK[Math.floor(Math.random() * MSG_OK.length)];
    estado.xp += 10;
  } else {
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)] + ' ' + t('era') + ' ' + (e.tipo === 'k2s' ? sig(e.objetivo) : e.objetivo.f);
    estado.vidas -= 1; errores++;
  }
  guardar(); actualizarHUD();
  setTimeout(avanzar, 900);
}

function renderOrdenar(e) {
  const f = e.frase;
  const trad = f[LANG] || f.es;
  e.tokens = f.k.split(' ');
  e.seleccion = [];
  e.restantes = barajar(e.tokens);
  e.resuelto = false;
  $('ejercicio').innerHTML = `
    <p class="prompt">${t('ordena')} <b>"${trad}"</b></p>
    <div id="zona-respuesta" class="zona-respuesta"></div>
    <div id="zona-palabras" class="zona-palabras"></div>
    <button id="btn-comprobar" class="btn-primario" style="display:none;margin-top:16px">${t('comprobar')}</button>`;
  pintarOrdenar(e);
}

function pintarOrdenar(e) {
  const resp = $('zona-respuesta');
  const pals = $('zona-palabras');
  resp.innerHTML = e.seleccion.map((t, i) => `<span class="chip" onclick="quitarToken(${i})">${t}</span>`).join('')
    || `<span class="placeholder">${t('tocaOrden')}</span>`;
  pals.innerHTML = e.restantes.map((t) => `<span class="chip" onclick="ponerToken('${t}')">${t}</span>`).join('');
  $('btn-comprobar').style.display = (e.seleccion.length === e.tokens.length && !e.resuelto) ? 'block' : 'none';
  if (e.seleccion.length === e.tokens.length && !e.resuelto) $('btn-comprobar').onclick = () => comprobarOrden(e);
}

function ponerToken(t) {
  const e = ejercicios[idxEjercicio];
  const i = e.restantes.indexOf(t);
  if (i < 0) return;
  e.seleccion.push(e.restantes.splice(i, 1)[0]);
  pintarOrdenar(e);
}
function quitarToken(i) {
  const e = ejercicios[idxEjercicio];
  e.restantes.push(e.seleccion.splice(i, 1)[0]);
  pintarOrdenar(e);
}
function comprobarOrden(e) {
  if (respondiendo) return;
  respondiendo = true;
  const correcto = e.seleccion.join(' ') === e.tokens.join(' ');
  e.resuelto = true;
  $('zona-respuesta').innerHTML = e.tokens.map(t => `<span class="chip ${correcto ? 'correcta' : 'incorrecta'}">${t}</span>`).join('');
  $('zona-palabras').innerHTML = '';
  $('btn-comprobar').style.display = 'none';
  if (correcto) {
    $('bocadillo').textContent = MSG_OK[Math.floor(Math.random() * MSG_OK.length)];
    estado.xp += 10;
  } else {
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)];
    estado.vidas -= 1; errores++;
  }
  guardar(); actualizarHUD();
  setTimeout(avanzar, 1000);
}

function renderEmparejar(e) {
  e.korlin = barajar(e.pares.map(p => p.f));
  e.sigs = barajar(e.pares.map(p => p.s));
  e.hechos = {};
  e.selF = null;
  $('ejercicio').innerHTML = `
    <p class="prompt">${t('empareja')}</p>
    <div class="emparejar">
      <div class="col" id="col-korlin"></div>
      <div class="col" id="col-sigs"></div>
    </div>`;
  pintarEmparejar(e);
}

function pintarEmparejar(e) {
  const colK = $('col-korlin');
  const colS = $('col-sigs');
  colK.innerHTML = e.korlin.map(f => {
    if (e.hechos[f]) return `<span class="chip correcta">${f}</span>`;
    return `<span class="chip ${e.selF === f ? 'seleccionada' : ''}" onclick="selKorlin('${f}')">${f}</span>`;
  }).join('');
  colS.innerHTML = e.sigs.map(s => {
    if (Object.values(e.hechos).includes(s)) return `<span class="chip correcta">${s}</span>`;
    return `<span class="chip" onclick="selSig('${s}')">${s}</span>`;
  }).join('');
}

function selKorlin(f) { const e = ejercicios[idxEjercicio]; e.selF = f; pintarEmparejar(e); }
function selSig(s) {
  const e = ejercicios[idxEjercicio];
  if (!e.selF) return;
  const par = e.pares.find(p => p.f === e.selF);
  if (par.s === s) {
    e.hechos[par.f] = par.s;
    e.selF = null;
    $('bocadillo').textContent = 'Gu! 👍';
    estado.xp += 5; guardar(); actualizarHUD();
    pintarEmparejar(e);
    if (Object.keys(e.hechos).length === e.pares.length) { $('bocadillo').textContent = '🎉'; setTimeout(avanzar, 800); }
  } else {
    e.selF = null;
    $('bocadillo').textContent = 'Na... 😅';
    pintarEmparejar(e);
  }
}

function crearFill(frase) {
  const tokens = frase.k.split(' ');
  const hueco = Math.floor(Math.random() * tokens.length);
  const respuesta = tokens[hueco];
  const distractores = barajar(LEXICO.filter(p => p.f !== respuesta)).slice(0, 3).map(p => p.f);
  const opciones = barajar([respuesta, ...distractores]);
  return { tipo: 'fill', frase, tokens, hueco, respuesta, opciones };
}

function renderFill(e) {
  const trad = e.frase[LANG] || e.frase.es;
  const tokensHtml = e.tokens.map((t, i) => i === e.hueco ? '<span class="hueco">____</span>' : t).join(' ');
  const opciones = e.opciones.map(t => `<button class="opcion" data-p="${t}" onclick="responderFill('${t}')">${t}</button>`).join('');
  $('ejercicio').innerHTML = `
    <p class="prompt">${t('completa')} <b>"${trad}"</b></p>
    <div class="palabra-grande">${tokensHtml}</div>
    <div class="opciones">${opciones}</div>`;
}

function responderFill(t) {
  if (respondiendo) return;
  respondiendo = true;
  const e = ejercicios[idxEjercicio];
  const correcto = t === e.respuesta;
  document.querySelectorAll('#ejercicio .opcion').forEach(b => {
    b.disabled = true;
    if (b.dataset.p === e.respuesta) b.classList.add('correcta');
    if (b.dataset.p === t && !correcto) b.classList.add('incorrecta');
  });
  if (correcto) {
    $('bocadillo').textContent = MSG_OK[Math.floor(Math.random() * MSG_OK.length)];
    estado.xp += 10;
  } else {
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)];
    estado.vidas -= 1; errores++;
  }
  guardar(); actualizarHUD();
  setTimeout(avanzar, 900);
}

function crearDictado(palabra) { return { tipo: 'dictado', objetivo: palabra }; }

function renderDictado(e) {
  $('ejercicio').innerHTML = `
    <p class="prompt">${t('escuchaEscribe')}</p>
    <div class="audio-grande">
      <button class="btn-audio-grande" onclick="hablar('${e.objetivo.f}')">🔊</button>
      <p class="sub">${t('escuchaDeNuevo')}</p>
    </div>
    <input type="text" id="input-dictado" placeholder="${t('escribePalabra')}" autocomplete="off" autocapitalize="off" spellcheck="false">
    <button class="btn-primario" style="width:100%" onclick="comprobarDictado()">${t('comprobar')}</button>`;
  hablar(e.objetivo.f);
  $('input-dictado').focus();
  $('input-dictado').addEventListener('keydown', (ev) => { if (ev.key === 'Enter') comprobarDictado(); });
}

function comprobarDictado() {
  if (respondiendo) return;
  const e = ejercicios[idxEjercicio];
  const valor = ($('input-dictado').value || '').trim().toLowerCase();
  const correcto = valor === e.objetivo.f;
  respondiendo = true;
  if (correcto) {
    $('bocadillo').textContent = MSG_OK[Math.floor(Math.random() * MSG_OK.length)];
    estado.xp += 10;
  } else {
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)] + ' ' + t('era') + ' ' + e.objetivo.f;
    estado.vidas -= 1; errores++;
  }
  guardar(); actualizarHUD();
  setTimeout(avanzar, 900);
}

// ===== Avanzar =====
function avanzar() {
  if (estado.vidas <= 0) {
    $('bocadillo').textContent = t('sinVidas');
    setTimeout(() => { mostrarVista('lecciones'); renderLecciones(); }, 1200);
    return;
  }
  idxEjercicio++;
  if (idxEjercicio >= ejercicios.length) completarLeccion();
  else renderEjercicio();
}

function completarLeccion() {
  const bonus = errores === 0 ? 15 : 0;
  estado.xp += bonus;
  estado.completadas[leccionActual.id] = (estado.completadas[leccionActual.id] || 0) + 1;
  actualizarRacha();
  guardar();
  $('resultado-icono').textContent = errores === 0 ? '🏆' : '🎉';
  $('resultado-titulo').textContent = errores === 0 ? t('perfecto') : t('leccionCompletada');
  $('resultado-detalle').textContent = `"${nom(leccionActual)}" · ${errores} ${t(errores === 1 ? 'error' : 'errores')}`;
  $('resultado-xp').textContent = (10 * 7 + 5 * 5) + bonus;
  $('btn-continuar').textContent = t('continuar');
  mostrarVista('resultado');
}

function actualizarRacha() {
  const hoy = new Date().toDateString();
  const ayer = new Date(Date.now() - 86400000).toDateString();
  if (estado.ultima === ayer) estado.racha += 1;
  else if (estado.ultima !== hoy) estado.racha = 1;
  estado.ultima = hoy;
}

// ===== Conversación por voz =====
const DIALOGO = [
  { m: 'Halo! Mi e-sa Lin.', es: '¡Hola! Yo soy Lin.', en: 'Hi! I am Lin.', esperado: ['halo'] },
  { m: 'Tu e-sa mo gu?', es: '¿Estás bien?', en: 'Are you ok?', esperado: ['ya', 'gu'] },
  { m: 'Gu! To.', es: '¡Bien! Cierto.', en: 'Good! Sure.', esperado: ['to', 'gu'] },
  { m: 'Mi e-sa u ko lin.', es: 'Soy una lengua corta.', en: 'I am a short language.', esperado: ['ko', 'lin'] },
  { m: 'Tu kan-ve sa mi.', es: 'Puedes aprenderme.', en: 'You can learn me.', esperado: ['ya', 'kan'] },
  { m: 'Na-toro na-kan-sa vi i mi.', es: 'La mentira no puede vivir en mí.', en: 'The lie cannot live in me.', esperado: ['toro', 'na-toro'] },
];

let idxDialogo = 0;
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
let rec = null;

function normalizar(s) { return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }

function iniciarConversacion() {
  idxDialogo = 0;
  $('btn-mic').style.display = '';
  $('btn-conversar').textContent = t('conversar');
  mostrarVista('conversar');
  siguienteTurno();
}

function siguienteTurno() {
  const turno = DIALOGO[idxDialogo];
  if (!turno) {
    $('conv-bocadillo').textContent = 'Gu! Tu sa Korlin! 🎉';
    $('conv-traduccion').textContent = t('yaSabesKorlin');
    $('conv-transcripcion').textContent = t('convCompletada');
    $('conv-pista').textContent = '';
    $('btn-mic').style.display = 'none';
    estado.xp += 20; guardar(); actualizarHUD();
    return;
  }
  $('conv-bocadillo').textContent = turno.m;
  $('conv-traduccion').textContent = turno[LANG] || turno.es;
  $('conv-transcripcion').textContent = t('tuRespuesta');
  $('conv-transcripcion').className = 'transcripcion';
  $('conv-pista').textContent = '';
  $('btn-escuchar').textContent = t('escuchar');
  hablar(turno.m);
}

function escuchar() {
  if (!SR) { alert(t('sinSoporte')); return; }
  if (!rec) {
    rec = new SR();
    rec.lang = 'es-ES';
    rec.interimResults = false;
    rec.maxAlternatives = 1;
    rec.onresult = (ev) => { verificar(ev.results[0][0].transcript); };
    rec.onerror = () => { $('btn-mic').classList.remove('escuchando'); $('conv-transcripcion').textContent = t('noTeEscuche'); };
    rec.onend = () => { $('btn-mic').classList.remove('escuchando'); };
  }
  $('btn-mic').classList.add('escuchando');
  $('conv-transcripcion').textContent = t('escuchando');
  rec.start();
}

function verificar(texto) {
  const turno = DIALOGO[idxDialogo];
  const n = normalizar(texto);
  const ok = turno.esperado.some(e => n.includes(normalizar(e)));
  const tc = $('conv-transcripcion');
  tc.textContent = (LANG === 'es' ? 'Tú: ' : 'You: ') + texto;
  tc.className = 'transcripcion ' + (ok ? 'correcta' : 'incorrecta');
  if (ok) {
    $('conv-bocadillo').textContent = 'Gu! 👍';
    estado.xp += 5; guardar(); actualizarHUD();
    setTimeout(() => { idxDialogo++; siguienteTurno(); }, 1200);
  } else {
    $('conv-pista').textContent = t('pista') + ' "' + turno.esperado[0] + '"';
  }
}

$('btn-conversar').addEventListener('click', iniciarConversacion);
$('btn-salir-conv').addEventListener('click', () => { if (rec) rec.abort(); speechSynthesis.cancel(); mostrarVista('lecciones'); renderLecciones(); });
$('btn-mic').addEventListener('click', escuchar);
$('btn-escuchar').addEventListener('click', () => { if (idxDialogo < DIALOGO.length) hablar(DIALOGO[idxDialogo].m); });

// ===== Botones =====
$('btn-salir').addEventListener('click', () => { speechSynthesis.cancel(); mostrarVista('lecciones'); renderLecciones(); });
$('btn-continuar').addEventListener('click', () => { mostrarVista('lecciones'); renderLecciones(); });
document.querySelectorAll('.langbtn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.langbtn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    LANG = btn.dataset.lang;
    if (vistaLecciones.classList.contains('active')) renderLecciones();
    else if (vistaLeccion.classList.contains('active')) renderEjercicio();
    else if (vistaConversar.classList.contains('active')) siguienteTurno();
  });
});

// ===== Flashcards =====
let flashIdx = 0;
let flashPalabras = [];
let flashVolteada = false;

function iniciarFlashcards() {
  flashPalabras = barajar(LEXICO).slice(0, 20);
  flashIdx = 0;
  mostrarVista('flashcards');
  renderFlash();
}

function renderFlash() {
  const p = flashPalabras[flashIdx];
  $('flash-frente').textContent = p.f;
  $('flash-reverso').textContent = sig(p);
  $('flash-card').classList.remove('volteada');
  flashVolteada = false;
  $('flash-contador').textContent = (flashIdx + 1) + ' / ' + flashPalabras.length;
  $('flash-btn-no').textContent = t('noLaSabia');
  $('flash-btn-si').textContent = t('laSabia');
}

function voltearFlash() {
  flashVolteada = !flashVolteada;
  $('flash-card').classList.toggle('volteada', flashVolteada);
}

function flashSiguiente() {
  flashIdx++;
  if (flashIdx >= flashPalabras.length) {
    estado.xp += 10; guardar(); actualizarHUD();
    mostrarVista('lecciones'); renderLecciones();
    return;
  }
  renderFlash();
}

$('btn-flashcards').addEventListener('click', iniciarFlashcards);
$('btn-salir-flash').addEventListener('click', () => { mostrarVista('lecciones'); renderLecciones(); });
$('flash-btn-no').addEventListener('click', flashSiguiente);
$('flash-btn-si').addEventListener('click', flashSiguiente);

// ===== Init =====
actualizarHUD();
renderLecciones();
