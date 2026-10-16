// Korlin (Shortlang) — interactive app with language selector
// Uses window.KORLIN_LEXICO (generated from data/lexico.yaml + data/traducciones.yaml)

const LEXICO = window.KORLIN_LEXICO || [];
let LANG = 'en';

// ===== i18n: interface strings =====
const I18N = {
  en: {
    tagline: "A short, honest, modern constructed language",
    tab_inicio: "🏠 Home", tab_why: "🚀 Why Korlin", tab_compare: "📊 Compare",
    tab_diccionario: "📖 Dictionary", tab_flashcards: "🎴 Flashcards", tab_traductor: "🔄 Translator", tab_aprender: "🎓 Learn",
    tab_ia: "🤖 For AI",
    ia_titulo: "For AI agents 🤖",
    ia_desc: "Any LLM can speak Korlin today — no training needed. Give it the spec and it will translate correctly.",
    ia_card1: "Self-contained spec pack (~16 KB). Paste it into any system prompt.",
    ia_card2: "Machine-readable lexicon, affixes and rules for tool calls.",
    ia_card3: "Deterministic rule-based translator. The code produces Korlin, not the model.",
    ia_pasos_t: "Three steps",
    ia_paso1: "Copy korlin-spec.md into your AI's system prompt.",
    ia_paso2: "Ask it to translate or chat in Korlin.",
    ia_paso3: "Check the three rules: SVO order, mandatory evidential, valid phonemes.",
    ia_nota: "Tip: give the model the translator as a tool and it will never invent a root word.",
    ia_ver: "View / download",
    hero_titulo: "Speak less, say more.",
    hero_sub: "Korlin is a constructed language that condenses meaning into tiny, honest, modern words.",
    stat_letras: "letters, 1 letter = 1 sound", stat_palabras: "core words", stat_idiomas: "documentation languages", stat_corto: "shorter than Esperanto",
    card_corta_t: "✂️ Short", card_corta_d: "Words of 1–2 syllables condense concepts. ~40% shorter than Esperanto.",
    card_honesta_t: "🛡️ Honest", card_honesta_d: "Mandatory evidentiality: every statement declares its source. Lying is costly and detectable.",
    card_moderna_t: "📱 Modern", card_moderna_d: "20 letters, no diacritics, emoji particles, and AI-ready.",
    ejemplo_titulo: "Example",
    ejemplo_gloss: '"The lie cannot live in me." · <code>na-toro</code> = lie (<code>na-</code> not + <code>toro</code> truth)',
    why_titulo: "Why Korlin? 🚀", why_desc: "Built for a connected, digital, honest world.",
    why_youth_t: "🧑‍🎤 Made for youth", why_youth_d: "Informal, playful, emoji-native. Attitude particles express feelings with two letters that map to emojis.",
    why_ia_t: "🤖 AI-ready", why_ia_d: "Fewer tokens, deterministic parsing, mandatory evidentiality. Machines understand it efficiently.",
    why_adopt_t: "🌍 Mass adoption", why_adopt_d: "Total regularity, no exceptions, easy for Asian and African speakers. Learnable in days, not years.",
    why_modern_t: "⚡ Super modern", why_modern_d: "Digital-native: no diacritics, emoji-compatible, designed for chat, phones and AI agents.",
    emoji_titulo: "Attitude particles → emoji", emoji_desc: "Two letters trigger the matching emoji on your phone keyboard.",
    emo_yo: "joy", emo_we: "surprise", emo_fi: "irony", emo_ri: "laugh", emo_hu: "sadness", emo_bu: "anger", emo_la: "love", emo_pu: "disgust", emo_ni: "fear",
    compare_titulo: "Comparisons 📊", compare_desc: "Korlin against its rivals and natural languages.",
    vs_esp_titulo: "Korlin vs Esperanto", vs_dut_titulo: "Korlin vs Dutton Speedwords",
    th_feat: "Feature", f_diacrit: "Diacritics", f_acc: "Accusative case (-n)", f_evid: "Evidentiality (anti-lie)", f_emoji: "Emoji particles", f_ia: "AI-ready", f_len: "Length (same text)", f_pron: "Pronounceable", f_reg: "Fully regular", f_tech: "Technical vocabulary",
    len_titulo: "Length: one sentence in several languages", len_desc: '"The lie cannot live in me" — characters per language.',
    len_nota: "On a longer text, Korlin saves ~44% characters vs Spanish, ~36% vs English, ~31% vs Japanese.",
    diccionario_titulo: "Dictionary 📖", busqueda_ph: "Search in Korlin, Spanish or English…",
    flashcards_titulo: "Flashcards 🎴", flashcards_desc: "Guess the meaning. Click the card to reveal.",
    flash_no: "🙈 Didn't know it", flash_si: "✅ Knew it",
    traductor_titulo: "Translator (word by word) 🔄", traductor_desc: "Translates Korlin → selected language, word by word (demo).",
    traductor_ph: "Type in Korlin… e.g. mi go a le ho", btn_traducir: "Translate →"
  },
  es: {
    tagline: "Una lengua corta, honesta y moderna",
    tab_inicio: "🏠 Inicio", tab_why: "🚀 Por qué", tab_compare: "📊 Compara",
    tab_diccionario: "📖 Diccionario", tab_flashcards: "🎴 Flashcards", tab_traductor: "🔄 Traductor", tab_aprender: "🎓 Aprender",
    tab_ia: "🤖 Para IA",
    ia_titulo: "Para agentes de IA 🤖",
    ia_desc: "Cualquier LLM puede hablar Korlin hoy mismo, sin entrenamiento. Dale la especificación y traducirá correctamente.",
    ia_card1: "Paquete de especificación autocontenido (~16 KB). Pégalo en cualquier system prompt.",
    ia_card2: "Léxico, afijos y reglas legibles por máquina para llamadas de herramienta.",
    ia_card3: "Traductor determinista por reglas. El código produce el Korlin, no el modelo.",
    ia_pasos_t: "Tres pasos",
    ia_paso1: "Copia korlin-spec.md en el system prompt de tu IA.",
    ia_paso2: "Pídele que traduzca o converse en Korlin.",
    ia_paso3: "Verifica las tres reglas: orden SVO, evidencial obligatorio, fonemas válidos.",
    ia_nota: "Consejo: dale al modelo el traductor como herramienta y nunca inventará una raíz.",
    ia_ver: "Ver / descargar",
    hero_titulo: "Habla menos, di más.",
    hero_sub: "Korlin es una lengua construida que condensa el significado en palabras diminutas, honestas y modernas.",
    stat_letras: "letras, 1 letra = 1 sonido", stat_palabras: "palabras núcleo", stat_idiomas: "idiomas de documentación", stat_corto: "más corto que el Esperanto",
    card_corta_t: "✂️ Corta", card_corta_d: "Palabras de 1–2 sílabas condensan conceptos. ~40% más corta que el Esperanto.",
    card_honesta_t: "🛡️ Honesta", card_honesta_d: "Evidencialidad obligatoria: toda afirmación declara su fuente. Mentir es costoso y detectable.",
    card_moderna_t: "📱 Moderna", card_moderna_d: "20 letras, sin tildes, partículas emoji y lista para IA.",
    ejemplo_titulo: "Ejemplo",
    ejemplo_gloss: '"La mentira no puede vivir en mí." · <code>na-toro</code> = mentira (<code>na-</code> no + <code>toro</code> verdad)',
    why_titulo: "¿Por qué Korlin? 🚀", why_desc: "Hecho para un mundo conectado, digital y honesto.",
    why_youth_t: "🧑‍🎤 Hecho para jóvenes", why_youth_d: "Informal, lúdico y nativo emoji. Las partículas de actitud expresan emociones con dos letras que mapean a emojis.",
    why_ia_t: "🤖 Listo para IA", why_ia_d: "Menos tokens, análisis determinista y evidencialidad obligatoria. Las máquinas lo entienden de forma eficiente.",
    why_adopt_t: "🌍 Adopción masiva", why_adopt_d: "Regularidad total, sin excepciones, fácil para hablantes asiáticos y africanos. Se aprende en días, no años.",
    why_modern_t: "⚡ Super moderno", why_modern_d: "Nativo digital: sin tildes, compatible con emoji, diseñado para chat, móviles y agentes de IA.",
    emoji_titulo: "Partículas de actitud → emoji", emoji_desc: "Dos letras activan el emoji correspondiente en el teclado del móvil.",
    emo_yo: "alegría", emo_we: "sorpresa", emo_fi: "ironía", emo_ri: "risa", emo_hu: "tristeza", emo_bu: "enfado", emo_la: "cariño", emo_pu: "asco", emo_ni: "miedo",
    compare_titulo: "Comparativas 📊", compare_desc: "Korlin frente a sus rivales y las lenguas naturales.",
    vs_esp_titulo: "Korlin vs Esperanto", vs_dut_titulo: "Korlin vs Dutton Speedwords",
    th_feat: "Característica", f_diacrit: "Tildes/diacríticos", f_acc: "Caso acusativo (-n)", f_evid: "Evidencialidad (anti-mentira)", f_emoji: "Partículas emoji", f_ia: "Listo para IA", f_len: "Longitud (mismo texto)", f_pron: "Pronunciable", f_reg: "Totalmente regular", f_tech: "Vocabulario técnico",
    len_titulo: "Longitud: una frase en varios idiomas", len_desc: '"La mentira no puede vivir en mí" — caracteres por idioma.',
    len_nota: "En un texto más largo, Korlin ahorra ~44% de caracteres vs español, ~36% vs inglés, ~31% vs japonés.",
    diccionario_titulo: "Diccionario 📖", busqueda_ph: "Busca en Korlin, español o inglés…",
    flashcards_titulo: "Flashcards 🎴", flashcards_desc: "Adivina el significado. Haz clic para revelar.",
    flash_no: "🙈 No la sabía", flash_si: "✅ La sabía",
    traductor_titulo: "Traductor (palabra por palabra) 🔄", traductor_desc: "Traduce Korlin → idioma seleccionado, palabra por palabra (demo).",
    traductor_ph: "Escribe en Korlin… ej. mi go a le ho", btn_traducir: "Traducir →"
  },
  fr: {
    tagline: "Une langue construite courte, honnête et moderne",
    tab_inicio: "🏠 Accueil", tab_why: "🚀 Pourquoi", tab_compare: "📊 Comparer",
    tab_diccionario: "📖 Dictionnaire", tab_flashcards: "🎴 Flashcards", tab_traductor: "🔄 Traducteur", tab_aprender: "🎓 Apprendre",
    tab_ia: "🤖 Pour l'IA",
    ia_titulo: "Pour les agents d'IA 🤖",
    ia_desc: "Tout LLM peut parler korlin dès aujourd'hui, sans entraînement. Donnez-lui la spécification et il traduira correctement.",
    ia_card1: "Pack de spécification autonome (~16 Ko). Collez-le dans n'importe quel prompt système.",
    ia_card2: "Lexique, affixes et règles lisibles par machine pour les appels d'outils.",
    ia_card3: "Traducteur déterministe à base de règles. Le code produit le korlin, pas le modèle.",
    ia_pasos_t: "Trois étapes",
    ia_paso1: "Copiez korlin-spec.md dans le prompt système de votre IA.",
    ia_paso2: "Demandez-lui de traduire ou de discuter en korlin.",
    ia_paso3: "Vérifiez les trois règles : ordre SVO, évidentiel obligatoire, phonèmes valides.",
    ia_nota: "Astuce : donnez le traducteur comme outil au modèle et il n'inventera jamais de racine.",
    ia_ver: "Voir / télécharger",
    hero_titulo: "Parlez moins, dites plus.",
    hero_sub: "Korlin est une langue construite qui condense le sens en petits mots honnêtes et modernes.",
    stat_letras: "lettres, 1 lettre = 1 son", stat_palabras: "mots de base", stat_idiomas: "langues de documentation", stat_corto: "plus court que l'espéranto",
    card_corta_t: "✂️ Courte", card_corta_d: "Des mots de 1–2 syllabes condensent les concepts. ~40 % plus courte que l'espéranto.",
    card_honesta_t: "🛡️ Honnête", card_honesta_d: "Évidentialité obligatoire : chaque affirmation déclare sa source. Mentir est coûteux et détectable.",
    card_moderna_t: "📱 Moderne", card_moderna_d: "20 lettres, sans diacritiques, particules emoji, et prête pour l'IA.",
    ejemplo_titulo: "Exemple",
    ejemplo_gloss: '« Le mensonge ne peut pas vivre en moi. » · <code>na-toro</code> = mensonge (<code>na-</code> non + <code>toro</code> vérité)',
    why_titulo: "Pourquoi Korlin ? 🚀", why_desc: "Conçu pour un monde connecté, numérique et honnête.",
    why_youth_t: "🧑‍🎤 Fait pour les jeunes", why_youth_d: "Informel, ludique, natif emoji. Les particules d'attitude expriment des émotions avec deux lettres liées à des emojis.",
    why_ia_t: "🤖 Prêt pour l'IA", why_ia_d: "Moins de jetons, analyse déterministe, évidentialité obligatoire. Les machines le comprennent efficacement.",
    why_adopt_t: "🌍 Adoption massive", why_adopt_d: "Régularité totale, sans exceptions, facile pour les Asiatiques et Africains. S'apprend en jours, pas en années.",
    why_modern_t: "⚡ Super moderne", why_modern_d: "Natif numérique : sans diacritiques, compatible emoji, conçu pour le chat, les téléphones et les agents IA.",
    emoji_titulo: "Particules d'attitude → emoji", emoji_desc: "Deux lettres déclenchent l'emoji correspondant sur le clavier.",
    emo_yo: "joie", emo_we: "surprise", emo_fi: "ironie", emo_ri: "rire", emo_hu: "tristesse", emo_bu: "colère", emo_la: "amour", emo_pu: "dégoût", emo_ni: "peur",
    compare_titulo: "Comparaisons 📊", compare_desc: "Korlin face à ses rivaux et aux langues naturelles.",
    vs_esp_titulo: "Korlin vs espéranto", vs_dut_titulo: "Korlin vs Dutton Speedwords",
    th_feat: "Caractéristique", f_diacrit: "Diacritiques", f_acc: "Accusatif (-n)", f_evid: "Évidentialité (anti-mensonge)", f_emoji: "Particules emoji", f_ia: "Prêt pour l'IA", f_len: "Longueur (même texte)", f_pron: "Prononçable", f_reg: "Entièrement régulier", f_tech: "Vocabulaire technique",
    len_titulo: "Longueur : une phrase en plusieurs langues", len_desc: '« Le mensonge ne peut pas vivre en moi » — caractères par langue.',
    len_nota: "Sur un texte plus long, Korlin économise ~44 % de caractères vs espagnol, ~36 % vs anglais, ~31 % vs japonais.",
    diccionario_titulo: "Dictionnaire 📖", busqueda_ph: "Cherchez en korlin, espagnol ou anglais…",
    flashcards_titulo: "Flashcards 🎴", flashcards_desc: "Devinez le sens. Cliquez sur la carte pour révéler.",
    flash_no: "🙈 Je ne savais pas", flash_si: "✅ Je savais",
    traductor_titulo: "Traducteur (mot à mot) 🔄", traductor_desc: "Traduit korlin → langue choisie, mot à mot (démo).",
    traductor_ph: "Écrivez en korlin… ex. mi go a le ho", btn_traducir: "Traduire →"
  },
  zh: {
    tagline: "一种简短、诚实、现代的人造语言",
    tab_inicio: "🏠 首页", tab_why: "🚀 为什么", tab_compare: "📊 比较",
    tab_diccionario: "📖 词典", tab_flashcards: "🎴 闪卡", tab_traductor: "🔄 翻译器", tab_aprender: "🎓 学习",
    tab_ia: "🤖 供人工智能使用",
    ia_titulo: "供人工智能代理使用 🤖",
    ia_desc: "任何大语言模型今天就能说克林语，无需训练。把规范交给它，它就能正确翻译。",
    ia_card1: "独立的规范包（约 16 KB）。粘贴到任何系统提示中即可。",
    ia_card2: "机器可读的词汇表、词缀和规则，供工具调用使用。",
    ia_card3: "确定性的规则翻译器。由代码而非模型生成克林语。",
    ia_pasos_t: "三个步骤",
    ia_paso1: "把 korlin-spec.md 复制到你的 AI 系统提示中。",
    ia_paso2: "让它用克林语翻译或对话。",
    ia_paso3: "检查三条规则：SVO 语序、强制示证、合法音位。",
    ia_nota: "提示：把翻译器作为工具交给模型，它就绝不会编造词根。",
    ia_ver: "查看 / 下载",
    hero_titulo: "说得更少，表达更多。",
    hero_sub: "Korlin 是一种人造语言，将意义浓缩为微小、诚实、现代的词语。",
    stat_letras: "字母，1 字母 = 1 音", stat_palabras: "核心词汇", stat_idiomas: "文档语言", stat_corto: "比世界语更短",
    card_corta_t: "✂️ 简短", card_corta_d: "1–2 个音节的单词浓缩概念，比世界语短约 40%。",
    card_honesta_t: "🛡️ 诚实", card_honesta_d: "强制示证：每句话都声明其来源。说谎代价高昂且可被察觉。",
    card_moderna_t: "📱 现代", card_moderna_d: "20 个字母，无变音符，emoji 助词，为 AI 就绪。",
    ejemplo_titulo: "示例",
    ejemplo_gloss: '「谎言无法活在我之中。」· <code>na-toro</code> = 谎言（<code>na-</code> 非 + <code>toro</code> 真相）',
    why_titulo: "为什么选择 Korlin？🚀", why_desc: "为互联、数字、诚实的世界而生。",
    why_youth_t: "🧑‍🎤 为年轻人而生", why_youth_d: "随意、有趣、emoji 原生。态度助词用两个字母表达情绪，并映射到 emoji。",
    why_ia_t: "🤖 为 AI 就绪", why_ia_d: "更少 token、确定性解析、强制示证。机器可高效理解。",
    why_adopt_t: "🌍 大规模采用", why_adopt_d: "完全规则、无例外，对亚洲和非洲使用者友好。数天即可学会，无需数年。",
    why_modern_t: "⚡ 超级现代", why_modern_d: "数字原生：无变音符、emoji 兼容，为聊天、手机和 AI 代理设计。",
    emoji_titulo: "态度助词 → emoji", emoji_desc: "两个字母在手机键盘上触发对应的 emoji。",
    emo_yo: "喜悦", emo_we: "惊讶", emo_fi: "讽刺", emo_ri: "笑", emo_hu: "悲伤", emo_bu: "愤怒", emo_la: "爱", emo_pu: "厌恶", emo_ni: "恐惧",
    compare_titulo: "比较 📊", compare_desc: "Korlin 与其对手及自然语言的对比。",
    vs_esp_titulo: "Korlin vs 世界语", vs_dut_titulo: "Korlin vs Dutton Speedwords",
    th_feat: "特性", f_diacrit: "变音符", f_acc: "宾格 (-n)", f_evid: "示证（反谎言）", f_emoji: "emoji 助词", f_ia: "AI 就绪", f_len: "长度（同一文本）", f_pron: "可发音", f_reg: "完全规则", f_tech: "技术词汇",
    len_titulo: "长度：多种语言中的同一句话", len_desc: '「谎言无法活在我之中」——每种语言的字符数。',
    len_nota: "在更长文本中，Korlin 比西班牙语节省约 44% 字符，比英语约 36%，比日语约 31%。",
    diccionario_titulo: "词典 📖", busqueda_ph: "用 Korlin、西班牙语或英语搜索…",
    flashcards_titulo: "闪卡 🎴", flashcards_desc: "猜猜意思。点击卡片揭晓。",
    flash_no: "🙈 不知道", flash_si: "✅ 知道",
    traductor_titulo: "翻译器（逐词）🔄", traductor_desc: "将 Korlin 逐词翻译为所选语言（演示）。",
    traductor_ph: "用 Korlin 输入…例如 mi go a le ho", btn_traducir: "翻译 →"
  },
  ja: {
    tagline: "短く、誠実で、現代的に作られた言語",
    tab_inicio: "🏠 ホーム", tab_why: "🚀 なぜ Korlin", tab_compare: "📊 比較",
    tab_diccionario: "📖 辞書", tab_flashcards: "🎴 フラッシュカード", tab_traductor: "🔄 翻訳", tab_aprender: "🎓 学ぶ",
    tab_ia: "🤖 AI 向け",
    ia_titulo: "AI エージェント向け 🤖",
    ia_desc: "どんな LLM も今日からコルリン語を話せます。学習は不要です。仕様を渡せば正しく翻訳します。",
    ia_card1: "自己完結型の仕様パック（約 16 KB）。任意のシステムプロンプトに貼り付けてください。",
    ia_card2: "ツール呼び出し用の、機械可読な語彙・接辞・規則。",
    ia_card3: "決定的な規則ベースの翻訳器。コルリン語を生成するのはモデルではなくコードです。",
    ia_pasos_t: "3 つの手順",
    ia_paso1: "korlin-spec.md をお使いの AI のシステムプロンプトにコピーします。",
    ia_paso2: "コルリン語で翻訳または会話するよう依頼します。",
    ia_paso3: "3 つの規則を確認します：SVO 語順、必須の証拠性、有効な音素。",
    ia_nota: "ヒント：翻訳器をツールとしてモデルに渡せば、語根を決してでっち上げません。",
    ia_ver: "表示 / ダウンロード",
    hero_titulo: "少なく話し、多くを伝える。",
    hero_sub: "Korlin は意味を小さく、誠実で、現代的な言葉に凝縮する人工言語です。",
    stat_letras: "文字、1 文字 = 1 音", stat_palabras: "基本語彙", stat_idiomas: "ドキュメント言語", stat_corto: "エスペラントより短い",
    card_corta_t: "✂️ 短い", card_corta_d: "1～2 音節の単語が概念を凝縮。エスペラントより約 40% 短い。",
    card_honesta_t: "🛡️ 誠実", card_honesta_d: "証拠性が必須：すべての発言が情報源を宣言。嘘はコストが高く、検出可能。",
    card_moderna_t: "📱 現代的", card_moderna_d: "20 文字、発音区別符号なし、絵文字助詞、AI 対応。",
    ejemplo_titulo: "例",
    ejemplo_gloss: '「嘘は私の中に生きられない。」· <code>na-toro</code> = 嘘（<code>na-</code> 非 + <code>toro</code> 真実）',
    why_titulo: "なぜ Korlin か？🚀", why_desc: "つながり、デジタルで、誠実な世界のために。",
    why_youth_t: "🧑‍🎤 若者向け", why_youth_d: "カジュアルで遊び心があり、絵文字ネイティブ。態度助詞は 2 文字で感情を表し、絵文字にマッピング。",
    why_ia_t: "🤖 AI 対応", why_ia_d: "少ないトークン、決定的な解析、必須の証拠性。機械は効率的に理解できる。",
    why_adopt_t: "🌍 大量採用", why_adopt_d: "完全に規則的で例外なし。アジア・アフリカの話者に簡単。年ではなく数日で学べる。",
    why_modern_t: "⚡ 超現代的", why_modern_d: "デジタルネイティブ：発音区別符号なし、絵文字対応、チャット・スマホ・AI エージェント向け。",
    emoji_titulo: "態度助詞 → 絵文字", emoji_desc: "2 文字がスマホのキーボードで対応する絵文字を呼び出す。",
    emo_yo: "喜び", emo_we: "驚き", emo_fi: "皮肉", emo_ri: "笑い", emo_hu: "悲しみ", emo_bu: "怒り", emo_la: "愛情", emo_pu: "嫌悪", emo_ni: "恐怖",
    compare_titulo: "比較 📊", compare_desc: "Korlin とライバル・自然言語の比較。",
    vs_esp_titulo: "Korlin vs エスペラント", vs_dut_titulo: "Korlin vs Dutton Speedwords",
    th_feat: "特徴", f_diacrit: "発音区別符号", f_acc: "対格 (-n)", f_evid: "証拠性（反嘘）", f_emoji: "絵文字助詞", f_ia: "AI 対応", f_len: "長さ（同一テキスト）", f_pron: "発音可能", f_reg: "完全に規則的", f_tech: "技術語彙",
    len_titulo: "長さ：複数言語での同一文", len_desc: '「嘘は私の中に生きられない」——言語ごとの文字数。',
    len_nota: "より長いテキストでは、Korlin はスペイン語比で約 44%、英語比で約 36%、日本語比で約 31% の文字を節約。",
    diccionario_titulo: "辞書 📖", busqueda_ph: "Korlin・スペイン語・英語で検索…",
    flashcards_titulo: "フラッシュカード 🎴", flashcards_desc: "意味を当ててください。カードをクリックして表示。",
    flash_no: "🙈 知らなかった", flash_si: "✅ 知っていた",
    traductor_titulo: "翻訳（単語ごと）🔄", traductor_desc: "Korlin を選択した言語へ単語ごとに翻訳（デモ）。",
    traductor_ph: "Korlin で入力…例 mi go a le ho", btn_traducir: "翻訳 →"
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
  renderDiccionario(document.getElementById('busqueda').value);
  actualizarFlashSignificado();
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

if (busqueda) busqueda.addEventListener('input', () => renderDiccionario(busqueda.value));

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
  document.getElementById('flash-score').textContent = `Score: ${aciertos} / ${total}`;
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
