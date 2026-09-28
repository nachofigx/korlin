// Korlin — app de aprendizaje tipo Duolingo
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

// ===== Utilidades =====
function getPalabra(f) { return LEXICO.find(p => p.f === f); }
function sig(p) { return p[LANG] || p.es; }
function barajar(arr) { const a = [...arr]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

const MSG_OK = ['Gu! 👍', 'To! ✅', 'Ra! ⚡', 'Gu-gu! 🎉'];
const MSG_NO = ['Na... 😅', 'Ku... ⚠️', 'Os... 🤔', 'Ba... 🙃'];

// ===== Motor de lección =====
let leccionActual = null;
let ejercicios = [];
let idxEjercicio = 0;
let errores = 0;
let respondiendo = false;

function mostrarVista(v) {
  [vistaLecciones, vistaLeccion, vistaResultado].forEach(x => x.classList.remove('active'));
  if (v === 'lecciones') vistaLecciones.classList.add('active');
  if (v === 'leccion') vistaLeccion.classList.add('active');
  if (v === 'resultado') vistaResultado.classList.add('active');
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
    const nivel = estado.completadas[l.id] || 0;
    const completada = nivel > 0;
    return `
      <div class="leccion-card ${completada ? 'completada' : ''}" onclick="iniciarLeccion('${l.id}')">
        <div class="ico">${l.icono}</div>
        <div class="info">
          <b>${l.nombre}</b>
          <span>${l.palabras.length} palabras · ${completada ? 'completada ✓' : 'nivel ' + (nivel + 1)}</span>
        </div>
        <div class="estado">${completada ? '✅' : '▶️'}</div>
      </div>`;
  }).join('');
}

// ===== Iniciar lección =====
function iniciarLeccion(id) {
  if (estado.vidas <= 0) { alert('Sin vidas ❤️. Vuelve mañana o reinicia tu progreso.'); return; }
  leccionActual = LECCIONES.find(l => l.id === id);
  const palabras = leccionActual.palabras.map(getPalabra).filter(Boolean);
  ejercicios = [];
  for (let i = 0; i < 8; i++) {
    ejercicios.push(crearEjercicio(palabras[i % palabras.length]));
  }
  idxEjercicio = 0;
  errores = 0;
  respondiendo = false;
  $('mascota-img').src = leccionActual.mascota;
  $('mascota-img').alt = leccionActual.nombre;
  mostrarVista('leccion');
  $('bocadillo').textContent = '¡Vamos! 🚀';
  renderEjercicio();
}

function crearEjercicio(objetivo) {
  const tipo = Math.random() < 0.5 ? 'k2s' : 's2k';
  const distractores = barajar(LEXICO.filter(p => p.f !== objetivo.f)).slice(0, 3);
  const opciones = barajar([objetivo, ...distractores]);
  const correcta = opciones.indexOf(objetivo);
  return { tipo, objetivo, opciones, correcta };
}

// ===== Render ejercicio =====
function renderEjercicio() {
  const e = ejercicios[idxEjercicio];
  $('barra-fill').style.width = ((idxEjercicio) / ejercicios.length * 100) + '%';

  const prompt = e.tipo === 'k2s'
    ? `¿Qué significa <span class="korlin">${e.objetivo.f}</span>?`
    : `¿Cómo se dice "${sig(e.objetivo)}" en Korlin?`;

  const opciones = e.opciones.map((p, i) => {
    const texto = e.tipo === 'k2s' ? sig(p) : `<span class="korlin">${p.f}</span>`;
    return `<button class="opcion" onclick="responder(${i})">${texto}</button>`;
  }).join('');

  $('ejercicio').innerHTML = `
    <p class="prompt">${prompt}</p>
    <div class="opciones">${opciones}</div>
  `;
  respondiendo = false;
}

// ===== Responder =====
function responder(i) {
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
    $('bocadillo').textContent = MSG_NO[Math.floor(Math.random() * MSG_NO.length)] + ` Era: ${sig(e.objetivo)}`;
    estado.vidas -= 1;
    errores++;
  }
  guardar();
  actualizarHUD();

  setTimeout(() => {
    if (estado.vidas <= 0) {
      $('bocadillo').textContent = 'Sin vidas... 💔';
      setTimeout(() => { mostrarVista('lecciones'); renderLecciones(); }, 1200);
      return;
    }
    idxEjercicio++;
    if (idxEjercicio >= ejercicios.length) completarLeccion();
    else renderEjercicio();
  }, 900);
}

// ===== Completar lección =====
function completarLeccion() {
  const bonus = errores === 0 ? 15 : 0;
  estado.xp += bonus;
  estado.completadas[leccionActual.id] = (estado.completadas[leccionActual.id] || 0) + 1;
  actualizarRacha();
  guardar();

  $('resultado-icono').textContent = errores === 0 ? '🏆' : '🎉';
  $('resultado-titulo').textContent = errores === 0 ? '¡Perfecto!' : '¡Lección completada!';
  $('resultado-detalle').textContent = `"${leccionActual.nombre}" · ${errores} error${errores === 1 ? '' : 'es'}`;
  $('resultado-xp').textContent = (10 * 8) + bonus;
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
$('btn-salir').addEventListener('click', () => { mostrarVista('lecciones'); renderLecciones(); });
$('btn-continuar').addEventListener('click', () => { mostrarVista('lecciones'); renderLecciones(); });

document.querySelectorAll('.langbtn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.langbtn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    LANG = btn.dataset.lang;
    if (vistaLeccion.classList.contains('active')) renderEjercicio();
  });
});

// ===== Init =====
actualizarHUD();
renderLecciones();
