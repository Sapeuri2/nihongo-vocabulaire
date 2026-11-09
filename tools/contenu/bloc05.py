import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save

# ---------- L21 La famille ----------
L = "v5-21"
l21 = {"id": L, "title": "La famille", "words": [
 W("{家族|かぞく}","かぞく","famille","{家族|かぞく}は{四人|よにん}です。{父|ちち}と{母|はは}と{弟|おとうと}と{私|わたし}です。","Nous sommes quatre dans ma famille : mon père, ma mère, mon petit frère et moi."),
 W("{父|ちち}","ちち","(mon) père","{父|ちち}は{銀行|ぎんこう}で{働|はたら}いています。","Mon père travaille dans une banque."),
 W("{母|はは}","はは","(ma) mère","{母|はは}は{料理|りょうり}が{上手|じょうず}です。","Ma mère cuisine très bien."),
 W("お{父|とう}さん","おとうさん","père (des autres) ; papa","{田中|たなか}さんのお{父|とう}さんは{先生|せんせい}です。","Le père de M. Tanaka est professeur."),
 W("お{母|かあ}さん","おかあさん","mère (des autres) ; maman","お{母|かあ}さん、ただいま。","Maman, je suis rentré !"),
 W("{兄|あに}","あに","(mon) grand frère","{兄|あに}は{東京|とうきょう}に{住|す}んでいます。","Mon grand frère habite à Tokyo."),
 W("{姉|あね}","あね","(ma) grande sœur","{姉|あね}は{二十五|にじゅうご}さいです。","Ma grande sœur a vingt-cinq ans."),
 W("{弟|おとうと}","おとうと","petit frère","{弟|おとうと}は{高校生|こうこうせい}です。","Mon petit frère est lycéen."),
 W("{妹|いもうと}","いもうと","petite sœur","{妹|いもうと}はピアノが{上手|じょうず}です。","Ma petite sœur joue bien du piano."),
 W("お{兄|にい}さん","おにいさん","grand frère (des autres)","{山田|やまだ}さんのお{兄|にい}さんは{医者|いしゃ}です。","Le grand frère de M. Yamada est médecin."),
 W("お{姉|ねえ}さん","おねえさん","grande sœur (des autres)","お{姉|ねえ}さんはお{元気|げんき}ですか。","Votre grande sœur va bien ?"),
 W("{兄弟|きょうだい}","きょうだい","frères et sœurs","{兄弟|きょうだい}はいますか。— はい、{妹|いもうと}が{一人|ひとり}います。","Tu as des frères et sœurs ? — Oui, une petite sœur."),
 W("りょうしん","りょうしん","les parents","りょうしんはフランスに{住|す}んでいます。","Mes parents habitent en France."),
 W("おじいさん","おじいさん","grand-père ; vieux monsieur","おじいさんは{毎朝|まいあさ}さんぽします。","Grand-père se promène tous les matins."),
 W("おばあさん","おばあさん","grand-mère ; vieille dame","おばあさんは{九十|きゅうじゅう}さいです。","Grand-mère a quatre-vingt-dix ans."),
], "sections": [
 {"h": "Ma famille, ta famille",
  "p": ["En parlant de **sa** famille à quelqu'un : mots simples ({父|ちち}, {母|はは}…). Pour la famille **des autres**, ou pour **appeler** ses aînés à la maison : mots polis en お〜さん."],
  "grid": {"head": ["", "ma famille → celle des autres"], "rows": [
   ["père", "{父|ちち} → お{父|とう}さん"],
   ["mère", "{母|はは} → お{母|かあ}さん"],
   ["grand frère", "{兄|あに} → お{兄|にい}さん"],
   ["grande sœur", "{姉|あね} → お{姉|ねえ}さん"],
   ["petit frère", "{弟|おとうと} → {弟|おとうと}さん"],
   ["petite sœur", "{妹|いもうと} → {妹|いもうと}さん"],
   ["famille", "{家族|かぞく} → ご{家族|かぞく}"]]}}
], "pieges": [
 "À la maison, on **appelle** ses parents お{父|とう}さん, お{母|かあ}さん. Mais en parlant d'eux à quelqu'un d'autre : {父|ちち}, {母|はは}.",
 "On appelle ses aînés お{兄|にい}さん, お{姉|ねえ}さん ; ses cadets, par leur prénom (jamais « {弟|おとうと}さん ! »).",
 "Même kanji, lectures différentes : {父|ちち} / お{父|とう}さん, {母|はは} / お{母|かあ}さん, {兄|あに} / お{兄|にい}さん, {姉|あね} / お{姉|ねえ}さん.",
 "おじいさん (grand-père) ≠ おじさん (oncle) ; おばあさん (grand-mère) ≠ おばさん (tante) : la voyelle longue change tout.",
 "{兄弟|きょうだい} = frères et sœurs en général, même si ce sont des sœurs.",
 "Pour compter les membres de la famille : 〜{人|にん}. {家族|かぞく}は{四人|よにん}です."
], "exercises": [
 C(L,1,["お{父|とう}さん","{父|ちち}","{母|はは}","{兄|あに}"],jp="{田中|たなか}さんの＿は{医者|いしゃ}ですか。",fr="Le père de M. Tanaka est médecin ?",explain="La famille des autres : お{父|とう}さん."),
 C(L,2,["{父|ちち}","お{父|とう}さん","お{母|かあ}さん","{母|はは}さん"],q="Tu parles de **ton** père à un collègue.",jp="＿は{銀行|ぎんこう}で{働|はたら}いています。",fr="Mon père travaille dans une banque.",uses=["v5-14"]),
 C(L,3,["お{母|かあ}さん、ただいま。","{母|はは}、ただいま。","お{母|かあ}さん、おかえりなさい。","{母|はは}さん、ただいま。"],q="Tu rentres à la maison et tu salues ta mère. Que dis-tu ?",uses=["v5-11"],explain="Pour appeler sa mère : お{母|かあ}さん. Celui qui rentre dit ただいま."),
 C(L,4,["おとうと","おとおと","いもうと","あに"],q=LECT+"**弟** ?"),
 C(L,5,["ma grande sœur","ma petite sœur","ma mère","mon grand frère"],q="Que veut dire **{姉|あね}** ?"),
 C(L,6,["frères et sœurs","les parents","les grands-parents","les enfants"],q="Que veut dire **{兄弟|きょうだい}** ?"),
 C(L,7,["grand-père","oncle","petit-fils","cousin"],q="Que veut dire **おじいさん** ?",explain="おじいさん (long い) = grand-père ; おじさん = oncle."),
 C(L,8,["に","を","へ","で"],jp="{昨日|きのう}、{山田|やまだ}さんのお{姉|ねえ}さん＿{会|あ}いました。",fr="Hier, j'ai vu la grande sœur de M. Yamada.",uses=["v5-02"]),
 C(L,9,["{四人|よにん}","{四|よっ}つ","{三人|さんにん}","{四台|よんだい}"],jp="{家族|かぞく}は＿です。{父|ちち}と{母|はは}と{姉|あね}と{私|わたし}です。",fr="Nous sommes quatre dans ma famille : mon père, ma mère, ma grande sœur et moi.",uses=["v5-08"]),
 C(L,10,["{弟|おとうと}さん","{弟|おとうと}","{父|ちち}","{兄|あに}"],jp="{山田|やまだ}さんの＿は{何|なん}さいですか。",fr="Quel âge a le petit frère de M. Yamada ?",uses=["v5-08","v5-09"]),
 C(L,11,["les parents","les frères et sœurs","les grands-parents","les cousins"],q="Que veut dire **りょうしん** ?"),
 C(L,12,["お{兄|にい}さん、ご{飯|はん}ですよ。","{兄|あに}、ご{飯|はん}ですよ。","{弟|おとうと}さん、ご{飯|はん}ですよ。","お{兄|にい}さん、いただきます。"],q="Tu appelles ton grand frère pour le dîner. Tu dis :",uses=["v5-06","v5-11"]),
 C(L,13,["おかあさん","おははさん","おかさん","おぼさん"],q=LECT+"**お母さん** ?"),
 C(L,14,["いもうと","いもおと","おとうと","いもと"],q=LECT+"**妹** ?"),
 C(L,15,["おばあさん (grand-mère)","おばさん (tante)","お{姉|ねえ}さん (grande sœur)","お{母|かあ}さん (mère)"],q="La mère de ta mère, c'est ta…"),
 C(L,16,["{母|はは}は{料理|りょうり}が{上手|じょうず}です。","{母|はは}さんは{料理|りょうり}が{上手|じょうず}です。","{母|はは}は{料理|りょうり}を{上手|じょうず}です。","{母|はは}は{料理|りょうり}が{上手|じょうず}ます。"],q="Tu parles de ta mère à ton professeur. Une seule phrase est correcte. Laquelle ?",uses=["v5-14","v5-19"]),
 C(L,17,["Combien vous êtes dans ta famille.","Comment s'appellent tes parents.","Où habite ta famille.","Si ta famille va bien."],q="Ton ami te demande : ご{家族|かぞく}は{何人|なんにん}ですか. Que veut-il savoir ?",uses=["v5-09"]),
 C(L,18,["お{姉|ねえ}さん","{姉|あね}","{母|はは}さん","お{兄|にい}"],q="Tu parles de la grande sœur de ton ami.",jp="{田中|たなか}さんの＿はきれいですね。",fr="La grande sœur de M. Tanaka est jolie, hein.",uses=["v5-19"]),
 O(L,19,"J'ai une petite sœur et un petit frère.",["{妹|いもうと}と","{弟|おとうと}が","います"]),
 O(L,20,"Le grand frère de M. Yamada est médecin.",["{山田|やまだ}さんの","お{兄|にい}さんは","{医者|いしゃ}","です"]),
]}

# ---------- L22 La maison ----------
L = "v5-22"
l22 = {"id": L, "title": "La maison", "words": [
 W("{台所|だいどころ}","だいどころ","cuisine (la pièce)","{母|はは}は{台所|だいどころ}で{料理|りょうり}をしています。","Ma mère cuisine dans la cuisine."),
 W("{窓|まど}","まど","fenêtre","{暑|あつ}いですから、{窓|まど}を{開|あ}けます。","Il fait chaud, alors j'ouvre la fenêtre."),
 W("ドア","ドア","porte","ドアの{前|まえ}に{子|こ}どもが{立|た}っています。","Un enfant est debout devant la porte."),
 W("にわ","にわ","jardin","にわに{木|き}が{三本|さんぼん}あります。","Il y a trois arbres dans le jardin."),
 W("おふろ","おふろ","bain ; salle de bain","この{家|いえ}のおふろは{広|ひろ}いです。","La salle de bain de cette maison est grande."),
 W("かいだん","かいだん","escalier","エレベーターがありませんから、かいだんを{使|つか}います。","Il n'y a pas d'ascenseur, alors je prends l'escalier."),
 W("〜かい","〜かい","… étage, … niveau","トイレは{二|に}かいにあります。","Les toilettes sont au premier étage."),
 W("いす","いす","chaise","このいすはとても{古|ふる}いです。","Cette chaise est très vieille."),
 W("ベッド","ベッド","lit","{毎晩|まいばん}{十一時|じゅういちじ}にベッドに{入|はい}ります。","Je me mets au lit à onze heures tous les soirs."),
 W("れいぞうこ","れいぞうこ","réfrigérateur","ぎゅうにゅうはれいぞうこの{中|なか}にあります。","Le lait est dans le frigo."),
 W("{電気|でんき}","でんき","électricité ; lumière","{部屋|へや}の{電気|でんき}をつけてください。","Allume la lumière de la pièce, s'il te plaît."),
 W("アパート","アパート","petit immeuble, appartement","{駅|えき}の{近|ちか}くのアパートに{住|す}んでいます。","J'habite dans un appartement près de la gare."),
 W("{建物|たてもの}","たてもの","bâtiment","あの{白|しろ}い{建物|たてもの}は{病院|びょういん}です。","Ce bâtiment blanc là-bas, c'est l'hôpital."),
 W("うち","うち","chez moi, la maison","{今日|きょう}はうちで{晩|ばん}ご{飯|はん}を{食|た}べます。","Ce soir, je dîne à la maison."),
 W("{本|ほん}だな","ほんだな","étagère à livres","{本|ほん}だなにじしょがあります。","Il y a un dictionnaire sur l'étagère."),
], "sections": [
 {"h": "Compter les étages : 〜かい",
  "p": ["Au Japon, on compte à partir du sol : {一|いっ}かい = le rez-de-chaussée, {二|に}かい = notre 1er étage."],
  "grid": {"head": ["", "lecture"], "rows": [
   ["à retenir", "1 ==いっ==かい · 3 さん==がい== · 6 ==ろっ==かい · 8 ==はっ==かい · 10 ==じゅっ==かい · ? なん==がい=="],
   ["les autres", "2 にかい · 4 よんかい · 5 ごかい · 7 ななかい · 9 きゅうかい"]]}}
], "pieges": [
 "{一|いっ}かい = rez-de-chaussée ! {二|に}かい = 1er étage français.",
 "{三|さん}がい et なんがい : か devient **が**.",
 "うち = chez moi, mon foyer ; {家|いえ} = la maison (le bâtiment). うちへ{帰|かえ}ります = je rentre chez moi.",
 "{電気|でんき} = l'électricité **et** la lumière : {電気|でんき}をつける = allumer la lumière.",
 "おふろに{入|はい}る = prendre un bain ; ベッドに{入|はい}る = se mettre au lit.",
 "{台所|だいどころ} = la cuisine (la pièce). La cuisine qu'on prépare, c'est {料理|りょうり}."
], "exercises": [
 C(L,1,["{台所|だいどころ}","おふろ","かいだん","{本|ほん}だな"],jp="{母|はは}は＿で{料理|りょうり}をしています。",fr="Ma mère cuisine dans la cuisine.",uses=["v5-14","v5-21"]),
 C(L,2,["おふろ","{台所|だいどころ}","にわ","れいぞうこ"],jp="{毎晩|まいばん}＿に{入|はい}って、{体|からだ}を{洗|あら}います。",fr="Tous les soirs, je prends un bain et je me lave.",uses=["v5-14"]),
 C(L,3,["れいぞうこ","ベッド","かいだん","{窓|まど}"],jp="ぎゅうにゅうは＿の{中|なか}にあります。",fr="Le lait est dans le frigo.",uses=["v5-06","v5-20"]),
 C(L,4,["かいだん","ドア","{窓|まど}","にわ"],jp="エレベーターがありませんから、＿を{使|つか}います。",fr="Il n'y a pas d'ascenseur, alors je prends l'escalier."),
 C(L,5,["いっかい","いちかい","ひとかい","いっがい"],q="Comment dit-on « rez-de-chaussée » (1er niveau) ?"),
 C(L,6,["ろっかい","ろくかい","ろくがい","むかい"],q="Comment dit-on « 6e niveau » ?"),
 C(L,7,["le rez-de-chaussée","le premier étage","le sous-sol","le dernier étage"],q="Dans un immeuble japonais, {一|いっ}かい, c'est…"),
 C(L,8,["{電気|でんき}","{窓|まど}","ドア","いす"],jp="{夜|よる}ですから、{部屋|へや}の＿をつけます。",fr="C'est la nuit, alors j'allume la lumière de la pièce.",uses=["v5-03","v5-04"]),
 C(L,9,["{建物|たてもの}","れいぞうこ","いす","ベッド"],jp="あの{白|しろ}い＿は{病院|びょういん}です。",fr="Ce bâtiment blanc là-bas, c'est l'hôpital.",uses=["v5-04"]),
 C(L,10,["étagère à livres","librairie","bibliothèque (bâtiment)","cahier"],q="Que veut dire **{本|ほん}だな** ?"),
 C(L,11,["うち","にわ","かいだん","れいぞうこ"],jp="{今日|きょう}は{雨|あめ}ですから、＿で{本|ほん}を{読|よ}みます。",fr="Aujourd'hui il pleut, alors je lis à la maison.",uses=["v5-02","v5-03"]),
 C(L,12,["ベッド","れいぞうこ","{本|ほん}だな","かいだん"],jp="{毎晩|まいばん}{十一時|じゅういちじ}に＿に{入|はい}ります。",fr="Je me mets au lit à onze heures tous les soirs.",uses=["v5-16"]),
 C(L,13,["fenêtre","porte","mur","toit"],q="Que veut dire **{窓|まど}** ?"),
 C(L,14,["にわ","{台所|だいどころ}","おふろ","{本|ほん}だな"],jp="＿に{木|き}が{三本|さんぼん}あります。",fr="Il y a trois arbres dans le jardin.",uses=["v5-08"]),
 C(L,15,["l'électricité ou la lumière","le chauffage","le téléphone","la télévision"],q="**{電気|でんき}**, c'est…"),
 C(L,16,["Je rentre chez moi.","Je rentre au bureau.","Je vais chez un ami.","Je sors de chez moi."],q="Que veut dire : うちへ{帰|かえ}ります。",uses=["v5-02"]),
 C(L,17,["に","で","を","が"],jp="トイレは{二|に}かい＿あります。",fr="Les toilettes sont au premier étage.",uses=["v5-04","v5-20"]),
 C(L,18,["un petit immeuble d'appartements","une maison individuelle","un hôtel","un bureau"],q="Que veut dire **アパート** ?"),
 O(L,19,"La cuisine est au rez-de-chaussée.",["{台所|だいどころ}は","{一|いっ}かいに","あります"]),
 O(L,20,"Il y a du lait dans le frigo.",["れいぞうこの","{中|なか}に","ぎゅうにゅうが","あります"],alt=[["ぎゅうにゅうが","れいぞうこの","{中|なか}に","あります"]],uses=["v5-06","v5-20"]),
]}

# ---------- L23 Le corps et la santé ----------
L = "v5-23"
l23 = {"id": L, "title": "Le corps et la santé", "words": [
 W("{頭|あたま}","あたま","tête","{頭|あたま}がいたいですから、{薬|くすり}を{飲|の}みます。","J'ai mal à la tête, alors je prends un médicament."),
 W("{目|め}","め","œil, yeux","{田中|たなか}さんは{目|め}が{大|おお}きいです。","M. Tanaka a de grands yeux."),
 W("{耳|みみ}","みみ","oreille","おじいさんは{耳|みみ}が{悪|わる}いです。","Grand-père entend mal."),
 W("{口|くち}","くち","bouche","{口|くち}を{大|おお}きく{開|あ}けてください。","Ouvrez grand la bouche, s'il vous plaît."),
 W("{手|て}","て","main","{食|た}べるまえに{手|て}を{洗|あら}います。","Je me lave les mains avant de manger."),
 W("{足|あし}","あし","pied ; jambe","たくさん{歩|ある}きましたから、{足|あし}がいたいです。","J'ai beaucoup marché, alors j'ai mal aux pieds."),
 W("おなか","おなか","ventre","{朝|あさ}ご{飯|はん}を{食|た}べませんでしたから、おなかがすきました。","Je n'ai pas pris de petit-déjeuner, alors j'ai faim."),
 W("{歯|は}","は","dent","{毎晩|まいばん}{歯|は}をみがきます。","Je me brosse les dents tous les soirs."),
 W("{顔|かお}","かお","visage","{毎朝|まいあさ}{顔|かお}を{洗|あら}います。","Je me lave le visage tous les matins."),
 W("{体|からだ}","からだ","corps ; santé","{体|からだ}に{気|き}をつけてください。","Prenez soin de vous."),
 W("{声|こえ}","こえ","voix","{田中|たなか}さんは{声|こえ}が{大|おお}きいです。","M. Tanaka a une voix forte."),
 W("{病気|びょうき}","びょうき","maladie ; malade","{父|ちち}は{病気|びょうき}で{会社|かいしゃ}を{休|やす}みました。","Mon père était malade et n'est pas allé au travail."),
 W("{薬|くすり}","くすり","médicament","{食|た}べたあとで、この{薬|くすり}を{飲|の}んでください。","Prenez ce médicament après le repas."),
 W("かぜ","かぜ","rhume","かぜをひきましたから、{学校|がっこう}を{休|やす}みます。","J'ai attrapé un rhume, alors je ne vais pas à l'école."),
 W("ねつ","ねつ","fièvre","ねつがありますから、{病院|びょういん}へ{行|い}きます。","J'ai de la fièvre, alors je vais à l'hôpital."),
], "sections": [
 {"h": "Être malade : les bonnes expressions",
  "p": ["Chaque expression a **sa** particule et **son** verbe : à apprendre en bloc."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["avoir mal à…", "{頭|あたま}==が==いたい"],
   ["avoir de la fièvre", "ねつ==が==ある"],
   ["attraper un rhume", "かぜ==を==ひく"],
   ["prendre un médicament", "{薬|くすり}==を=={飲|の}む"],
   ["avoir faim", "おなか==が==すく"],
   ["mal voir / mal entendre", "{目|め}==が=={悪|わる}い · {耳|みみ}==が=={悪|わる}い"]]}}
], "pieges": [
 "On « boit » les médicaments, même les comprimés : {薬|くすり}を**{飲|の}む**.",
 "かぜを**ひく** = attraper un rhume. ねつが**ある** = avoir de la fièvre.",
 "かぜ (rhume) ≠ {風|かぜ} (vent) : même son, sens différent.",
 "{目|め}が{悪|わる}い = avoir une mauvaise vue (pas « avoir mal aux yeux » : {目|め}がいたい).",
 "{足|あし} = le pied **et** la jambe.",
 "{体|からだ}に{気|き}をつけてください = prenez soin de vous (pour finir une lettre, quitter un malade…)."
], "exercises": [
 C(L,1,["{薬|くすり}","かぜ","ねつ","{病気|びょうき}"],jp="{頭|あたま}がいたいですから、＿を{飲|の}みます。",fr="J'ai mal à la tête, alors je prends un médicament.",uses=["v5-02","v5-18"]),
 C(L,2,["ひきました","とりました","{飲|の}みました","しました"],jp="{昨日|きのう}はとても{寒|さむ}かったですから、かぜを＿。",fr="Hier il faisait très froid, alors j'ai attrapé un rhume.",explain="かぜを**ひく**."),
 C(L,3,["ねつ","かぜ","{薬|くすり}","{体|からだ}"],jp="＿がありますから、{今日|きょう}は{学校|がっこう}を{休|やす}みます。",fr="J'ai de la fièvre, alors aujourd'hui je ne vais pas à l'école.",uses=["v5-14"],explain="ねつが**ある**. Le rhume, lui, s'« attrape » : かぜをひく."),
 C(L,4,["{手|て}","{耳|みみ}","{声|こえ}","{病気|びょうき}"],jp="{食|た}べるまえに＿を{洗|あら}います。",fr="Je me lave les mains avant de manger.",uses=["v5-14"]),
 C(L,5,["{耳|みみ}","{目|め}","{口|くち}","{足|あし}"],jp="{大|おお}きい{声|こえ}で{話|はな}してください。おじいさんは＿が{悪|わる}いですから。",fr="Parlez fort, s'il vous plaît : grand-père entend mal.",uses=["v5-21"]),
 C(L,6,["{目|め}","{耳|みみ}","{歯|は}","{足|あし}"],jp="＿が{悪|わる}いですから、めがねをかけています。",fr="J'ai une mauvaise vue, alors je porte des lunettes.",uses=["v5-12","v5-13"]),
 C(L,7,["{足|あし}","{耳|みみ}","{歯|は}","{声|こえ}"],jp="{三時間|さんじかん}{歩|ある}きましたから、＿がいたいです。",fr="J'ai marché trois heures, alors j'ai mal aux pieds.",uses=["v5-15","v5-18"]),
 C(L,8,["{顔|かお}","{声|こえ}","{病気|びょうき}","ねつ"],jp="{毎朝|まいあさ}＿を{洗|あら}って、{歯|は}をみがきます。",fr="Tous les matins, je me lave le visage et je me brosse les dents.",uses=["v5-14"]),
 C(L,9,["からだ","てい","かだら","からた"],q=LECT+"**体** (le corps) ?"),
 C(L,10,["かお","かう","がお","こう"],q=LECT+"**顔** (le visage) ?"),
 C(L,11,["おなかがすきました","おなかがいたいです","おなかがあります","おなかをすきました"],q="Comment dit-on « j'ai faim » ?"),
 C(L,12,["Prenez soin de vous.","Faites du sport.","Vous avez l'air en forme.","Allez à l'hôpital."],q="Que veut dire : {体|からだ}に{気|き}をつけてください。"),
 C(L,13,["{薬|くすり}を{飲|の}む","{薬|くすり}を{食|た}べる","{薬|くすり}をとる","{薬|くすり}をする"],q="Comment dit-on « prendre un médicament » ?"),
 C(L,14,["{病気|びょうき}","{薬|くすり}","{体|からだ}","{声|こえ}"],jp="{父|ちち}は＿で{会社|かいしゃ}を{休|やす}みました。",fr="Mon père était malade et n'est pas allé au travail.",uses=["v5-14","v5-21"]),
 C(L,15,["un rhume","le vent","la fièvre","une blessure"],q="Dans « {昨日|きのう}、かぜをひきました », かぜ veut dire…"),
 C(L,16,["{口|くち}","{耳|みみ}","{足|あし}","{声|こえ}"],jp="{歯|は}を{見|み}ますから、＿を{大|おお}きく{開|あ}けてください。",fr="Je vais regarder vos dents, alors ouvrez grand la bouche, s'il vous plaît."),
 C(L,17,["ねつがあります","ねつがいます","ねつをします","ねつがいたいです"],q="Comment dit-on « j'ai de la fièvre » ?"),
 C(L,18,["la voix","le cou","le souffle","la gorge"],q="Que veut dire **{声|こえ}** ?"),
 O(L,19,"J'ai mal à la tête, alors je prends un médicament.",["{頭|あたま}が","いたいですから、","{薬|くすり}を","{飲|の}みます"],uses=["v5-18"]),
 O(L,20,"Je me lave les mains avant de manger.",["{食|た}べるまえに","{手|て}を","{洗|あら}います"],uses=["v5-14"]),
]}

# ---------- L24 Couleurs et sensations ----------
L = "v5-24"
l24 = {"id": L, "title": "Couleurs et sensations", "words": [
 W("{赤|あか}い","あかい","rouge","{赤|あか}いセーターを{買|か}いました。","J'ai acheté un pull rouge."),
 W("{青|あお}い","あおい","bleu","{今日|きょう}は{空|そら}が{青|あお}いです。","Aujourd'hui, le ciel est bleu."),
 W("{白|しろ}い","しろい","blanc","{白|しろ}いシャツを{着|き}ています。","Je porte une chemise blanche."),
 W("{黒|くろ}い","くろい","noir","{黒|くろ}いくつをはきます。","Je mets des chaussures noires."),
 W("きいろい","きいろい","jaune","きいろいかさを{持|も}っています。","J'ai un parapluie jaune."),
 W("{茶色|ちゃいろ}","ちゃいろ","marron","{茶色|ちゃいろ}のかばんを{買|か}いました。","J'ai acheté un sac marron."),
 W("{色|いろ}","いろ","couleur","どんな{色|いろ}が{好|す}きですか。","Quelle couleur aimes-tu ?"),
 W("{明|あか}るい","あかるい","clair, lumineux","この{部屋|へや}は{窓|まど}が{大|おお}きくて、{明|あか}るいです。","Cette pièce a de grandes fenêtres, elle est lumineuse."),
 W("{暗|くら}い","くらい","sombre","{冬|ふゆ}は{五時|ごじ}ごろ{暗|くら}くなります。","En hiver, il fait nuit vers cinq heures."),
 W("{重|おも}い","おもい","lourd","このかばんはとても{重|おも}いです。","Ce sac est très lourd."),
 W("{軽|かる}い","かるい","léger","この{自転車|じてんしゃ}は{軽|かる}いです。","Ce vélo est léger."),
 W("{広|ひろ}い","ひろい","spacieux, large","{新|あたら}しい{部屋|へや}は{広|ひろ}いです。","Ma nouvelle chambre est spacieuse."),
 W("せまい","せまい","étroit, exigu","この{道|みち}はせまいですから、{車|くるま}に{気|き}をつけてください。","Cette rue est étroite, alors faites attention aux voitures."),
 W("つめたい","つめたい","froid (au toucher)","つめたいビールはおいしいです。","La bière fraîche, c'est bon."),
 W("うるさい","うるさい","bruyant","となりの{部屋|へや}がうるさいです。","La chambre d'à côté est bruyante."),
], "sections": [
 {"h": "Les couleurs : adjectif ou nom ?",
  "p": ["Les couleurs de base sont des adjectifs en い ({赤|あか}いかさ) qui ont aussi une forme nom ({赤|あか}が{好|す}き). {茶色|ちゃいろ} et みどり (vert) ne sont **que** des noms : {茶色|ちゃいろ}**の**かばん."],
  "grid": {"head": ["", "adjectif → nom"], "rows": [
   ["rouge", "{赤|あか}==い== → {赤|あか}"],
   ["bleu", "{青|あお}==い== → {青|あお}"],
   ["blanc", "{白|しろ}==い== → {白|しろ}"],
   ["noir", "{黒|くろ}==い== → {黒|くろ}"],
   ["jaune", "きいろ==い== → きいろ"],
   ["marron, vert", "nom seulement : {茶色|ちゃいろ}==の==, みどり==の=="]]}}
], "pieges": [
 "{茶色|ちゃいろ}**の**かばん, jamais {茶色|ちゃいろ}いかばん : {茶色|ちゃいろ} est un nom.",
 "{青|あお}い = bleu, mais le feu « vert » et les légumes verts se disent aussi {青|あお}.",
 "つめたい = froid **au toucher** (eau, boisson, main) ; {寒|さむ}い = il fait froid (l'air, le temps).",
 "{広|ひろ}い / せまい parlent de **surface** (pièce, rue). Pour la taille d'un objet : {大|おお}きい / {小|ちい}さい.",
 "{明|あか}るい (あかるい, lumineux) ≠ {赤|あか}い (あかい, rouge).",
 "{暗|くら}くなる = il commence à faire nuit."
], "exercises": [
 C(L,1,["{軽|かる}い","{低|ひく}い","せまい","{暗|くら}い"],q="Contraire de **{重|おも}い** ?"),
 C(L,2,["{暗|くら}い","{黒|くろ}い","{軽|かる}い","せまい"],q="Contraire de **{明|あか}るい** ?"),
 C(L,3,["せまい","{短|みじか}い","{低|ひく}い","{軽|かる}い"],q="Contraire de **{広|ひろ}い** (une pièce) ?",uses=["v5-05"]),
 C(L,4,["{青|あお}い","{黒|くろ}い","{重|おも}い","せまい"],jp="{空|そら}が＿です。いい{天気|てんき}ですね。",fr="Le ciel est bleu. Il fait beau, hein."),
 C(L,5,["{重|おも}い","{軽|かる}い","{明|あか}るい","つめたい"],jp="かばんに{本|ほん}がたくさん{入|はい}っていますから、とても＿です。",fr="Il y a beaucoup de livres dans le sac, alors il est très lourd.",uses=["v5-12"]),
 C(L,6,["{暗|くら}い","{明|あか}るい","うるさい","{重|おも}い"],jp="{部屋|へや}が＿ですから、{電気|でんき}をつけます。",fr="La pièce est sombre, alors j'allume la lumière.",uses=["v5-22"]),
 C(L,7,["つめたい","うるさい","せまい","{暗|くら}い"],jp="{暑|あつ}い{日|ひ}は、＿{水|みず}がおいしいです。",fr="Les jours de chaleur, l'eau fraîche est délicieuse.",uses=["v5-06"]),
 C(L,8,["{茶色|ちゃいろ}の","{茶色|ちゃいろ}い","{茶色|ちゃいろ}な","{茶色|ちゃいろ}"],jp="＿かばんを{買|か}いました。",fr="J'ai acheté un sac marron.",explain="{茶色|ちゃいろ} est un nom : {茶色|ちゃいろ}**の**かばん."),
 C(L,9,["{赤|あか}い","{赤|あか}な","{赤|あか}いの","{赤|あか}く"],jp="＿セーターを{着|き}ています。",fr="Je porte un pull rouge.",uses=["v5-13"]),
 C(L,10,["あかるい","あきるい","めいるい","あけるい"],q=LECT+"**明るい** ?"),
 C(L,11,["くろい","くらい","こくい","しろい"],q=LECT+"**黒い** ?",explain="くろい = noir ; くらい ({暗|くら}い) = sombre."),
 C(L,12,["うるさい","{静|しず}か","{明|あか}るい","{広|ひろ}い"],jp="となりの{部屋|へや}が＿ですから、{勉強|べんきょう}ができません。",fr="La pièce d'à côté est bruyante, alors je n'arrive pas à étudier.",uses=["v5-14","v5-19"]),
 C(L,13,["せまい","{広|ひろ}い","{明|あか}るい","うるさい"],jp="＿{部屋|へや}ですから、ベッドが{入|はい}りません。",fr="La pièce est trop petite, alors le lit n'y rentre pas.",uses=["v5-22"]),
 C(L,14,["couleur","forme","taille","goût"],q="Que veut dire **{色|いろ}** ?"),
 C(L,15,["きいろい","{茶色|ちゃいろ}","{青|あお}い","{白|しろ}い"],q="Comment dit-on « jaune » ?"),
 C(L,16,["{白|しろ}い","{黒|くろ}い","{赤|あか}い","{青|あお}い"],jp="ぎゅうにゅうは＿です。",fr="Le lait est blanc.",uses=["v5-06"]),
 C(L,17,["{水|みず}がつめたいです。","{水|みず}が{寒|さむ}いです。","{水|みず}がつめたです。","{水|みず}が{寒|さむ}です。"],q="« L'eau est froide » se dit…",explain="Au toucher : つめたい. {寒|さむ}い, c'est pour l'air et le temps."),
 O(L,18,"J'ai acheté un pull rouge.",["{赤|あか}い","セーターを","{買|か}いました"],uses=["v5-13"]),
 O(L,19,"Cette pièce est spacieuse et lumineuse.",["この","{部屋|へや}は","{広|ひろ}くて","{明|あか}るいです"],explain="Pour relier deux adjectifs en い : い → くて."),
]}

# ---------- L25 Météo et saisons ----------
L = "v5-25"
l25 = {"id": L, "title": "Météo et saisons", "words": [
 W("{天気|てんき}","てんき","temps (météo)","{明日|あした}の{天気|てんき}はどうですか。","Quel temps fera-t-il demain ?"),
 W("{雨|あめ}","あめ","pluie","{雨|あめ}ですから、かさを{持|も}って{行|い}きます。","Il pleut, alors j'emporte un parapluie."),
 W("ゆき","ゆき","neige","{冬|ふゆ}は{山|やま}にゆきがたくさん{降|ふ}ります。","En hiver, il neige beaucoup sur les montagnes."),
 W("{風|かぜ}","かぜ","vent","{風|かぜ}がつめたいですから、コートを{着|き}ます。","Le vent est froid, alors je mets mon manteau."),
 W("{春|はる}","はる","printemps","{日本|にほん}の{学校|がっこう}は{春|はる}に{始|はじ}まります。","Au Japon, l'école commence au printemps."),
 W("{夏|なつ}","なつ","été","{夏|なつ}は{海|うみ}へ{行|い}きます。","En été, je vais à la mer."),
 W("{秋|あき}","あき","automne","{秋|あき}は{果物|くだもの}がおいしいです。","En automne, les fruits sont bons."),
 W("{冬|ふゆ}","ふゆ","hiver","{冬|ふゆ}はとても{寒|さむ}いです。","L'hiver est très froid."),
 W("{暑|あつ}い","あつい","chaud (temps)","{今日|きょう}は{暑|あつ}いですね。","Il fait chaud aujourd'hui, hein."),
 W("{寒|さむ}い","さむい","froid (temps)","{寒|さむ}いですから、{窓|まど}をしめてください。","Il fait froid, alors ferme la fenêtre, s'il te plaît."),
 W("あたたかい","あたたかい","doux, tiède","{春|はる}はあたたかいです。","Le printemps est doux."),
 W("すずしい","すずしい","frais (agréable)","{夕方|ゆうがた}はすずしいですね。","En fin d'après-midi, il fait frais, hein."),
 W("{降|ふ}る","ふる","tomber (pluie, neige)","{昨日|きのう}は{雨|あめ}がたくさん{降|ふ}りました。","Hier, il a beaucoup plu."),
 W("{晴|は}れ","はれ","beau temps","{明日|あした}は{晴|は}れです。","Demain, il fera beau."),
 W("くもり","くもり","temps nuageux","{今日|きょう}はくもりですが、{雨|あめ}は{降|ふ}りません。","Aujourd'hui c'est nuageux, mais il ne pleut pas."),
], "sections": [
 {"h": "Saisons et températures",
  "p": ["Pluie et neige « tombent » : {雨|あめ}が{降|ふ}る, ゆきが{降|ふ}る. Le temps qu'il fait : {晴|は}れ, くもり, {雨|あめ} (des noms)."],
  "grid": {"head": ["", "typique"], "rows": [
   ["{春|はる} printemps", "あたたかい (doux)"],
   ["{夏|なつ} été", "{暑|あつ}い (chaud)"],
   ["{秋|あき} automne", "すずしい (frais, agréable)"],
   ["{冬|ふゆ} hiver", "{寒|さむ}い (froid), ゆき"]]}}
], "pieges": [
 "{暑|あつ}い = il fait chaud (le temps) ; あつい (écrit avec un autre kanji) = chaud au toucher (thé, bain). Leurs contraires : {寒|さむ}い / つめたい.",
 "Il pleut = {雨|あめ}が**{降|ふ}る** (jamais {雨|あめ}がある). Il neige = ゆきが{降|ふ}る.",
 "{降|ふ}る (ふる, tomber, groupe 1) ≠ {降|お}りる (おりる, descendre, groupe 2).",
 "{風|かぜ} (vent) ≠ かぜ (rhume).",
 "すずしい = frais **et agréable**. Pas « froid » !",
 "いい{天気|てんき}ですね : la petite phrase de politesse par excellence."
], "exercises": [
 C(L,1,["{暑|あつ}い","{寒|さむ}い","つめたい","{暗|くら}い"],jp="{夏|なつ}は＿ですから、{海|うみ}へ{行|い}きます。",fr="En été il fait chaud, alors je vais à la mer.",uses=["v5-24"]),
 C(L,2,["{降|ふ}っています","あります","{来|き}ています","しています"],jp="{雨|あめ}が＿から、かさを{持|も}って{行|い}きます。",fr="Il pleut, alors j'emporte un parapluie.",uses=["v5-12"],explain="Il pleut : {雨|あめ}が{降|ふ}る."),
 C(L,3,["ゆき","{風|かぜ}","{晴|は}れ","くもり"],jp="{冬|ふゆ}は{山|やま}に＿が{降|ふ}ります。",fr="En hiver, il neige sur les montagnes."),
 C(L,4,["{寒|さむ}い","つめたい","{軽|かる}い","{低|ひく}い"],q="Contraire de **{暑|あつ}い** (le temps qu'il fait) ?",uses=["v5-24"],explain="つめたい est le contraire de あつい « chaud au toucher » (une boisson…)."),
 C(L,5,["{秋|あき}","{春|はる}","{夏|なつ}","{冬|ふゆ}"],jp="{春|はる}、{夏|なつ}、＿、{冬|ふゆ}",fr="Printemps, été, automne, hiver."),
 C(L,6,["あき","あさ","はる","ふゆ"],q=LECT+"**秋** (automne) ?"),
 C(L,7,["ふゆ","ほゆ","ふゆう","ふよ"],q=LECT+"**冬** (hiver) ?"),
 C(L,8,["{天気|てんき}","{風|かぜ}","{雨|あめ}","{夏|なつ}"],jp="{明日|あした}の＿はどうですか。— {晴|は}れです。",fr="Quel temps fera-t-il demain ? — Il fera beau.",uses=["v5-09"]),
 C(L,9,["nuageux","ensoleillé","pluvieux","neigeux"],q="Que veut dire **くもり** ?"),
 C(L,10,["{風|かぜ}","{晴|は}れ","くもり","{夏|なつ}"],jp="{今日|きょう}は＿が{強|つよ}くて、{寒|さむ}いです。",fr="Aujourd'hui, le vent est fort et il fait froid.",uses=["v5-18"]),
 C(L,11,["あたたかい","つめたい","せまい","{重|おも}い"],jp="{春|はる}は＿です。",fr="Le printemps est doux.",uses=["v5-24"]),
 C(L,12,["frais (et agréable)","glacial","humide","étouffant"],q="Que veut dire **すずしい** ?"),
 C(L,13,["このお{茶|ちゃ}はあついです。","このお{茶|ちゃ}は{暑|あつ}いです。","このお{茶|ちゃ}はあたたかです。","このお{茶|ちゃ}はつめたいです。"],q="« Ce thé est chaud » se dit…",uses=["v5-06"],explain="Chaud au toucher : あつい (autre kanji). {暑|あつ}い, c'est pour le temps."),
 C(L,14,["{晴|は}れ","{雨|あめ}","{風|かぜ}","かぜ"],jp="{明日|あした}は＿ですから、{公園|こうえん}へ{行|い}きましょう。",fr="Demain il fera beau, alors allons au parc.",uses=["v5-04"]),
 C(L,15,["Il neige.","Il pleut.","Il grêle.","Il y a du vent."],q="Que veut dire : ゆきが{降|ふ}ります。"),
 C(L,16,["Il fait beau, hein.","Quel temps fera-t-il ?","Il va pleuvoir.","Il fait froid, hein."],q="Ton voisin te dit : いい{天気|てんき}ですね. Que veut-il dire ?",uses=["v5-05"]),
 C(L,17,["{降|ふ}りました","{降|ふ}ります","{降|ふ}って","{降|ふ}るでした"],jp="{昨日|きのう}は{雨|あめ}がたくさん＿。",fr="Hier, il a beaucoup plu.",uses=["v5-03"]),
 C(L,18,["{冬|ふゆ}","{夏|なつ}","{晴|は}れ","{天気|てんき}"],jp="＿はゆきが{降|ふ}って、とても{寒|さむ}いです。",fr="En hiver, il neige et il fait très froid."),
 O(L,19,"Demain, il va neiger.",["{明日|あした}は","ゆきが","{降|ふ}ります"],uses=["v5-03"]),
 O(L,20,"L'été japonais est chaud.",["{日本|にほん}の","{夏|なつ}は","{暑|あつ}いです"]),
]}

TC, TO, XC, XO = make_block("v5-b05")
test = [
 TC(1,["お{母|かあ}さん","{母|はは}","{父|ちち}","{姉|あね}"],jp="{田中|たなか}さんの＿は{何|なん}さいですか。",fr="Quel âge a la mère de M. Tanaka ?",uses=["v5-21"]),
 TC(2,["あります","います","です","します"],jp="{頭|あたま}がいたくて、ねつも＿。",fr="J'ai mal à la tête, et j'ai aussi de la fièvre.",uses=["v5-23"]),
 TC(3,["{暗|くら}い","{明|あか}るい","{広|ひろ}い","{重|おも}い"],jp="{部屋|へや}が＿ですから、{電気|でんき}をつけます。",fr="La pièce est sombre, alors j'allume la lumière.",uses=["v5-22","v5-24"]),
 TC(4,["{降|ふ}ります","あります","{来|き}ます","します"],jp="{冬|ふゆ}は{北海道|ほっかいどう}でゆきがたくさん＿。",fr="En hiver, il neige beaucoup à Hokkaidō.",uses=["v5-25"]),
 TC(5,["いもうと","おとうと","あね","いもと"],q=LECT+"**妹** ?",uses=["v5-21"]),
 TC(6,["ひいて","とって","して","{飲|の}んで"],jp="かぜを＿、{学校|がっこう}を{休|やす}みました。",fr="J'ai attrapé un rhume et je ne suis pas allé à l'école.",uses=["v5-14","v5-23"]),
 TC(7,["{台所|だいどころ}","おふろ","かいだん","ベッド"],jp="{母|はは}は＿で{晩|ばん}ご{飯|はん}を{作|つく}っています。",fr="Ma mère prépare le dîner dans la cuisine.",uses=["v5-06","v5-22"]),
 TC(8,["{茶色|ちゃいろ}のくつをはいています。","{茶色|ちゃいろ}いくつをはいています。","{茶色|ちゃいろ}のくつを{着|き}ています。","{茶色|ちゃいろ}なくつをはいています。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-13","v5-24"]),
 TC(9,["すずしい","{暑|あつ}い","つめたい","{重|おも}い"],jp="{夏|なつ}は{暑|あつ}いですが、{秋|あき}は＿です。",fr="L'été est chaud, mais l'automne est frais.",uses=["v5-25"]),
 TC(10,["le rez-de-chaussée","le premier étage","le sous-sol","le dernier étage"],q="Dans un immeuble japonais, {一|いっ}かい, c'est…",uses=["v5-22"]),
 TC(11,["{体|からだ}に{気|き}をつけてください。","いただきます。","いってきます。","はじめまして。"],q="Ton ami est malade. En le quittant, tu lui dis :",uses=["v5-11","v5-23"]),
 TC(12,["めがね","ぼうし","くつ","コート"],jp="{目|め}が{悪|わる}いですから、＿をかけています。",fr="J'ai une mauvaise vue, alors je porte des lunettes.",uses=["v5-12","v5-13","v5-23"]),
 TC(13,["うるさい","{静|しず}か","{広|ひろ}い","{軽|かる}い"],jp="{外|そと}が＿ですから、{窓|まど}をしめます。",fr="C'est bruyant dehors, alors je ferme la fenêtre.",uses=["v5-20","v5-22","v5-24"]),
 TO(14,"Mes parents habitent en France.",["りょうしんは","フランスに","{住|す}んでいます"],uses=["v5-21"]),
 TC(15,["あたたかい","つめたい","すずしい","{暑|あつ}い"],jp="{今日|きょう}は{寒|さむ}いですから、＿{飲|の}み{物|もの}がほしいです。",fr="Il fait froid aujourd'hui, alors j'ai envie d'une boisson chaude.",uses=["v5-06","v5-25"],explain="Une boisson chaude : あたたかい (ou あつい, au toucher). {暑|あつ}い ne se dit que du temps."),
 TC(16,["お{兄|にい}さん","{兄|あに}","{弟|おとうと}","{兄弟|きょうだい}"],q="Tu parles du grand frère de ton ami.",jp="{田中|たなか}さんの＿はお{元気|げんき}ですか。",fr="Le grand frère de M. Tanaka va bien ?",uses=["v5-21"]),
]
bloc = {"id": "v5-b05", "level": "N5", "title": "Chez soi : famille, maison, corps, couleurs, météo",
        "lessons": [l21, l22, l23, l24, l25], "test": test}
save(bloc, sys.argv[1])
