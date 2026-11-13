import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L61 Loisirs et événements ----------
L = "v4-61"
l61 = {"id": L, "title": "Loisirs et événements", "words": [
 W("しゅみ","しゅみ","loisir, passe-temps","しゅみは{写真|しゃしん}をとることです。","Mon passe-temps, c'est la photo."),
 W("きょうみ","きょうみ","intérêt","{日本|にほん}のれきしにきょうみがあります。","Je m'intéresse à l'histoire du Japon."),
 W("おまつり","おまつり","fête (traditionnelle)","{夏|なつ}になると、{町|まち}でおまつりがあります。","En été, il y a une fête en ville."),
 W("{花見|はなみ}","はなみ","contemplation des cerisiers","{春|はる}は{公園|こうえん}で{花見|はなみ}をします。","Au printemps, on va admirer les cerisiers au parc."),
 W("{見物|けんぶつ}する","けんぶつする","visiter (en touriste)","{京都|きょうと}で{古|ふる}いおてらを{見物|けんぶつ}しました。","J'ai visité de vieux temples à Kyoto."),
 W("{試合|しあい}","しあい","match","{明日|あした}はサッカーの{試合|しあい}があります。","Demain, il y a un match de foot."),
 W("てんらんかい","てんらんかい","exposition","{週末|しゅうまつ}、{写真|しゃしん}のてんらんかいに{行|い}きました。","Ce week-end, je suis allé à une exposition de photos."),
 W("つり","つり","pêche (à la ligne)","{父|ちち}は{日曜日|にちようび}によく{川|かわ}でつりをします。","Mon père va souvent pêcher à la rivière le dimanche."),
 W("{小説|しょうせつ}","しょうせつ","roman","ねる{前|まえ}に{小説|しょうせつ}を{読|よ}みます。","Je lis un roman avant de dormir."),
 W("まんが","まんが","manga, bande dessinée","{日本|にほん}のまんがは{外国|がいこく}でも{人気|にんき}があります。","Les mangas japonais sont populaires à l'étranger aussi."),
 W("がっき","がっき","instrument de musique","{何|なに}かがっきをひきますか。— ギターをひきます。","Tu joues d'un instrument ? — De la guitare."),
 W("ハイキング","ハイキング","randonnée","{週末|しゅうまつ}は{山|やま}へハイキングに{行|い}きます。","Ce week-end, je vais faire de la randonnée en montagne."),
 W("ドライブ","ドライブ","promenade en voiture","{天気|てんき}がいいので、{海|うみ}までドライブしました。","Il faisait beau, alors on est allés en voiture jusqu'à la mer."),
 W("{音楽会|おんがくかい}","おんがくかい","concert (d'école)","{学校|がっこう}の{音楽会|おんがくかい}でピアノをひきました。","J'ai joué du piano au concert de l'école."),
 W("{運動会|うんどうかい}","うんどうかい","fête sportive (de l'école)","{秋|あき}に{小学校|しょうがっこう}で{運動会|うんどうかい}があります。","En automne, il y a la fête sportive à l'école primaire."),
], "sections": [
 {"h": "Parler de ses loisirs",
  "p": ["Pour dire son loisir : しゅみは + verbe + **こと**です."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["mon loisir, c'est…", "しゅみ==は==〜ことです"],
   ["s'intéresser à", "〜==に==きょうみ==が==ある"],
   ["aller faire…", "ハイキング・つり==に=={行|い}く"],
   ["admirer les cerisiers", "{花見|はなみ}==を==する"],
   ["visiter (touriste)", "〜==を=={見物|けんぶつ}する"]]}}
], "pieges": [
 "しゅみ = ce qu'on fait par plaisir, souvent ; きょうみ = intérêt (〜**に**きょうみがある).",
 "しゅみは + verbe + **こと**です : しゅみは{泳|およ}ぐことです.",
 "{花見|はなみ} : on va voir les cerisiers en fleurs au printemps, souvent avec un pique-nique.",
 "〜{会|かい} = réunion, fête : {音楽会|おんがくかい}, {運動会|うんどうかい}, てんらんかい.",
 "がっきを**ひく** (instrument à cordes, clavier) : rappel de la leçon 31.",
 "{見物|けんぶつ} se lit けんぶつ quand c'est « visiter »."
], "exercises": [
 C(L,1,["しゅみ","きょうみ","{試合|しあい}","つり"],jp="＿は{写真|しゃしん}をとることです。{毎週|まいしゅう}{山|やま}へとりに{行|い}きます。",fr="Mon passe-temps, c'est la photo. Je vais en prendre en montagne toutes les semaines.",uses=["v5-38"]),
 C(L,2,["きょうみ","しゅみ","{試合|しあい}","おまつり"],jp="{日本|にほん}のれきしに＿があります。",fr="Je m'intéresse à l'histoire du Japon.",uses=["v4-52"]),
 C(L,3,["おまつり","てんらんかい","{小説|しょうせつ}","つり"],jp="{夏|なつ}になると、{町|まち}で＿があって、みんなでおどります。",fr="En été, il y a une fête en ville et tout le monde danse.",uses=["v4-45"]),
 C(L,4,["{花見|はなみ}","{見物|けんぶつ}","まんが","がっき"],jp="{春|はる}は{公園|こうえん}で＿をします。さくらがきれいです。",fr="Au printemps, on admire les cerisiers au parc. Ils sont magnifiques.",uses=["v5-25"]),
 C(L,5,["{見物|けんぶつ}","{花見|はなみ}","ドライブ","つり"],jp="{京都|きょうと}で{古|ふる}いおてらを＿しました。",fr="J'ai visité de vieux temples à Kyoto.",uses=["v5-33"]),
 C(L,6,["{試合|しあい}","{小説|しょうせつ}","まんが","がっき"],jp="{明日|あした}はサッカーの＿がありますから、{早|はや}くねます。",fr="Demain il y a un match de foot, alors je me couche tôt.",uses=["v5-31"]),
 C(L,7,["てんらんかい","つり","ドライブ","{運動会|うんどうかい}"],jp="{週末|しゅうまつ}、{写真|しゃしん}の＿に{行|い}きました。きれいな{写真|しゃしん}がたくさんありました。",fr="Ce week-end, je suis allé à une exposition de photos. Il y avait plein de belles photos.",uses=["v5-12"]),
 C(L,8,["つり","ドライブ","{花見|はなみ}","ハイキング"],jp="{父|ちち}は{日曜日|にちようび}によく{川|かわ}で＿をします。{魚|さかな}がたくさんとれます。",fr="Mon père va souvent pêcher à la rivière le dimanche. Il attrape beaucoup de poissons.",uses=["v5-35"]),
 C(L,9,["{小説|しょうせつ}","がっき","{試合|しあい}","{運動会|うんどうかい}"],jp="ねる{前|まえ}に＿を{読|よ}みます。",fr="Je lis un roman avant de dormir.",uses=["v5-02"]),
 C(L,10,["まんが","がっき","{試合|しあい}","つり"],jp="{日本|にほん}の＿は{外国|がいこく}でも{人気|にんき}があります。{子|こ}どもも{大人|おとな}も{読|よ}みます。",fr="Les mangas japonais sont populaires à l'étranger aussi. Enfants et adultes en lisent.",uses=["v5-33"]),
 C(L,11,["がっき","まんが","{小説|しょうせつ}","{試合|しあい}"],jp="{何|なに}か＿をひきますか。— はい、ギターをひきます。",fr="Tu joues d'un instrument ? — Oui, de la guitare.",uses=["v5-31"]),
 C(L,12,["ハイキング","まんが","{小説|しょうせつ}","がっき"],jp="{週末|しゅうまつ}は{山|やま}へ＿に{行|い}きます。",fr="Ce week-end, je vais faire de la randonnée en montagne.",uses=["v5-35"]),
 C(L,13,["ドライブ","ハイキング","つり","{見物|けんぶつ}"],jp="{天気|てんき}がいいので、{車|くるま}で{海|うみ}まで＿しました。",fr="Il faisait beau, alors on est allés en voiture jusqu'à la mer.",uses=["v5-15"]),
 C(L,14,["{運動会|うんどうかい}","{音楽会|おんがくかい}","てんらんかい","{花見|はなみ}"],jp="{秋|あき}に{小学校|しょうがっこう}で＿があります。{子|こ}どもたちがいっしょうけんめい{走|はし}ります。",fr="En automne, il y a la fête sportive à l'école primaire. Les enfants courent de toutes leurs forces.",uses=["v4-52","v4-55"]),
 C(L,15,["loisir, passe-temps","intérêt","talent","travail"],q="Que veut dire **しゅみ** ?"),
 C(L,16,["けんぶつ","げんぶつ","けんもの","みぶつ"],q=LECT+"**見物** (visiter) ?"),
 O(L,17,"Je m'intéresse à l'histoire du Japon.",["{日本|にほん}の","れきしに","きょうみが","あります"],uses=["v4-52"]),
 O(L,18,"Mon passe-temps, c'est la pêche.",["{私|わたし}の","しゅみは","つり","です"]),
]}

# ---------- L62 Voyage et tourisme ----------
L = "v4-62"
l62 = {"id": L, "title": "Voyage et tourisme", "words": [
 W("くうこう","くうこう","aéroport","くうこうまでバスで{一時間|いちじかん}です。","L'aéroport est à une heure en bus."),
 W("かんこう","かんこう","tourisme","かんこうで{京都|きょうと}に{来|き}ました。","Je suis venu à Kyoto en touriste."),
 W("{旅館|りょかん}","りょかん","auberge japonaise","{日本|にほん}の{旅館|りょかん}にとまってみたいです。","J'aimerais dormir dans une auberge japonaise."),
 W("けしき","けしき","paysage, vue","{山|やま}の{上|うえ}から{見|み}るけしきはきれいです。","La vue du haut de la montagne est magnifique."),
 W("かたみち","かたみち","aller simple","{東京|とうきょう}までかたみちでいくらですか。","Combien coûte un aller simple pour Tokyo ?"),
 W("おうふく","おうふく","aller-retour","おうふくのきっぷを{買|か}いました。","J'ai acheté un billet aller-retour."),
 W("〜{行|ゆ}き","〜ゆき","à destination de …","これは{東京|とうきょう}{行|ゆ}きの{電車|でんしゃ}ですか。","C'est bien le train pour Tokyo ?"),
 W("とまる","とまる","loger, passer la nuit","{昨日|きのう}はホテルにとまりました。","Hier, j'ai dormi à l'hôtel."),
 W("みなと","みなと","port","みなとの{近|ちか}くで{魚|さかな}を{食|た}べました。","J'ai mangé du poisson près du port."),
 W("しま","しま","île","{日本|にほん}にはしまがたくさんあります。","Il y a beaucoup d'îles au Japon."),
 W("みずうみ","みずうみ","lac","みずうみでボートに{乗|の}りました。","J'ai fait du bateau sur le lac."),
 W("おんせん","おんせん","source chaude","{冬|ふゆ}はおんせんに{入|はい}りたいです。","En hiver, j'ai envie d'aller aux sources chaudes."),
 W("{海外|かいがい}","かいがい","étranger (outre-mer)","{毎年|まいとし}{海外|かいがい}{旅行|りょこう}をします。","Je voyage à l'étranger tous les ans."),
 W("{旅|たび}","たび","voyage","{一人|ひとり}で{旅|たび}をするのが{好|す}きです。","J'aime voyager seul."),
 W("{地方|ちほう}","ちほう","région","この{地方|ちほう}は{冬|ふゆ}にゆきがたくさん{降|ふ}ります。","Dans cette région, il neige beaucoup en hiver."),
], "sections": [
 {"h": "Billets et hébergement",
  "p": ["Les mots du guichet et de l'hôtel."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["aller simple / aller-retour", "かたみち / おうふく"],
   ["le train pour Tokyo", "{東京|とうきょう}{行|ゆ}きの{電車|でんしゃ}"],
   ["loger à", "〜==に==とまる"],
   ["auberge japonaise", "{旅館|りょかん} (tatamis, bains)"],
   ["voyage à l'étranger", "{海外|かいがい}{旅行|りょこう}"]]}}
], "pieges": [
 "〜**に**とまる = loger à (hôtel, auberge). Même son que {止|と}まる (s'arrêter, leçon 36).",
 "〜{行|ゆ}き = à destination de : {大阪|おおさか}{行|ゆ}きのバス (on entend aussi いき).",
 "けしき = le paysage, la vue.",
 "{旅|たび} = voyage (un peu littéraire) ; {旅行|りょこう} = voyage (courant) ; かんこう = tourisme.",
 "{海外|かいがい} = l'étranger (outre-mer), presque comme {外国|がいこく}.",
 "おんせん**に{入|はい}る** = aller au bain des sources chaudes."
], "exercises": [
 C(L,1,["くうこう","みなと","しま","みずうみ"],jp="{飛行機|ひこうき}は{三時|さんじ}ですから、{一時|いちじ}に＿に{着|つ}きたいです。",fr="L'avion est à trois heures, alors je veux arriver à l'aéroport à une heure.",uses=["v5-15"]),
 C(L,2,["かんこう","おうふく","けしき","{地方|ちほう}"],jp="＿で{京都|きょうと}に{来|き}ました。{古|ふる}いおてらを{見|み}たいです。",fr="Je suis venu à Kyoto en touriste. Je veux voir les vieux temples.",uses=["v5-33"]),
 C(L,3,["{旅館|りょかん}","くうこう","みなと","しま"],jp="たたみの{部屋|へや}でねてみたいですから、＿にとまります。",fr="Je veux essayer de dormir dans une chambre à tatamis, alors je loge dans une auberge japonaise.",uses=["v5-22"]),
 C(L,4,["けしき","かんこう","かたみち","{旅|たび}"],jp="{山|やま}の{上|うえ}から{見|み}る＿はとてもきれいです。",fr="La vue du haut de la montagne est magnifique.",uses=["v5-35"]),
 C(L,5,["かたみち","おうふく","かんこう","けしき"],jp="{東京|とうきょう}まで＿でいくらですか。— {行|い}きだけですね。{五千円|ごせんえん}です。",fr="Combien coûte un aller simple pour Tokyo ? — Seulement l'aller ? Cinq mille yens.",uses=["v5-07"]),
 C(L,6,["おうふく","かたみち","{旅館|りょかん}","しま"],jp="{帰|かえ}りのきっぷもいりますから、＿のきっぷをください。",fr="J'ai aussi besoin du retour, alors un billet aller-retour, s'il vous plaît.",uses=["v5-36","v5-40"]),
 C(L,7,["{行|ゆ}き","かたみち","おうふく","かんこう"],jp="すみません、これは{大阪|おおさか}＿の{電車|でんしゃ}ですか。",fr="Excusez-moi, c'est bien le train pour Osaka ?",uses=["v5-15"]),
 C(L,8,["とまりました","とどきました","{乗|の}りかえました","かよいました"],jp="{昨日|きのう}は{駅|えき}の{近|ちか}くのホテルに＿。",fr="Hier, j'ai dormi dans un hôtel près de la gare.",uses=["v5-33"]),
 C(L,9,["みなと","くうこう","おうふく","けしき"],jp="＿の{近|ちか}くで、とれたばかりの{魚|さかな}を{食|た}べました。",fr="Près du port, j'ai mangé du poisson tout juste pêché.",uses=["v5-06"]),
 C(L,10,["しま","みなと","みずうみ","おんせん"],jp="{日本|にほん}は＿の{国|くに}です。{大|おお}きいのが{四|よっ}つあります。",fr="Le Japon est un pays d'îles. Il y en a quatre grandes.",uses=["v5-08"]),
 C(L,11,["みずうみ","しま","くうこう","おんせん"],jp="＿でボートに{乗|の}りました。{水|みず}がとてもきれいでした。",fr="J'ai fait du bateau sur le lac. L'eau était très claire.",uses=["v5-15"]),
 C(L,12,["おんせん","みずうみ","みなと","しま"],jp="{寒|さむ}い{日|ひ}は、＿に{入|はい}ると{体|からだ}があたたかくなります。",fr="Les jours de froid, quand on entre dans un bain de source chaude, le corps se réchauffe.",uses=["v5-23","v5-25"]),
 C(L,13,["{海外|かいがい}","{地方|ちほう}","かたみち","おうふく"],jp="{毎年|まいとし}{夏|なつ}は＿{旅行|りょこう}に{行|い}きます。{去年|きょねん}はイタリアでした。",fr="Tous les étés, je pars en voyage à l'étranger. L'an dernier, c'était l'Italie.",uses=["v5-38"]),
 C(L,14,["{旅|たび}","しま","みなと","くうこう"],jp="{一人|ひとり}で＿をするのが{好|す}きです。いろいろな{町|まち}を{見|み}ます。",fr="J'aime voyager seul. Je vois toutes sortes de villes.",uses=["v5-37"]),
 C(L,15,["{地方|ちほう}","{旅|たび}","かたみち","おうふく"],jp="この＿は{冬|ふゆ}にゆきがたくさん{降|ふ}ります。",fr="Dans cette région, il neige beaucoup en hiver.",uses=["v5-25"]),
 C(L,16,["{旅館|りょかん}にとまります。","{旅館|りょかん}をとまります。","{旅館|りょかん}がとまります。","{旅館|りょかん}にとめます。"],q="« Je loge dans une auberge japonaise » se dit…"),
 C(L,17,["かいがい","うみそと","かいそと","うみがい"],q=LECT+"**海外** ?"),
 O(L,18,"Un aller-retour pour Kyoto, s'il vous plaît.",["{京都|きょうと}まで","おうふく","おねがいします"],uses=["v5-11"]),
]}

# ---------- L63 Nature et météo (2) ----------
L = "v4-63"
l63 = {"id": L, "title": "Ciel, météo, catastrophes", "words": [
 W("{台風|たいふう}","たいふう","typhon","{台風|たいふう}で{電車|でんしゃ}が{止|と}まりました。","Les trains se sont arrêtés à cause du typhon."),
 W("じしん","じしん","tremblement de terre","{昨日|きのう}の{夜|よる}、{大|おお}きいじしんがありました。","Hier soir, il y a eu un gros tremblement de terre."),
 W("{火事|かじ}","かじ","incendie","{昨日|きのう}、{駅|えき}の{近|ちか}くで{火事|かじ}がありました。","Hier, il y a eu un incendie près de la gare."),
 W("ほし","ほし","étoile","{山|やま}の{上|うえ}ではほしがたくさん{見|み}えます。","En montagne, on voit beaucoup d'étoiles."),
 W("{月|つき}","つき","lune","{今夜|こんや}は{月|つき}がきれいですね。","La lune est belle ce soir."),
 W("{晴|は}れる","はれる","s'éclaircir, faire beau","{明日|あした}は{晴|は}れるでしょう。","Demain, il fera sans doute beau."),
 W("くもる","くもる","se couvrir (nuages)","{午後|ごご}からくもってきました。","Le ciel se couvre depuis l'après-midi."),
 W("{光|ひか}る","ひかる","briller","{空|そら}で{何|なに}かが{光|ひか}りました。","Quelque chose a brillé dans le ciel."),
 W("きおん","きおん","température (de l'air)","{今日|きょう}はきおんが{高|たか}いですね。","Il fait chaud aujourd'hui (la température est élevée)."),
 W("{天気|てんき}よほう","てんきよほう","prévisions météo","{天気|てんき}よほうによると、{明日|あした}は{雨|あめ}です。","D'après la météo, il pleuvra demain."),
 W("{空気|くうき}","くうき","air","{山|やま}の{空気|くうき}はおいしいです。","L'air de la montagne est pur."),
 W("くも","くも","nuage","{空|そら}にくもが{一|ひと}つもありません。","Il n'y a pas un nuage dans le ciel."),
 W("かみなり","かみなり","tonnerre, foudre","かみなりがなって、こわかったです。","Le tonnerre a grondé, j'ai eu peur."),
 W("いし","いし","pierre","{子|こ}どもが{川|かわ}にいしをなげています。","Un enfant lance des pierres dans la rivière."),
 W("むし","むし","insecte","{夏|なつ}の{夜|よる}はむしがたくさんいます。","Les nuits d'été, il y a beaucoup d'insectes."),
], "sections": [
 {"h": "Le ciel et la météo",
  "p": ["Les noms de la leçon 25 ({晴|は}れ, くもり) ont leurs verbes : {晴|は}れる, くもる."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["il fait beau / ça se couvre", "{晴|は}れる / くもる"],
   ["selon la météo", "{天気|てんき}よほう==によると=="],
   ["température élevée / basse", "きおん==が=={高|たか}い / {低|ひく}い"],
   ["le tonnerre gronde", "かみなり==が==なる"],
   ["catastrophes", "{台風|たいふう} · じしん · {火事|かじ}"]]}}
], "pieges": [
 "きおんが**{高|たか}い** / **{低|ひく}い** (température) — jamais きおんが{暑|あつ}い.",
 "{空気|くうき}がおいしい = l'air est pur, agréable à respirer.",
 "くも (nuage) et くもる (se couvrir) : même racine. くもってきました = ça commence à se couvrir.",
 "{月|つき} = la lune (et « un mois » : {一|ひと}つき) ; 〜{月|がつ} = le nom du mois.",
 "〜によると = selon, d'après (les prévisions, la radio) : souvent suivi de 〜そうです.",
 "Une catastrophe « a lieu » : じしん**が**ある, {火事|かじ}**が**ある."
], "exercises": [
 C(L,1,["{台風|たいふう}","ほし","{月|つき}","{空気|くうき}"],jp="＿で{電車|でんしゃ}が{止|と}まって、{会社|かいしゃ}に{行|い}けませんでした。",fr="Les trains se sont arrêtés à cause du typhon, je n'ai pas pu aller au bureau.",uses=["v5-36"]),
 C(L,2,["じしん","ほし","くも","むし"],jp="{昨日|きのう}の{夜|よる}、{大|おお}きい＿がありました。とてもこわかったです。",fr="Hier soir, il y a eu un gros tremblement de terre. J'ai eu très peur.",uses=["v4-41"]),
 C(L,3,["{火事|かじ}","{台風|たいふう}","ほし","くも"],jp="{駅|えき}の{近|ちか}くで＿があって、{家|いえ}が{三|みっ}つもえました。",fr="Il y a eu un incendie près de la gare : trois maisons ont brûlé.",uses=["v4-56"]),
 C(L,4,["ほし","いし","きおん","{空気|くうき}"],jp="{山|やま}の{上|うえ}では、{夜|よる}＿がたくさん{見|み}えます。",fr="En montagne, la nuit, on voit beaucoup d'étoiles.",uses=["v5-40"]),
 C(L,5,["{月|つき}","ほし","くも","かみなり"],jp="{今夜|こんや}は＿がまるくて、きれいですね。",fr="Ce soir, la lune est pleine et belle.",uses=["v5-19"]),
 C(L,6,["{晴|は}れる","{光|ひか}る","もえる","わく"],jp="{明日|あした}は＿でしょう。{天気|てんき}よほうでそう{言|い}っていました。",fr="Demain, il fera sans doute beau. C'est ce qu'ils ont dit à la météo.",uses=["v5-25"]),
 C(L,7,["くもって","{晴|は}れて","{光|ひか}って","もえて"],jp="{午後|ごご}から{空|そら}が＿きました。{雨|あめ}が{降|ふ}るかもしれません。",fr="Le ciel se couvre depuis l'après-midi. Il va peut-être pleuvoir.",uses=["v5-25"]),
 C(L,8,["{光|ひか}りました","くもりました","{晴|は}れました","わきました"],jp="{夜|よる}の{空|そら}で、{何|なに}かが＿。{飛行機|ひこうき}でしょうか。",fr="Quelque chose a brillé dans le ciel nocturne. Un avion, peut-être ?",uses=["v5-15"]),
 C(L,9,["きおん","{空気|くうき}","{天気|てんき}よほう","くも"],jp="{今日|きょう}は＿が{高|たか}くて、{暑|あつ}いです。{三十五度|さんじゅうごど}です。",fr="Aujourd'hui la température est élevée, il fait chaud : 35 degrés.",uses=["v5-25"]),
 C(L,10,["{天気|てんき}よほう","{空気|くうき}","きおん","かみなり"],jp="＿によると、{明日|あした}は{雨|あめ}が{降|ふ}るそうです。",fr="D'après la météo, il paraît qu'il pleuvra demain.",uses=["v5-25"]),
 C(L,11,["{空気|くうき}","くも","いし","むし"],jp="{山|やま}の＿はきれいで、おいしいです。",fr="L'air de la montagne est pur et agréable.",uses=["v5-35"]),
 C(L,12,["くも","いし","{台風|たいふう}","{月|つき}"],jp="{空|そら}に＿が{一|ひと}つもありません。いい{天気|てんき}です。",fr="Il n'y a pas un nuage dans le ciel. Il fait beau.",uses=["v5-35"]),
 C(L,13,["かみなり","ほし","{月|つき}","いし"],jp="＿がなって、{子|こ}どもがこわがっています。",fr="Le tonnerre gronde, l'enfant a peur.",uses=["v4-41"]),
 C(L,14,["いし","むし","ほし","くも"],jp="{子|こ}どもが{川|かわ}に＿をなげて{遊|あそ}んでいます。",fr="Un enfant s'amuse à lancer des pierres dans la rivière.",uses=["v4-45","v5-31"]),
 C(L,15,["むし","いし","ほし","{月|つき}"],jp="{夏|なつ}の{夜|よる}は＿がたくさんいて、まどを{開|あ}けられません。",fr="Les nuits d'été, il y a tant d'insectes qu'on ne peut pas ouvrir la fenêtre.",uses=["v5-27"]),
 C(L,16,["たいふう","だいふう","たいかぜ","だいかぜ"],q=LECT+"**台風** ?"),
 C(L,17,["きおんが{高|たか}いです。","きおんが{暑|あつ}いです。","きおんが{大|おお}きいです。","きおんを{高|たか}いです。"],q="« La température est élevée » se dit…"),
 O(L,18,"Le ciel se couvre depuis l'après-midi.",["{午後|ごご}から","{空|そら}が","くもってきました"],uses=["v5-16"]),
]}

# ---------- L64 Culture japonaise ----------
L = "v4-64"
l64 = {"id": L, "title": "Culture japonaise", "words": [
 W("じんじゃ","じんじゃ","sanctuaire shinto","お{正月|しょうがつ}にじんじゃへ{行|い}きます。","Au Nouvel An, on va au sanctuaire."),
 W("おてら","おてら","temple bouddhiste","{京都|きょうと}には{古|ふる}いおてらがたくさんあります。","Il y a beaucoup de vieux temples à Kyoto."),
 W("{着物|きもの}","きもの","kimono","{姉|あね}はけっこんしきで{着物|きもの}を{着|き}ました。","Ma grande sœur a porté un kimono pour le mariage."),
 W("お{正月|しょうがつ}","おしょうがつ","Nouvel An","お{正月|しょうがつ}は{家族|かぞく}みんなで{集|あつ}まります。","Au Nouvel An, toute la famille se réunit."),
 W("ぶんか","ぶんか","culture","{日本|にほん}のぶんかにきょうみがあります。","Je m'intéresse à la culture japonaise."),
 W("むかし","むかし","autrefois","むかし、ここは{小|ちい}さい{村|むら}でした。","Autrefois, c'était un petit village ici."),
 W("おぼん","おぼん","Obon (fête des ancêtres, août)","おぼんには{国|くに}に{帰|かえ}る{人|ひと}が{多|おお}いです。","À Obon, beaucoup de gens rentrent dans leur région natale."),
 W("けっこんしき","けっこんしき","cérémonie de mariage","{来月|らいげつ}、{姉|あね}のけっこんしきがあります。","Le mois prochain, c'est le mariage de ma grande sœur."),
 W("おいわい","おいわい","félicitations, cadeau (pour fêter)","{友|とも}だちのけっこんのおいわいに、{時計|とけい}をあげました。","J'ai offert une montre à un ami pour son mariage."),
 W("すもう","すもう","sumo","テレビですもうを{見|み}ます。","Je regarde le sumo à la télé."),
 W("ふとん","ふとん","futon","{日本|にほん}ではたたみの{上|うえ}にふとんをしいてねます。","Au Japon, on dort sur un futon posé sur les tatamis."),
 W("たたみ","たたみ","tatami","たたみの{部屋|へや}が{好|す}きです。","J'aime les pièces à tatamis."),
 W("おじぎ","おじぎ","révérence, salut (en s'inclinant)","{日本|にほん}では、あいさつのときにおじぎをします。","Au Japon, on s'incline pour saluer."),
 W("かみさま","かみさま","dieu, divinité","じんじゃでかみさまにおねがいをしました。","Au sanctuaire, j'ai fait un vœu aux dieux."),
 W("ゆかた","ゆかた","yukata (kimono d'été)","{夏|なつ}のおまつりでゆかたを{着|き}ました。","J'ai porté un yukata à la fête d'été."),
], "sections": [
 {"h": "Le Japon traditionnel",
  "p": ["Quelques mots de la vie et des fêtes japonaises."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["sanctuaire / temple", "じんじゃ (shinto) / おてら (bouddhiste)"],
   ["Nouvel An / Obon", "お{正月|しょうがつ} (janvier) / おぼん (août)"],
   ["kimono / kimono d'été", "{着物|きもの} / ゆかた"],
   ["natte / matelas", "たたみ / ふとん"],
   ["saluer en s'inclinant", "おじぎ==を==する"]]}}
], "pieges": [
 "じんじゃ (shinto, avec un portique rouge) ≠ おてら (bouddhiste) : on prie dans les deux.",
 "お{正月|しょうがつ} = le Nouvel An ; おぼん = la mi-août, on rentre dans sa famille. (おぼん veut aussi dire « plateau ».)",
 "{着物|きもの} et ゆかた se **portent** avec {着|き}る (leçon 13).",
 "おいわい = cadeau ou fête pour célébrer : けっこんのおいわい ; おみまい (leçon 44) = pour un malade.",
 "むかし = autrefois ; むかしむかし… = il était une fois.",
 "Au Japon, on enlève ses chaussures avant de marcher sur les たたみ."
], "exercises": [
 C(L,1,["じんじゃ","おぼん","たたみ","けっこんしき"],jp="お{正月|しょうがつ}には、＿へ{行|い}って、かみさまにおねがいをします。",fr="Au Nouvel An, on va au sanctuaire faire un vœu aux dieux."),
 C(L,2,["おてら","おぼん","おじぎ","おいわい"],jp="{京都|きょうと}には{古|ふる}い＿がたくさんあります。",fr="Il y a beaucoup de vieux temples à Kyoto.",uses=["v5-05"]),
 C(L,3,["{着物|きもの}","たたみ","ふとん","すもう"],jp="{姉|あね}はけっこんしきで、きれいな＿を{着|き}ました。",fr="Ma grande sœur a porté un beau kimono pour le mariage.",uses=["v5-13"]),
 C(L,4,["お{正月|しょうがつ}","おぼん","けっこんしき","おいわい"],jp="{一月|いちがつ}{一日|ついたち}は＿です。{家族|かぞく}みんなで{集|あつ}まります。",fr="Le 1er janvier, c'est le Nouvel An. Toute la famille se réunit.",uses=["v4-46","v5-17"]),
 C(L,5,["culture","histoire","langue","religion"],q="Que veut dire **ぶんか** ?"),
 C(L,6,["むかし","しょうらい","{今度|こんど}","さっき"],jp="＿、ここは{小|ちい}さい{村|むら}でした。{今|いま}は{大|おお}きい{町|まち}です。",fr="Autrefois, c'était un petit village ici. Maintenant, c'est une grande ville.",uses=["v4-54"]),
 C(L,7,["おぼん","お{正月|しょうがつ}","おじぎ","すもう"],jp="{八月|はちがつ}の＿には、{国|くに}に{帰|かえ}る{人|ひと}が{多|おお}いです。",fr="À Obon, en août, beaucoup de gens rentrent dans leur région natale.",uses=["v5-17"]),
 C(L,8,["けっこんしき","おぼん","すもう","たたみ"],jp="{来月|らいげつ}、{姉|あね}の＿があります。{姉|あね}は{二十八|にじゅうはち}さいでけっこんします。",fr="Le mois prochain, c'est le mariage de ma grande sœur. Elle se marie à vingt-huit ans.",uses=["v5-36"]),
 C(L,9,["おいわい","おじぎ","おみまい","おぼん"],jp="{友|とも}だちがけっこんしましたから、＿に{時計|とけい}をあげました。",fr="Mon ami s'est marié, alors je lui ai offert une montre pour le féliciter.",uses=["v4-44","v5-26"]),
 C(L,10,["すもう","たたみ","ふとん","ゆかた"],jp="テレビで＿を{見|み}ます。{日本|にほん}のとても{古|ふる}いスポーツです。",fr="Je regarde le sumo à la télé. C'est un sport japonais très ancien.",uses=["v5-31"]),
 C(L,11,["ふとん","おじぎ","すもう","おいわい"],jp="{日本|にほん}の{家|いえ}では、ベッドじゃなくて、＿でねる{人|ひと}もいます。",fr="Dans les maisons japonaises, certains dorment sur un futon et pas dans un lit.",uses=["v5-22"]),
 C(L,12,["たたみ","ゆかた","おぼん","おじぎ"],jp="この{部屋|へや}は＿の{部屋|へや}ですから、くつをぬいでください。",fr="C'est une pièce à tatamis, alors enlevez vos chaussures, s'il vous plaît.",uses=["v5-13"]),
 C(L,13,["おじぎ","おいわい","すもう","ふとん"],jp="{日本|にほん}では、あいさつのときに＿をします。",fr="Au Japon, on s'incline pour saluer.",uses=["v4-53"]),
 C(L,14,["かみさま","おじぎ","おぼん","ゆかた"],jp="じんじゃで＿に「{試験|しけん}にごうかくしますように」とおねがいしました。",fr="Au sanctuaire, j'ai demandé aux dieux de réussir mon examen.",uses=["v4-52"]),
 C(L,15,["ゆかた","ふとん","たたみ","おじぎ"],jp="{夏|なつ}のおまつりで＿を{着|き}ました。",fr="J'ai porté un yukata à la fête d'été.",uses=["v4-61"]),
 C(L,16,["じんじゃ : shinto ; おてら : bouddhiste","じんじゃ : bouddhiste ; おてら : shinto","じんじゃ : un musée ; おてら : un parc","Aucune : ce sont deux noms du même lieu."],q="Quelle différence entre じんじゃ et おてら ?"),
 C(L,17,["きもの","ちゃくもの","きぶつ","きるもの"],q=LECT+"**着物** ?"),
 O(L,18,"Au Nouvel An, je vais au sanctuaire.",["お{正月|しょうがつ}に","じんじゃへ","{行|い}きます"],alt=[["じんじゃへ","お{正月|しょうがつ}に","{行|い}きます"]],uses=["v5-02"]),
]}

# ---------- L65 Sport et compétition ----------
L = "v4-65"
l65 = {"id": L, "title": "Sport et compétition", "words": [
 W("かつ","かつ","gagner","{昨日|きのう}の{試合|しあい}は{三|さん}たい{一|いち}でかちました。","Hier, on a gagné le match 3 à 1."),
 W("まける","まける","perdre","{雨|あめ}の{中|なか}の{試合|しあい}で、まけてしまいました。","On a perdu le match sous la pluie."),
 W("せんしゅ","せんしゅ","joueur, athlète","{兄|あに}はやきゅうのせんしゅです。","Mon grand frère est joueur de baseball."),
 W("チーム","チーム","équipe","このチームはとても{強|つよ}いです。","Cette équipe est très forte."),
 W("おうえんする","おうえんする","encourager, supporter","みんなで{日本|にほん}のチームをおうえんしました。","On a tous encouragé l'équipe du Japon."),
 W("えらぶ","えらぶ","choisir","{好|す}きな{色|いろ}をえらんでください。","Choisis ta couleur préférée."),
 W("やきゅう","やきゅう","baseball","{日本|にほん}ではやきゅうがとても{人気|にんき}があります。","Le baseball est très populaire au Japon."),
 W("{水泳|すいえい}","すいえい","natation","{毎週|まいしゅう}{水泳|すいえい}を{習|なら}っています。","Je prends des cours de natation toutes les semaines."),
 W("じゅうどう","じゅうどう","judo","じゅうどうは{日本|にほん}で{生|う}まれたスポーツです。","Le judo est un sport né au Japon."),
 W("スキー","スキー","ski","{冬|ふゆ}は{北海道|ほっかいどう}へスキーに{行|い}きます。","En hiver, je vais skier à Hokkaidō."),
 W("ボール","ボール","balle, ballon","{子|こ}どもたちが{公園|こうえん}でボールをなげています。","Les enfants lancent un ballon au parc."),
 W("がんばる","がんばる","faire de son mieux","{試験|しけん}、がんばってください。","Bon courage pour l'examen !"),
 W("{人気|にんき}","にんき","popularité","このレストランは{若|わか}い{人|ひと}に{人気|にんき}があります。","Ce restaurant est populaire auprès des jeunes."),
 W("プール","プール","piscine","{夏|なつ}は{毎日|まいにち}プールで{泳|およ}ぎます。","En été, je nage à la piscine tous les jours."),
 W("{運動場|うんどうじょう}","うんどうじょう","terrain de sport","{学校|がっこう}の{運動場|うんどうじょう}でサッカーをしました。","On a joué au foot sur le terrain de l'école."),
], "sections": [
 {"h": "Gagner, perdre, encourager",
  "p": ["L'adversaire (ou le match) prend **に** : {試合|しあい}にかつ, {強|つよ}いチームにまける."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["gagner / perdre", "〜==に==かつ / 〜==に==まける"],
   ["encourager", "チーム==を==おうえんする"],
   ["courage !", "がんばって（ください）"],
   ["être populaire auprès de", "〜==に=={人気|にんき}==が==ある"],
   ["choisir", "〜==を==えらぶ"]]}}
], "pieges": [
 "〜**に**かつ / 〜**に**まける : gagner / perdre **contre** (ou **au** match : {試合|しあい}にかつ).",
 "がんばって！ = courage ! bon courage ! : la phrase d'encouragement par excellence.",
 "{人気|にんき}がある = être populaire : 〜**に**{人気|にんき}がある (auprès de…).",
 "かつ (gagner) → かって : même son que {買|か}って (acheter) !",
 "やきゅう, じゅうどう, スキー, {水泳|すいえい} : avec する ({水泳|すいえい}をする).",
 "せんしゅ = joueur, athlète de compétition."
], "exercises": [
 C(L,1,["かちました","まけました","えらびました","がんばりました"],jp="{昨日|きのう}の{試合|しあい}は{三|さん}たい{一|いち}で＿。うれしいです。",fr="Hier, on a gagné le match 3 à 1. Je suis content.",uses=["v4-41","v4-61"],star={"jp":"かつ","kana":"かつ","fr":"gagner"}),
 C(L,2,["まけて","かって","えらんで","おうえんして"],jp="いっしょうけんめいれんしゅうしましたが、＿しまいました。ざんねんです。",fr="On s'est entraînés de toutes nos forces, mais on a perdu. C'est dommage.",uses=["v4-41","v4-55"]),
 C(L,3,["せんしゅ","チーム","ボール","{人気|にんき}"],jp="{兄|あに}はプロのやきゅうの＿です。",fr="Mon grand frère est joueur de baseball professionnel.",uses=["v5-21"]),
 C(L,4,["チーム","ボール","プール","スキー"],jp="この＿はせんしゅがみんな{上手|じょうず}で、とても{強|つよ}いです。",fr="Dans cette équipe, tous les joueurs sont bons : elle est très forte.",uses=["v5-18","v5-19"]),
 C(L,5,["おうえん","えらび","まけ","がんばり"],jp="みんなで{日本|にほん}のチームを＿しました。{日本|にほん}がかちました。",fr="On a tous encouragé l'équipe du Japon. Le Japon a gagné."),
 C(L,6,["えらんで","おうえんして","まけて","がんばって"],jp="この{中|なか}から{好|す}きな{色|いろ}を＿ください。",fr="Choisis ta couleur préférée parmi celles-ci.",uses=["v5-24"]),
 C(L,7,["やきゅう","ボール","プール","{運動場|うんどうじょう}"],jp="{日本|にほん}では＿がとても{人気|にんき}があります。{高校|こうこう}の{試合|しあい}もテレビで{見|み}ます。",fr="Le baseball est très populaire au Japon. On regarde même les matchs des lycées à la télé.",uses=["v4-52"]),
 C(L,8,["{水泳|すいえい}","スキー","やきゅう","じゅうどう"],jp="{毎週|まいしゅう}プールで＿を{習|なら}っています。",fr="Je prends des cours de natation à la piscine toutes les semaines.",uses=["v5-28"]),
 C(L,9,["スキー","{水泳|すいえい}","やきゅう","プール"],jp="{冬|ふゆ}は{山|やま}へ＿に{行|い}きます。ゆきがたくさんあります。",fr="En hiver, je vais skier à la montagne. Il y a beaucoup de neige.",uses=["v5-25"]),
 C(L,10,["ボール","チーム","プール","せんしゅ"],jp="{子|こ}どもたちが{公園|こうえん}で＿をなげて{遊|あそ}んでいます。",fr="Les enfants jouent au parc en lançant un ballon.",uses=["v4-45"]),
 C(L,11,["がんばって","まけて","えらんで","かって"],jp="{明日|あした}は{試験|しけん}ですね。＿ください。",fr="C'est l'examen demain. Bon courage !",uses=["v5-29"]),
 C(L,12,["{人気|にんき}","{気分|きぶん}","{気持|きも}ち","きょうみ"],jp="このレストランは{若|わか}い{人|ひと}に＿があります。いつもこんでいます。",fr="Ce restaurant est populaire auprès des jeunes. Il est toujours bondé.",uses=["v4-50"]),
 C(L,13,["{運動場|うんどうじょう}","プール","せんしゅ","ボール"],jp="{学校|がっこう}の＿でサッカーをしました。",fr="On a joué au foot sur le terrain de l'école.",uses=["v5-31"]),
 C(L,14,["Courage ! Bon courage !","Bravo !","Attention !","Doucement !"],q="Que veut dire **がんばって** ?"),
 C(L,15,["まける","えらぶ","がんばる","おうえんする"],q="Contraire de **かつ** ?"),
 C(L,16,["にんき","ひとき","じんき","にんけ"],q=LECT+"**人気** (popularité) ?"),
 O(L,17,"Notre équipe a gagné le match.",["{私|わたし}たちのチームが","{試合|しあい}に","かちました"],uses=["v4-61"]),
 O(L,18,"Ce chanteur est populaire auprès des jeunes.",["この{歌手|かしゅ}は","{若|わか}い{人|ひと}に","{人気|にんき}が","あります"],uses=["v5-30"]),
]}

TC, TO, XC, XO = make_block("v4-b13")
test = [
 TC(1,["きょうみ","しゅみ","{試合|しあい}","おまつり"],jp="{日本|にほん}のまんがに＿があって、{日本語|にほんご}を{勉強|べんきょう}しています。",fr="Je m'intéresse aux mangas japonais, alors j'étudie le japonais.",uses=["v4-61"]),
 TC(2,["おうふく","かたみち","かんこう","けしき"],jp="{帰|かえ}りのきっぷもいりますから、＿でおねがいします。",fr="J'ai aussi besoin du retour, alors un aller-retour, s'il vous plaît.",uses=["v4-62"]),
 TC(3,["{天気|てんき}よほう","{空気|くうき}","ほし","いし"],jp="{台風|たいふう}が{来|く}るそうですから、＿をよく{聞|き}いてください。",fr="Il paraît qu'un typhon arrive, alors écoutez bien la météo.",uses=["v4-63"]),
 TC(4,["じんじゃ","おぼん","すもう","ゆかた"],jp="お{正月|しょうがつ}には{家族|かぞく}で＿へ{行|い}きます。",fr="Au Nouvel An, on va au sanctuaire en famille.",uses=["v4-64"]),
 TC(5,["かちました","おうえんしました","えらびました","{人気|にんき}でした"],jp="{昨日|きのう}の{試合|しあい}は、{日本|にほん}が{二|に}たい{一|いち}で＿。",fr="Au match d'hier, le Japon a gagné 2 à 1.",uses=["v4-65"],star={"jp":"かつ","kana":"かつ","fr":"gagner"}),
 TC(6,["りょかん","たびかん","りょうかん","りょやかた"],q=LECT+"**旅館** ?",uses=["v4-62"]),
 TC(7,["くもって","{晴|は}れて","{光|ひか}って","もえて"],jp="{午後|ごご}から{空|そら}が＿、{雨|あめ}が{降|ふ}ってきました。",fr="L'après-midi, le ciel s'est couvert et il s'est mis à pleuvoir.",uses=["v4-63"]),
 TC(8,["{着|き}て","はいて","かぶって","かけて"],jp="{夏|なつ}のおまつりに、ゆかたを＿{行|い}きました。",fr="Je suis allé à la fête d'été en yukata.",uses=["v4-64","v5-13"]),
 TC(9,["しゅみ","きょうみ","{旅|たび}","{人気|にんき}"],jp="＿は{写真|しゃしん}をとることです。",fr="Mon passe-temps, c'est la photo.",uses=["v4-61"]),
 TC(10,["みなと","くうこう","おうふく","かたみち"],jp="＿の{近|ちか}くのすしやで、とれたばかりの{魚|さかな}を{食|た}べました。",fr="Dans un restaurant de sushis près du port, j'ai mangé du poisson tout juste pêché.",uses=["v4-62"]),
 TC(11,["tremblement de terre","typhon","incendie","tonnerre"],q="Que veut dire **じしん** ?",uses=["v4-63"]),
 TC(12,["ふとん","おじぎ","すもう","おぼん"],jp="{毎晩|まいばん}、たたみの{部屋|へや}に＿をしいてねます。",fr="Tous les soirs, je déplie mon futon dans la pièce à tatamis pour dormir.",uses=["v4-64"]),
 TC(13,["がんばりましょう","まけましょう","えらびましょう","おじぎしましょう"],jp="{明日|あした}は{大事|だいじ}な{試合|しあい}です。みんな、＿！",fr="Demain, c'est un match important. Allez, tout le monde, on donne tout !",uses=["v4-65"]),
 TO(14,"Je loge dans une auberge japonaise à Kyoto.",["{京都|きょうと}の","{旅館|りょかん}に","とまります"],uses=["v4-62"]),
 TC(15,["{花見|はなみ}","すもう","おぼん","スキー"],jp="{春|はる}になると、みんなで{公園|こうえん}に＿に{行|い}きます。",fr="Au printemps, on va tous au parc admirer les cerisiers.",uses=["v4-61"]),
 TC(16,["{人気|にんき}","{気分|きぶん}","しゅみ","{空気|くうき}"],jp="この{歌手|かしゅ}は{子|こ}どもにとても＿があります。",fr="Ce chanteur est très populaire auprès des enfants.",uses=["v4-65"]),
]
bloc = {"id": "v4-b13", "level": "N4", "title": "Sortir (2) : loisirs, voyages, météo, culture, sport",
        "lessons": [l61, l62, l63, l64, l65], "test": test}
save_n4(bloc, sys.argv[1])
