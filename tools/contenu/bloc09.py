import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L41 Sentiments ----------
L = "v4-41"
l41 = {"id": L, "title": "Sentiments", "words": [
 W("うれしい","うれしい","heureux, content","{友|とも}だちから{手紙|てがみ}が{来|き}て、うれしかったです。","J'ai reçu une lettre d'un ami, j'étais content."),
 W("かなしい","かなしい","triste","{犬|いぬ}が{死|し}んで、とてもかなしかったです。","Mon chien est mort, j'étais très triste."),
 W("さびしい","さびしい","se sentir seul","{家族|かぞく}に{会|あ}えなくて、さびしいです。","Je ne peux pas voir ma famille, je me sens seul."),
 W("こわい","こわい","effrayant ; avoir peur","{夜|よる}の{森|もり}はこわいです。","La forêt la nuit, ça fait peur."),
 W("はずかしい","はずかしい","gêné, avoir honte","みんなの{前|まえ}で{歌|うた}うのは、はずかしいです。","Chanter devant tout le monde, ça me gêne."),
 W("{心配|しんぱい}する","しんぱいする","s'inquiéter","{子|こ}どもが{帰|かえ}ってこないので、{母|はは}は{心配|しんぱい}しています。","L'enfant ne rentre pas, sa mère s'inquiète."),
 W("{安心|あんしん}する","あんしんする","être rassuré","{試験|しけん}がやさしかったので、{安心|あんしん}しました。","L'examen était facile, j'ai été rassuré."),
 W("びっくりする","びっくりする","être surpris","{急|きゅう}に{大|おお}きい{音|おと}がして、びっくりしました。","Il y a eu un grand bruit d'un coup, j'ai sursauté."),
 W("よろこぶ","よろこぶ","se réjouir (les autres)","{母|はは}はプレゼントをとてもよろこびました。","Ma mère a été ravie du cadeau."),
 W("おこる","おこる","se fâcher","{宿題|しゅくだい}をわすれて、{先生|せんせい}がおこりました。","J'ai oublié mes devoirs, le professeur s'est fâché."),
 W("なく","なく","pleurer","{赤|あか}ちゃんが{夜|よる}ずっとないています。","Le bébé pleure toute la nuit."),
 W("わらう","わらう","rire, sourire","{田中|たなか}さんはいつもわらっています。","M. Tanaka sourit toujours."),
 W("{気持|きも}ち","きもち","sentiment, sensation","{朝|あさ}のさんぽは{気持|きも}ちがいいです。","La promenade du matin, c'est agréable."),
 W("ざんねん","ざんねん","dommage, regrettable","{雨|あめ}で{試合|しあい}がなくなって、ざんねんです。","Le match est annulé à cause de la pluie, c'est dommage."),
 W("{楽|たの}しみ","たのしみ","avoir hâte ; plaisir","{来週|らいしゅう}の{旅行|りょこう}が{楽|たの}しみです。","J'ai hâte du voyage de la semaine prochaine."),
], "sections": [
 {"h": "Ce que je ressens, ce que ressentent les autres",
  "p": ["Les adjectifs de sentiment (うれしい, かなしい, こわい…) disent en principe ce que **je** ressens. Pour les autres, on décrit ce qu'on voit, avec un verbe."],
  "grid": {"head": ["", "emploi"], "rows": [
   ["うれしい · かなしい · さびしい · こわい", "ce que **je** ressens"],
   ["よろこぶ · おこる · なく · わらう", "ce qu'on **voit** chez les autres : {母|はは}はよろこんでいます"],
   ["{心配|しんぱい}する · {安心|あんしん}する · びっくりする", "verbes en する : {心配|しんぱい}しています"],
   ["{楽|たの}しい / {楽|たの}しみ", "c'est agréable (pendant) / j'ai hâte (avant)"]]}}
], "pieges": [
 "{弟|おとうと}はうれしいです sonne bizarre : on dit {弟|おとうと}は**よろこんでいます** (on décrit ce qu'on voit).",
 "{旅行|りょこう}が**{楽|たの}しみ**です = j'ai hâte du voyage. {旅行|りょこう}は**{楽|たの}しかった**です = le voyage était agréable.",
 "ざんねん = c'est dommage (une chose ratée), pas « triste ».",
 "さびしい = on se sent seul, quelqu'un nous manque ; かなしい = triste.",
 "{気持|きも}ちがいい = c'est agréable (sensation) ; {気持|きも}ちが{悪|わる}い = ça dégoûte, j'ai la nausée.",
 "おこる au passif : {先生|せんせい}に**おこられました** = je me suis fait gronder."
], "exercises": [
 C(L,1,["うれしかった","かなしかった","さびしかった","こわかった"],jp="{友|とも}だちがたんじょうびにケーキをくれました。とても＿です。",fr="Mon ami m'a offert un gâteau pour mon anniversaire. J'étais très content.",uses=["v5-17","v5-26"]),
 C(L,2,["かなしかったです","うれしかったです","{楽|たの}しかったです","はずかしかったです"],jp="{犬|いぬ}が{死|し}んで、とても＿。",fr="Mon chien est mort, j'étais très triste.",uses=["v5-35","v5-36"]),
 C(L,3,["さびしく","うれしく","あたたかく","はずかしく"],jp="{一人|ひとり}で{外国|がいこく}に{住|す}んでいますから、ときどき＿なります。",fr="J'habite seul à l'étranger, alors parfois je me sens seul.",uses=["v5-33","v5-36"]),
 C(L,4,["こわい","うれしい","{楽|たの}しい","ざんねん"],jp="{夜|よる}の{森|もり}は＿ですから、{一人|ひとり}で{行|い}きたくないです。",fr="La forêt la nuit fait peur, alors je ne veux pas y aller seul.",uses=["v5-35"]),
 C(L,5,["はずかしかった","うれしかった","{安心|あんしん}した","さびしかった"],jp="みんなの{前|まえ}で{歌|うた}を{歌|うた}いました。{下手|へた}ですから、とても＿です。",fr="J'ai chanté devant tout le monde. Je chante mal, alors j'avais très honte.",uses=["v5-19","v5-31"]),
 C(L,6,["{心配|しんぱい}して","{安心|あんしん}して","よろこんで","わらって"],jp="{子|こ}どもがまだ{帰|かえ}ってきませんから、{母|はは}は＿います。",fr="L'enfant n'est pas encore rentré, alors sa mère s'inquiète."),
 C(L,7,["{安心|あんしん}","{心配|しんぱい}","ざんねん","けっこん"],jp="{子|こ}どもが{元気|げんき}に{帰|かえ}ってきて、{母|はは}は＿しました。",fr="L'enfant est rentré en bonne santé, sa mère a été rassurée.",uses=["v5-19","v5-36"]),
 C(L,8,["びっくり","{安心|あんしん}","さんぽ","れんしゅう"],jp="{急|きゅう}に{大|おお}きい{音|おと}がして、＿しました。",fr="Il y a eu un grand bruit d'un coup, j'ai sursauté.",uses=["v5-14","v5-29"]),
 C(L,9,["{母|はは}はプレゼントをとてもよろこびました。","{母|はは}はプレゼントをとてもうれしいでした。","{母|はは}はプレゼントをとてもよろこいました。","{母|はは}はプレゼントにとてもよろこびです。"],q="« Ma mère a été ravie du cadeau » se dit…",uses=["v5-26"],explain="Pour quelqu'un d'autre : よろこぶ (よろこびました). Et jamais うれしいでした (→ うれしかったです)."),
 C(L,10,["おこられました","わらいました","なきました","よろこびました"],jp="{宿題|しゅくだい}をわすれて、{先生|せんせい}に＿。",fr="J'ai oublié mes devoirs et je me suis fait gronder par le professeur.",uses=["v5-28","v5-29"],explain="{先生|せんせい}**に**おこられる (passif) = se faire gronder par le professeur.",star={"jp":"おこる","kana":"おこる","fr":"se fâcher"}),
 C(L,11,["ないて","{安心|あんしん}して","びっくりして","さびしくて"],jp="{赤|あか}ちゃんが{夜|よる}ずっと＿います。ねられません。",fr="Le bébé pleure toute la nuit. Je n'arrive pas à dormir."),
 C(L,12,["dommage, regrettable","triste à pleurer","effrayant","embarrassant"],q="Que veut dire **ざんねん** ?"),
 C(L,13,["{楽|たの}しみ","{楽|たの}しかった","{楽|たの}しく","{楽|たの}しむ"],jp="{来週|らいしゅう}の{旅行|りょこう}がとても＿です。",fr="J'ai très hâte du voyage de la semaine prochaine.",uses=["v5-18","v5-33"],explain="Une chose à venir qu'on attend avec plaisir : {楽|たの}しみです."),
 C(L,14,["いい","{安心|あんしん}","うれしい","{楽|たの}しみ"],jp="{朝|あさ}、{公園|こうえん}を{走|はし}ると、{気持|きも}ちが＿です。",fr="Le matin, courir dans le parc, c'est agréable.",uses=["v5-15"]),
 C(L,15,["{心配|しんぱい}する","びっくりする","よろこぶ","わらう"],q="Contraire de **{安心|あんしん}する** ?"),
 C(L,16,["se fâcher","pleurer","rire","avoir peur"],q="Que veut dire **おこる** ?"),
 C(L,17,["ざんねん","{楽|たの}しみ","{上手|じょうず}","{便利|べんり}"],jp="{雨|あめ}で{試合|しあい}がなくなりました。とても＿です。",fr="Le match est annulé à cause de la pluie. C'est vraiment dommage.",uses=["v5-25"]),
 O(L,18,"J'ai hâte de te voir demain.",["{明日|あした}","{会|あ}うのが","{楽|たの}しみ","です"],uses=["v5-02"]),
 O(L,19,"Ma mère s'inquiète pour moi.",["{母|はは}は","{私|わたし}のことを","{心配|しんぱい}して","います"],uses=["v5-21","v5-39"]),
]}

# ---------- L42 Caractère et apparence ----------
L = "v4-42"
l42 = {"id": L, "title": "Caractère et apparence", "words": [
 W("きびしい","きびしい","sévère, strict","{父|ちち}はとてもきびしい{人|ひと}です。","Mon père est quelqu'un de très strict."),
 W("まじめ","まじめ","sérieux","{田中|たなか}さんはまじめで、{毎日|まいにち}よく{勉強|べんきょう}します。","M. Tanaka est sérieux, il travaille bien tous les jours."),
 W("ていねい","ていねい","poli, soigné","{先生|せんせい}はていねいに{説明|せつめい}してくれました。","Le professeur m'a expliqué avec soin."),
 W("ねっしん","ねっしん","appliqué, passionné","{妹|いもうと}はねっしんにピアノをれんしゅうしています。","Ma petite sœur s'exerce au piano avec ardeur."),
 W("しょうじき","しょうじき","honnête","しょうじきに{話|はな}してください。","Parle-moi honnêtement."),
 W("らんぼう","らんぼう","brutal, violent","らんぼうな{運転|うんてん}はあぶないです。","Conduire brutalement est dangereux."),
 W("ひどい","ひどい","terrible, cruel","ひどい{雨|あめ}ですね。","Quelle pluie terrible !"),
 W("うつくしい","うつくしい","beau (soutenu)","{山|やま}の{上|うえ}から{見|み}る{海|うみ}はうつくしいです。","La mer vue du haut de la montagne est magnifique."),
 W("すてき","すてき","joli, chouette","すてきなセーターですね。","Quel joli pull !"),
 W("{太|ふと}る","ふとる","grossir","{毎晩|まいばん}ケーキを{食|た}べて、{太|ふと}りました。","J'ai mangé du gâteau tous les soirs, j'ai grossi."),
 W("やせる","やせる","maigrir","{毎日|まいにち}{走|はし}って、{三|さん}キロやせました。","J'ai couru tous les jours, j'ai perdu trois kilos."),
 W("せ","せ","taille (d'une personne)","{兄|あに}はせが{高|たか}いです。","Mon grand frère est grand."),
 W("にる","にる","ressembler (à)","{田中|たなか}さんはお{父|とう}さんによくにています。","M. Tanaka ressemble beaucoup à son père."),
 W("かみ","かみ","cheveux","{姉|あね}はかみが{長|なが}いです。","Ma grande sœur a les cheveux longs."),
 W("ひげ","ひげ","barbe, moustache","おじいさんは{白|しろ}いひげがあります。","Grand-père a une barbe blanche."),
], "sections": [
 {"h": "Décrire quelqu'un",
  "p": ["Le physique se dit avec 〜**が** + adjectif : せ**が**{高|たか}い, かみ**が**{長|なが}い."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["taille", "せ==が=={高|たか}い / せ==が=={低|ひく}い"],
   ["cheveux", "かみ==が=={長|なが}い / {短|みじか}い"],
   ["ressembler à", "〜==に==にている (toujours en ている)"],
   ["corpulence", "{太|ふと}っている (gros) / やせている (mince)"],
   ["caractère (な)", "まじめ, ていねい, ねっしん, しょうじき, らんぼう"]]}}
], "pieges": [
 "{太|ふと}っています = il **est** gros ; {太|ふと}りました = il **a grossi**. Pareil pour やせています / やせました.",
 "にる s'emploie presque toujours en **〜にています** : {母|はは}**に**にています = je ressemble à ma mère.",
 "まじめ, ていねい, ねっしん, しょうじき, らんぼう, すてき : adjectifs en な. Devant un verbe : ていねい**に**, しょうじき**に**.",
 "Pour la taille d'une personne : せが{高|たか}い (plutôt que {大|おお}きい).",
 "うつくしい = beau, un peu soutenu (paysage) ; きれい = beau, propre (courant).",
 "かみ (cheveux) a le même son que かみ (papier, {紙|かみ}) : contexte !"
], "exercises": [
 C(L,1,["きびしい","やさしい","うれしい","すてき"],jp="{父|ちち}はとても＿ですから、{夜|よる}{十時|じゅうじ}までに{帰|かえ}らなければなりません。",fr="Mon père est très strict, alors je dois rentrer avant dix heures du soir.",uses=["v5-18","v5-36"]),
 C(L,2,["まじめ","ざんねん","ひどい","うつくしい"],jp="{田中|たなか}さんは＿な{学生|がくせい}で、{授業|じゅぎょう}を{休|やす}んだことがありません。",fr="M. Tanaka est un étudiant sérieux : il n'a jamais manqué un cours.",uses=["v5-29"]),
 C(L,3,["ていねいに","ていねいな","ていねいく","ていねいで"],jp="{先生|せんせい}はいつも＿{説明|せつめい}してくれます。",fr="Le professeur m'explique toujours avec soin.",explain="Adjectif en な devant un verbe : ていねい**に**."),
 C(L,4,["ねっしん","ざんねん","ひげ","せ"],jp="{妹|いもうと}は{毎日|まいにち}＿にピアノをれんしゅうしています。",fr="Ma petite sœur s'exerce au piano avec ardeur tous les jours.",uses=["v5-29","v5-31"]),
 C(L,5,["しょうじき","らんぼう","ひどい","きびしい"],jp="うそはいやです。＿に{話|はな}してください。",fr="Je déteste les mensonges. Parle-moi honnêtement."),
 C(L,6,["せ","かみ","ひげ","{目|め}"],jp="{兄|あに}は＿が{高|たか}いですから、バスケットボールが{上手|じょうず}です。",fr="Mon grand frère est grand, alors il est bon au basket.",uses=["v5-19"]),
 C(L,7,["かみ","せ","{声|こえ}","ひげ"],jp="{姉|あね}は＿が{長|なが}くて、きれいです。",fr="Ma grande sœur a les cheveux longs, elle est jolie.",uses=["v5-05","v5-21"]),
 C(L,8,["{太|ふと}りました","やせました","にました","{太|ふと}いました"],jp="{毎晩|まいばん}ケーキを{食|た}べて、{三|さん}キロ＿。",fr="J'ai mangé du gâteau tous les soirs et j'ai pris trois kilos."),
 C(L,9,["やせました","わらいました","にました","やせりました"],jp="{毎日|まいにち}{走|はし}って、{五|ご}キロ＿。",fr="J'ai couru tous les jours et j'ai perdu cinq kilos.",uses=["v5-15"]),
 C(L,10,["にて","にって","にんで","にいて"],jp="{田中|たなか}さんはお{父|とう}さんによく＿います。",fr="M. Tanaka ressemble beaucoup à son père.",explain="にる est du groupe 2 : にて.",star={"jp":"にる","kana":"にる","fr":"ressembler (à)"}),
 C(L,11,["に","を","へ","で"],jp="むすめさんはお{母|かあ}さん＿よくにていますね。",fr="Votre fille ressemble beaucoup à sa mère.",explain="Ressembler **à** : 〜に にている."),
 C(L,12,["beau (soutenu)","sale","jeune","sévère"],q="Que veut dire **うつくしい** ?"),
 C(L,13,["すてき","ひどい","らんぼう","きびしい"],jp="＿なセーターですね。どこで{買|か}いましたか。",fr="Quel joli pull ! Où l'as-tu acheté ?",uses=["v5-13"]),
 C(L,14,["らんぼう","ていねい","まじめ","しょうじき"],jp="＿な{運転|うんてん}はあぶないです。",fr="Conduire brutalement est dangereux.",uses=["v5-15"]),
 C(L,15,["ひどい","すてきな","まじめな","うつくしい"],jp="{今日|きょう}は＿{雨|あめ}ですね。かさがこわれました。",fr="Quelle pluie terrible aujourd'hui ! Mon parapluie s'est cassé.",uses=["v5-25"]),
 C(L,16,["やせています","やせます","やせました","やせいます"],q="« Elle est mince » (c'est son état) se dit…",explain="État actuel : 〜ています. やせました = elle a maigri."),
 O(L,17,"Mon grand frère est grand et a les cheveux courts.",["{兄|あに}は","せが{高|たか}くて、","かみが","{短|みじか}いです"],uses=["v5-05","v5-24"]),
 O(L,18,"Je ressemble beaucoup à ma mère.",["{私|わたし}は","{母|はは}に","よく","にています"],alt=[["{私|わたし}は","よく","{母|はは}に","にています"]],uses=["v5-21"]),
]}

# ---------- L43 Relations ----------
L = "v4-43"
l43 = {"id": L, "title": "Couples, enfants, entourage", "words": [
 W("かれ","かれ","il ; petit ami","かれは{大学|だいがく}の{友|とも}だちです。","Lui, c'est un ami de l'université."),
 W("かのじょ","かのじょ","elle ; petite amie","{兄|あに}のかのじょはとてもやさしいです。","La copine de mon frère est très gentille."),
 W("おっと","おっと","(mon) mari","おっとは{銀行|ぎんこう}で{働|はたら}いています。","Mon mari travaille dans une banque."),
 W("つま","つま","(ma) femme","つまは{料理|りょうり}が{上手|じょうず}です。","Ma femme cuisine très bien."),
 W("{主人|しゅじん}","しゅじん","(mon) mari ; maître de maison","{主人|しゅじん}は{今|いま}、{出|で}かけています。","Mon mari est sorti pour le moment."),
 W("おくさん","おくさん","épouse (des autres)","{田中|たなか}さんのおくさんはフランス{人|じん}です。","La femme de M. Tanaka est française."),
 W("むすこ","むすこ","(mon) fils","むすこは{今年|ことし}{大学生|だいがくせい}になりました。","Mon fils est entré à l'université cette année."),
 W("むすめ","むすめ","(ma) fille","むすめは{五|ご}さいです。","Ma fille a cinq ans."),
 W("{赤|あか}ちゃん","あかちゃん","bébé","{赤|あか}ちゃんがねています。{静|しず}かにしてください。","Le bébé dort. Silence, s'il vous plaît."),
 W("{親|おや}","おや","parent(s)","{週末|しゅうまつ}、{親|おや}に{電話|でんわ}をしました。","Ce week-end, j'ai téléphoné à mes parents."),
 W("そふ","そふ","(mon) grand-père","そふは{九十|きゅうじゅう}さいで、まだ{元気|げんき}です。","Mon grand-père a quatre-vingt-dix ans, il est encore en forme."),
 W("そぼ","そぼ","(ma) grand-mère","そぼの{家|いえ}は{山|やま}の{近|ちか}くにあります。","La maison de ma grand-mère est près des montagnes."),
 W("おじさん","おじさん","oncle ; monsieur (âge mûr)","おじさんは{父|ちち}の{兄|あに}です。","Mon oncle est le grand frère de mon père."),
 W("おばさん","おばさん","tante ; madame (âge mûr)","となりのおばさんがりんごをくれました。","La dame d'à côté m'a donné des pommes."),
 W("{知|し}り{合|あ}い","しりあい","connaissance (personne)","{田中|たなか}さんは{友|とも}だちじゃなくて、{知|し}り{合|あ}いです。","M. Tanaka n'est pas un ami, c'est une connaissance."),
], "sections": [
 {"h": "Ma famille, celle des autres (suite)",
  "p": ["Comme au N5 : mot simple pour **sa** famille, mot poli pour celle des autres."],
  "grid": {"head": ["", "la mienne → celle des autres"], "rows": [
   ["mari", "おっと, {主人|しゅじん} → ご{主人|しゅじん}"],
   ["épouse", "つま → おくさん"],
   ["fils", "むすこ → むすこさん"],
   ["fille", "むすめ → むすめさん"],
   ["grands-parents", "そふ, そぼ → おじいさん, おばあさん"]]}}
], "pieges": [
 "おっと, つま, そふ, そぼ, むすこ, むすめ : pour **sa propre** famille. Pour les autres : ご{主人|しゅじん}, おくさん, おじいさん, おばあさん, むすこさん, むすめさん.",
 "{主人|しゅじん} (sans ご) = **mon** mari ; ご{主人|しゅじん} = le mari de quelqu'un d'autre.",
 "かれ / かのじょ = il / elle, mais souvent « petit ami » / « petite amie ».",
 "おじさん / おばさん = oncle / tante, **et** « monsieur / madame » d'un certain âge.",
 "おじいさん (grand-père) ≠ おじさん (oncle) ; おばあさん ≠ おばさん.",
 "{知|し}り{合|あ}い = une connaissance : moins proche qu'un ami."
], "exercises": [
 C(L,1,["おくさん","つま","{主人|しゅじん}","おっと"],jp="{田中|たなか}さんの＿はフランス{人|じん}だそうです。",fr="Il paraît que la femme de M. Tanaka est française.",uses=["v5-33"],explain="L'épouse de quelqu'un d'autre : おくさん. つま, c'est la sienne."),
 C(L,2,["つま","おくさん","ご{主人|しゅじん}","むすこさん"],q="Tu parles de **ta** femme à un collègue.",jp="＿は{料理|りょうり}が{上手|じょうず}です。",fr="Ma femme cuisine très bien.",uses=["v5-19"]),
 C(L,3,["ご{主人|しゅじん}","おっと","つま","おくさん"],q="Tu parles du mari de Mme Yamada.",jp="{山田|やまだ}さんの＿はお{医者|いしゃ}さんですね。",fr="Le mari de Mme Yamada est médecin, n'est-ce pas ?",uses=["v5-30"]),
 C(L,4,["{赤|あか}ちゃん","そふ","かのじょ","{知|し}り{合|あ}い"],jp="＿はまだ{歩|ある}けません。{生|う}まれて{三|さん}か{月|げつ}です。",fr="Le bébé ne marche pas encore. Il est né il y a trois mois.",uses=["v5-36","v5-38"]),
 C(L,5,["(mon) fils","(ma) fille","(mon) neveu","(mon) petit-fils"],q="Que veut dire **むすこ** ?"),
 C(L,6,["(ma) fille","(ma) femme","(ma) sœur","(ma) nièce"],q="Que veut dire **むすめ** ?"),
 C(L,7,["おじさん","おじいさん","お{兄|にい}さん","むすこ"],jp="{父|ちち}の{兄|あに}は{私|わたし}の＿です。",fr="Le grand frère de mon père est mon oncle.",uses=["v5-21"]),
 C(L,8,["そぼ","おばさん","そふ","むすめ"],q="Tu parles de **ta** grand-mère à ton professeur.",jp="＿は{今年|ことし}{八十|はちじゅう}さいです。",fr="Ma grand-mère a quatre-vingts ans cette année."),
 C(L,9,["かれ","かのじょ","おくさん","つま"],jp="{姉|あね}の＿はとてもやさしい{男|おとこ}の{人|ひと}です。",fr="Le petit ami de ma grande sœur est un homme très gentil.",uses=["v5-01","v5-21"]),
 C(L,10,["{知|し}り{合|あ}い","{親|おや}","むすこ","つま"],jp="{仕事|しごと}で{一度|いちど}{会|あ}っただけの{人|ひと}は、{友|とも}だちじゃなくて＿です。",fr="Quelqu'un qu'on n'a vu qu'une fois pour le travail n'est pas un ami, c'est une connaissance.",uses=["v5-30","v5-38"]),
 C(L,11,["parent(s)","ami proche","enfant","voisin"],q="Que veut dire **{親|おや}** ?"),
 C(L,12,["おばさん","おっと","つま","むすこ"],jp="となりの＿がりんごをくれました。",fr="La dame d'à côté m'a donné des pommes.",uses=["v5-20","v5-26"]),
 C(L,13,["de son mari","de son patron","de son fils","de son père"],q="Une femme te dit : {主人|しゅじん}は{今|いま}、{出|で}かけています. De qui parle-t-elle ?"),
 C(L,14,["{父|ちち}","{兄|あに}","むすこ","おっと"],jp="そふは{私|わたし}の＿の{父|ちち}です。",fr="Mon grand-père est le père de mon père.",uses=["v5-21"]),
 C(L,15,["むすこは{今年|ことし}{大学生|だいがくせい}になりました。","むすこさんは{今年|ことし}{大学生|だいがくせい}になりました。","むすめは{今年|ことし}{大学生|だいがくせい}になりました。","むすこは{今年|ことし}{大学生|だいがくせい}がなりました。"],q="« Mon fils est entré à l'université cette année » se dit…",uses=["v5-30"],explain="Son propre fils : むすこ (sans さん). 〜**に**なる."),
 O(L,16,"Le mari de Mme Tanaka est français.",["{田中|たなか}さんの","ご{主人|しゅじん}は","フランス{人|じん}","です"],uses=["v5-33"]),
 O(L,17,"J'ai téléphoné à mes parents.",["{親|おや}に","{電話|でんわ}を","しました"],alt=[["{電話|でんわ}を","{親|おや}に","しました"]],uses=["v5-12"]),
]}

# ---------- L44 Santé et hôpital ----------
L = "v4-44"
l44 = {"id": L, "title": "Santé et hôpital", "words": [
 W("けが","けが","blessure","サッカーをして、{足|あし}にけがをしました。","J'ai joué au foot et je me suis blessé au pied."),
 W("なおる","なおる","guérir","かぜはもうなおりましたか。","Ton rhume est guéri ?"),
 W("{入院|にゅういん}する","にゅういんする","être hospitalisé","{父|ちち}は{一週間|いっしゅうかん}{入院|にゅういん}しました。","Mon père a été hospitalisé une semaine."),
 W("たいいんする","たいいんする","sortir de l'hôpital","{母|はは}は{来週|らいしゅう}たいいんします。","Ma mère sort de l'hôpital la semaine prochaine."),
 W("{歯医者|はいしゃ}","はいしゃ","dentiste","{歯|は}がいたいですから、{歯医者|はいしゃ}に{行|い}きます。","J'ai mal aux dents, alors je vais chez le dentiste."),
 W("ぐあい","ぐあい","état (de santé)","お{母|かあ}さんのぐあいはどうですか。","Comment va votre mère ?"),
 W("{気分|きぶん}","きぶん","humeur, se sentir (bien, mal)","{今日|きょう}は{気分|きぶん}が{悪|わる}いですから、{早|はや}くねます。","Je ne me sens pas bien aujourd'hui, je me couche tôt."),
 W("ちゅうしゃ","ちゅうしゃ","piqûre","{病院|びょういん}でちゅうしゃをしてもらいました。","On m'a fait une piqûre à l'hôpital."),
 W("{注意|ちゅうい}する","ちゅういする","faire attention ; avertir","{車|くるま}に{注意|ちゅうい}してください。","Faites attention aux voitures."),
 W("お{大事|だいじ}に","おだいじに","prenez soin de vous (à un malade)","かぜですか。お{大事|だいじ}に。","Un rhume ? Soigne-toi bien."),
 W("おみまい","おみまい","visite à un malade","{友|とも}だちのおみまいに{病院|びょういん}へ{行|い}きました。","Je suis allé rendre visite à un ami à l'hôpital."),
 W("{顔色|かおいろ}","かおいろ","mine, teint","{顔色|かおいろ}が{悪|わる}いですね。だいじょうぶですか。","Tu as mauvaise mine. Ça va ?"),
 W("ほね","ほね","os","スキーで{足|あし}のほねをおりました。","Je me suis cassé la jambe au ski."),
 W("{生|い}きる","いきる","vivre (être en vie)","そふは{百|ひゃく}さいまで{生|い}きました。","Mon grand-père a vécu jusqu'à cent ans."),
 W("きゅうきゅうしゃ","きゅうきゅうしゃ","ambulance","きゅうきゅうしゃをよんでください。","Appelez une ambulance !"),
], "sections": [
 {"h": "Chez le médecin",
  "p": ["Chaque expression a sa particule : à retenir en bloc."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["comment ça va ?", "ぐあい==は==どうですか"],
   ["ne pas se sentir bien", "{気分|きぶん}==が=={悪|わる}い"],
   ["avoir mauvaise mine", "{顔色|かおいろ}==が=={悪|わる}い"],
   ["se blesser au pied", "{足|あし}==に==けが==を==する"],
   ["le rhume guérit", "かぜ==が==なおる"],
   ["à un malade", "お{大事|だいじ}に"]]}}
], "pieges": [
 "けが**を**する = se blesser ; {足|あし}**に**けがをする = se blesser au pied.",
 "なおる : c'est la maladie qui guérit → かぜ**が**なおる.",
 "{顔色|かおいろ}が{悪|わる}い se dit **des autres** (ce qu'on voit) ; {気分|きぶん}が{悪|わる}い, c'est ce qu'on ressent soi-même.",
 "お{大事|だいじ}に : la formule pour quitter quelqu'un de malade.",
 "おみまい = la visite (ou le cadeau) à un malade. ≠ おみやげ (souvenir de voyage).",
 "ちゅうしゃ (piqûre) a le même son que ちゅうしゃ (stationnement) : contexte !",
 "{生|い}きる (いきる, vivre) ≠ {生|う}まれる (うまれる, naître) : même kanji."
], "exercises": [
 C(L,1,["けが","ぐあい","{顔色|かおいろ}","おみまい"],jp="サッカーをして、{足|あし}に＿をしました。",fr="J'ai joué au foot et je me suis blessé au pied.",uses=["v5-23","v5-31"]),
 C(L,2,["なおりました","{入院|にゅういん}しました","ひきました","{生|い}きました"],jp="{薬|くすり}を{飲|の}んで、かぜが＿。",fr="J'ai pris des médicaments et mon rhume a guéri.",uses=["v5-23"]),
 C(L,3,["{入院|にゅういん}しました","たいいんしました","けがしました","おみまいしました"],jp="{父|ちち}は{病気|びょうき}で{二週間|にしゅうかん}＿。",fr="Mon père, malade, a été hospitalisé deux semaines.",uses=["v5-23","v5-38"]),
 C(L,4,["{歯医者|はいしゃ}","{入院|にゅういん}","{気分|きぶん}","ほね"],jp="{歯|は}がいたいですから、＿に{行|い}きます。",fr="J'ai mal aux dents, alors je vais chez le dentiste.",uses=["v5-23"]),
 C(L,5,["ぐあい","ちゅうしゃ","おみまい","きゅうきゅうしゃ"],jp="お{母|かあ}さんの＿はどうですか。— もう{元気|げんき}になりました。",fr="Comment va votre mère ? — Elle est rétablie.",uses=["v5-19","v5-21"]),
 C(L,6,["{気分|きぶん}","{注意|ちゅうい}","けが","おみまい"],jp="{今日|きょう}は＿が{悪|わる}いですから、{早|はや}く{帰|かえ}ります。",fr="Je ne me sens pas bien aujourd'hui, je rentre tôt.",uses=["v5-16"]),
 C(L,7,["{顔色|かおいろ}","{注意|ちゅうい}","おみまい","きゅうきゅうしゃ"],jp="＿が{悪|わる}いですね。だいじょうぶですか。",fr="Tu as mauvaise mine. Ça va ?",uses=["v5-19"]),
 C(L,8,["お{大事|だいじ}に。","おめでとうございます。","いただきます。","はじめまして。"],q="Ton collègue a la grippe et rentre chez lui. Tu lui dis :",uses=["v5-11"]),
 C(L,9,["おみまい","おみやげ","{歯医者|はいしゃ}","けが"],jp="{友|とも}だちが{入院|にゅういん}しましたから、＿に{行|い}きます。",fr="Mon ami est hospitalisé, alors je vais lui rendre visite.",uses=["v5-26"]),
 C(L,10,["きゅうきゅうしゃ","おみまい","{歯医者|はいしゃ}","{気分|きぶん}"],jp="{人|ひと}がたおれています。すぐ＿をよんでください。",fr="Quelqu'un s'est effondré. Appelez vite une ambulance !",uses=["v5-28"]),
 C(L,11,["{注意|ちゅうい}","{安心|あんしん}","{入院|にゅういん}","けが"],jp="この{道|みち}は{車|くるま}が{多|おお}いですから、＿してください。",fr="Il y a beaucoup de voitures dans cette rue, faites attention.",uses=["v4-41","v5-15"]),
 C(L,12,["ほね","けが","{顔色|かおいろ}","ぐあい"],jp="スキーで{足|あし}の＿をおりました。",fr="Je me suis cassé la jambe au ski (l'os de la jambe).",uses=["v5-23"]),
 C(L,13,["{生|い}きました","{生|う}まれました","{入院|にゅういん}しました","なおりました"],jp="そふは{百|ひゃく}さいまで＿。",fr="Mon grand-père a vécu jusqu'à cent ans.",uses=["v4-43","v5-36"]),
 C(L,14,["にゅういん","にゅいん","いりいん","にゅうえん"],q=LECT+"**入院** ?"),
 C(L,15,["はいしゃ","はいじゃ","しいしゃ","はいしや"],q=LECT+"**歯医者** ?"),
 C(L,16,["une piqûre","une opération","un parking","un médicament"],q="Dans « {病院|びょういん}でちゅうしゃをしてもらいました », ちゅうしゃ veut dire…"),
 O(L,17,"Mon père est sorti de l'hôpital hier.",["{父|ちち}は","{昨日|きのう}","たいいん","しました"],alt=[["{昨日|きのう}","{父|ちち}は","たいいん","しました"]],uses=["v5-03"]),
 O(L,18,"Je me suis blessé au pied.",["{足|あし}に","けがを","しました"],uses=["v5-23"]),
]}

# ---------- L45 Corps et gestes ----------
L = "v4-45"
l45 = {"id": L, "title": "Corps et gestes", "words": [
 W("{首|くび}","くび","cou","{長|なが}い{時間|じかん}パソコンを{使|つか}って、{首|くび}がいたいです。","J'ai utilisé l'ordinateur longtemps, j'ai mal au cou."),
 W("うで","うで","bras","{重|おも}いにもつを{持|も}って、うでがいたいです。","J'ai porté des bagages lourds, j'ai mal aux bras."),
 W("せなか","せなか","dos","{子|こ}どものせなかを{洗|あら}いました。","J'ai lavé le dos de l'enfant."),
 W("ゆび","ゆび","doigt","ナイフでゆびを{切|き}りました。","Je me suis coupé le doigt avec un couteau."),
 W("かた","かた","épaule","かたにかばんをかけて{歩|ある}きます。","Je marche le sac sur l'épaule."),
 W("のど","のど","gorge","かぜで、のどがいたいです。","J'ai mal à la gorge à cause du rhume."),
 W("{力|ちから}","ちから","force","{兄|あに}は{力|ちから}が{強|つよ}いです。","Mon grand frère est fort."),
 W("{動|うご}く","うごく","bouger ; marcher (machine)","この{時計|とけい}は{動|うご}きません。","Cette montre ne marche pas."),
 W("{運動|うんどう}する","うんどうする","faire de l'exercice","{毎日|まいにち}{三十分|さんじゅっぷん}{運動|うんどう}しています。","Je fais trente minutes d'exercice par jour."),
 W("おどる","おどる","danser","パーティーでみんなでおどりました。","On a tous dansé à la fête."),
 W("なげる","なげる","lancer","ボールをなげてください。","Lance la balle !"),
 W("ひろう","ひろう","ramasser","{道|みち}でさいふをひろいました。","J'ai ramassé un portefeuille dans la rue."),
 W("さわる","さわる","toucher","ここにあるものにさわらないでください。","Ne touchez pas aux objets exposés ici."),
 W("たおれる","たおれる","tomber, s'effondrer","{風|かぜ}で{木|き}がたおれました。","L'arbre est tombé à cause du vent."),
 W("あせ","あせ","sueur","{走|はし}って、あせをたくさんかきました。","J'ai couru, j'ai beaucoup transpiré."),
], "sections": [
 {"h": "Gestes : verbe et particule",
  "p": ["Quelques gestes du quotidien, avec la particule qui va avec."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["lancer / ramasser", "ボール==を==なげる / さいふ==を==ひろう"],
   ["toucher", "〜==に==さわる"],
   ["transpirer", "あせ==を==かく"],
   ["tomber (de sa hauteur)", "{人|ひと}・{木|き}==が==たおれる"],
   ["marcher (machine)", "{時計|とけい}==が=={動|うご}く"]]}}
], "pieges": [
 "〜**に**さわる : on touche **à** quelque chose.",
 "あせを**かく** = transpirer (le même かく que « écrire » s'écrit autrement, mais se prononce pareil).",
 "たおれる = tomber de toute sa hauteur (personne, arbre). Tomber d'en haut : おちる (leçon 48).",
 "{動|うご}く = bouger, et **marcher** pour une machine : {時計|とけい}が{動|うご}かない = la montre ne marche pas.",
 "かた (épaule) a le même son que {方|かた} (manière ; personne).",
 "{足|あし} = le pied **et** la jambe ; うで = le bras ; ゆび = le doigt (de la main ou du pied)."
], "exercises": [
 C(L,1,["のど","ゆび","あせ","{力|ちから}"],jp="かぜで、＿がいたいです。{水|みず}も{飲|の}みにくいです。",fr="À cause du rhume, j'ai mal à la gorge. J'ai même du mal à boire de l'eau.",uses=["v5-23"]),
 C(L,2,["ゆび","あせ","{力|ちから}","せ"],jp="{料理|りょうり}のとき、ナイフで＿を{切|き}りました。",fr="En cuisinant, je me suis coupé le doigt avec un couteau.",uses=["v5-27","v5-34"]),
 C(L,3,["{力|ちから}","あせ","のど","かみ"],jp="{兄|あに}は＿が{強|つよ}いですから、{重|おも}いものも{持|も}てます。",fr="Mon grand frère est fort, il peut porter des choses lourdes.",uses=["v5-18","v5-24"]),
 C(L,4,["{動|うご}き","おどり","なげ","ひろい"],jp="この{時計|とけい}は{古|ふる}くて、もう＿ません。",fr="Cette montre est vieille, elle ne marche plus.",uses=["v5-12"]),
 C(L,5,["{運動|うんどう}","おどる","あせ","{力|ちから}"],jp="{毎日|まいにち}{三十分|さんじゅっぷん}＿しています。",fr="Je fais trente minutes d'exercice par jour.",uses=["v5-16"]),
 C(L,6,["おどりました","なげました","ひろいました","さわりました"],jp="パーティーで{音楽|おんがく}を{聞|き}きながら、みんなで＿。",fr="À la fête, on a tous dansé en écoutant la musique.",uses=["v5-31"]),
 C(L,7,["なげて","ひろって","おどって","たおれて"],jp="ボールを＿ください。{私|わたし}がとります。",fr="Lance-moi la balle. Je l'attrape.",uses=["v5-26"]),
 C(L,8,["ひろって","なげて","おどって","さわって"],jp="{道|みち}でさいふを＿、こうばんに{持|も}って{行|い}きました。",fr="J'ai ramassé un portefeuille dans la rue et je l'ai apporté au poste de police.",uses=["v5-32"]),
 C(L,9,["さわら","ひろわ","おどら","{運動|うんどう}し"],jp="ここにあるものに＿ないでください。",fr="Ne touchez pas aux objets exposés ici.",explain="〜**に**さわる : toucher à quelque chose."),
 C(L,10,["たおれました","おどりました","なげました","ひろいました"],jp="{強|つよ}い{風|かぜ}で、{公園|こうえん}の{木|き}が＿。",fr="Avec le vent fort, l'arbre du parc est tombé.",uses=["v5-25","v5-35"]),
 C(L,11,["あせ","{字|じ}","{力|ちから}","かた"],jp="{暑|あつ}い{日|ひ}に{走|はし}って、＿をたくさんかきました。",fr="J'ai couru par une journée chaude, j'ai beaucoup transpiré.",uses=["v5-25"],explain="あせを**かく** = transpirer."),
 C(L,12,["le dos","le ventre","l'épaule","la nuque"],q="Que veut dire **せなか** ?"),
 C(L,13,["le bras","la jambe","le doigt","le cou"],q="Que veut dire **うで** ?"),
 C(L,14,["l'épaule","la manière","la personne","le dos"],q="Dans « かたがいたいです », かた veut dire…"),
 C(L,15,["くび","くぶ","くひ","くみ"],q=LECT+"**首** (le cou) ?"),
 C(L,16,["{時計|とけい}が{動|うご}きません。","{時計|とけい}が{歩|ある}きません。","{時計|とけい}が{運動|うんどう}しません。","{時計|とけい}を{動|うご}きません。"],q="« Ma montre ne marche pas » se dit…",uses=["v5-12"]),
 O(L,17,"J'ai ramassé un portefeuille dans la rue.",["{道|みち}で","さいふを","ひろいました"],alt=[["さいふを","{道|みち}で","ひろいました"]],uses=["v5-12"]),
 O(L,18,"Ne touchez pas à ceci, s'il vous plaît.",["これに","さわらないで","ください"]),
]}

TC, TO, XC, XO = make_block("v4-b09")
test = [
 TC(1,["びっくり","{安心|あんしん}","{運動|うんどう}","ざんねん"],jp="{急|きゅう}に{電気|でんき}が{消|き}えて、＿しました。",fr="La lumière s'est éteinte d'un coup, j'ai sursauté.",uses=["v4-41","v5-40"]),
 TC(2,["つまは{今|いま}、{入院|にゅういん}しています。","おくさんは{今|いま}、{入院|にゅういん}しています。","ご{主人|しゅじん}は{今|いま}、{入院|にゅういん}しています。","つまは{今|いま}、{入院|にゅういん}がしています。"],q="Tu dis à ton patron que **ta** femme est à l'hôpital :",uses=["v4-43","v4-44"]),
 TC(3,["{安心|あんしん}","{心配|しんぱい}","けが","{運動|うんどう}"],jp="{試験|しけん}がかんたんでしたから、＿しました。",fr="L'examen était facile, j'ai été rassuré.",uses=["v4-41","v5-29"]),
 TC(4,["に","を","で","へ"],jp="むすめさんはお{父|とう}さん＿よくにていますね。",fr="Votre fille ressemble beaucoup à son père.",uses=["v4-42","v4-43"]),
 TC(5,["なおりました","{生|い}きました","たおれました","{動|うご}きました"],jp="かぜはもう＿か。— はい、{元気|げんき}になりました。",fr="Ton rhume est guéri ? — Oui, je suis rétabli.",uses=["v4-44"]),
 TC(6,["ないて","わらって","おどって","{入院|にゅういん}して"],jp="{赤|あか}ちゃんが＿います。おなかがすいたのでしょう。",fr="Le bébé pleure. Il doit avoir faim.",uses=["v4-41","v4-43"]),
 TC(7,["せが{高|たか}いです。","せが{大|おお}きいです。","{体|からだ}が{高|たか}いです。","せを{高|たか}いです。"],q="« Il est grand (de taille) » se dit…",uses=["v4-42"]),
 TC(8,["きびしい","やさしい","うれしい","すてき"],jp="{先生|せんせい}はとても＿ですから、{宿題|しゅくだい}をわすれるとおこります。",fr="Le professeur est très strict : si on oublie ses devoirs, il se fâche.",uses=["v4-41","v4-42"]),
 TC(9,["きぶん","きふん","けぶん","きわけ"],q=LECT+"**気分** ?",uses=["v4-44"]),
 TC(10,["うで","のど","あせ","{気分|きぶん}"],jp="{重|おも}いにもつを{持|も}って、＿がいたいです。",fr="J'ai porté des bagages lourds, j'ai mal aux bras.",uses=["v4-45","v5-33"]),
 TC(11,["{知|し}り{合|あ}い","{親|おや}","むすこ","つま"],jp="{一度|いちど}{会|あ}っただけの{人|ひと}は、{友|とも}だちじゃなくて＿です。",fr="Quelqu'un qu'on n'a vu qu'une fois n'est pas un ami, c'est une connaissance.",uses=["v4-43"]),
 TC(12,["{楽|たの}しみ","{楽|たの}しかった","{楽|たの}しむ","{楽|たの}しく"],jp="{明日|あした}のコンサートがとても＿です。",fr="J'ai très hâte du concert de demain.",uses=["v4-41","v5-31"]),
 TC(13,["une visite à un malade","un souvenir de voyage","un cadeau d'anniversaire","un remerciement"],q="Que veut dire **おみまい** ?",uses=["v4-44"]),
 TO(14,"Mon père a été hospitalisé une semaine.",["{父|ちち}は","{一週間|いっしゅうかん}","{入院|にゅういん}","しました"],uses=["v4-44","v5-38"]),
 TC(15,["かきました","{出|だ}しました","しました","ひろいました"],jp="{走|はし}って、あせを＿。",fr="J'ai couru, j'ai transpiré.",uses=["v4-45"]),
 TC(16,["{弟|おとうと}はプレゼントをもらって、よろこんでいます。","{弟|おとうと}はプレゼントをもらって、うれしいでした。","{弟|おとうと}はプレゼントをもらって、よろこびです。","{弟|おとうと}はプレゼントをもらって、よろこいでいます。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v4-41","v5-26"]),
]
bloc = {"id": "v4-b09", "level": "N4", "title": "Émotions et personnes : sentiments, caractère, relations, santé, gestes",
        "lessons": [l41, l42, l43, l44, l45], "test": test}
save_n4(bloc, sys.argv[1])
