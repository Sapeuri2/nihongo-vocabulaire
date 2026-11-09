import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save

# ---------- L26 Donner, prêter, rendre ----------
L = "v5-26"
l26 = {"id": L, "title": "Donner, prêter, rendre", "words": [
 W("あげる","あげる","donner (à quelqu'un d'autre)","{友|とも}だちにプレゼントをあげました。","J'ai offert un cadeau à un ami."),
 W("もらう","もらう","recevoir","{父|ちち}に{時計|とけい}をもらいました。","Mon père m'a donné une montre (j'ai reçu de mon père)."),
 W("くれる","くれる","donner (à moi)","{姉|あね}がかばんをくれました。","Ma grande sœur m'a donné un sac."),
 W("{貸|か}す","かす","prêter","{友|とも}だちにかさを{貸|か}しました。","J'ai prêté mon parapluie à un ami."),
 W("{借|か}りる","かりる","emprunter","{図書館|としょかん}で{本|ほん}を{借|か}ります。","J'emprunte des livres à la bibliothèque."),
 W("かえす","かえす","rendre","{明日|あした}、{図書館|としょかん}に{本|ほん}をかえします。","Demain, je rends les livres à la bibliothèque."),
 W("{見|み}せる","みせる","montrer","{旅行|りょこう}の{写真|しゃしん}を{見|み}せてください。","Montre-moi les photos du voyage, s'il te plaît."),
 W("{持|も}つ","もつ","tenir, porter ; avoir sur soi","かさを{持|も}っていますか。","Tu as un parapluie (sur toi) ?"),
 W("{送|おく}る","おくる","envoyer","{国|くに}の{母|はは}に{手紙|てがみ}を{送|おく}りました。","J'ai envoyé une lettre à ma mère, dans mon pays."),
 W("{売|う}る","うる","vendre","あの{店|みせ}は{古|ふる}い{本|ほん}を{売|う}っています。","Ce magasin vend des livres d'occasion."),
 W("とる","とる","prendre ; passer (un objet)","その{新聞|しんぶん}をとってください。","Passe-moi ce journal, s'il te plaît."),
 W("わたす","わたす","remettre (en main propre)","この{手紙|てがみ}を{田中|たなか}さんにわたしてください。","Remettez cette lettre à M. Tanaka, s'il vous plaît."),
 W("{出|だ}す","だす","sortir (un objet) ; poster","{駅|えき}の{前|まえ}で{手紙|てがみ}を{出|だ}しました。","J'ai posté une lettre devant la gare."),
 W("プレゼント","プレゼント","cadeau","たんじょうびにプレゼントをもらいました。","J'ai reçu un cadeau pour mon anniversaire."),
 W("おみやげ","おみやげ","souvenir (rapporté pour offrir)","{京都|きょうと}のおみやげを{買|か}いました。","J'ai acheté des souvenirs de Kyoto."),
], "sections": [
 {"h": "Qui donne à qui ?",
  "p": ["Trois verbes pour « donner », selon la direction. Le donneur ou le receveur est toujours marqué par **に**."],
  "grid": {"head": ["", "direction"], "rows": [
   ["あげる", "moi (ou quelqu'un) → **un autre** : {友|とも}だち==に==あげる"],
   ["くれる", "quelqu'un → **moi** : {友|とも}だち==が==くれる"],
   ["もらう", "je reçois **de** quelqu'un : {友|とも}だち==に==もらう"],
   ["{貸|か}す ↔ {借|か}りる", "prêter ↔ emprunter : {友|とも}だち==に=={貸|か}す / {友|とも}だち==に=={借|か}りる"]]}}
], "pieges": [
 "あげる va vers les autres ; くれる vient **vers moi**. {友|とも}だちが{私|わたし}にあげました ✗ → {友|とも}だちが**くれました**.",
 "もらう : le receveur est le sujet ; celui qui donne prend **に** (ou から) : {父|ちち}に（から）もらう.",
 "{貸|か}す = prêter, {借|か}りる = emprunter. L'autre personne prend に dans les deux cas !",
 "{借|か}りる est du groupe 2 ({借|か}ります, {借|か}りて) ; {貸|か}す du groupe 1 ({貸|か}します, {貸|か}して).",
 "{持|も}っています = avoir sur soi, posséder. Attention : {持|も}つ (もつ) ≠ {待|ま}つ (まつ, attendre).",
 "{出|だ}す (sortir **quelque chose**, poster) ≠ {出|で}る (sortir **soi-même**).",
 "おみやげ = le petit cadeau qu'on rapporte d'un voyage pour ses proches ou ses collègues."
], "exercises": [
 C(L,1,["あげます","もらいます","くれます","{借|か}ります"],jp="{明日|あした}は{友|とも}だちのたんじょうびですから、プレゼントを＿。",fr="Demain c'est l'anniversaire de mon ami, alors je lui offre un cadeau.",uses=["v5-17"]),
 C(L,2,["くれました","あげました","もらいました"],jp="{姉|あね}が{私|わたし}にかばんを＿。",fr="Ma grande sœur m'a donné un sac.",uses=["v5-21"],explain="Quelqu'un me donne quelque chose : くれる."),
 C(L,3,["もらいました","あげました","くれました","{貸|か}しました"],jp="たんじょうびに、{父|ちち}から{時計|とけい}を＿。",fr="Pour mon anniversaire, mon père m'a offert une montre.",uses=["v5-12","v5-17"],explain="から marque celui qui donne : je **reçois** de mon père → もらう."),
 C(L,4,["{借|か}りました","{貸|か}しました","{売|う}りました","くれました"],jp="{図書館|としょかん}で{本|ほん}を{三|さん}さつ＿。{来週|らいしゅう}かえします。",fr="J'ai emprunté trois livres à la bibliothèque. Je les rends la semaine prochaine.",uses=["v5-04","v5-08"]),
 C(L,5,["{貸|か}しました","{借|か}りました","もらいました","くれました"],jp="{友|とも}だちがかさを{持|も}っていませんでしたから、{私|わたし}のかさを＿。",fr="Mon ami n'avait pas de parapluie, alors je lui ai prêté le mien.",uses=["v5-12"]),
 C(L,6,["かえします","くれます","{借|か}ります","{見|み}せます"],jp="{明日|あした}、{図書館|としょかん}に{本|ほん}を＿。",fr="Demain, je rends les livres à la bibliothèque."),
 C(L,7,["{見|み}せて","{見|み}て","{借|か}りて","もらって"],jp="{田中|たなか}さん、{旅行|りょこう}の{写真|しゃしん}を＿ください。{私|わたし}も{見|み}たいです。",fr="Monsieur Tanaka, montrez-moi les photos du voyage. Je veux les voir, moi aussi.",uses=["v5-12"]),
 C(L,8,["{持|も}って","{待|ま}って","{見|み}せて","{貸|か}して"],jp="かさを＿いますか。— いいえ、{持|も}っていません。",fr="Tu as un parapluie sur toi ? — Non, je n'en ai pas.",uses=["v5-12"],explain="{持|も}つ (tenir, avoir sur soi) ≠ {待|ま}つ (attendre)."),
 C(L,9,["{送|おく}りました","{売|う}りました","{借|か}りました","とりました"],jp="{国|くに}の{母|はは}に{手紙|てがみ}を＿。",fr="J'ai envoyé une lettre à ma mère, dans mon pays.",uses=["v5-04","v5-12"]),
 C(L,10,["{売|う}って","{借|か}りて","かえして","くれて"],jp="あの{店|みせ}は{古|ふる}い{本|ほん}を＿います。",fr="Ce magasin vend des livres d'occasion.",uses=["v5-04","v5-05"]),
 C(L,11,["Passe-moi ce journal, s'il te plaît.","Achète ce journal, s'il te plaît.","Lis ce journal, s'il te plaît.","Rends ce journal, s'il te plaît."],q="Que veut dire : その{新聞|しんぶん}をとってください。",uses=["v5-12"]),
 C(L,12,["remettre (en main propre)","envoyer par la poste","vendre","rendre"],q="Que veut dire **わたす** ?"),
 C(L,13,["{出|だ}しました","{出|で}ました","{出|で}かけました","{借|か}りました"],jp="{駅|えき}の{前|まえ}で{手紙|てがみ}を＿。",fr="J'ai posté une lettre devant la gare.",uses=["v5-14"],explain="Sortir **quelque chose** (ou poster une lettre) : {出|だ}す. {出|で}る = sortir soi-même."),
 C(L,14,["おみやげ","{手紙|てがみ}","ねつ","かぜ"],jp="{京都|きょうと}で{家族|かぞく}に＿を{買|か}いました。",fr="À Kyoto, j'ai acheté des souvenirs pour ma famille.",uses=["v5-21"]),
 C(L,15,["{田中|たなか}さんが{本|ほん}をくれました。","{田中|たなか}さんが{私|わたし}に{本|ほん}をあげました。","{私|わたし}は{田中|たなか}さんに{本|ほん}をくれました。","{田中|たなか}さんに{本|ほん}をくれました。"],q="Une seule de ces phrases est correcte. Laquelle ?",explain="Vers moi : くれる, avec le donneur marqué par が. Vers les autres : あげる."),
 C(L,16,["{借|か}ります","{借|か}りります","{借|か}るます","{借|か}らます"],q="Forme ます de **{借|か}りる** ?",uses=["v5-02"],explain="{借|か}りる est du groupe 2 : る → ます."),
 C(L,17,["{貸|か}して","{貸|か}って","{貸|か}いて","{貸|か}すて"],q="Forme て de **{貸|か}す** ?",uses=["v5-02"],explain="す → して."),
 C(L,18,["Tu as de l'argent sur toi ?","Tu attends de l'argent ?","Tu prêtes de l'argent ?","Tu as reçu de l'argent ?"],q="Que veut dire : お{金|かね}を{持|も}っていますか。",uses=["v5-07"]),
 O(L,19,"J'ai offert un souvenir à ma mère.",["{母|はは}に","おみやげを","あげました"],alt=[["おみやげを","{母|はは}に","あげました"]],uses=["v5-21"]),
 O(L,20,"Montre-moi cet appareil photo, s'il te plaît.",["その","カメラを","{見|み}せて","ください"],uses=["v5-12"]),
]}

# ---------- L27 Ouvrir, allumer, utiliser ----------
L = "v5-27"
l27 = {"id": L, "title": "Ouvrir, allumer, utiliser", "words": [
 W("{開|あ}ける","あける","ouvrir (quelque chose)","{窓|まど}を{開|あ}けてもいいですか。","Je peux ouvrir la fenêtre ?"),
 W("{開|あ}く","あく","s'ouvrir, ouvrir (ça ouvre)","{銀行|ぎんこう}は{九時|くじ}に{開|あ}きます。","La banque ouvre à neuf heures."),
 W("しめる","しめる","fermer (quelque chose)","{寒|さむ}いですから、ドアをしめてください。","Il fait froid, alors ferme la porte, s'il te plaît."),
 W("しまる","しまる","se fermer, fermer (ça ferme)","{店|みせ}は{八時|はちじ}にしまります。","Le magasin ferme à huit heures."),
 W("つける","つける","allumer","テレビをつけて、ニュースを{見|み}ます。","J'allume la télé et je regarde les informations."),
 W("{消|け}す","けす","éteindre ; effacer","ねるまえに{電気|でんき}を{消|け}します。","J'éteins la lumière avant de dormir."),
 W("{使|つか}う","つかう","utiliser","このペンを{使|つか}ってもいいですか。","Je peux utiliser ce stylo ?"),
 W("{作|つく}る","つくる","faire, fabriquer ; préparer","{母|はは}はケーキを{作|つく}りました。","Ma mère a fait un gâteau."),
 W("おく","おく","poser, mettre","かぎはつくえの{上|うえ}においてください。","Pose la clé sur le bureau, s'il te plaît."),
 W("{入|い}れる","いれる","mettre dedans","コーヒーにさとうを{入|い}れますか。","Tu mets du sucre dans ton café ?"),
 W("{切|き}る","きる","couper","ナイフで{肉|にく}を{切|き}ります。","Je coupe la viande avec un couteau."),
 W("おす","おす","pousser ; appuyer","このボタンをおしてください。","Appuyez sur ce bouton, s'il vous plaît."),
 W("{引|ひ}く","ひく","tirer","このドアは{引|ひ}いて{開|あ}けます。","Cette porte s'ouvre en tirant."),
 W("ならべる","ならべる","aligner, disposer","テーブルにおさらをならべます。","Je dispose les assiettes sur la table."),
], "sections": [
 {"h": "Je fais (を) / ça se fait (が)",
  "p": ["Beaucoup de verbes vont par paire : l'un dit qu'on **fait** l'action sur quelque chose (を), l'autre que la chose **change d'elle-même** (が)."],
  "grid": {"head": ["", "を〜 ↔ が〜"], "rows": [
   ["ouvrir", "ドア==を=={開|あ}ける ↔ ドア==が=={開|あ}く"],
   ["fermer", "ドア==を==しめる ↔ ドア==が==しまる"],
   ["mettre / entrer", "{水|みず}==を=={入|い}れる ↔ {部屋|へや}==に=={入|はい}る"],
   ["sortir", "{手紙|てがみ}==を=={出|だ}す ↔ {部屋|へや}==を=={出|で}る"]]}}
], "pieges": [
 "{開|あ}ける / しめる : quelqu'un ouvre / ferme quelque chose (を). {開|あ}く / しまる : ça s'ouvre / ça ferme (が) : {店|みせ}**が**{開|あ}く.",
 "{入|い}れる (いれる, mettre dedans) ≠ {入|はい}る (はいる, entrer) : même kanji, deux verbes.",
 "{切|き}る (couper) est du groupe 1 : {切|き}ります, {切|き}って. {着|き}る (porter) est du groupe 2 : {着|き}ます, {着|き}て.",
 "Sur les portes : おす (pousser) / {引|ひ}く (tirer).",
 "つける / {消|け}す : allumer / éteindre (lumière, télé). {消|け}す veut aussi dire effacer.",
 "{作|つく}る : fabriquer, et aussi préparer un plat : {料理|りょうり}を{作|つく}る."
], "exercises": [
 C(L,1,["{開|あ}けます","{開|あ}きます","しまります","{消|け}します"],jp="{暑|あつ}いですから、{窓|まど}を＿。",fr="Il fait chaud, alors j'ouvre la fenêtre.",uses=["v5-22","v5-25"]),
 C(L,2,["{開|あ}きます","{開|あ}けます","しめます","つけます"],jp="{銀行|ぎんこう}のドアは{九時|くじ}に＿。",fr="Les portes de la banque ouvrent à neuf heures.",uses=["v5-04","v5-16"],explain="La porte s'ouvre (d'elle-même, pour nous) : {開|あ}く."),
 C(L,3,["しめて","しまって","{開|あ}けて","{開|あ}いて"],jp="{寒|さむ}いですから、ドアを＿ください。",fr="Il fait froid, alors fermez la porte, s'il vous plaît.",uses=["v5-25"]),
 C(L,4,["しまって","しめて","{開|あ}けて","つけて"],jp="{店|みせ}が＿いますから、{買|か}い{物|もの}ができません。",fr="Le magasin est fermé, alors je ne peux pas faire les courses.",explain="{店|みせ}**が** : la chose elle-même → verbe « ça se fait » : しまる."),
 C(L,5,["つけて","{消|け}して","しめて","{切|き}って"],jp="テレビを＿、ニュースを{見|み}ます。",fr="J'allume la télé et je regarde les informations.",uses=["v5-12"]),
 C(L,6,["{消|け}して","ならべて","{開|あ}けて","{作|つく}って"],jp="{部屋|へや}を{出|で}るときは、{電気|でんき}を＿ください。",fr="Quand vous sortez de la pièce, éteignez la lumière, s'il vous plaît.",uses=["v5-14","v5-22"]),
 C(L,7,["{作|つく}りました","{使|つか}いました","{開|あ}けました","おしました"],jp="{母|はは}はたんじょうびのケーキを＿。",fr="Ma mère a fait le gâteau d'anniversaire.",uses=["v5-17","v5-21"]),
 C(L,8,["{使|つか}って","{作|つく}って","{消|け}して","しまって"],jp="すみません、このペンを＿もいいですか。",fr="Excusez-moi, je peux utiliser ce stylo ?"),
 C(L,9,["{入|い}れます","{入|はい}ります","おします","{引|ひ}きます"],jp="コーヒーにさとうを＿か。",fr="Tu mets du sucre dans ton café ?",uses=["v5-06"],explain="Mettre dedans : {入|い}れる (いれる). {入|はい}る (はいる), c'est entrer soi-même."),
 C(L,10,["{切|き}ります","{着|き}ます","{消|け}します","おします"],jp="ナイフで{肉|にく}を＿。",fr="Je coupe la viande avec un couteau.",uses=["v5-06"]),
 C(L,11,["tirer","pousser","entrer","sortir"],q="Sur une porte, il est écrit **{引|ひ}** (ひく). Que dois-tu faire ?"),
 C(L,12,["おして","{開|あ}けて","{消|け}して","ならべて"],jp="{二|に}かいへ{行|い}きますから、エレベーターのボタンを＿ください。",fr="Je vais au premier étage, alors appuyez sur le bouton de l'ascenseur, s'il vous plaît.",uses=["v5-22"]),
 C(L,13,["おいて","おして","{切|き}って","しまって"],jp="かぎはつくえの{上|うえ}に＿ください。",fr="Pose la clé sur le bureau, s'il te plaît.",uses=["v5-12","v5-20"]),
 C(L,14,["が","を","で","へ"],jp="{風|かぜ}で{窓|まど}＿{開|あ}きました。",fr="La fenêtre s'est ouverte à cause du vent.",uses=["v5-25"],explain="{開|あ}く : la chose s'ouvre d'elle-même → が."),
 C(L,15,["を","が","に","で"],jp="{田中|たなか}さんが{窓|まど}＿{開|あ}けました。",fr="M. Tanaka a ouvert la fenêtre.",explain="{開|あ}ける : quelqu'un ouvre quelque chose → を."),
 C(L,16,["{切|き}って","{切|き}て","{切|き}りて","{切|き}んで"],q="Forme て de **{切|き}る** (couper) ?",uses=["v5-02"],explain="{切|き}る est un faux groupe 2 (groupe 1) : る → って."),
 C(L,17,["いれます","はいれます","はいります","いります"],q="Dans « かばんに本を入れます », comment se lit **入れます** ?"),
 C(L,18,["aligner, disposer","empiler","jeter","laver"],q="Que veut dire **ならべる** ?"),
 O(L,19,"Je peux ouvrir la fenêtre ?",["{窓|まど}を","{開|あ}けても","いいですか"],uses=["v5-22"]),
 O(L,20,"J'éteins la télé et je me couche.",["テレビを","{消|け}して","ねます"],uses=["v5-02","v5-12"]),
]}

# ---------- L28 Communiquer et savoir ----------
L = "v5-28"
l28 = {"id": L, "title": "Communiquer et savoir", "words": [
 W("{言|い}う","いう","dire","{先生|せんせい}は「{明日|あした}テストがあります」と{言|い}いました。","Le professeur a dit : « Il y a un contrôle demain. »"),
 W("{答|こた}える","こたえる","répondre","{先生|せんせい}の{質問|しつもん}に{答|こた}えます。","Je réponds à la question du professeur."),
 W("{教|おし}える","おしえる","enseigner ; indiquer","{田中|たなか}さんは{子|こ}どもに{英語|えいご}を{教|おし}えています。","M. Tanaka enseigne l'anglais aux enfants."),
 W("{習|なら}う","ならう","apprendre (avec quelqu'un)","{毎週|まいしゅう}ピアノを{習|なら}っています。","Je prends des cours de piano toutes les semaines."),
 W("{知|し}る","しる","savoir, connaître","{田中|たなか}さんの{電話|でんわ}ばんごうを{知|し}っていますか。","Tu connais le numéro de téléphone de M. Tanaka ?"),
 W("{分|わ}かる","わかる","comprendre","この{漢字|かんじ}の{意味|いみ}が{分|わ}かりません。","Je ne comprends pas le sens de ce kanji."),
 W("おぼえる","おぼえる","retenir, mémoriser","{毎日|まいにち}{漢字|かんじ}を{五|いつ}つおぼえます。","Je mémorise cinq kanji par jour."),
 W("わすれる","わすれる","oublier","{電車|でんしゃ}にかさをわすれました。","J'ai oublié mon parapluie dans le train."),
 W("{思|おも}う","おもう","penser, croire","{明日|あした}は{雨|あめ}が{降|ふ}ると{思|おも}います。","Je pense qu'il pleuvra demain."),
 W("{考|かんが}える","かんがえる","réfléchir","よく{考|かんが}えてから、{答|こた}えてください。","Réfléchissez bien avant de répondre."),
 W("よぶ","よぶ","appeler (quelqu'un)","タクシーをよびましょうか。","Je vous appelle un taxi ?"),
 W("{話|はなし}","はなし","histoire, propos, conversation","{先生|せんせい}の{話|はなし}はおもしろいです。","Ce que raconte le professeur est intéressant."),
 W("ニュース","ニュース","informations, nouvelles","{毎朝|まいあさ}テレビでニュースを{見|み}ます。","Tous les matins, je regarde les informations à la télé."),
], "sections": [
 {"h": "Savoir, comprendre, apprendre",
  "p": ["Ces verbes ont chacun leur petite manie : à retenir avec leur particule."],
  "grid": {"head": ["", "comment l'utiliser"], "rows": [
   ["{知|し}る", "{知|し}っています (je sais) · ==**{知|し}りません**== (je ne sais pas)"],
   ["{分|わ}かる", "{日本語|にほんご}==が=={分|わ}かります"],
   ["{答|こた}える", "{質問|しつもん}==に=={答|こた}える"],
   ["{言|い}う · {思|おも}う", "「…」==と=={言|い}う · …==と=={思|おも}う"],
   ["{習|なら}う · おぼえる", "apprendre avec un prof · retenir par cœur"]]}}
], "pieges": [
 "{知|し}っていますか → はい、{知|し}っています / いいえ、**{知|し}りません** (jamais {知|し}っていません).",
 "{分|わ}かる : la chose comprise prend **が** : {日本語|にほんご}**が**{分|わ}かります.",
 "{答|こた}える : on répond **à** une question → {質問|しつもん}**に**{答|こた}える.",
 "{教|おし}える = enseigner **et** indiquer : {道|みち}を{教|おし}えてください = indiquez-moi le chemin.",
 "{習|なら}う = apprendre auprès de quelqu'un ; おぼえる = mémoriser ; {勉強|べんきょう}する = étudier.",
 "わすれる : oublier quelque chose **quelque part** → {電車|でんしゃ}**に**かさをわすれる.",
 "{話|はなし} (はなし, nom) ≠ {話|はな}す (はなす, verbe parler)."
], "exercises": [
 C(L,1,["{知|し}りません","{知|し}っていません","{知|し}りませんです","{知|し}るません"],jp="{田中|たなか}さんの{電話|でんわ}ばんごうを{知|し}っていますか。— いいえ、＿。",fr="Tu connais le numéro de téléphone de M. Tanaka ? — Non, je ne le connais pas.",explain="Au négatif, on ne dit pas {知|し}っていません mais {知|し}りません."),
 C(L,2,["が","を","に","で"],jp="この{漢字|かんじ}の{意味|いみ}＿{分|わ}かりますか。",fr="Tu comprends le sens de ce kanji ?",explain="{分|わ}かる : ce qu'on comprend prend が."),
 C(L,3,["に","を","が","と"],jp="{先生|せんせい}の{質問|しつもん}＿{答|こた}えます。",fr="Je réponds à la question du professeur.",uses=["v5-01"]),
 C(L,4,["わすれました","おぼえました","{教|おし}えました","{答|こた}えました"],jp="{電車|でんしゃ}にかさを＿。",fr="J'ai oublié mon parapluie dans le train.",uses=["v5-12","v5-15"]),
 C(L,5,["{習|なら}って","{教|おし}えて","わすれて","{答|こた}えて"],uses=["v5-19"],jp="{毎週|まいしゅう}、{田中|たなか}{先生|せんせい}にピアノを＿います。{先生|せんせい}はとても{上手|じょうず}です。",fr="Toutes les semaines, je prends des cours de piano avec M. Tanaka. Il joue très bien."),
 C(L,6,["{教|おし}えて","{習|なら}って","おぼえて","{答|こた}えて"],jp="すみません、{駅|えき}へ{行|い}く{道|みち}を＿ください。",fr="Excusez-moi, pouvez-vous m'indiquer le chemin de la gare ?",uses=["v5-04","v5-11"]),
 C(L,7,["{思|おも}います","おぼえます","わすれます","{習|なら}います"],jp="{明日|あした}は{雨|あめ}が{降|ふ}ると＿。",fr="Je pense qu'il pleuvra demain.",uses=["v5-25"]),
 C(L,8,["と","を","に","が"],jp="{先生|せんせい}は「{明日|あした}テストがあります」＿{言|い}いました。",fr="Le professeur a dit : « Il y a un contrôle demain. »",explain="Ce qu'on dit ou pense est marqué par と."),
 C(L,9,["よび","{言|い}い","{答|こた}え","{習|なら}い"],jp="タクシーを＿ましょうか。",fr="Je vous appelle un taxi ?",uses=["v5-15"]),
 C(L,10,["retenir, mémoriser","oublier","enseigner","répondre"],q="Que veut dire **おぼえる** ?"),
 C(L,11,["わすれる","{教|おし}える","{考|かんが}える","{分|わ}かる"],q="Contraire de **おぼえる** ?"),
 C(L,12,["{考|かんが}えて","わすれて","よんで","{言|い}って"],jp="よく＿から、{答|こた}えてください。",fr="Réfléchissez bien avant de répondre."),
 C(L,13,["{話|はなし}","{話|はな}す","{言|い}う","{答|こた}える"],jp="{先生|せんせい}の＿はいつもおもしろいです。",fr="Ce que raconte le professeur est toujours intéressant.",uses=["v5-10","v5-18"],explain="Après の il faut un nom : {話|はなし}."),
 C(L,14,["ニュース","{話|はなし}","{質問|しつもん}","{意味|いみ}"],jp="{毎朝|まいあさ}テレビで＿を{見|み}ます。",fr="Tous les matins, je regarde les informations à la télé.",uses=["v5-12","v5-16"]),
 C(L,15,["{田中|たなか}さんを{知|し}っています。","{田中|たなか}さんを{知|し}ります。","{田中|たなか}さんが{知|し}っています。","{田中|たなか}さんに{知|し}っています。"],q="« Je connais M. Tanaka » se dit…",explain="Connaître : {知|し}っています (forme en ている), avec を."),
 C(L,16,["{言|い}って","{言|い}いて","{言|い}んで","{言|い}うて"],q="Forme て de **{言|い}う** ?",uses=["v5-02"],explain="う → って."),
 C(L,17,["こたえる","とうえる","こたる","かたえる"],q=LECT+"**答える** ?"),
 C(L,18,["おしえる","きょうえる","おそえる","おしる"],q=LECT+"**教える** ?"),
 O(L,19,"Je ne connais pas le nom de ce professeur.",["あの","{先生|せんせい}の","{名前|なまえ}を","{知|し}りません"],uses=["v5-01"]),
 O(L,20,"J'ai oublié mon parapluie dans le train.",["{電車|でんしゃ}に","かさを","わすれました"],alt=[["かさを","{電車|でんしゃ}に","わすれました"]],uses=["v5-12","v5-15"]),
]}

# ---------- L29 École et études ----------
L = "v5-29"
l29 = {"id": L, "title": "École et études", "words": [
 W("{宿題|しゅくだい}","しゅくだい","devoirs","{今晩|こんばん}は{宿題|しゅくだい}がたくさんあります。","Ce soir, j'ai beaucoup de devoirs."),
 W("{試験|しけん}","しけん","examen","{来週|らいしゅう}、{日本語|にほんご}の{試験|しけん}があります。","La semaine prochaine, j'ai un examen de japonais."),
 W("{問題|もんだい}","もんだい","exercice, question ; problème","この{問題|もんだい}はむずかしいです。","Cet exercice est difficile."),
 W("{質問|しつもん}","しつもん","question","{質問|しつもん}がありますか。— はい、{一|ひと}つあります。","Vous avez des questions ? — Oui, une."),
 W("{意味|いみ}","いみ","sens, signification","この{漢字|かんじ}の{意味|いみ}は{何|なん}ですか。","Quel est le sens de ce kanji ?"),
 W("ことば","ことば","mot ; langue","{新|あたら}しいことばを{毎日|まいにち}{十|じゅう}おぼえます。","Je retiens dix mots nouveaux par jour."),
 W("{漢字|かんじ}","かんじ","kanji","{漢字|かんじ}で{名前|なまえ}を{書|か}いてください。","Écrivez votre nom en kanji, s'il vous plaît."),
 W("{授業|じゅぎょう}","じゅぎょう","cours (la séance)","{授業|じゅぎょう}は{九時|くじ}に{始|はじ}まります。","Le cours commence à neuf heures."),
 W("{教室|きょうしつ}","きょうしつ","salle de classe","{教室|きょうしつ}に{学生|がくせい}が{二十人|にじゅうにん}います。","Il y a vingt étudiants dans la salle."),
 W("ノート","ノート","cahier","ノートに{漢字|かんじ}を{書|か}きます。","J'écris des kanji dans mon cahier."),
 W("えんぴつ","えんぴつ","crayon","えんぴつで{書|か}いてもいいですか。","Je peux écrire au crayon ?"),
 W("ペン","ペン","stylo","ペンを{貸|か}してください。","Prête-moi un stylo, s'il te plaît."),
 W("れんしゅうする","れんしゅうする","s'exercer, s'entraîner","{毎日|まいにち}ピアノをれんしゅうします。","Je m'exerce au piano tous les jours."),
 W("{作文|さくぶん}","さくぶん","rédaction","{週末|しゅうまつ}に{日本語|にほんご}で{作文|さくぶん}を{書|か}きました。","Ce week-end, j'ai écrit une rédaction en japonais."),
 W("{字|じ}","じ","caractère, écriture","{田中|たなか}さんは{字|じ}がきれいです。","M. Tanaka a une belle écriture."),
], "sections": [
 {"h": "Étudier : quel verbe ?",
  "p": ["Le français dit souvent « apprendre ». Le japonais précise."],
  "grid": {"head": ["", "sens"], "rows": [
   ["{勉強|べんきょう}する", "étudier (en général)"],
   ["{習|なら}う", "apprendre avec un professeur"],
   ["れんしゅうする", "s'exercer, répéter"],
   ["おぼえる", "retenir par cœur"],
   ["{宿題|しゅくだい}をする", "faire ses devoirs"]]}}
], "pieges": [
 "{宿題|しゅくだい}**を**する = faire ses devoirs ; {試験|しけん}**が**ある = avoir un examen.",
 "{質問|しつもん}**を**する = poser une question ; {質問|しつもん}**に**{答|こた}える = y répondre.",
 "{問題|もんだい} = un exercice **et** un problème : {問題|もんだい}ありません = pas de problème.",
 "Avec quoi on écrit : **で** → えんぴつ**で**, {漢字|かんじ}**で**, {日本語|にほんご}**で**.",
 "{授業|じゅぎょう} = le cours (la séance) ; {教室|きょうしつ} = la salle de classe.",
 "{日本語|にほんご}で{何|なん}と{言|い}いますか = comment dit-on en japonais ? Phrase en or !"
], "exercises": [
 C(L,1,["{宿題|しゅくだい}","{教室|きょうしつ}","えんぴつ","{字|じ}"],jp="{今晩|こんばん}は＿をします。{明日|あした}{先生|せんせい}に{出|だ}しますから。",fr="Ce soir, je fais mes devoirs : je les rends au professeur demain.",uses=["v5-16","v5-26"]),
 C(L,2,["{質問|しつもん}","{教室|きょうしつ}","ノート","ペン"],jp="{先生|せんせい}、＿があります。この{漢字|かんじ}はどう{読|よ}みますか。",fr="Monsieur, j'ai une question. Comment se lit ce kanji ?",uses=["v5-09"]),
 C(L,3,["{意味|いみ}","{教室|きょうしつ}","{授業|じゅぎょう}","{宿題|しゅくだい}"],jp="この{漢字|かんじ}の＿が{分|わ}かりません。じしょで{見|み}ます。",fr="Je ne comprends pas le sens de ce kanji. Je regarde dans le dictionnaire.",uses=["v5-12","v5-28"]),
 C(L,4,["で","を","に","が"],jp="えんぴつ＿{書|か}いてもいいですか。",fr="Je peux écrire au crayon ?",explain="L'outil avec lequel on fait l'action : で."),
 C(L,5,["{試験|しけん}","{字|じ}","ノート","えんぴつ"],jp="{来週|らいしゅう}{日本語|にほんご}の＿がありますから、{毎日|まいにち}{勉強|べんきょう}しています。",fr="J'ai un examen de japonais la semaine prochaine, alors j'étudie tous les jours.",uses=["v5-03","v5-14"]),
 C(L,6,["{教室|きょうしつ}","{宿題|しゅくだい}","{問題|もんだい}","{質問|しつもん}"],jp="{授業|じゅぎょう}は{二|に}かいの＿であります。",fr="Le cours a lieu dans la salle du premier étage.",uses=["v5-22"]),
 C(L,7,["れんしゅうします","おぼえます","{答|こた}えます","{書|か}きます"],jp="{毎日|まいにち}ピアノを＿。",fr="Je m'exerce au piano tous les jours.",uses=["v5-28"]),
 C(L,8,["{字|じ}","{宿題|しゅくだい}","{試験|しけん}","{授業|じゅぎょう}"],jp="{田中|たなか}さんは＿がきれいですから、{手紙|てがみ}がよく{読|よ}めます。",fr="M. Tanaka a une belle écriture, alors ses lettres se lisent bien.",uses=["v5-12","v5-19"]),
 C(L,9,["une rédaction","un examen","une dictée","un manuel"],q="Que veut dire **{作文|さくぶん}** ?"),
 C(L,10,["しゅくだい","やどだい","しゅくたい","すくだい"],q=LECT+"**宿題** ?"),
 C(L,11,["しけん","しげん","しっけん","しあい"],q=LECT+"**試験** ?"),
 C(L,12,["しました","{答|こた}えました","{習|なら}いました","{開|あ}けました"],jp="{授業|じゅぎょう}のあとで、{先生|せんせい}に{質問|しつもん}を＿。",fr="Après le cours, j'ai posé une question au professeur.",uses=["v5-28"],explain="Poser une question : {質問|しつもん}をする."),
 C(L,13,["problème (souci)","exercice","examen","question"],q="Dans « {問題|もんだい}ありません » (réponse à « ça va ? »), {問題|もんだい} veut dire…"),
 C(L,14,["{言|い}います","{話|はな}します","{習|なら}います"],jp="« merci » は{日本語|にほんご}で{何|なん}と＿か。",fr="Comment dit-on « merci » en japonais ?",uses=["v5-28"]),
 C(L,15,["{貸|か}して","{借|か}りて","あげて","もらって"],jp="ペンを＿ください。{私|わたし}のペンをわすれましたから。",fr="Prête-moi un stylo, s'il te plaît : j'ai oublié le mien.",uses=["v5-26","v5-28"]),
 C(L,16,["le cours (la séance)","la salle de classe","l'école","le professeur"],q="Que veut dire **{授業|じゅぎょう}** ?"),
 C(L,17,["で","を","が","へ"],jp="{漢字|かんじ}＿{名前|なまえ}を{書|か}いてください。",fr="Écrivez votre nom en kanji, s'il vous plaît.",uses=["v5-01"]),
 O(L,18,"J'ai fait mes devoirs à la bibliothèque.",["{図書館|としょかん}で","{宿題|しゅくだい}を","しました"],alt=[["{宿題|しゅくだい}を","{図書館|としょかん}で","しました"]],uses=["v5-04"]),
 O(L,19,"J'écris des kanji dans mon cahier.",["ノートに","{漢字|かんじ}を","{書|か}きます"],alt=[["{漢字|かんじ}を","ノートに","{書|か}きます"]],uses=["v5-02"]),
]}

# ---------- L30 Travail et métiers ----------
L = "v5-30"
l30 = {"id": L, "title": "Travail et métiers", "words": [
 W("{仕事|しごと}","しごと","travail","{仕事|しごと}は{何時|なんじ}に{終|お}わりますか。","À quelle heure finit ton travail ?"),
 W("{医者|いしゃ}","いしゃ","médecin","{兄|あに}は{病院|びょういん}で{医者|いしゃ}をしています。","Mon grand frère est médecin à l'hôpital."),
 W("{店員|てんいん}","てんいん","vendeur, employé de magasin","{店員|てんいん}さん、これはいくらですか。","Excusez-moi (vendeur), c'est combien ?"),
 W("かんごし","かんごし","infirmier, infirmière","{姉|あね}は{病院|びょういん}でかんごしをしています。","Ma grande sœur est infirmière à l'hôpital."),
 W("{歌手|かしゅ}","かしゅ","chanteur, chanteuse","{有名|ゆうめい}な{歌手|かしゅ}のコンサートに{行|い}きました。","Je suis allé au concert d'un chanteur célèbre."),
 W("{運転手|うんてんしゅ}","うんてんしゅ","chauffeur","タクシーの{運転手|うんてんしゅ}に{道|みち}を{聞|き}きました。","J'ai demandé le chemin au chauffeur de taxi."),
 W("おまわりさん","おまわりさん","agent de police (du quartier)","{道|みち}が{分|わ}かりませんでしたから、おまわりさんに{聞|き}きました。","Je ne connaissais pas le chemin, alors j'ai demandé à un agent de police."),
 W("{休|やす}み","やすみ","congé, jour de repos","{明日|あした}は{仕事|しごと}が{休|やす}みです。","Demain, je ne travaille pas."),
 W("{大学|だいがく}","だいがく","université","{兄|あに}は{東京|とうきょう}の{大学|だいがく}で{勉強|べんきょう}しています。","Mon grand frère étudie dans une université de Tokyo."),
 W("{大学生|だいがくせい}","だいがくせい","étudiant (à l'université)","{田中|たなか}さんは{大学生|だいがくせい}です。","M. Tanaka est étudiant."),
 W("{高校生|こうこうせい}","こうこうせい","lycéen","{弟|おとうと}は{高校生|こうこうせい}で、サッカーが{好|す}きです。","Mon petit frère est lycéen et il aime le foot."),
 W("{工場|こうじょう}","こうじょう","usine","{父|ちち}は{車|くるま}の{工場|こうじょう}で{働|はたら}いています。","Mon père travaille dans une usine automobile."),
 W("じむしょ","じむしょ","bureau (lieu de travail)","じむしょは{三|さん}がいにあります。","Le bureau est au deuxième étage."),
 W("{銀行員|ぎんこういん}","ぎんこういん","employé de banque","{銀行員|ぎんこういん}の{仕事|しごと}はいそがしいです。","Le travail d'employé de banque est prenant."),
 W("{作家|さっか}","さっか","écrivain","この{本|ほん}の{作家|さっか}はとても{有名|ゆうめい}です。","L'auteur de ce livre est très célèbre."),
], "sections": [
 {"h": "Les suffixes des métiers",
  "p": ["Pour dire son métier : 〜です, ou 〜をしています (« j'exerce comme… »). Beaucoup de métiers se reconnaissent à leur suffixe."],
  "grid": {"head": ["", "exemples"], "rows": [
   ["〜{員|いん} (membre de)", "{会社員|かいしゃいん}, {銀行員|ぎんこういん}, {店員|てんいん}"],
   ["〜{手|しゅ} (qui fait)", "{歌手|かしゅ}, {運転手|うんてんしゅ}"],
   ["〜{者|しゃ} · 〜{家|か}", "{医者|いしゃ} · {作家|さっか}"],
   ["〜{生|せい} (élève)", "{学生|がくせい}, {大学生|だいがくせい}, {高校生|こうこうせい}"]]}}
], "pieges": [
 "〜をしています = exercer un métier : {医者|いしゃ}をしています = il est médecin.",
 "Pour interpeller : {店員|てんいん}さん, {運転手|うんてんしゅ}さん (on ajoute さん).",
 "おまわりさん = le policier du quartier (mot gentil et courant).",
 "{休|やす}み (nom) = le congé : {明日|あした}は{休|やす}みです. {休|やす}む (verbe) = se reposer, être absent.",
 "{工場|こうじょう} = usine ; じむしょ = bureau (le lieu) ; {会社|かいしゃ} = l'entreprise.",
 "{大学|だいがく} (université) → {大学生|だいがくせい} (étudiant) ; {高校|こうこう} (lycée) → {高校生|こうこうせい} (lycéen)."
], "exercises": [
 C(L,1,["{医者|いしゃ}","{歌手|かしゅ}","{作家|さっか}","おまわりさん"],jp="{兄|あに}は{病院|びょういん}で＿をしています。",fr="Mon grand frère est médecin à l'hôpital.",uses=["v5-04","v5-21"]),
 C(L,2,["{運転手|うんてんしゅ}","{医者|いしゃ}","{店員|てんいん}","{作家|さっか}"],jp="タクシーの＿に{駅|えき}までの{道|みち}を{聞|き}きました。",fr="J'ai demandé au chauffeur de taxi le chemin jusqu'à la gare.",uses=["v5-15"]),
 C(L,3,["{店員|てんいん}","{医者|いしゃ}","{歌手|かしゅ}","{作家|さっか}"],jp="＿さん、このシャツはいくらですか。",fr="Excusez-moi (vendeur), combien coûte cette chemise ?",uses=["v5-07","v5-13"]),
 C(L,4,["{休|やす}み","{休|やす}む","{休|やす}みます","{休|やす}んで"],jp="{明日|あした}は{日曜日|にちようび}ですから、{仕事|しごと}が＿です。",fr="Demain c'est dimanche, alors je ne travaille pas.",uses=["v5-17"],explain="Devant です, il faut le nom : {休|やす}み."),
 C(L,5,["{工場|こうじょう}","{大学|だいがく}","{教室|きょうしつ}","{病院|びょういん}"],jp="{父|ちち}は{車|くるま}を{作|つく}る＿で{働|はたら}いています。",fr="Mon père travaille dans une usine qui fabrique des voitures.",uses=["v5-14","v5-27"]),
 C(L,6,["un agent de police","un facteur","un voisin","un chauffeur"],q="Qui est **おまわりさん** ?"),
 C(L,7,["{大学生|だいがくせい}","{高校生|こうこうせい}","{会社員|かいしゃいん}","{医者|いしゃ}"],jp="{田中|たなか}さんは{東京|とうきょう}の{大学|だいがく}で{勉強|べんきょう}しています。＿です。",fr="M. Tanaka étudie dans une université de Tokyo. Il est étudiant.",uses=["v5-01"]),
 C(L,8,["いしゃ","いしや","いじゃ","いしょ"],q=LECT+"**医者** ?"),
 C(L,9,["かしゅ","うたて","かて","かしゅう"],q=LECT+"**歌手** ?"),
 C(L,10,["こうじょう","くじょう","こうしょう","こうちょう"],q=LECT+"**工場** (usine) ?"),
 C(L,11,["{銀行員|ぎんこういん}","{店員|てんいん}","{歌手|かしゅ}","{作家|さっか}"],jp="{銀行|ぎんこう}で{働|はたら}いている{人|ひと}は＿です。",fr="Les gens qui travaillent à la banque sont des employés de banque.",uses=["v5-04","v5-14"]),
 C(L,12,["〜{員|いん}","〜{者|しゃ}","〜{手|しゅ}","〜{家|か}"],q="Quel suffixe veut dire « membre du personnel de… » ({会社員|かいしゃいん}, {店員|てんいん}) ?"),
 C(L,13,["{作家|さっか}","{歌手|かしゅ}","{運転手|うんてんしゅ}","{店員|てんいん}"],jp="この{本|ほん}を{書|か}いた＿はフランス{人|じん}です。",fr="L'écrivain qui a écrit ce livre est français.",uses=["v5-02","v5-12"]),
 C(L,14,["{仕事|しごと}","{休|やす}み","{作家|さっか}","{歌手|かしゅ}"],jp="{毎日|まいにち}{八時|はちじ}に{家|いえ}を{出|で}て、＿に{行|い}きます。",fr="Tous les jours, je pars de chez moi à huit heures et je vais au travail.",uses=["v5-14","v5-16"]),
 C(L,15,["bureau (lieu de travail)","usine","magasin","salle de classe"],q="Que veut dire **じむしょ** ?"),
 C(L,16,["infirmier, infirmière","médecin","pharmacien","dentiste"],q="Que veut dire **かんごし** ?"),
 C(L,17,["{姉|あね}はかんごしをしています。","{姉|あね}はかんごしがしています。","{姉|あね}はかんごしでしています。","{姉|あね}はかんごしにしています。"],q="« Ma grande sœur est infirmière (c'est son métier) » se dit…",uses=["v5-21"]),
 O(L,18,"Mon père travaille dans une usine.",["{父|ちち}は","{工場|こうじょう}で","{働|はたら}いています"],uses=["v5-14","v5-21"]),
 O(L,19,"Demain, c'est mon jour de congé.",["{明日|あした}は","{仕事|しごと}が","{休|やす}みです"],uses=["v5-03"]),
]}

TC, TO, XC, XO = make_block("v5-b06", "v5-x03")
test = [
 TC(1,["{借|か}りました","{貸|か}しました","あげました","{売|う}りました"],jp="{友|とも}だちに{本|ほん}を＿。{来週|らいしゅう}かえします。",fr="J'ai emprunté un livre à un ami. Je le lui rends la semaine prochaine.",uses=["v5-26"]),
 TC(2,["が","を","で","へ"],jp="{窓|まど}＿{開|あ}いていますよ。",fr="La fenêtre est ouverte, tu sais.",uses=["v5-22","v5-27"]),
 TC(3,["{答|こた}えました","{言|い}いました","{教|おし}えました","{聞|き}きました"],jp="{先生|せんせい}の{質問|しつもん}に＿。",fr="J'ai répondu à la question du professeur.",uses=["v5-28","v5-29"]),
 TC(4,["{借|か}りて","{借|か}って","{借|か}りって","{借|か}んで"],q="Forme て de **{借|か}りる** ?",uses=["v5-02","v5-26"]),
 TC(5,["{宿題|しゅくだい}","{教室|きょうしつ}","えんぴつ","{字|じ}"],jp="＿がたくさんありますから、{今晩|こんばん}はテレビを{見|み}ません。",fr="J'ai beaucoup de devoirs, alors ce soir je ne regarde pas la télé.",uses=["v5-16","v5-29"]),
 TC(6,["くれました","あげました","もらいました"],jp="{姉|あね}が{私|わたし}にセーターを＿。",fr="Ma grande sœur m'a donné un pull.",uses=["v5-13","v5-26"]),
 TC(7,["つけます","{消|け}します","{開|あ}けます","{切|き}ります"],jp="{部屋|へや}が{暗|くら}いですから、{電気|でんき}を＿。",fr="La pièce est sombre, alors j'allume la lumière.",uses=["v5-22","v5-24","v5-27"]),
 TC(8,["{医者|いしゃ}","{歌手|かしゅ}","{作家|さっか}"],jp="{兄|あに}は{病院|びょういん}で{働|はたら}いています。＿です。",fr="Mon grand frère travaille à l'hôpital. Il est médecin.",uses=["v5-30"]),
 TC(9,["いいえ、{知|し}りません。","いいえ、{知|し}っていません。","いいえ、{分|わ}かっていません。","いいえ、{知|し}りませんでした。"],q="On te demande : この{人|ひと}を{知|し}っていますか. Tu ne le connais pas. Tu réponds :",uses=["v5-28"]),
 TC(10,["{入|い}れます","{入|はい}ります","{開|あ}けます","{出|で}ます"],jp="コーヒーにぎゅうにゅうを＿。",fr="Je mets du lait dans mon café.",uses=["v5-06","v5-27"]),
 TC(11,["{意味|いみ}","{宿題|しゅくだい}","{教室|きょうしつ}","{試験|しけん}"],jp="このことばの＿が{分|わ}かりません。",fr="Je ne comprends pas le sens de ce mot.",uses=["v5-28","v5-29"]),
 TC(12,["{送|おく}りました","{売|う}りました","{借|か}りました","{消|け}しました"],jp="{国|くに}の{家族|かぞく}に{写真|しゃしん}を＿。",fr="J'ai envoyé des photos à ma famille, dans mon pays.",uses=["v5-12","v5-21","v5-26"]),
 TO(13,"Je mets du sucre dans le café.",["コーヒーに","さとうを","{入|い}れます"],alt=[["さとうを","コーヒーに","{入|い}れます"]],uses=["v5-27"]),
 TC(14,["{運転手|うんてんしゅ}","{店員|てんいん}","{作家|さっか}","{医者|いしゃ}"],q="Qui conduit un taxi ? タクシーの…",uses=["v5-15","v5-30"]),
 TC(15,["わすれました","おぼえました","{答|こた}えました","{習|なら}いました"],jp="すみません、{宿題|しゅくだい}をうちに＿。",fr="Pardon, j'ai oublié mes devoirs à la maison.",uses=["v5-22","v5-28","v5-29"]),
 TC(16,["{作|つく}ります","{使|つか}います","{開|あ}けます","{入|い}れます"],jp="{母|はは}は{毎日|まいにち}{晩|ばん}ご{飯|はん}を＿。",fr="Ma mère prépare le dîner tous les jours.",uses=["v5-06","v5-27"]),
]
exam = [
 XC(1,["{田中|たなか}さんのお{母|かあ}さんに{本|ほん}を{借|か}りました。","{田中|たなか}さんの{母|はは}に{本|ほん}を{借|か}りました。","{田中|たなか}さんのお{母|かあ}さんを{本|ほん}を{借|か}りました。","{田中|たなか}さんのお{母|かあ}さんに{本|ほん}を{貸|か}りました。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-21","v5-26"],explain="La mère des autres : お{母|かあ}さん ; on emprunte **à** quelqu'un : に{借|か}りる."),
 XC(2,["つけて","{消|け}して","{開|あ}けて","しまって"],jp="{部屋|へや}が{暗|くら}くて、{寒|さむ}いです。{電気|でんき}を＿、{窓|まど}をしめてください。",fr="La pièce est sombre et froide. Allume la lumière et ferme la fenêtre, s'il te plaît.",uses=["v5-22","v5-24","v5-25","v5-27"]),
 XC(3,["ありました","いました","ひきました","しました"],jp="かぜをひいて、ねつが＿から、{医者|いしゃ}に{薬|くすり}をもらいました。",fr="J'ai attrapé un rhume et j'avais de la fièvre, alors le médecin m'a donné des médicaments.",uses=["v5-23","v5-26","v5-30"]),
 XC(4,["Il enseigne le japonais.","Il apprend le japonais.","Il cherche un professeur de japonais.","Il connaît un professeur de japonais."],q="Ton ami te dit : {日本語|にほんご}の{先生|せんせい}をしています. Que fait-il ?",uses=["v5-30"]),
 XC(5,["{寒|さむ}い","つめたい","すずしい","あたたかい"],jp="{冬|ふゆ}の{北海道|ほっかいどう}はゆきが{降|ふ}って、とても＿です。",fr="L'hiver à Hokkaidō, il neige et il fait très froid.",uses=["v5-20","v5-24","v5-25"]),
 XC(6,["{借|か}りて","{貸|か}して","くれて","あげて"],jp="{妹|いもうと}が{私|わたし}の{赤|あか}いセーターを＿、まだかえしません。",fr="Ma petite sœur m'a emprunté mon pull rouge et ne me l'a toujours pas rendu.",uses=["v5-21","v5-24","v5-26"]),
 XC(7,["{教|おし}えて","{習|なら}って","おぼえて","{答|こた}えて"],jp="この{漢字|かんじ}の{読|よ}み{方|かた}を＿ください。わすれました。",fr="Dis-moi comment se lit ce kanji, s'il te plaît. Je l'ai oublié.",uses=["v5-28","v5-29"]),
 XO(8,"Il y a un dictionnaire sur l'étagère de la salle de classe.",["{教室|きょうしつ}の","{本|ほん}だなに","じしょが","あります"],alt=[["じしょが","{教室|きょうしつ}の","{本|ほん}だなに","あります"]],uses=["v5-12","v5-22","v5-29"]),
 XC(9,["しまります","しめます","{開|あ}けます","{消|け}します"],jp="{店|みせ}が{十時|じゅうじ}に{開|あ}いて、{夜|よる}{八時|はちじ}に＿。",fr="Le magasin ouvre à dix heures et ferme à vingt heures.",uses=["v5-16","v5-27"],explain="{店|みせ}**が** : la chose elle-même → {開|あ}く / しまる."),
 XC(10,["{姉|あね}は{高校|こうこう}で{英語|えいご}を{教|おし}えています。","{姉|あね}は{高校|こうこう}で{英語|えいご}を{習|なら}えています。","{姉|あね}は{高校|こうこう}に{英語|えいご}を{教|おし}えています。","{姉|あね}は{高校|こうこう}で{英語|えいご}が{教|おし}えています。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-21","v5-28"]),
 XC(11,["{兄|あに}は{銀行員|ぎんこういん}です。","お{兄|にい}さんは{銀行員|ぎんこういん}です。","{兄|あに}さんは{銀行員|ぎんこういん}です。","{兄|あに}は{銀行員|ぎんこういん}ます。"],q="Ton professeur te demande : お{兄|にい}さんは{何|なに}をしていますか. Tu réponds :",uses=["v5-21","v5-30"]),
 XC(12,["{飲|の}み{物|もの}","{食|た}べ{物|もの}","{薬|くすり}","{天気|てんき}"],jp="{夏|なつ}は{暑|あつ}いですから、つめたい＿をよく{飲|の}みます。",fr="En été il fait chaud, alors je bois souvent des boissons fraîches.",uses=["v5-06","v5-24","v5-25"]),
 XC(13,["{声|こえ}","{口|くち}","{字|じ}","{色|いろ}"],jp="おじいさんは{耳|みみ}が{悪|わる}いですから、{大|おお}きい＿で{話|はな}してください。",fr="Grand-père entend mal, alors parlez fort, s'il vous plaît.",uses=["v5-21","v5-23"]),
 XC(14,["6","5","4","7"],q="Combien sont-ils ? {家族|かぞく}は{父|ちち}と{母|はは}と{兄|あに}と{妹|いもうと}{二人|ふたり}と{私|わたし}です。",uses=["v5-08","v5-21"]),
 XC(15,["{貸|か}しました","{借|か}りました","もらいました","くれました"],jp="{雨|あめ}が{降|ふ}っていました。{友|とも}だちはかさを{持|も}っていませんでしたから、{私|わたし}のかさを＿。",fr="Il pleuvait. Mon ami n'avait pas de parapluie, alors je lui ai prêté le mien.",uses=["v5-25","v5-26"]),
]
bloc = {"id": "v5-b06", "level": "N5", "title": "Agir : donner, utiliser, communiquer, étudier, travailler",
        "lessons": [l26, l27, l28, l29, l30], "test": test, "examTest": exam}
save(bloc, sys.argv[1])
