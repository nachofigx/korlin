// Korlin — app de aprendizaje tipo Duolingo (v2: más tipos de ejercicio)
// Usa window.KORLIN_LEXICO (generado desde data/lexico.yaml)

const LEXICO = window.KORLIN_LEXICO || [];
let LANG = 'es';

// ===== Lecciones =====
const LECCIONES = [
  { id: 'saludos', nombre: 'Saludos', icono: '👋', mascota: 'assets/personajes/pez.jpg', palabras: ['halo','mi','tu','e','ya','na'] },
  { id: 'verbos', nombre: 'Verbos', icono: '🏃', mascota: 'assets/personajes/monstruo.jpg', palabras: ['go','ven','ve','man','bi','do','pa','di'] },
  { id: 'cosas', nombre: 'Personas y cosas', icono: '📦', mascota: 'assets/personajes/cocodrilo.jpg', palabras: ['pe','re','ho','wa','fo','kin'] },
  { id: 'adjetivos', nombre: 'Adjetivos', icono: '✨', mascota: 'assets/personajes/ovoide.jpg', palabras: ['gu','fe','me','pi','ko','ne','an'] },
  { id: 'numeros', nombre: 'Números', icono: '🔢', mascota: 'assets/personajes/cocodrilo2.jpg', palabras: ['u','du','san','fu','sin'] },
  { id: 'colores', nombre: 'Colores', icono: '🎨', mascota: 'assets/personajes/pez.jpg', palabras: ['ru','gi','ro','lumi','noi','sui'] },
  { id: 'actitud', nombre: 'Emociones', icono: '💖', mascota: 'assets/personajes/monstruo.jpg', palabras: ['yo','we','fi','ri','hu','bu','la'] },
  { id: 'frases', nombre: 'Frases', icono: '💬', mascota: 'assets/personajes/ovoide.jpg', tipo: 'frases' },
];

// ===== Frases (para el ejercicio de ordenar) =====
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

// ===== Utilidades =====
function getPalabra(f) { return LEXICO.find(p => p.f === f); }
function sig(p) { return p[LANG] || p.es; }
function barajar(arr) { const a = [...arr]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

const MSG_OK = ['Gu! 👍', 'To! ✅', 'Ra! ⚡', 'Gu-gu! 🎉'];
const MSG_NO = ['Na... 😅', 'Ku... ⚠️', 'Os... 🤔', 'Ba... 🙃'];

// ===== Audio (Web Speech API) =====
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
let pendientes = [];   // estado temporal para ordenar/emparejar

function mostrarVista(v) {
  [vistaLecciones, vistaLeccion, vistaResultado, vistaConversar].forEach(x => x.classList.remove('active'));
  if (v === 'lecciones') vistaLecciones.classList.add('active');
  if (v === 'leccion') vistaLeccion.classList.add('active');
  if (v === 'resultado') vistaResultado.classList.add('active');
  if (v === 'conversar') vistaConversar.classList.add('active');
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
  lista.innerHTML = LECCIONES.map((l, i) => {
    const nivel = Math.min(estado.completadas[l.id] || 0, 5);
    const completada = nivel > 0;
    const dominada = nivel >= 5;
    const bloqueada = i > 0 && (estado.completadas[LECCIONES[i - 1].id] || 0) === 0;
    const detalle = l.tipo === 'frases' ? 'frases completas' : (l.palabras.length + ' palabras');
    const estadoTxt = dominada ? 'dominada 🏆' : (completada ? 'nivel ' + nivel + '/5' : 'disponible');
    return `
      <div class="leccion-card ${completada ? 'completada' : ''} ${bloqueada ? 'bloqueada' : ''}" onclick="${bloqueada ? '' : "iniciarLeccion('" + l.id + "')"}">
        <div class="ico">${l.icono}</div>
        <div class="info">
          <b>${l.nombre}</b>
          <span>${detalle} · ${estadoTxt}</span>
        </div>
        <div class="estado">${dominada ? '🏆' : completada ? '✅' : bloqueada ? '🔒' : '▶️'}</div>
      </div>`;
  }).join('');
}

// ===== Iniciar lección =====
function iniciarLeccion(id) {
  if (estado.vidas <= 0) { alert('Sin vidas ❤️. Vuelve mañana o reinicia tu progreso.'); return; }
  leccionActual = LECCIONES.find(l => l.id === id);

  if (leccionActual.tipo === 'frases') {
    ejercicios = barajar(FRASES.slice(0, 6)).map((f, i) => i % 2 === 0 ? { tipo: 'ordenar', frase: f } : crearFill(f));
  } else {
    const palabras = leccionActual.palabras.map(getPalabra).filter(Boolean);
    ejercicios = [];
    for (let i = 0; i < 7; i++) {
      if (i % 4 === 3) ejercicios.push(crearDictado(palabras[i % palabras.length]));
      else ejercicios.push(crearChoice(palabras[i % palabras.length]));
    }
    // último ejercicio: emparejar
    ejercicios.push(crearEmparejar(barajar(palabras).slice(0, 5)));
  }

  idxEjercicio = 0;
  errores = 0;
  respondiendo = false;
  $('mascota-img').src = leccionActual.mascota;
  mostrarVista('leccion');
  $('bocadillo').textContent = '¡Vamos! 🚀';
  renderEjercicio();
}

function crearChoice(objetivo) {
  const tipo = Math.random() < 0.5 ? 'k2s' : 's2k';
  const distractores = barajar(LEXICO.filter(p => p.f !== objetivo.f)).slice(0, 3);
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

  if (e.tipo === 'k2s' || e.tipo === 's2k') {
    renderChoice(e);
  } else if (e.tipo === 'ordenar') {
    renderOrdenar(e);
  } else if (e.tipo === 'emparejar') {
    renderEmparejar(e);
  } else if (e.tipo === 'fill') {
    renderFill(e);
  } else if (e.tipo === 'dictado') {
    renderDictado(e);
  }
}

// --- Choice ---
function renderChoice(e) {
  const prompt = e.tipo === 'k2s'
    ? `<span class="korlin">${e.objetivo.f}</span>`
    : `"${sig(e.objetivo)}"`;
  const pregunta = e.tipo === 'k2s' ? '¿Qué significa?' : '¿Cómo se dice en Korlin?';
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
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)] + ` Era: ${e.tipo === 'k2s' ? sig(e.objetivo) : e.objetivo.f}`;
    estado.vidas -= 1; errores++;
  }
  guardar(); actualizarHUD();
  setTimeout(avanzar, 900);
}

// --- Ordenar palabras ---
function renderOrdenar(e) {
  const f = e.frase;
  const trad = f[LANG] || f.es;
  e.tokens = f.k.split(' ');
  e.seleccion = [];
  e.restantes = barajar(e.tokens);
  e.resuelto = false;
  $('ejercicio').innerHTML = `
    <p class="prompt">Ordena la frase: <b>"${trad}"</b></p>
    <div id="zona-respuesta" class="zona-respuesta"></div>
    <div id="zona-palabras" class="zona-palabras"></div>
    <button id="btn-comprobar" class="btn-primario" style="display:none;margin-top:16px">Comprobar</button>`;
  pintarOrdenar(e);
}

function pintarOrdenar(e) {
  const resp = $('zona-respuesta');
  const pals = $('zona-palabras');
  resp.innerHTML = e.seleccion.map((t, i) => `<span class="chip" onclick="quitarToken(${i})">${t}</span>`).join('')
    || '<span class="placeholder">Toca las palabras en orden…</span>';
  pals.innerHTML = e.restantes.map((t) => `<span class="chip" onclick="ponerToken('${t}')">${t}</span>`).join('');
  $('btn-comprobar').style.display = (e.seleccion.length === e.tokens.length && !e.resuelto) ? 'block' : 'none';
  if (e.seleccion.length === e.tokens.length && !e.resuelto) {
    $('btn-comprobar').onclick = () => comprobarOrden(e);
  }
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

// --- Emparejar ---
function renderEmparejar(e) {
  e.korlin = barajar(e.pares.map(p => p.f));
  e.sigs = barajar(e.pares.map(p => p.s));
  e.hechos = {};
  e.selF = null;
  $('ejercicio').innerHTML = `
    <p class="prompt">Empareja cada palabra con su significado</p>
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
    const hecho = e.hechos[f];
    if (hecho) return `<span class="chip correcta">${f}</span>`;
    const sel = e.selF === f ? 'seleccionada' : '';
    return `<span class="chip ${sel}" onclick="selKorlin('${f}')">${f}</span>`;
  }).join('');
  colS.innerHTML = e.sigs.map(s => {
    const hecho = Object.values(e.hechos).includes(s);
    if (hecho) return `<span class="chip correcta">${s}</span>`;
    return `<span class="chip" onclick="selSig('${s}')">${s}</span>`;
  }).join('');
}

function selKorlin(f) {
  const e = ejercicios[idxEjercicio];
  e.selF = f;
  pintarEmparejar(e);
}
function selSig(s) {
  const e = ejercicios[idxEjercicio];
  if (!e.selF) return;
  const par = e.pares.find(p => p.f === e.selF);
  if (par.s === s) {
    e.hechos[par.f] = par.s;
    e.selF = null;
    $('bocadillo').textContent = 'Gu! 👍';
    estado.xp += 5;
    guardar(); actualizarHUD();
    pintarEmparejar(e);
    if (Object.keys(e.hechos).length === e.pares.length) {
      $('bocadillo').textContent = '¡Perfecto! 🎉';
      setTimeout(avanzar, 800);
    }
  } else {
    e.selF = null;
    $('bocadillo').textContent = 'Na... 😅';
    pintarEmparejar(e);
  }
}

// --- Completar hueco ---
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
    <p class="prompt">Completa la frase: <b>"${trad}"</b></p>
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

// --- Dictado (escucha y escribe) ---
function crearDictado(palabra) {
  return { tipo: 'dictado', objetivo: palabra };
}

function renderDictado(e) {
  $('ejercicio').innerHTML = `
    <p class="prompt">Escucha y escribe lo que oyes en Korlin</p>
    <div class="audio-grande">
      <button class="btn-audio-grande" onclick="hablar('${e.objetivo.f}')">🔊</button>
      <p class="sub">(pulsa para escuchar de nuevo)</p>
    </div>
    <input type="text" id="input-dictado" placeholder="Escribe la palabra…" autocomplete="off" autocapitalize="off" spellcheck="false">
    <button class="btn-primario" style="width:100%" onclick="comprobarDictado()">Comprobar</button>`;
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
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)] + ` Era: ${e.objetivo.f}`;
    estado.vidas -= 1; errores++;
  }
  guardar(); actualizarHUD();
  setTimeout(avanzar, 900);
}

// ===== Avanzar =====
function avanzar() {
  if (estado.vidas <= 0) {
    $('bocadillo').textContent = 'Sin vidas... 💔';
    setTimeout(() => { mostrarVista('lecciones'); renderLecciones(); }, 1200);
    return;
  }
  idxEjercicio++;
  if (idxEjercicio >= ejercicios.length) completarLeccion();
  else renderEjercicio();
}

// ===== Completar =====
function completarLeccion() {
  const bonus = errores === 0 ? 15 : 0;
  estado.xp += bonus;
  estado.completadas[leccionActual.id] = (estado.completadas[leccionActual.id] || 0) + 1;
  actualizarRacha();
  guardar();
  $('resultado-icono').textContent = errores === 0 ? '🏆' : '🎉';
  $('resultado-titulo').textContent = errores === 0 ? '¡Perfecto!' : '¡Lección completada!';
  $('resultado-detalle').textContent = `"${leccionActual.nombre}" · ${errores} error${errores === 1 ? '' : 'es'}`;
  $('resultado-xp').textContent = (10 * 7 + 5 * 5) + bonus;
  mostrarVista('resultado');
}

function actualizarRacha() {
  const hoy = new Date().toDateString();
  const ayer = new Date(Date.now() - 86400000).toDateString();
  if (estado.ultima === ayer) estado.racha += 1;
  else if (estado.ultima !== hoy) estado.racha = 1;
  estado.ultima = hoy;
}

// ===== Botones =====
$('btn-salir').addEventListener('click', () => { speechSynthesis.cancel(); mostrarVista('lecciones'); renderLecciones(); });
$('btn-continuar').addEventListener('click', () => { mostrarVista('lecciones'); renderLecciones(); });
document.querySelectorAll('.langbtn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.langbtn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    LANG = btn.dataset.lang;
  });
});

// ===== Conversación por voz =====
const DIALOGO = [
  { m: 'Halo! Mi e-sa Lin.', t: '¡Hola! Yo soy Lin.', esperado: ['halo'] },
  { m: 'Tu e-sa mo gu?', t: '¿Estás bien?', esperado: ['ya', 'gu'] },
  { m: 'Gu! To.', t: '¡Bien! Cierto.', esperado: ['to', 'gu'] },
  { m: 'Mi e-sa u ko lin.', t: 'Soy una lengua corta.', esperado: ['ko', 'lin'] },
  { m: 'Tu kan-ve sa mi.', t: 'Puedes aprenderme.', esperado: ['ya', 'kan'] },
  { m: 'Na-toro na-kan-sa vi i mi.', t: 'La mentira no puede vivir en mí.', esperado: ['toro', 'na-toro'] },
];

let idxDialogo = 0;
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
let rec = null;

function normalizar(s) {
  return (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function iniciarConversacion() {
  idxDialogo = 0;
  $('btn-mic').style.display = '';
  mostrarVista('conversar');
  siguienteTurno();
}

function siguienteTurno() {
  const turno = DIALOGO[idxDialogo];
  if (!turno) {
    $('conv-bocadillo').textContent = 'Gu! Tu sa Korlin! 🎉';
    $('conv-traduccion').textContent = '¡Bien! ¡Ya sabes Korlin!';
    $('conv-transcripcion').textContent = 'Conversación completada. ¡Enhorabuena!';
    $('conv-pista').textContent = '';
    $('btn-mic').style.display = 'none';
    estado.xp += 20; guardar(); actualizarHUD();
    return;
  }
  $('conv-bocadillo').textContent = turno.m;
  $('conv-traduccion').textContent = turno.t;
  $('conv-transcripcion').textContent = 'Tu respuesta aparecerá aquí…';
  $('conv-transcripcion').className = 'transcripcion';
  $('conv-pista').textContent = '';
  hablar(turno.m);
}

function escuchar() {
  if (!SR) { alert('Tu navegador no soporta reconocimiento de voz. Usa Chrome o Edge.'); return; }
  if (!rec) {
    rec = new SR();
    rec.lang = 'es-ES';
    rec.interimResults = false;
    rec.maxAlternatives = 1;
    rec.onresult = (ev) => { const texto = ev.results[0][0].transcript; verificar(texto); };
    rec.onerror = () => { $('btn-mic').classList.remove('escuchando'); $('conv-transcripcion').textContent = 'No te escuché. Intenta de nuevo.'; };
    rec.onend = () => { $('btn-mic').classList.remove('escuchando'); };
  }
  $('btn-mic').classList.add('escuchando');
  $('conv-transcripcion').textContent = 'Escuchando… 🎙️';
  rec.start();
}

function verificar(texto) {
  const turno = DIALOGO[idxDialogo];
  const n = normalizar(texto);
  const ok = turno.esperado.some(e => n.includes(normalizar(e)));
  const tc = $('conv-transcripcion');
  tc.textContent = 'Tú: ' + texto;
  tc.className = 'transcripcion ' + (ok ? 'correcta' : 'incorrecta');
  if (ok) {
    $('conv-bocadillo').textContent = 'Gu! 👍';
    estado.xp += 5; guardar(); actualizarHUD();
    setTimeout(() => { idxDialogo++; siguienteTurno(); }, 1200);
  } else {
    $('conv-pista').textContent = 'Pista: intenta decir "' + turno.esperado[0] + '"';
  }
}

$('btn-conversar').addEventListener('click', iniciarConversacion);
$('btn-salir-conv').addEventListener('click', () => { if (rec) rec.abort(); speechSynthesis.cancel(); mostrarVista('lecciones'); renderLecciones(); });
$('btn-mic').addEventListener('click', escuchar);
$('btn-escuchar').addEventListener('click', () => { if (idxDialogo < DIALOGO.length) hablar(DIALOGO[idxDialogo].m); });

// ===== Init =====
actualizarHUD();
renderLecciones();
