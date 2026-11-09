import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save

# ---------- L36 Verbes d'état et de situation ----------
L = "v5-36"
l36 = {"id": L, "title": "Verbes d'état et de situation", "words": [
 W("ある","ある","il y a, avoir (choses)","つくえの{上|うえ}にペンがあります。","Il y a un stylo sur le bureau."),
 W("いる","いる","avoir besoin de","{日本|にほん}へ{行|い}くとき、ビザがいりますか。","Faut-il un visa pour aller au Japon ?"),
 W("{住|す}む","すむ","habiter","{兄|あに}は{大阪|おおさか}に{住|す}んでいます。","Mon grand frère habite à Osaka."),
 W("{立|た}つ","たつ","se lever, être debout","{駅|えき}の{前|まえ}に{田中|たなか}さんが{立|た}っています。","M. Tanaka est debout devant la gare."),
 W("すわる","すわる","s'asseoir","どうぞ、ここにすわってください。","Je vous en prie, asseyez-vous ici."),
 W("{待|ま}つ","まつ","attendre","{駅|えき}で{友|とも}だちを{待|ま}っています。","J'attends un ami à la gare."),
 W("つかれる","つかれる","se fatiguer","たくさん{働|はたら}いて、つかれました。","J'ai beaucoup travaillé, je suis fatigué."),
 W("こまる","こまる","être embêté","さいふをわすれて、こまりました。","J'ai oublié mon portefeuille, j'étais bien embêté."),
 W("ちがう","ちがう","être différent ; être faux","これは{私|わたし}のかさじゃないです。{色|いろ}がちがいます。","Ce n'est pas mon parapluie. La couleur est différente."),
 W("けっこんする","けっこんする","se marier","{姉|あね}は{来月|らいげつ}けっこんします。","Ma grande sœur se marie le mois prochain."),
 W("{生|う}まれる","うまれる","naître","{弟|おとうと}はフランスで{生|う}まれました。","Mon petit frère est né en France."),
 W("{死|し}ぬ","しぬ","mourir","{去年|きょねん}、うちの{犬|いぬ}が{死|し}にました。","L'an dernier, notre chien est mort."),
 W("{止|と}まる","とまる","s'arrêter","{電車|でんしゃ}が{駅|えき}に{止|と}まりました。","Le train s'est arrêté en gare."),
 W("{急|いそ}ぐ","いそぐ","se dépêcher","{時間|じかん}がありませんから、{急|いそ}いでください。","On n'a pas le temps, dépêchez-vous."),
], "sections": [
 {"h": "〜ています : un état",
  "p": ["Avec ces verbes, la forme 〜ています décrit souvent un **état** qui dure, pas une action en cours."],
  "grid": {"head": ["", "sens"], "rows": [
   ["{住|す}んでいます", "j'habite (état durable)"],
   ["{立|た}っています · すわっています", "être debout · être assis"],
   ["けっこんしています", "être marié (≠ けっこんします : se marier)"],
   ["つかれています", "être fatigué"],
   ["{待|ま}っています", "être en train d'attendre"]]}}
], "pieges": [
 "けっこん**しています** = je **suis** marié ; けっこん**します** = je **vais** me marier.",
 "{住|す}む : le lieu prend **に** : {大阪|おおさか}**に**{住|す}んでいます.",
 "いる (avoir besoin) : la chose prend **が** : ビザ**が**いります. Ne pas confondre avec いる (être) : いります (besoin, groupe 1) ≠ います (être).",
 "{待|ま}つ (まつ, attendre) ≠ {持|も}つ (もつ, tenir) : kanji proches !",
 "ちがう = être différent **et** « non, c'est faux » : ちがいます.",
 "Formes て : {待|ま}つ → {待|ま}って ; {死|し}ぬ → {死|し}んで (le seul verbe en ぬ) ; {急|いそ}ぐ → {急|いそ}いで."
], "exercises": [
 C(L,1,["に","で","を","へ"],jp="{兄|あに}は{大阪|おおさか}＿{住|す}んでいます。",fr="Mon grand frère habite à Osaka.",uses=["v5-21"],explain="{住|す}む : lieu + に."),
 C(L,2,["しています","します","していません","しませんでした"],jp="{姉|あね}はもうけっこん＿。{子|こ}どもが{二人|ふたり}います。",fr="Ma grande sœur est déjà mariée. Elle a deux enfants.",uses=["v5-08","v5-10","v5-21"]),
 C(L,3,["いります","います","すわります","{住|す}みます"],jp="{日本|にほん}へ{行|い}くとき、ビザが＿か。",fr="Faut-il un visa pour aller au Japon ?",explain="Avoir besoin : いる → いります (groupe 1). います, c'est « être » (personnes, animaux)."),
 C(L,4,["{待|ま}って","{持|も}って","{住|す}んで","すわって"],jp="{駅|えき}で{友|とも}だちを＿います。",fr="J'attends un ami à la gare.",uses=["v5-26"]),
 C(L,5,["すわって","{立|た}って","{死|し}んで","けっこんして"],jp="いすがありますから、どうぞ＿ください。",fr="Il y a une chaise, alors asseyez-vous, je vous en prie.",uses=["v5-11","v5-22"]),
 C(L,6,["つかれました","ちがいました","{生|う}まれました","{住|す}みました"],jp="{今日|きょう}はたくさん{歩|ある}きましたから、＿。",fr="J'ai beaucoup marché aujourd'hui, alors je suis fatigué.",uses=["v5-15"]),
 C(L,7,["こまりました","つかれました","{生|う}まれました","すわりました"],jp="さいふをうちにわすれて、＿。お{金|かね}がありません。",fr="J'ai oublié mon portefeuille à la maison, j'étais bien embêté. Je n'ai pas d'argent.",uses=["v5-12","v5-28"]),
 C(L,8,["ちがいます","{待|ま}ちます","{住|す}みます","いります"],jp="これは{私|わたし}のかさじゃないです。{色|いろ}が＿。",fr="Ce n'est pas mon parapluie. La couleur est différente.",uses=["v5-24"]),
 C(L,9,["Mon petit frère est né en France.","Mon petit frère habite en France.","Mon petit frère s'est marié en France.","Mon petit frère est mort en France."],q="Que veut dire : {弟|おとうと}はフランスで{生|う}まれました。",uses=["v5-21"]),
 C(L,10,["{止|と}まりました","{止|と}めました","すわりました","{立|た}ちました"],jp="{電車|でんしゃ}が{駅|えき}に＿。",fr="Le train s'est arrêté en gare.",uses=["v5-15"]),
 C(L,11,["{急|いそ}いで","{住|す}んで","すわって","つかれて"],jp="{時間|じかん}がありませんから、＿ください。",fr="On n'a pas le temps, dépêchez-vous."),
 C(L,12,["{死|し}んで","{死|し}いで","{死|し}って","{死|し}ぬて"],q="Forme て de **{死|し}ぬ** ?",uses=["v5-02"],explain="ぬ → んで (comme む et ぶ)."),
 C(L,13,["{待|ま}って","{待|ま}ちて","{待|ま}んで","{待|ま}いて"],q="Forme て de **{待|ま}つ** ?",uses=["v5-02"],explain="つ → って."),
 C(L,14,["{急|いそ}いで","{急|いそ}いて","{急|いそ}んで","{急|いそ}って"],q="Forme て de **{急|いそ}ぐ** ?",uses=["v5-02"],explain="ぐ → いで."),
 C(L,15,["ちがいます","いります","あります","こまります"],jp="これは{田中|たなか}さんのペンですか。— いいえ、＿。{私|わたし}のです。",fr="C'est le stylo de M. Tanaka ? — Non, ce n'est pas ça. C'est le mien.",uses=["v5-29"]),
 C(L,16,["けっこんしています","けっこんします","けっこんがいます","けっこんであります"],q="« Il est marié » se dit…"),
 C(L,17,["すむ","じゅうむ","すすむ","いむ"],q=LECT+"**住む** ?"),
 O(L,18,"J'attends un ami devant la gare.",["{駅|えき}の{前|まえ}で","{友|とも}だちを","{待|ま}っています"],alt=[["{友|とも}だちを","{駅|えき}の{前|まえ}で","{待|ま}っています"]],uses=["v5-04","v5-20"]),
 O(L,19,"Mon grand frère habite à Osaka.",["{兄|あに}は","{大阪|おおさか}に","{住|す}んでいます"],uses=["v5-21"]),
]}

# ---------- L37 Mots de liaison et adverbes ----------
L = "v5-37"
l37 = {"id": L, "title": "Mots de liaison et adverbes", "words": [
 W("でも","でも","mais (en début de phrase)","{日本語|にほんご}はむずかしいです。でも、おもしろいです。","Le japonais est difficile. Mais c'est intéressant."),
 W("それから","それから","et ensuite","{朝|あさ}ご{飯|はん}を{食|た}べました。それから、{会社|かいしゃ}へ{行|い}きました。","J'ai pris mon petit-déjeuner. Ensuite, je suis allé au bureau."),
 W("そして","そして","et (en plus)","この{部屋|へや}は{広|ひろ}いです。そして、{明|あか}るいです。","Cette pièce est spacieuse. Et elle est lumineuse."),
 W("だから","だから","donc, c'est pourquoi","{雨|あめ}が{降|ふ}っています。だから、{今日|きょう}は{出|で}かけません。","Il pleut. Donc aujourd'hui, je ne sors pas."),
 W("もっと","もっと","plus, davantage","もっと{食|た}べてください。","Mangez encore, je vous en prie."),
 W("ゆっくり","ゆっくり","lentement ; tranquillement","ゆっくり{休|やす}んでください。","Reposez-vous bien."),
 W("ほんとうに","ほんとうに","vraiment","ほんとうにありがとうございました。","Merci vraiment beaucoup."),
 W("いちばん","いちばん","le plus ; numéro un","{果物|くだもの}の{中|なか}でりんごがいちばん{好|す}きです。","Parmi les fruits, c'est la pomme que je préfère."),
 W("いろいろ","いろいろ","divers, toutes sortes de","いろいろな{国|くに}の{料理|りょうり}を{食|た}べました。","J'ai mangé des plats de toutes sortes de pays."),
 W("たぶん","たぶん","sans doute, probablement","{明日|あした}はたぶん{雨|あめ}でしょう。","Demain, il pleuvra sans doute."),
 W("たいへん","たいへん","dur, pénible ; très","{毎日|まいにち}{仕事|しごと}が{多|おお}くて、たいへんです。","J'ai beaucoup de travail tous les jours, c'est dur."),
 W("じゃあ","じゃあ","bon, alors","じゃあ、また{明日|あした}。","Bon, à demain !"),
 W("あとで","あとで","plus tard","{今|いま}いそがしいですから、あとで{電話|でんわ}します。","Je suis occupé, je t'appelle plus tard."),
 W("どうも","どうも","vraiment, très (merci)","どうもありがとうございます。","Merci beaucoup."),
 W("{先|さき}に","さきに","d'abord, avant (les autres)","どうぞ、{先|さき}に{食|た}べてください。","Je vous en prie, commencez à manger sans moi."),
], "sections": [
 {"h": "Relier deux phrases",
  "p": ["Ces mots se mettent **au début** de la deuxième phrase, suivis d'une virgule."],
  "grid": {"head": ["", "sens"], "rows": [
   ["そして", "et (on ajoute une information)"],
   ["それから", "et ensuite (ordre dans le temps)"],
   ["でも", "mais"],
   ["だから", "donc, c'est pourquoi"],
   ["じゃあ", "bon, alors (pour conclure, changer de sujet)"]]}}
], "pieges": [
 "でも commence une phrase : 〜です。**でも**、〜. Au milieu d'une phrase, « mais » se dit 〜です**が**、〜.",
 "**だから**、〜 (donc, en début de phrase) ; 〜**から** (parce que, en fin de proposition).",
 "それから = et puis (l'ordre des actions) ; そして = et (une information de plus).",
 "たいへん : « c'est dur » ({仕事|しごと}がたいへんです) ou « très » en langage poli (たいへんおいしい).",
 "いろいろ**な** + nom : いろいろな{国|くに}.",
 "いちばん = le plus : いちばん{好|す}き = préféré ; いちばん{高|たか}い = le plus haut / cher."
], "exercises": [
 C(L,1,["でも","だから","それから","じゃあ"],jp="{日本語|にほんご}はむずかしいです。＿、おもしろいです。",fr="Le japonais est difficile. Mais c'est intéressant.",uses=["v5-18"]),
 C(L,2,["だから","でも","それから","もっと"],jp="{雨|あめ}が{降|ふ}っています。＿、{今日|きょう}は{出|で}かけません。",fr="Il pleut. Donc aujourd'hui, je ne sors pas.",uses=["v5-14","v5-25"]),
 C(L,3,["それから","でも","だから","もっと"],jp="{朝|あさ}ご{飯|はん}を{食|た}べました。＿、{会社|かいしゃ}へ{行|い}きました。",fr="J'ai pris mon petit-déjeuner. Ensuite, je suis allé au bureau.",uses=["v5-06"]),
 C(L,4,["もっと","いちばん","たぶん","じゃあ"],jp="すみません、＿ゆっくり{話|はな}してください。",fr="Excusez-moi, parlez plus lentement, s'il vous plaît."),
 C(L,5,["いちばん","もっと","ゆっくり","あとで"],jp="{果物|くだもの}の{中|なか}でりんごが＿{好|す}きです。",fr="Parmi les fruits, c'est la pomme que je préfère.",uses=["v5-06","v5-19"]),
 C(L,6,["たぶん","いちばん","もっと","ゆっくり"],jp="{明日|あした}は＿{雨|あめ}でしょう。",fr="Demain, il pleuvra sans doute.",uses=["v5-25"]),
 C(L,7,["あとで","{先|さき}に","いちばん","いろいろ"],jp="{今|いま}いそがしいですから、＿{電話|でんわ}します。",fr="Je suis occupé, je t'appelle plus tard.",uses=["v5-18"]),
 C(L,8,["いろいろ","たくさん","いちばん","たぶん"],jp="＿な{国|くに}の{料理|りょうり}を{食|た}べました。",fr="J'ai mangé des plats de toutes sortes de pays.",uses=["v5-10"]),
 C(L,9,["lentement, tranquillement","vite","bientôt","souvent"],q="Que veut dire **ゆっくり** ?"),
 C(L,10,["たいへん","ゆっくり","たぶん","{先|さき}に"],jp="{毎日|まいにち}{仕事|しごと}が{多|おお}くて、＿です。",fr="J'ai beaucoup de travail tous les jours, c'est dur.",uses=["v5-30"]),
 C(L,11,["じゃあ、また{明日|あした}。","だから、また{明日|あした}。","でも、また{明日|あした}。","もっと、また{明日|あした}。"],q="À la fin d'une conversation, tu dis « Bon, à demain ! » :"),
 C(L,12,["Merci vraiment beaucoup.","Merci quand même.","Merci d'avance.","Merci, c'est assez."],q="Que veut dire : ほんとうにありがとうございました。"),
 C(L,13,["{先|さき}に","あとで","いちばん","たぶん"],jp="どうぞ、＿{食|た}べてください。{私|わたし}はあとで{食|た}べます。",fr="Je vous en prie, mangez d'abord. Moi, je mangerai plus tard."),
 C(L,14,["そして","でも","もっと","じゃあ"],jp="この{部屋|へや}は{広|ひろ}いです。＿、{明|あか}るいです。",fr="Cette pièce est spacieuse. Et elle est lumineuse.",uses=["v5-24"]),
 C(L,15,["{寒|さむ}いです。だから、コートを{着|き}ます。","{寒|さむ}いです。から、コートを{着|き}ます。","{寒|さむ}いですだから、コートを{着|き}ます。","{寒|さむ}いから、だからコートを{着|き}ます。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-13","v5-25"],explain="だから commence une nouvelle phrase ; から se colle à la fin de la première."),
 C(L,16,["vraiment, beaucoup","pourquoi","comment","déjà"],q="Que veut dire **どうも** dans « どうもありがとう » ?"),
 C(L,17,["vraiment","peut-être","lentement","encore"],q="Que veut dire **ほんとうに** ?"),
 O(L,18,"Parlez plus lentement, s'il vous plaît.",["もっと","ゆっくり","{話|はな}してください"],uses=["v5-02"]),
 O(L,19,"Je me suis levé, puis j'ai pris une douche.",["{起|お}きました。","それから、","シャワーを","あびました"],uses=["v5-14"]),
]}

# ---------- L38 Durées et fréquences ----------
L = "v5-38"
l38 = {"id": L, "title": "Durées et fréquences", "words": [
 W("〜{度|ど}","〜ど","… fois","{一週間|いっしゅうかん}に{二度|にど}テニスをします。","Je joue au tennis deux fois par semaine."),
 W("〜{週間|しゅうかん}","〜しゅうかん","… semaine(s) (durée)","{日本|にほん}に{二週間|にしゅうかん}いました。","Je suis resté deux semaines au Japon."),
 W("〜か{月|げつ}","〜かげつ","… mois (durée)","{三|さん}か{月|げつ}{日本語|にほんご}を{勉強|べんきょう}しました。","J'ai étudié le japonais pendant trois mois."),
 W("〜{年|ねん}","〜ねん","… an(s) ; l'année …","{五年|ごねん}{日本|にほん}に{住|す}んでいます。","J'habite au Japon depuis cinq ans."),
 W("〜{時間|じかん}","〜じかん","… heure(s) (durée)","{毎日|まいにち}{七時間|しちじかん}ねます。","Je dors sept heures par nuit."),
 W("{毎週|まいしゅう}","まいしゅう","toutes les semaines","{毎週|まいしゅう}{土曜日|どようび}にプールへ{行|い}きます。","Je vais à la piscine tous les samedis."),
 W("{毎月|まいつき}","まいつき","tous les mois","{毎月|まいつき}{家族|かぞく}に{手紙|てがみ}を{書|か}きます。","J'écris à ma famille tous les mois."),
 W("{毎年|まいとし}","まいとし","tous les ans","{毎年|まいとし}{夏|なつ}は{海|うみ}へ{行|い}きます。","Tous les ans, l'été, je vais à la mer."),
 W("{今月|こんげつ}","こんげつ","ce mois-ci","{今月|こんげつ}はいそがしいです。","Ce mois-ci, je suis occupé."),
 W("おととい","おととい","avant-hier","おととい{友|とも}だちに{会|あ}いました。","Avant-hier, j'ai vu un ami."),
 W("あさって","あさって","après-demain","あさってはひまですか。","Tu es libre après-demain ?"),
 W("{一日|いちにち}","いちにち","une journée","{一日|いちにち}に{三時間|さんじかん}{勉強|べんきょう}します。","J'étudie trois heures par jour."),
 W("〜ぐらい","〜ぐらい","environ","{駅|えき}まで{歩|ある}いて{十分|じゅっぷん}ぐらいです。","La gare est à environ dix minutes à pied."),
 W("とき","とき","quand, moment","{子|こ}どものとき、{大阪|おおさか}に{住|す}んでいました。","Quand j'étais enfant, j'habitais à Osaka."),
], "sections": [
 {"h": "D'avant-hier à après-demain",
  "p": ["Tu connais déjà presque tout : il manque les deux bouts de chaque ligne."],
  "grid": {"head": ["", "passé → présent → futur"], "rows": [
   ["jours", "==おととい== → {昨日|きのう} → {今日|きょう} → {明日|あした} → ==あさって=="],
   ["semaines", "{先週|せんしゅう} → {今週|こんしゅう} → {来週|らいしゅう}"],
   ["mois", "{先月|せんげつ} → =={今月|こんげつ}== → {来月|らいげつ}"],
   ["années", "{去年|きょねん} → {今年|ことし} → {来年|らいねん}"],
   ["chaque…", "{毎日|まいにち} · =={毎週|まいしゅう}== · =={毎月|まいつき}== · =={毎年|まいとし}=="]]}},
 {"h": "Pendant combien de temps ?",
  "p": ["Une durée se place devant le verbe, **sans particule**."],
  "grid": {"head": ["", "durée"], "rows": [
   ["heures", "{二時間|にじかん}"],
   ["jours", "{一日|いちにち} · {二日|ふつか} · {三日|みっか}…"],
   ["semaines", "{一週間|いっしゅうかん} · {二週間|にしゅうかん}"],
   ["mois", "{一|いっ}か{月|げつ} · {三|さん}か{月|げつ}"],
   ["années", "{一年|いちねん} · {五年|ごねん}"]]}}
], "pieges": [
 "Durée : **pas de に** → {二時間|にじかん}{勉強|べんきょう}する. Heure précise : に → {二時|にじ}に{勉強|べんきょう}する.",
 "〜か{月|げつ} (durée : trois mois) ≠ 〜{月|がつ} (le mois : {三月|さんがつ} = mars).",
 "{一日|いちにち} (une journée) ≠ {一日|ついたち} (le 1er du mois).",
 "Fréquence : période + **に** + nombre de fois → {一週間|いっしゅうかん}**に**{二度|にど}.",
 "〜ぐらい = environ (durée, quantité) ; 〜ごろ = vers (un moment précis) : {十分|じゅっぷん}ぐらい / {十時|じゅうじ}ごろ.",
 "{毎月|まいつき} et {毎年|まいとし} : つき et とし, lectures japonaises."
], "exercises": [
 C(L,1,["に","で","を","が"],jp="{一週間|いっしゅうかん}＿{二度|にど}テニスをします。",fr="Je joue au tennis deux fois par semaine.",uses=["v5-31"],explain="Fréquence : période + に + nombre de fois."),
 C(L,2,["{毎日|まいにち}{二時間|にじかん}{勉強|べんきょう}します。","{毎日|まいにち}{二時間|にじかん}に{勉強|べんきょう}します。","{毎日|まいにち}に{二時間|にじかん}{勉強|べんきょう}します。","{毎日|まいにち}{二時間|にじかん}を{勉強|べんきょう}します。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-03","v5-14"],explain="Une durée n'a pas de particule ; {毎日|まいにち} non plus."),
 C(L,3,["{三|さん}か{月|げつ}","{三月|さんがつ}","{三週間|さんしゅうかん}","{三年|さんねん}"],q="« pendant trois mois » se dit…",uses=["v5-17"]),
 C(L,4,["おととい","あさって","{昨日|きのう}","{明日|あした}"],jp="{今日|きょう}は{水曜日|すいようび}です。{月曜日|げつようび}は＿でした。",fr="Aujourd'hui, nous sommes mercredi. Lundi, c'était avant-hier.",uses=["v5-03","v5-17"]),
 C(L,5,["あさって","おととい","{明日|あした}","{来週|らいしゅう}"],jp="{今日|きょう}は{水曜日|すいようび}です。＿は{金曜日|きんようび}です。",fr="Aujourd'hui, nous sommes mercredi. Après-demain, c'est vendredi.",uses=["v5-03","v5-17"]),
 C(L,6,["{二週間|にしゅうかん}","{二時|にじ}","{二|ふた}つ","{二|に}まい"],jp="{日本|にほん}に＿いました。とても{楽|たの}しかったです。",fr="Je suis resté deux semaines au Japon. C'était très agréable.",uses=["v5-08","v5-18"]),
 C(L,7,["とき","{時間|じかん}","ぐらい","{度|ど}"],jp="{子|こ}どもの＿、{大阪|おおさか}に{住|す}んでいました。",fr="Quand j'étais enfant, j'habitais à Osaka.",uses=["v5-36"]),
 C(L,8,["ぐらい","ごろ","とき","{度|ど}"],jp="{駅|えき}まで{歩|ある}いて{十分|じゅっぷん}＿です。",fr="La gare est à environ dix minutes à pied.",uses=["v5-16"],explain="Une durée approximative : ぐらい. ごろ, c'est pour une heure précise."),
 C(L,9,["{土曜日|どようび}","{今月|こんげつ}","おととい","あさって"],jp="{毎週|まいしゅう}＿にプールへ{行|い}きます。",fr="Je vais à la piscine tous les samedis.",uses=["v5-17"]),
 C(L,10,["{今月|こんげつ}","おととい","{先月|せんげつ}","{去年|きょねん}"],jp="＿は{仕事|しごと}がたくさんありますから、いそがしいです。",fr="Ce mois-ci, j'ai beaucoup de travail, alors je suis occupé.",uses=["v5-03","v5-17","v5-18"]),
 C(L,11,["いちにち","ついたち","ひとひ","いちび"],q="Dans « 一日に三時間勉強します », comment se lit **一日** ?",uses=["v5-17"]),
 C(L,12,["avant-hier","après-demain","hier soir","la semaine dernière"],q="Que veut dire **おととい** ?"),
 C(L,13,["tous les mois","tous les ans","le mois prochain","ce mois-ci"],q="Que veut dire **{毎月|まいつき}** ?"),
 C(L,14,["{何時間|なんじかん}","{何時|なんじ}","{何度|なんど}","いくら"],jp="{毎日|まいにち}＿ねますか。— {七時間|しちじかん}ぐらいです。",fr="Tu dors combien d'heures par nuit ? — Environ sept heures.",uses=["v5-02","v5-09"]),
 C(L,15,["{八時|はちじ}ごろ","{八時間|はちじかん}ぐらい","{八時|はちじ}まで","{八|はち}ごろ"],q="« vers 8 h » se dit…",uses=["v5-16"]),
 C(L,16,["いっかげつ","いちかげつ","ひとかげつ","いっかがつ"],q=LECT+"**一か月** (un mois) ?"),
 O(L,17,"Je joue au tennis deux fois par semaine.",["{一週間|いっしゅうかん}に","{二度|にど}","テニスを","します"],alt=[["テニスを","{一週間|いっしゅうかん}に","{二度|にど}","します"]],uses=["v5-31"]),
 O(L,18,"J'ai étudié le japonais pendant trois mois.",["{三|さん}か{月|げつ}","{日本語|にほんご}を","{勉強|べんきょう}しました"],alt=[["{日本語|にほんご}を","{三|さん}か{月|げつ}","{勉強|べんきょう}しました"]],uses=["v5-14"]),
]}

# ---------- L39 Petits noms utiles ----------
L = "v5-39"
l39 = {"id": L, "title": "Petits noms utiles", "words": [
 W("{物|もの}","もの","chose, objet","あの{店|みせ}ではいろいろな{物|もの}を{売|う}っています。","Ce magasin vend toutes sortes de choses."),
 W("こと","こと","chose (abstraite), sujet","{日本|にほん}のことをもっと{知|し}りたいです。","Je veux en savoir plus sur le Japon."),
 W("ところ","ところ","endroit","{静|しず}かなところに{住|す}みたいです。","Je veux habiter dans un endroit calme."),
 W("{方|かた}","かた","personne (poli)","あの{方|かた}はどなたですか。","Qui est cette personne ?"),
 W("〜{方|かた}","〜かた","manière de …","この{漢字|かんじ}の{読|よ}み{方|かた}を{教|おし}えてください。","Apprenez-moi comment se lit ce kanji."),
 W("{半分|はんぶん}","はんぶん","moitié","ケーキを{半分|はんぶん}{食|た}べました。","J'ai mangé la moitié du gâteau."),
 W("つぎ","つぎ","suivant, prochain","つぎの{駅|えき}で{降|お}ります。","Je descends à la prochaine gare."),
 W("ほか","ほか","autre","ほかに{質問|しつもん}はありますか。","Avez-vous d'autres questions ?"),
 W("{自分|じぶん}","じぶん","soi-même","{自分|じぶん}の{部屋|へや}をそうじしてください。","Range ta propre chambre."),
 W("{用事|ようじ}","ようじ","affaire, chose à faire","{明日|あした}は{用事|ようじ}があります。","Demain, j'ai quelque chose à faire."),
 W("お{手洗|てあら}い","おてあらい","toilettes","すみません、お{手洗|てあら}いはどこですか。","Excusez-moi, où sont les toilettes ?"),
 W("みなさん","みなさん","tout le monde (en s'adressant à un groupe)","みなさん、おはようございます。","Bonjour à tous."),
 W("{別|べつ}","べつ","autre, différent","これはちょっと{高|たか}いですから、{別|べつ}のをください。","C'est un peu cher, donnez-m'en un autre."),
], "sections": [
 {"h": "もの, こと, ところ, 〜かた",
  "p": ["Quatre petits noms qui servent partout."],
  "grid": {"head": ["", "sens"], "rows": [
   ["{物|もの}", "une chose concrète : {食|た}べ{物|もの}, {飲|の}み{物|もの}, {買|か}い{物|もの}"],
   ["こと", "une chose abstraite, un sujet : {日本|にほん}のこと"],
   ["ところ", "un endroit : {静|しず}かなところ"],
   ["〜{方|かた}", "la manière de : {読|よ}み{方|かた}, {書|か}き{方|かた}, {使|つか}い{方|かた}"]]}}
], "pieges": [
 "{物|もの} = ce qu'on peut toucher ; こと = une idée, un événement, un sujet.",
 "〜{方|かた} : radical du verbe (forme ます sans ます) + {方|かた} → {書|か}き{方|かた}, {行|い}き{方|かた}.",
 "あの{方|かた} = cette personne, en très poli (= あの{人|ひと}).",
 "お{手洗|てあら}い = les toilettes, en poli (= トイレ).",
 "ほかに = d'autre, à part ça : ほかに{何|なに}かありますか.",
 "{自分|じぶん}で = soi-même, tout seul : {自分|じぶん}で{作|つく}りました.",
 "みなさん s'adresse à un groupe ; みんな parle de tout le monde."
], "exercises": [
 C(L,1,["{方|かた}","こと","{物|もの}","ところ"],jp="この{漢字|かんじ}の{読|よ}み＿を{教|おし}えてください。",fr="Apprenez-moi comment se lit ce kanji.",uses=["v5-28","v5-29"]),
 C(L,2,["ところ","こと","{物|もの}","{方|かた}"],jp="{静|しず}かな＿に{住|す}みたいです。",fr="Je veux habiter dans un endroit calme.",uses=["v5-19","v5-36"]),
 C(L,3,["こと","ところ","{半分|はんぶん}","つぎ"],jp="{日本|にほん}の＿をもっと{知|し}りたいです。",fr="Je veux en savoir plus sur le Japon.",uses=["v5-28","v5-37"]),
 C(L,4,["{物|もの}","こと","ところ","{方|かた}"],jp="この{店|みせ}はいろいろな{食|た}べ＿を{売|う}っています。",fr="Ce magasin vend toutes sortes de choses à manger.",uses=["v5-26","v5-37"]),
 C(L,5,["{半分|はんぶん}","ほか","つぎ","{自分|じぶん}"],jp="ケーキを＿{食|た}べました。あとの{半分|はんぶん}は{妹|いもうと}にあげました。",fr="J'ai mangé la moitié du gâteau. J'ai donné l'autre moitié à ma petite sœur.",uses=["v5-21","v5-26"]),
 C(L,6,["つぎ","{半分|はんぶん}","{用事|ようじ}","お{手洗|てあら}い"],jp="＿の{駅|えき}で{降|お}ります。",fr="Je descends à la prochaine gare.",uses=["v5-15"]),
 C(L,7,["お{手洗|てあら}いはどこですか。","お{手洗|てあら}いはだれですか。","お{手洗|てあら}いはいつですか。","お{手洗|てあら}いをどこですか。"],q="Comment demander poliment où sont les toilettes ?",uses=["v5-09"]),
 C(L,8,["{用事|ようじ}","{半分|はんぶん}","つぎ","{方|かた}"],jp="{明日|あした}は＿がありますから、パーティーに{行|い}きません。",fr="Demain j'ai quelque chose à faire, alors je ne vais pas à la fête.",uses=["v5-31"]),
 C(L,9,["{方|かた}","{物|もの}","こと","ところ"],jp="あの＿はどなたですか。",fr="Qui est cette personne ?",uses=["v5-09"]),
 C(L,10,["ほか","{半分|はんぶん}","{自分|じぶん}","{用事|ようじ}"],jp="＿に{質問|しつもん}はありますか。",fr="Avez-vous d'autres questions ?",uses=["v5-29"]),
 C(L,11,["{自分|じぶん}","ほか","つぎ","{方|かた}"],jp="この{料理|りょうり}は{店|みせ}で{買|か}いましたか。— いいえ、＿で{作|つく}りました。",fr="Tu as acheté ce plat au magasin ? — Non, je l'ai fait moi-même.",uses=["v5-27"]),
 C(L,12,["みなさん","{方|かた}","{自分|じぶん}","ほか"],jp="＿、おはようございます。{授業|じゅぎょう}を{始|はじ}めます。",fr="Bonjour à tous. Nous commençons le cours.",uses=["v5-11","v5-29"]),
 C(L,13,["{別|べつ}","{半分|はんぶん}","{自分|じぶん}","{用事|ようじ}"],jp="これはちょっと{高|たか}いですから、＿のをください。",fr="C'est un peu cher, donnez-m'en un autre, s'il vous plaît.",uses=["v5-05"]),
 C(L,14,["la manière d'utiliser, le mode d'emploi","l'utilisateur","l'utilité","l'outil"],q="Que veut dire {使|つか}い{方|かた} ?",uses=["v5-27"]),
 C(L,15,["{何|なに}か{飲|の}み{物|もの}がほしいです。","{何|なに}か{飲|の}みことがほしいです。","{何|なに}か{飲|の}みところがほしいです。","{何|なに}か{飲|の}み{方|かた}がほしいです。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-06"]),
 C(L,16,["じぶん","じふん","しぶん","じぷん"],q=LECT+"**自分** ?"),
 C(L,17,["はんぶん","はんふん","はんぷん","なかぶん"],q=LECT+"**半分** ?"),
 O(L,18,"Apprenez-moi comment s'écrit ce kanji.",["この","{漢字|かんじ}の","{書|か}き{方|かた}を","{教|おし}えてください"],uses=["v5-28","v5-29"]),
 O(L,19,"Je descends à la prochaine gare.",["つぎの","{駅|えき}で","{降|お}ります"],uses=["v5-15"]),
]}

# ---------- L40 Paires piégeuses du N5 ----------
L = "v5-40"
l40 = {"id": L, "title": "Paires piégeuses du N5", "words": [
 W("もどる","もどる","revenir (là où on était)","すぐもどりますから、ここで{待|ま}っていてください。","Je reviens tout de suite, attendez-moi ici."),
 W("{見|み}える","みえる","se voir, être visible","{窓|まど}から{山|やま}が{見|み}えます。","On voit la montagne depuis la fenêtre."),
 W("{聞|き}こえる","きこえる","s'entendre, être audible","となりの{部屋|へや}から{音楽|おんがく}が{聞|き}こえます。","On entend de la musique dans la pièce d'à côté."),
 W("つく","つく","s'allumer","この{部屋|へや}の{電気|でんき}がつきません。","La lumière de cette pièce ne s'allume pas."),
 W("{消|き}える","きえる","s'éteindre ; disparaître","{急|きゅう}に{電気|でんき}が{消|き}えました。","La lumière s'est éteinte d'un coup."),
 W("{同|おな}じ","おなじ","même, identique","{田中|たなか}さんと{私|わたし}は{同|おな}じ{会社|かいしゃ}で{働|はたら}いています。","M. Tanaka et moi travaillons dans la même entreprise."),
 W("{大|おお}きな","おおきな","grand (devant un nom)","{駅|えき}の{前|まえ}に{大|おお}きな{木|き}があります。","Il y a un grand arbre devant la gare."),
 W("{小|ちい}さな","ちいさな","petit (devant un nom)","{小|ちい}さな{町|まち}に{住|す}んでいます。","J'habite dans une petite ville."),
 W("あつい","あつい","chaud (au toucher)","このお{茶|ちゃ}はとてもあついです。","Ce thé est très chaud."),
 W("{答|こた}え","こたえ","réponse","この{問題|もんだい}の{答|こた}えが{分|わ}かりますか。","Tu connais la réponse à cet exercice ?"),
 W("{上|のぼ}る","のぼる","monter","かいだんを{上|のぼ}って、{二|に}かいへ{行|い}きます。","Je monte l'escalier et je vais au premier étage."),
 W("{帰|かえ}り","かえり","retour","{帰|かえ}りにスーパーで{買|か}い{物|もの}をします。","Au retour, je fais les courses au supermarché."),
], "sections": [
 {"h": "Les paires à ne pas confondre",
  "p": ["Ces paires reviennent sans arrêt au JLPT N5. Le nouveau mot est à droite."],
  "grid": {"head": ["", "différence"], "rows": [
   ["{帰|かえ}る / もどる", "rentrer chez soi / revenir là où on était"],
   ["{見|み}る / {見|み}える", "regarder (exprès, を) / être visible (が)"],
   ["{聞|き}く / {聞|き}こえる", "écouter (を) / s'entendre (が)"],
   ["つける / つく", "allumer (を) / s'allumer (が)"],
   ["{消|け}す / {消|き}える", "éteindre (を) / s'éteindre (が)"],
   ["{暑|あつ}い / あつい", "chaud (le temps) / chaud (au toucher)"],
   ["{大|おお}きい / {大|おお}きな", "grand / grand, mais seulement devant un nom"]]}},
 {"h": "Rappel : les paires déjà vues",
  "p": ["{会|あ}う (rencontrer : {友|とも}だち**に**) ≠ {見|み}る (regarder : **を**).",
        "{知|し}る (savoir une information) ≠ {分|わ}かる (comprendre).",
        "{言|い}う (dire des mots : 「…」**と**) ≠ {話|はな}す (parler, converser).",
        "{入|はい}る / {入|い}れる, {出|で}る / {出|だ}す, {開|あ}く / {開|あ}ける : leçon 27."]}
], "pieges": [
 "{見|み}える / {聞|き}こえる : ce qu'on voit ou entend prend **が** : {山|やま}**が**{見|み}えます.",
 "{消|け}す (けす) et {消|き}える (きえる) : même kanji, deux lectures.",
 "{大|おお}きな{木|き} ✓ ; {木|き}が{大|おお}きなです ✗ → {木|き}が{大|おお}きいです.",
 "{同|おな}じ est spécial : pas de な ni de の devant un nom → {同|おな}じ{会社|かいしゃ}.",
 "{帰|かえ}る = rentrer **chez soi** (ou dans son pays) ; もどる = revenir à un endroit qu'on vient de quitter (bureau, place…).",
 "{答|こた}え (nom : la réponse) ≠ {答|こた}える (verbe : répondre)."
], "exercises": [
 C(L,1,["もどります","{帰|かえ}ります","{見|み}えます","{消|き}えます"],jp="{先生|せんせい}はすぐ{教室|きょうしつ}に＿。ちょっと{待|ま}ってください。",fr="Le professeur revient tout de suite en classe. Attendez un peu.",uses=["v5-29","v5-36"],explain="Revenir à un endroit qu'on vient de quitter : もどる. {帰|かえ}る, c'est rentrer chez soi."),
 C(L,2,["{帰|かえ}ります","{見|み}えます","{聞|き}こえます","{消|き}えます"],jp="{仕事|しごと}が{終|お}わって、うちに＿。",fr="Le travail est fini, je rentre à la maison.",uses=["v5-02","v5-22"]),
 C(L,3,["が","を","に","で"],jp="{窓|まど}から{山|やま}＿{見|み}えます。",fr="On voit la montagne depuis la fenêtre.",uses=["v5-35"],explain="{見|み}える : ce qu'on voit prend が."),
 C(L,4,["を","が","に","へ"],jp="{毎晩|まいばん}テレビ＿{見|み}ます。",fr="Je regarde la télé tous les soirs.",uses=["v5-02","v5-12"],explain="{見|み}る (regarder exprès) : を."),
 C(L,5,["{聞|き}こえます","{聞|き}きます","{見|み}えます","{見|み}ます"],jp="となりの{部屋|へや}から{音楽|おんがく}が＿。",fr="On entend de la musique dans la pièce d'à côté.",uses=["v5-31"]),
 C(L,6,["つきません","つけません","{消|け}しません","{見|み}えません"],jp="スイッチをおしましたが、{電気|でんき}が＿。",fr="J'ai appuyé sur l'interrupteur, mais la lumière ne s'allume pas.",uses=["v5-27"],explain="{電気|でんき}**が** : la lumière elle-même → つく."),
 C(L,7,["{消|き}えました","{消|け}しました","つきました","{見|み}えました"],jp="{急|きゅう}に{電気|でんき}が＿。{何|なに}も{見|み}えません。",fr="La lumière s'est éteinte d'un coup. On ne voit plus rien.",uses=["v5-27"]),
 C(L,8,["{同|おな}じ","{同|おな}じな","{同|おな}じの","{同|おな}じい"],jp="{田中|たなか}さんと{私|わたし}は＿{会社|かいしゃ}で{働|はたら}いています。",fr="M. Tanaka et moi travaillons dans la même entreprise.",uses=["v5-14"]),
 C(L,9,["{大|おお}きな","{大|おお}きいな","{大|おお}きの","{大|おお}きく"],jp="{駅|えき}の{前|まえ}に＿{木|き}があります。",fr="Il y a un grand arbre devant la gare.",uses=["v5-35"]),
 C(L,10,["{大|おお}きい","{大|おお}きな","{大|おお}きく","{大|おお}きいな"],jp="この{木|き}はとても＿です。",fr="Cet arbre est très grand.",uses=["v5-05","v5-35"],explain="Devant です, seulement {大|おお}きい. {大|おお}きな ne s'emploie que devant un nom."),
 C(L,11,["あつい","{暑|あつ}い","つめたい","すずしい"],jp="このお{茶|ちゃ}はとても＿ですから、{少|すこ}し{待|ま}ってから{飲|の}みます。",fr="Ce thé est très chaud, alors j'attends un peu avant de le boire.",uses=["v5-24","v5-25"]),
 C(L,12,["{答|こた}え","{答|こた}える","{答|こた}えて","{答|こた}えます"],jp="この{問題|もんだい}の＿が{分|わ}かりますか。",fr="Tu connais la réponse à cet exercice ?",uses=["v5-28","v5-29"]),
 C(L,13,["{上|のぼ}って","わたって","{入|い}れて","{消|け}して"],jp="かいだんを＿、{二|に}かいへ{行|い}きます。",fr="Je monte l'escalier et je vais au premier étage.",uses=["v5-22"]),
 C(L,14,["{帰|かえ}り","{帰|かえ}る","{帰|かえ}って","もどる"],jp="＿にスーパーで{買|か}い{物|もの}をします。",fr="Au retour, je fais les courses au supermarché.",uses=["v5-32"]),
 C(L,15,["に","を","で","へ"],jp="{昨日|きのう}、{駅|えき}で{先生|せんせい}＿{会|あ}いました。",fr="Hier, j'ai croisé le professeur à la gare.",uses=["v5-02"],explain="{会|あ}う : la personne rencontrée prend に."),
 C(L,16,["{分|わ}かります","{知|し}ります","{知|し}っています","{言|い}います"],jp="{日本語|にほんご}が{少|すこ}し＿。",fr="Je comprends un peu le japonais.",uses=["v5-10","v5-28"]),
 C(L,17,["{話|はな}しました","{言|い}いました","{知|し}りました","{分|わ}かりました"],jp="{田中|たなか}さんと{電話|でんわ}で{一時間|いちじかん}＿。",fr="J'ai parlé une heure au téléphone avec M. Tanaka.",uses=["v5-02","v5-28"]),
 C(L,18,["on voit (c'est visible)","je regarde exprès","je montre","je cherche"],q="Dans « {窓|まど}から{海|うみ}が{見|み}えます », que veut dire {見|み}えます ?"),
 C(L,19,["きえる","けえる","けせる","しょうえる"],q=LECT+"**消える** ?"),
 O(L,20,"On voit la mer depuis ma chambre.",["{部屋|へや}から","{海|うみ}が","{見|み}えます"],alt=[["{海|うみ}が","{部屋|へや}から","{見|み}えます"]],uses=["v5-04","v5-35"]),
]}

TC, TO, XC, XO = make_block("v5-b08", "v5-x04")
test = [
 TC(1,["{急|いそ}いで","すわって","つかれて","{住|す}んで"],jp="もうすぐ{電車|でんしゃ}が{出|で}ますから、＿ください。",fr="Le train part bientôt, alors dépêchez-vous.",uses=["v5-15","v5-36"]),
 TC(2,["{一週間|いっしゅうかん}に{三度|さんど}","{三度|さんど}に{一週間|いっしゅうかん}","{一週間|いっしゅうかん}を{三度|さんど}","{三週間|さんしゅうかん}に{一度|いちど}"],q="« trois fois par semaine » se dit…",uses=["v5-38"]),
 TC(3,["だから","でも","{先|さき}に","もっと"],jp="{雨|あめ}です。＿、{出|で}かけません。",fr="Il pleut. Donc je ne sors pas.",uses=["v5-14","v5-37"]),
 TC(4,["しています","します","していません","しませんでした"],jp="{姉|あね}はけっこん＿。{子|こ}どもが{一人|ひとり}います。",fr="Ma grande sœur est mariée. Elle a un enfant.",uses=["v5-36"]),
 TC(5,["が","を","で","へ"],jp="{窓|まど}からふじさん＿{見|み}えます。",fr="On voit le mont Fuji depuis la fenêtre.",uses=["v5-40"]),
 TC(6,["{金曜日|きんようび}","{土曜日|どようび}","{水曜日|すいようび}","{月曜日|げつようび}"],jp="{明日|あした}は{木曜日|もくようび}です。あさっては＿です。",fr="Demain, c'est jeudi. Après-demain, c'est vendredi.",uses=["v5-17","v5-38"]),
 TC(7,["とき","ところ","こと","{物|もの}"],jp="{子|こ}どもの＿、{犬|いぬ}がいました。",fr="Quand j'étais enfant, j'avais un chien.",uses=["v5-35","v5-38"]),
 TC(8,["{方|かた}","こと","ところ","{物|もの}"],jp="この{漢字|かんじ}の{書|か}き＿が{分|わ}かりません。",fr="Je ne sais pas comment s'écrit ce kanji.",uses=["v5-39"]),
 TC(9,["ぐらい","ごろ","とき","{度|ど}"],jp="{毎日|まいにち}{六時間|ろくじかん}＿ねます。",fr="Je dors environ six heures par nuit.",uses=["v5-38"]),
 TC(10,["ゆっくり","いちばん","たぶん","あとで"],jp="すみません、もっと＿{話|はな}してください。",fr="Excusez-moi, parlez plus lentement, s'il vous plaît.",uses=["v5-37"]),
 TC(11,["{消|き}えました","{消|け}しました","つけました","{見|み}えました"],jp="{風|かぜ}で、ろうそくの{火|ひ}が＿。",fr="Avec le vent, la flamme de la bougie s'est éteinte.",uses=["v5-25","v5-40"]),
 TC(12,["{帰|かえ}りました","{見|み}えました","{聞|き}こえました","{上|のぼ}りました"],jp="{仕事|しごと}が{終|お}わって、{家|いえ}に＿。",fr="Le travail fini, je suis rentré à la maison.",uses=["v5-40"]),
 TO(13,"J'ai mangé la moitié du gâteau.",["ケーキを","{半分|はんぶん}","{食|た}べました"],uses=["v5-39"]),
 TC(14,["ほんとうにありがとうございました。","だからありがとうございました。","いちばんありがとうございました。","たぶんありがとうございました。"],q="Tu remercies quelqu'un très sincèrement :",uses=["v5-37"]),
 TC(15,["ほか","{半分|はんぶん}","{自分|じぶん}","{同|おな}じ"],jp="＿に{何|なに}かありますか。— いいえ、それだけです。",fr="Il y a autre chose ? — Non, c'est tout.",uses=["v5-39"]),
 TC(16,["{大|おお}きな{家|いえ}に{住|す}んでいます。","{大|おお}きなの{家|いえ}に{住|す}んでいます。","{家|いえ}が{大|おお}きなです。","{大|おお}きいな{家|いえ}に{住|す}んでいます。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-36","v5-40"]),
]
exam = [
 XC(1,["{妹|いもうと}はフランスで{生|う}まれて、{今|いま}は{東京|とうきょう}に{住|す}んでいます。","{妹|いもうと}はフランスで{生|う}まれて、{今|いま}は{東京|とうきょう}で{住|す}んでいます。","{妹|いもうと}はフランスで{生|う}まれて、{今|いま}は{東京|とうきょう}を{住|す}んでいます。","{妹|いもうと}はフランスで{生|う}まれて、{今|いま}は{東京|とうきょう}に{住|す}みます。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-21","v5-36"]),
 XC(2,["だから","でも","たぶん","いちばん"],jp="{雨|あめ}が{降|ふ}っていました。＿、{友|とも}だちにかさを{貸|か}しました。",fr="Il pleuvait. C'est pourquoi j'ai prêté mon parapluie à un ami.",uses=["v5-25","v5-26","v5-37"]),
 XC(3,["わたって","まがって","{上|のぼ}って","{降|お}りて"],jp="つぎのかどを{左|ひだり}にまがって、はしを＿、まっすぐ{行|い}ってください。",fr="Tournez à gauche au prochain coin, traversez le pont et allez tout droit.",uses=["v5-20","v5-32"]),
 XC(4,["ぐらい","ごろ","とき","{度|ど}"],jp="{毎朝|まいあさ}{犬|いぬ}と{三十分|さんじゅっぷん}＿さんぽします。",fr="Tous les matins, je promène le chien une trentaine de minutes.",uses=["v5-35","v5-38"]),
 XC(5,["ばい","はい","ぱい","びき"],jp="コーヒーを{三|さん}＿{飲|の}みました。",fr="J'ai bu trois tasses de café.",uses=["v5-34"]),
 XC(6,["あつい","{暑|あつ}い","すずしい","{寒|さむ}い"],jp="このスープはとても＿ですから、{少|すこ}し{待|ま}ちます。",fr="Cette soupe est très chaude, alors j'attends un peu.",uses=["v5-25","v5-36","v5-40"]),
 XC(7,["かえし","{借|か}り","{売|う}り","くれ"],jp="{図書館|としょかん}で{借|か}りた{本|ほん}を＿に{行|い}きます。",fr="Je vais rendre les livres empruntés à la bibliothèque.",uses=["v5-26","v5-31"]),
 XO(8,"Il y a trois chiens et un chat dans le jardin.",["にわに","{犬|いぬ}が{三|さん}びきと","ねこが{一|いっ}ぴき","います"],uses=["v5-22","v5-35"]),
 XC(9,["à tous les élèves","à un élève en particulier","à lui-même","au directeur"],q="Le professeur entre en classe : みなさん、おはようございます. À qui parle-t-il ?",uses=["v5-29","v5-39"]),
 XC(10,["{見|み}えます","{見|み}ます","{見|み}せます","{見|み}えません"],jp="{部屋|へや}から{海|うみ}が＿。とてもきれいです。",fr="On voit la mer depuis la chambre. C'est très beau.",uses=["v5-35","v5-40"]),
 XC(11,["{四月|しがつ}{二十九日|にじゅうくにち}","{四月|しがつ}{三十日|さんじゅうにち}","{五月|ごがつ}{三日|みっか}","{四月|しがつ}{二十八日|にじゅうはちにち}"],q="Aujourd'hui, nous sommes le {五月|ごがつ}{一日|ついたち}. おととい, c'était le…",uses=["v5-17","v5-38"],explain="Avril a 30 jours : la veille du 1er mai est le 30 avril, l'avant-veille le 29."),
 XC(12,["こまりました","つかれました","{生|う}まれました","{止|と}まりました"],jp="{電車|でんしゃ}にかさをわすれて、＿。{外|そと}は{雨|あめ}です。",fr="J'ai oublié mon parapluie dans le train, j'étais bien embêté. Dehors, il pleut.",uses=["v5-28","v5-36"]),
 XC(13,["{作|つく}ります","{使|つか}います","{消|け}します","{借|か}ります"],jp="{田中|たなか}さんは{料理|りょうり}が{上手|じょうず}です。{毎日|まいにち}{自分|じぶん}でおべんとうを＿。",fr="M. Tanaka cuisine bien. Tous les jours, il prépare lui-même son bentō.",uses=["v5-19","v5-27","v5-34","v5-39"]),
 XC(14,["{先生|せんせい}","{学生|がくせい}","{医者|いしゃ}","{店員|てんいん}"],jp="{兄|あに}は{大学|だいがく}で{英語|えいご}を{教|おし}えています。{兄|あに}の{仕事|しごと}は＿です。",fr="Mon grand frère enseigne l'anglais à l'université. Son métier : professeur.",uses=["v5-28","v5-30","v5-33"]),
 XC(15,["Le matin, on entend les oiseaux par la fenêtre.","Le matin, j'écoute la radio près de la fenêtre.","Le matin, on voit des oiseaux par la fenêtre.","Le matin, les oiseaux entrent par la fenêtre."],q="Que veut dire : {朝|あさ}、{窓|まど}から{鳥|とり}の{声|こえ}が{聞|き}こえます。",uses=["v5-23","v5-35","v5-40"]),
]
bloc = {"id": "v5-b08", "level": "N5", "title": "Consolider le N5 : états, liaisons, durées, petits noms, paires",
        "lessons": [l36, l37, l38, l39, l40], "test": test, "examTest": exam}
save(bloc, sys.argv[1])
