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
    --ev=ve|pen|di|sa   evidencial a usar (default: sa = asumido/se sabe)
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
    "es": {"ir": "go", "venir": "ven", "ver": "ve", "decir": "di", "hablar": "pa",
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
           "estoy": ("e", None), "está": ("e", None), "están": ("e", None)},
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


def otro_a_korlin(texto, lex, idioma="es", evidencial="-sa", tiempo=None, glosa=False):
    lengua = idioma if idioma in ("es", "en") else "es"
    func, indice = FUNCIONALES[lengua], INDICE_V[lengua]

    tokens = re.findall(r"[\wÁÉÍÓÚÑáéíóúñ]+|[¿?¡!.,]", texto)
    norm = [normaliza(t) for t in tokens]

    plural = any(n in [normaliza(x) for x in PLURALES[lengua]] for n in norm)
    negacion = any(n in ("no", "not") for n in norm)
    pregunta = "?" in texto or "¿" in texto
    if tiempo is None:
        for n in norm:
            if n in indice and indice[n][1]:
                tiempo = indice[n][1]
                break

    salida, glosas = [], []
    verbo_puesto = False
    for tok, n in zip(tokens, norm):
        if n in ("¿", "?"):
            continue
        if n == "!":
            salida.append("!")
            continue
        if n in (".", ","):
            salida.append(tok)
            continue
        if n in ("no", "not") and negacion:
            continue  # se aplica junto al verbo

        # 1) verbo conjugado
        if n in indice and not verbo_puesto:
            raiz, tp = indice[n]
            t = tiempo if tiempo is not None else tp
            # v0.2: la pregunta exime el evidencial en SU cláusula
            ev_v = "" if (pregunta and "," not in salida) else evidencial
            forma = (t or "") + raiz + ev_v
            if negacion:
                forma = "na " + forma
            salida.append(forma)
            glosas.append(f"{tok}=[{t or ''}{raiz}{ev_v}]")
            verbo_puesto = True
            continue

        # 2) palabra funcional
        if n in func:
            f = func[n]
            # v0.2: la cópula `e` lleva evidencial en la declarativa
            if f == "e" and not pregunta:
                f = "e" + evidencial
            salida.append(f)
            glosas.append(f"{tok}={f}")
            continue

        # 3) derivado ("comida" = cosa de comer -> man-re)
        der = lex.k_a_derivado.get((lengua, n))
        if der:
            salida.append(der)
            glosas.append(f"{tok}=>{der}")
            continue

        # 4) léxico directo (con plural)
        formas, era_plural = lex.con_plural(tok, lengua)
        if formas:
            f = formas[0]
            cat = lex.por_forma[f]["categoria"]
            if (plural or era_plural) and cat == "sustantivo" and not f.endswith("s"):
                f += "s"
            salida.append(f)
            glosas.append(f"{tok}={f}")
            continue
        salida.append(f"[{tok}?]")
        glosas.append(f"{tok}=?")

    if pregunta:
        salida.append("mo")

    out = " ".join(salida)
    out = re.sub(r"\s+", " ", out).strip()
    out = re.sub(r"\s+([.,!?])", r"\1", out)
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
    evidencial, tiempo, glosa = "-sa", None, False
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
