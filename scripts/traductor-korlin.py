#!/usr/bin/env python3
"""
Traductor por reglas Korlin <-> Español/Inglés.

Determinista: aplica la gramática de Korlin con reglas explícitas, sin
estadística ni adivinación. Es la pieza que hace que un agente de IA produzca
Korlin CORRECTO en lugar de plausible.

Uso:
    python scripts/traductor-korlin.py es "Yo como comida."
    python scripts/traductor-korlin.py es --ev=di "Ella fue a la casa."
    python scripts/traductor-korlin.py en "I want water."
    python scripts/traductor-korlin.py k  "Mi man-ve man-re."
    echo "Yo quiero comer" | python scripts/traductor-korlin.py es --stdin

Opciones:
    --ev=ve|pen|di|sa   evidencial a usar; SIN --ev se marca [?fuente] (nunca -sa)
    --time=an|ne        fuerza pasado/futuro
    --gloss             muestra la glosa morfema a morfema
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_LEX = RAIZ / "korlin.json"


# ================================================================== utilidades

def normaliza(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def blindaje(p):
    """YAML 1.1 convierte no/yes en booleanos: lo revertimos."""
    for campo in ("forma", "es", "en", "categoria", "afi"):
        if not isinstance(p.get(campo), str):
            v = p.get(campo)
            if campo == "forma":
                p[campo] = {True: "ya", False: "no"}.get(v, str(v))
            elif campo in ("es", "en"):
                p[campo] = {True: "yes", False: "no"}.get(v, str(v))
            else:
                p[campo] = str(v if v is not None else "")
    return p


# ================================================================== léxico

SUFIJOS_DERIV = {
    "-pe": ("agente", "the one who"), "-lo": ("lugar", "place of"),
    "-re": ("cosa", "thing of"), "-ro": ("cualidad", "quality of"),
    "-i": ("relativo", "relating to"),
}


class Lexico:
    def __init__(self, ruta=JSON_LEX):
        doc = json.loads(ruta.read_text(encoding="utf-8"))
        self.palabras = [blindaje(dict(p)) for p in doc["lexico"]]
        self.afijos = doc["afijos"]
        self.reglas = doc["reglas"]
        self.por_forma = {p["forma"]: p for p in self.palabras}

        self.es_a_k, self.en_a_k = {}, {}
        for p in self.palabras:
            for t in re.split(r"[,;/]", p.get("es", "")):
                t = normaliza(t.strip())
                if t:
                    self.es_a_k.setdefault(t, []).append(p["forma"])
            for t in re.split(r"[,;/]", p.get("en", "")):
                t = normaliza(t.strip())
                if t:
                    self.en_a_k.setdefault(t, []).append(p["forma"])

        # derivados: raíz + sufijo derivacional -> significado compuesto
        self.derivados = {}
        self.k_a_derivado = {}
        for p in self.palabras:
            if p["categoria"] not in ("verbo", "sustantivo", "adjetivo"):
                continue
            for suf, (es_s, en_s) in SUFIJOS_DERIV.items():
                forma = p["forma"] + suf
                self.derivados[forma] = {
                    "es": f"{p['es'].split(',')[0].strip()} ({es_s})",
                    "en": f"{p['en'].split(',')[0].strip()} ({en_s})",
                    "base": p["forma"], "sufijo": suf,
                }
                self.derivados.setdefault(p["forma"] + suf.lstrip("-"), self.derivados[forma])
                # índice inverso: "comida" (cosa de comer) -> man-re
                for lg, campo in (("es", "es"), ("en", "en")):
                    clave = normaliza(f"{p[campo].split(',')[0].strip()} {es_s if lg == 'es' else en_s}")
                    self.k_a_derivado.setdefault((lg, clave), forma)

    def buscar(self, palabra, idioma="es"):
        return (self.es_a_k if idioma == "es" else self.en_a_k).get(normaliza(palabra), [])

    def con_plural(self, termino, idioma="es"):
        """Prueba el término tal cual y sus variantes de plural/género."""
        t = normaliza(termino)
        claves = self.es_a_k if idioma == "es" else self.en_a_k
        if t in claves:
            return claves[t], False
        if idioma == "es":
            # quita -s/-es y luego -a/-o (concordancia de género del español)
            variantes = [re.sub(r"(es|s)$", "", t), re.sub(r"(es|s)$", "", t)[:-1],
                         t[:-1], re.sub(r"a$", "o", t), re.sub(r"as$", "o", t),
                         re.sub(r"os$", "o", t)]
            for v in variantes:
                if v and v in claves:
                    return claves[v], t != v
        else:
            variantes = [t[:-1], t[:-2], PLURAL_EN.get(t, "")]
            for v in variantes:
                if v and v in claves:
                    return claves[v], True
        return [], False


# ================================================================== morfología K

EVS = ["-ve", "-pen", "-di", "-sa"]
EV_SIG = {
    "es": {"-ve": "lo vi", "-pen": "lo deduzco", "-di": "me lo contaron", "-sa": "es sabido"},
    "en": {"-ve": "I saw it", "-pen": "I infer it", "-di": "I was told", "-sa": "it is known"},
}
DERIV_K = ["-pe", "-lo", "-re", "-ro", "-i", "-s"]
PREFIJOS_K = ["an-", "ne-", "na-", "me-", "pi-"]
SIGNIFICADO = {
    "es": {"an-": "pasado", "ne-": "futuro", "na-": "no-", "me-": "grande/muy",
           "pi-": "pequeño", "-pe": "agente", "-lo": "lugar", "-re": "cosa",
           "-ro": "cualidad", "-i": "relativo", "-s": "plural"},
    "en": {"an-": "past", "ne-": "future", "na-": "not-", "me-": "big/very",
           "pi-": "little", "-pe": "agent", "-lo": "place", "-re": "thing",
           "-ro": "quality", "-i": "relating", "-s": "plural"},
}

# palabras cuya forma en korlin ya es "negada" (na- + raíz) pero el idioma
# destino tiene una palabra propia
NEGADOS = {
    "es": {"na-toro": "mentira", "na-gu": "malo", "na-me": "pequeño"},
    "en": {"na-toro": "lie", "na-gu": "bad", "na-me": "small"},
}
PRONOMBRES_OBJ = {"es": {"mi": "mí", "tu": "ti", "li": "él"}, "en": {}}
# F2: 'conmigo/contigo' se derivan con kon + pronombre (regla 17), no son raices
CON_PRONOMBRE = {"es": {"conmigo": "kon mi", "contigo": "kon tu", "connosco": "kon wi",
                        "con nosotros": "kon wi", "con él": "kon li", "con ella": "kon li"},
                 "en": {"with me": "kon mi", "with you": "kon tu", "with us": "kon wi"}}


def analiza(palabra, lex=None):
    """Descompone korlin en (prefijo, raíz, [sufijos]).

    En la ortografía de Korlin el guion marca frontera de morfema:
        an-go-ve   = [an-] + go + [-ve]
        man-re     = man + [-re]
        na-toro    = [na-] + toro
        e-sa       = e + [-sa]
    """
    p = palabra.lower()
    TODOS_SUF = DERIV_K + EVS
    PREF_SIN = {x.rstrip("-") for x in PREFIJOS_K}

    if "-" in p:
        segs = p.split("-")
        pref = None
        if len(segs) > 1 and segs[0] in PREF_SIN:
            pref = segs.pop(0) + "-"
        sufs = []
        while len(segs) > 1 and ("-" + segs[-1]) in TODOS_SUF:
            sufs.insert(0, "-" + segs.pop())
        return pref, "-".join(segs), sufs

    # sin guiones: corte heurístico validado contra el léxico
    pref = None
    for pre in sorted(PREFIJOS_K, key=len, reverse=True):
        if p.startswith(pre) and len(p) > len(pre):
            pref, p = pre, p[len(pre):]
            break
    sufs = []
    cambio = True
    while cambio:
        cambio = False
        for suf in sorted(TODOS_SUF, key=len, reverse=True):
            s = suf.lstrip("-")
            if p.endswith(s) and len(p) > len(s):
                raiz_cand = p[: -len(s)]
                if lex is None or raiz_cand in lex.por_forma or raiz_cand in lex.derivados:
                    sufs.insert(0, suf)
                    p = raiz_cand
                    cambio = True
                    break
    return pref, p, sufs


# ================================================================== K -> ES/EN

def korlin_a_otro(texto, lex, idioma="es", glosa=False):
    lineas, glosas = [], []
    for crudo in re.findall(r"[\wÁÉÍÓÚÑáéíóúñ'\-]+|[¡!¿?.,]", texto):
        tok = crudo.lower()
        if tok in ("¡", "!", "¿", "?", ".", ","):
            if tok in ("¿", "?"):
                lineas.append("?")
            else:
                lineas.append(crudo)
            continue
        if tok == "mo":
            lineas.append("?")
            glosas.append("mo=pregunta")
            continue

        pre, raiz, sufs = analiza(tok, lex)

        # palabra negada con forma propia en el idioma destino
        if pre == "na-" and tok in NEGADOS[idioma]:
            lineas.append(NEGADOS[idioma][tok])
            glosas.append(f"{tok}=na-+{raiz}")
            continue

        clave_der = raiz + "".join(sufs)

        # forma completa en el léxico (p.ej. "ru-sui")
        if tok in lex.por_forma:
            lineas.append(lex.por_forma[tok][idioma].split(",")[0].strip())
            glosas.append(f"{tok}")
            continue
        # derivado conocido (man-re, sa-pe, gu-ro, man-lo...)
        if clave_der in lex.derivados:
            lineas.append(lex.derivados[clave_der][idioma])
            glosas.append(f"{tok}=>{clave_der}")
            continue
        base = lex.por_forma.get(raiz)
        if base is None:
            lineas.append(f"[{crudo}?]")
            glosas.append(f"{tok}=?")
            continue

        partes = [base[idioma].split(",")[0].strip()]
        for s in sufs:
            if s == "-s":
                partes[0] += "s"
            elif s in EV_SIG[idioma]:
                partes.append(f"({EV_SIG[idioma][s]})")
            elif s in SIGNIFICADO[idioma]:
                partes.append(f"({SIGNIFICADO[idioma][s]})")
        if pre:
            if pre == "na-" and pre not in ("an-",):
                partes[0] = "no-" + partes[0] if idioma == "es" else "not-" + partes[0]
            elif pre == "me-":
                partes[0] = "gran " + partes[0] if idioma == "es" else "great " + partes[0]
            elif pre == "pi-":
                partes[0] = "pequeñ" + ("a " if idioma == "es" else "little ") + partes[0]
            else:
                partes.insert(0, f"({SIGNIFICADO[idioma][pre]})")
        lineas.append(" ".join(partes))
        glosas.append(f"{tok}={'+'.join(filter(None, [pre, raiz] + sufs))}")

    out = " ".join(lineas)
    out = re.sub(r"\s+([.,!?])", r"\1", out)
    if glosa:
        return out + "\nGlosa: " + "  ".join(glosas)
    return out


# ================================================================== ES/EN -> K

FUNCIONALES = {
    "es": {"yo": "mi", "me": "mi", "mí": "mi", "mi": "mi", "tú": "tu", "tu": "tu", "usted": "tu",
           "él": "li", "ella": "li", "nosotros": "wi", "nosotras": "wi",
           "ustedes": "yu", "ellos": "lis", "ellas": "lis",
           "el": "le", "la": "le", "los": "le", "las": "le",
           "un": "u", "una": "u", "uno": "u",
           "y": "ka", "e": "ka", "o": "o", "u": "o", "pero": "ba",
           "que": "ki", "si": "si", "entonces": "so", "no": "na", "sí": "ya",
           "de": "de", "del": "de", "con": "kon", "para": "po", "por": "po",
           "en": "i", "a": "a", "hacia": "a", "es": "e", "son": "e", "está": "e",
           "estoy": "e", "están": "e", "hola": "halo", "este": "se", "esta": "se",
           "ese": "te", "esa": "te", "eso": "te"},
    "en": {"i": "mi", "me": "mi", "my": "mi", "you": "tu", "your": "tu", "he": "li",
           "she": "li", "we": "wi", "our": "wi", "they": "lis",
           "the": "le", "a": "u", "an": "u", "one": "u",
           "and": "ka", "or": "o", "but": "ba", "that": "ki", "if": "si", "then": "so",
           "not": "na", "yes": "ya", "of": "de", "with": "kon", "for": "po", "by": "po",
           "in": "i", "to": "a", "is": "e", "are": "e", "am": "e", "be": "e",
           "hello": "halo", "hi": "halo", "this": "se"},
}

# infinitivo -> raíz korlin
VERBOS = {
    "es": {"ir": "go", "venir": "ven", "ver": "ve", "mirar": "ve", "decir": "di", "hablar": "pa",
           "hacer": "fa", "tener": "ha", "querer": "vo", "poder": "kan", "deber": "mus",
           "saber": "sa", "dar": "da", "tomar": "ta", "pensar": "pen", "sentir": "sen",
           "comer": "man", "beber": "bi", "dormir": "do", "vivir": "vi", "morir": "mu",
           "construir": "ban", "proteger": "gan", "poner": "pon", "calcular": "num",
           "simular": "sim", "comprar": "ken", "aprender": "sa", "estudiar": "sa",
           "ser": "e", "estar": "e"},
    "en": {"go": "go", "come": "ven", "see": "ve", "say": "di", "speak": "pa",
           "do": "fa", "make": "fa", "have": "ha", "want": "vo", "can": "kan", "must": "mus",
           "know": "sa", "give": "da", "take": "ta", "think": "pen", "feel": "sen",
           "eat": "man", "drink": "bi", "sleep": "do", "live": "vi", "die": "mu",
           "build": "ban", "protect": "gan", "put": "pon", "calculate": "num",
           "simulate": "sim", "buy": "ken", "learn": "sa", "study": "sa",
           "be": "e"},
}

IRREGULARES = {
    "es": {"voy": ("go", None), "vas": ("go", None), "va": ("go", None), "vamos": ("go", None),
           "van": ("go", None), "fui": ("go", "an-"), "fue": ("go", "an-"), "fuiste": ("go", "an-"),
           "iré": ("go", "ne-"), "irá": ("go", "ne-"),
           "tengo": ("ha", None), "tiene": ("ha", None), "tienen": ("ha", None), "tenemos": ("ha", None),
           "tuve": ("ha", "an-"), "hago": ("fa", None), "hace": ("fa", None), "hizo": ("fa", "an-"),
           "hice": ("fa", "an-"), "sé": ("sa", None), "digo": ("di", None), "dice": ("di", None),
           "dije": ("di", "an-"), "vengo": ("ven", None), "viene": ("ven", None), "vine": ("ven", "an-"),
           "quiero": ("vo", None), "quiere": ("vo", None), "quieres": ("vo", None),
           "puedo": ("kan", None), "puede": ("kan", None), "puedes": ("kan", None),
           "veo": ("ve", None), "ves": ("ve", None), "vio": ("ve", "an-"), "vi": ("ve", "an-"),
           "soy": ("e", None), "eres": ("e", None), "somos": ("e", None), "era": ("e", "an-"),
           "doy": ("da", None), "da": ("da", None), "di": ("da", "an-"),
           "estoy": ("e", None), "está": ("e", None), "están": ("e", None),
           "duermo": ("do", None), "duermes": ("do", None), "duerme": ("do", None), "duermen": ("do", None),
           "pienso": ("pen", None), "piensas": ("pen", None), "piensa": ("pen", None), "piensan": ("pen", None),
           "sé": ("sa", None), "sabes": ("sa", None), "sabe": ("sa", None), "saben": ("sa", None),
           "miro": ("ve", None), "miras": ("ve", None), "mira": ("ve", None), "miran": ("ve", None),
           "como": ("man", None), "comes": ("man", None), "come": ("man", None), "comen": ("man", None),
           "bebo": ("bi", None), "bebes": ("bi", None), "bebe": ("bi", None), "beben": ("bi", None),
           "ven": ("ven", None)},
    "en": {"went": ("go", "an-"), "gone": ("go", "an-"), "ate": ("man", "an-"), "eaten": ("man", "an-"),
           "saw": ("ve", "an-"), "seen": ("ve", "an-"), "said": ("di", "an-"), "made": ("fa", "an-"),
           "did": ("fa", "an-"), "had": ("ha", "an-"), "was": ("e", "an-"), "were": ("e", "an-"),
           "took": ("ta", "an-"), "gave": ("da", "an-"), "came": ("ven", "an-"), "felt": ("sen", "an-"),
           "drank": ("bi", "an-"), "knew": ("sa", "an-"),
           "goes": ("go", None), "eats": ("man", None), "wants": ("vo", None), "sees": ("ve", None),
           "has": ("ha", None), "does": ("fa", None), "knows": ("sa", None), "thinks": ("pen", None),
           "feels": ("sen", None), "drinks": ("bi", None), "lives": ("vi", None), "gives": ("da", None),
           "takes": ("ta", None), "comes": ("ven", None), "makes": ("fa", None), "says": ("di", None),
           "speaks": ("pa", None)},
}

# terminaciones regulares por clase verbal (-ar / -er / -ir)
TERM_ES = {
    "ar": {
        None: ["o", "as", "a", "amos", "áis", "an"],
        "an-": ["é", "aste", "ó", "amos", "asteis", "aron"],
    },
    "er": {
        None: ["o", "es", "e", "emos", "éis", "en"],
        "an-": ["í", "iste", "ió", "imos", "isteis", "ieron"],
    },
    "ir": {
        None: ["o", "es", "e", "imos", "ís", "en"],
        "an-": ["í", "iste", "ió", "imos", "isteis", "ieron"],
    },
}
TERM_EN = {None: ["", "s", "es"], "an-": ["ed"]}

NUMERALES = {"es": {"cero": "nul", "un": "u", "una": "u", "uno": "u", "dos": "du", "tres": "san",
                      "cuatro": "fu", "cinco": "sin", "seis": "sis", "siete": "sem", "ocho": "om",
                      "nueve": "nu", "diez": "des", "cien": "sento", "ciento": "sento", "mil": "kilo"},
             "en": {"zero": "nul", "one": "u", "two": "du", "three": "san", "four": "fu",
                    "five": "sin", "six": "sis", "seven": "sem", "eight": "om", "nine": "nu",
                    "ten": "des", "hundred": "sento", "thousand": "kilo"}}
PLURALES = {"es": ["los", "las", "unos", "unas", "varios", "varias", "algunos", "algunas",
                   "muchos", "muchas", "ambos", "ambas", "dos", "tres", "cuatro", "cinco"],
            "en": ["many", "some", "several", "all", "both", "few", "two", "three", "four", "five"]}

# plurales irregulares del inglés -> singular
PLURAL_EN = {"people": "person", "children": "child", "men": "man", "women": "woman",
             "teeth": "tooth", "feet": "foot", "mice": "mouse", "lives": "life"}


def construye_indice(lengua):
    """Todas las formas conjugadas -> (raíz_korlin, tiempo_de_la_forma)."""
    idx = dict(IRREGULARES[lengua])
    for inf, raiz in VERBOS.get(lengua, {}).items():
        idx.setdefault(inf, (raiz, None))
        if inf in ("ser", "estar"):  # irregulares: no generar 'se', 'so', 'esta'...
            continue
        if lengua == "es":
            stem, terminacion = inf, None
            for s in ("ar", "er", "ir"):
                if inf.endswith(s):
                    stem, terminacion = inf[: -len(s)], s
                    break
            if terminacion and stem:  # stem vacío (p.ej. 'ir') produce colisiones
                for tiempo, terms in TERM_ES[terminacion].items():
                    for t in terms:
                        idx.setdefault(stem + t, (raiz, tiempo))
                for t in ("é", "ás", "á", "emos", "éis", "án"):
                    idx.setdefault(inf + t, (raiz, "ne-"))
        else:
            for t in ("", "s", "es"):
                idx.setdefault(inf + t, (raiz, None))
            for t in ("ed", "ing"):
                idx.setdefault(inf + t, (raiz, "an-"))
    return idx


INDICE_V = {lg: construye_indice(lg) for lg in ("es", "en")}


def otro_a_korlin(texto, lex, idioma="es", evidencial="?", tiempo=None, glosa=False):
    lengua = idioma if idioma in ("es", "en") else "es"
    func, indice = FUNCIONALES[lengua], INDICE_V[lengua]

    tokens = re.findall(r"[\wÁÉÍÓÚÑáéíóúñ]+|[¿?¡!.,]", texto)
    norm = [normaliza(t) for t in tokens]

    plural = any(n in [normaliza(x) for x in PLURALES[lengua]] for n in norm)
    negacion = any(n in ("no", "not") for n in norm)
    pregunta = "?" in texto or "¿" in texto
    orden = "!" in texto and not re.match(r"^\s*(yo|tú|tu|él|ella|nosotros|ustedes|ellos)\b", texto, re.I)
    # C-26/C-19: cada clausula finita lleva SU tiempo, SU evidencial y UN verbo finito.
    # Fronteras de clausula: la coma, el complementante `ki` y el conector `so`.
    clausula = []
    cid = 0
    for nm in norm:
        if nm in (",", "ki", "so", "que", "and", "then"):   # fronteras de clausula
            cid += 1
        clausula.append(cid)

    salida, glosas = [], []
    verbo_puesto = set()          # por clausula, no global
    for i_tok, (tok, n) in enumerate(zip(tokens, norm)):
        k = tok.lower()  # los indices de verbos/funcionales llevan tildes
        if n in ("¿", "?", "¡"):
            continue
        if n == "!":
            salida.append("!")
            continue
        if n in (".", ","):
            salida.append(tok)
            continue
        if n in ("no", "not") and negacion:
            continue  # se aplica junto al verbo

        # 1) verbo conjugado (uno por clausula)
        ci = clausula[i_tok] if i_tok < len(clausula) else cid
        if k in indice and ci not in verbo_puesto:
            raiz, tp = indice[k]
            t = tiempo if tiempo is not None else tp   # el tiempo es el del PROPIO verbo
            # regla 14: la subordinada finita lleva su evidencial; la raiz tambien.
            # Exencion (a)/(b): pregunta u orden eximen SU clausula.
            ev_v = evidencial
            if ev_v == "?":
                ev_v = "-[?fuente]"
            if pregunta and ci == cid:        # el `mo` final afecta a la ultima clausula
                ev_v = ""
            if orden and ci == 0:
                ev_v = ""
            # regla 15: la PROTASIS ('si ... ,') va desnuda
            if "si" in norm[:i_tok] and "," not in norm[:i_tok]:
                ev_v = ""
            forma = (t or "") + raiz + ev_v
            if negacion:
                forma = "na " + forma
            salida.append(forma)
            glosas.append(f"{tok}=[{t or ''}{raiz}{ev_v}]")
            verbo_puesto.add(ci)
            continue

        # 2) palabra funcional
        if k in func:
            f = func[k]
            # v0.2: la cópula `e` lleva evidencial en la declarativa
            if f == "e" and not pregunta:
                f = "e" + ("-[?fuente]" if evidencial == "?" else evidencial)
            if f.split("-")[0] == "e" and negacion and not verbo_puesto:
                f = "na " + f          # negar tambien la copula (regla 7a)
                verbo_puesto = True
            salida.append(f)
            glosas.append(f"{tok}={f}")
            continue

        # 3) derivado ("comida" = cosa de comer -> man-re)
        der = lex.k_a_derivado.get((lengua, n))
        if der:
            salida.append(der)
            glosas.append(f"{tok}=>{der}")
            continue

        # 2b) numerales (C-06/C-17)
        num = NUMERALES.get(lengua, {})
        if n in num:
            salida.append(num[n])
            glosas.append(f"{tok}={num[n]}")
            continue

        # 3b) F2: 'conmigo/contigo' se derivan (kon + pronombre, regla 17)
        cp = CON_PRONOMBRE.get(lengua, {})
        if n in cp:
            for w in cp[n].split():
                salida.append(w)
            glosas.append(f"{tok}=>{cp[n]}")
            continue

        # 4) léxico directo (con plural)
        formas, era_plural = lex.con_plural(tok, lengua)
        if formas:
            f = formas[0]
            cat = lex.por_forma[f]["categoria"]
            if (plural or era_plural) and cat == "sustantivo" and not f.endswith("s"):
                f += "es" if f[-1] in "mns" else "s"   # C-03
            salida.append(f)
            glosas.append(f"{tok}={f}")
            continue
        salida.append(f"[{tok}?]")
        glosas.append(f"{tok}=?")

    if pregunta:
        salida.append("mo")

    # PR-13 / regla 3: el modificador (adjetivo) va ANTES del sustantivo.
    # En ES/EN el adjetivo suele ir despues ("casa grande") -> invertir el par.
    def _cat(f):
        f = f.lstrip("-").split("-")[0]
        e = lex.por_forma.get(f)
        if e is None and f.endswith("s"):   # plural pegado (regla 18)
            e = lex.por_forma.get(f[:-1])
        return e.get("categoria") if e else None
    i = 0
    while i < len(salida) - 1:
        a, b = salida[i], salida[i + 1]
        if _cat(a) == "sustantivo" and _cat(b) == "adjetivo":
            salida[i], salida[i + 1] = b, a
            i += 2
        else:
            i += 1

    out = " ".join(salida)
    out = re.sub(r"\s+", " ", out).strip()
    out = re.sub(r"\s+([.,!?])", r"\1", out)
    # PR-15b: conservar el signo de interrogacion al final
    if pregunta and not out.endswith("?"):
        out = out.rstrip(".!") + "?"
    if glosa:
        return out + "\nGlosa: " + "  ".join(glosas)
    return out


# ================================================================== CLI

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    modo = args[0]
    lex = Lexico()
    evidencial, tiempo, glosa = "?", None, False   # C-01: sin --ev no se asume -sa
    resto = []
    for a in args[1:]:
        if a.startswith("--ev="):
            evidencial = "-" + a.split("=", 1)[1].lstrip("-")
        elif a.startswith("--time="):
            v = a.split("=", 1)[1]
            tiempo = {"an": "an-", "ne": "ne-", "pasado": "an-", "futuro": "ne-", "past": "an-", "future": "ne-"}.get(v)
        elif a == "--gloss":
            glosa = True
        elif a == "--stdin":
            resto.append(sys.stdin.read())
        else:
            resto.append(a)
    texto = " ".join(resto).strip()

    if modo == "es":
        print(otro_a_korlin(texto, lex, "es", evidencial, tiempo, glosa))
    elif modo == "en":
        print(otro_a_korlin(texto, lex, "en", evidencial, tiempo, glosa))
    elif modo in ("k", "korlin"):
        print("ES:", korlin_a_otro(texto, lex, "es", glosa))
        print("EN:", korlin_a_otro(texto, lex, "en", glosa))
    elif modo == "json":
        print(json.dumps({"lexico": len(lex.palabras), "afijos": len(lex.afijos),
                          "derivados": len(lex.derivados)}, ensure_ascii=False))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
