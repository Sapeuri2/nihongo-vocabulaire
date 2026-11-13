import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L46 Se déplacer ----------
L = "v4-46"
l46 = {"id": L, "title": "Se déplacer, aller chercher, accompagner", "words": [
 W("{通|とお}る","とおる","passer (par)","この{道|みち}は{車|くるま}がたくさん{通|とお}ります。","Beaucoup de voitures passent par cette rue."),
 W("{進|すす}む","すすむ","avancer","{前|まえ}へ{進|すす}んでください。","Avancez, s'il vous plaît."),
 W("{引|ひ}っこす","ひっこす","déménager","{来月|らいげつ}、{大阪|おおさか}に{引|ひ}っこします。","Le mois prochain, je déménage à Osaka."),
 W("{集|あつ}まる","あつまる","se rassembler","{駅|えき}の{前|まえ}に{人|ひと}がたくさん{集|あつ}まっています。","Beaucoup de gens sont rassemblés devant la gare."),
 W("{集|あつ}める","あつめる","rassembler, collectionner","{古|ふる}い{切手|きって}を{集|あつ}めています。","Je collectionne les vieux timbres."),
 W("むかえる","むかえる","accueillir, aller chercher","くうこうへ{友|とも}だちをむかえに{行|い}きます。","Je vais chercher un ami à l'aéroport."),
 W("{出発|しゅっぱつ}する","しゅっぱつする","partir (départ)","バスは{八時|はちじ}に{出発|しゅっぱつ}します。","Le bus part à huit heures."),
 W("とうちゃくする","とうちゃくする","arriver (arrivée)","{飛行機|ひこうき}は{三時|さんじ}に{東京|とうきょう}にとうちゃくします。","L'avion arrive à Tokyo à trois heures."),
 W("{通|かよ}う","かよう","aller régulièrement (à)","{毎日|まいにち}バスで{学校|がっこう}に{通|かよ}っています。","Je vais à l'école en bus tous les jours."),
 W("すぎる","すぎる","passer, dépasser","もう{十二時|じゅうにじ}をすぎました。","Il est déjà plus de midi."),
 W("あんないする","あんないする","guider, faire visiter","{京都|きょうと}を{友|とも}だちにあんないしました。","J'ai fait visiter Kyoto à un ami."),
 W("{見送|みおく}る","みおくる","accompagner (au départ)","{駅|えき}で{友|とも}だちを{見送|みおく}りました。","J'ai accompagné mon ami à la gare (pour son départ)."),
 W("{帰国|きこく}する","きこくする","rentrer dans son pays","マリーさんは{来月|らいげつ}フランスに{帰国|きこく}します。","Marie rentre en France le mois prochain."),
 W("{外出|がいしゅつ}する","がいしゅつする","sortir (de chez soi)","{雨|あめ}ですから、{今日|きょう}は{外出|がいしゅつ}しません。","Il pleut, je ne sors pas aujourd'hui."),
 W("{近道|ちかみち}","ちかみち","raccourci","この{道|みち}は{駅|えき}への{近道|ちかみち}です。","Cette rue est un raccourci vers la gare."),
], "sections": [
 {"h": "Aller, venir, accompagner",
  "p": ["Des verbes précis pour ce que le français dit avec « aller » ou « passer »."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["aller chercher quelqu'un", "むかえに{行|い}く"],
   ["accompagner au départ", "{見送|みおく}る"],
   ["aller régulièrement à", "〜==に=={通|かよ}う (école, travail)"],
   ["passer par", "〜==を=={通|とお}る"],
   ["partir / arriver", "{出発|しゅっぱつ}する / とうちゃくする"]]}}
], "pieges": [
 "{通|とお}る (とおる, passer par, を) ≠ {通|かよ}う (かよう, aller régulièrement, に) : même kanji !",
 "{集|あつ}まる : les gens se rassemblent (が) ; {集|あつ}める : je rassemble, je collectionne (を).",
 "むかえに{行|い}く = aller chercher (à la gare, à l'aéroport) ; {見送|みおく}る = accompagner quelqu'un qui part.",
 "すぎる = passer, dépasser (une heure, un lieu) : {十二時|じゅうにじ}**を**すぎました.",
 "{帰国|きこく}する = rentrer **dans son pays** ; {帰|かえ}る = rentrer (chez soi, en général).",
 "{外出|がいしゅつ}する = sortir de chez soi ; {出|で}かける est plus courant à l'oral."
], "exercises": [
 C(L,1,["{通|とお}ります","{通|かよ}います","{集|あつ}めます","{見送|みおく}ります"],jp="この{道|みち}は{大|おお}きいトラックがたくさん＿。",fr="Beaucoup de gros camions passent par cette rue."),
 C(L,2,["{通|かよ}って","{進|すす}んで","{集|あつ}まって","すぎて"],jp="{毎日|まいにち}バスで{学校|がっこう}に＿います。",fr="Je vais à l'école en bus tous les jours.",uses=["v5-15"],explain="Aller régulièrement à l'école, au travail : 〜に{通|かよ}う."),
 C(L,3,["{引|ひ}っこします","{通|とお}ります","{集|あつ}まります","むかえます"],jp="{来月|らいげつ}、{東京|とうきょう}から{大阪|おおさか}に＿。{新|あたら}しいアパートは{広|ひろ}いです。",fr="Le mois prochain, je déménage de Tokyo à Osaka. Le nouvel appartement est grand.",uses=["v5-22","v5-24"]),
 C(L,4,["{集|あつ}まって","{集|あつ}めて","{通|かよ}って","{引|ひ}っこして"],jp="{駅|えき}の{前|まえ}に{人|ひと}がたくさん＿います。",fr="Beaucoup de gens sont rassemblés devant la gare."),
 C(L,5,["{集|あつ}めて","{集|あつ}まって","{見送|みおく}って","{出発|しゅっぱつ}して"],jp="{古|ふる}い{切手|きって}を＿います。もう{千|せん}まいあります。",fr="Je collectionne les vieux timbres. J'en ai déjà mille.",uses=["v5-08"]),
 C(L,6,["むかえ","{見送|みおく}り","{通|かよ}い","{集|あつ}め"],jp="{友|とも}だちがフランスから{来|き}ますから、くうこうまで＿に{行|い}きます。",fr="Mon ami arrive de France, alors je vais le chercher à l'aéroport."),
 C(L,7,["{出発|しゅっぱつ}","{外出|がいしゅつ}","あんない","{近道|ちかみち}"],jp="バスは{八時|はちじ}に＿しますから、{七時|しちじ}{半|はん}までに{来|き}てください。",fr="Le bus part à huit heures, alors venez avant sept heures et demie.",uses=["v5-16"]),
 C(L,8,["とうちゃく","{外出|がいしゅつ}","{帰国|きこく}","あんない"],jp="{飛行機|ひこうき}は{三時|さんじ}に{東京|とうきょう}に＿します。",fr="L'avion arrive à Tokyo à trois heures.",uses=["v5-15"]),
 C(L,9,["すぎました","{通|かよ}いました","{集|あつ}まりました","{引|ひ}っこしました"],jp="もう{夜|よる}の{十二時|じゅうにじ}を＿。{早|はや}くねましょう。",fr="Il est déjà plus de minuit. Allons vite dormir.",uses=["v5-16"]),
 C(L,10,["あんない","{見送|みおく}り","とうちゃく","{外出|がいしゅつ}"],jp="{京都|きょうと}は{私|わたし}が＿しますよ。いいところをたくさん{知|し}っていますから。",fr="Je te ferai visiter Kyoto : je connais plein de bons endroits.",uses=["v5-28","v5-39"]),
 C(L,11,["{見送|みおく}りました","むかえました","{通|とお}りました","{集|あつ}めました"],jp="{駅|えき}で、{国|くに}へ{帰|かえ}る{友|とも}だちを＿。",fr="À la gare, j'ai accompagné mon ami qui rentrait dans son pays."),
 C(L,12,["{帰国|きこく}","{外出|がいしゅつ}","あんない","{近道|ちかみち}"],jp="マリーさんは{来月|らいげつ}フランスに＿します。{日本|にほん}で{三年|さんねん}{働|はたら}きました。",fr="Marie rentre en France le mois prochain. Elle a travaillé trois ans au Japon.",uses=["v5-38"]),
 C(L,13,["{外出|がいしゅつ}","とうちゃく","あんない","{近道|ちかみち}"],jp="{雨|あめ}ですから、{今日|きょう}は＿しないで、うちにいます。",fr="Il pleut, alors aujourd'hui je ne sors pas, je reste à la maison.",uses=["v5-22"]),
 C(L,14,["{近道|ちかみち}","{外出|がいしゅつ}","あんない","{出発|しゅっぱつ}"],jp="この{道|みち}を{通|とお}ると{早|はや}いです。{駅|えき}への＿です。",fr="Si on passe par cette rue, c'est plus rapide. C'est un raccourci vers la gare."),
 C(L,15,["かよう","とおう","つうう","かおう"],q=LECT+"**通う** (aller régulièrement) ?"),
 C(L,16,["とうちゃくする","{外出|がいしゅつ}する","{帰国|きこく}する","あんないする"],q="Contraire de **{出発|しゅっぱつ}する** ?"),
 C(L,17,["avancer","reculer","s'arrêter","tourner"],q="Que veut dire **{進|すす}む** ?"),
 O(L,18,"Je vais à l'école à vélo tous les jours.",["{毎日|まいにち}","{自転車|じてんしゃ}で","{学校|がっこう}に","{通|かよ}っています"],alt=[["{毎日|まいにち}","{学校|がっこう}に","{自転車|じてんしゃ}で","{通|かよ}っています"]],uses=["v5-15"]),
]}

# ---------- L47 Paires を / が (1) ----------
L = "v4-47"
l47 = {"id": L, "title": "Je fais / ça se fait (1)", "words": [
 W("{始|はじ}める","はじめる","commencer (qqch)","{九時|くじ}に{会議|かいぎ}を{始|はじ}めます。","Nous commençons la réunion à neuf heures."),
 W("{止|と}める","とめる","arrêter ; garer","{駅|えき}の{前|まえ}に{車|くるま}を{止|と}めました。","J'ai garé la voiture devant la gare."),
 W("かわる","かわる","changer (ça change)","この{町|まち}は{十年|じゅうねん}でかわりました。","Cette ville a changé en dix ans."),
 W("かえる","かえる","changer (qqch)","かみの{色|いろ}をかえました。","J'ai changé la couleur de mes cheveux."),
 W("つづく","つづく","continuer (ça continue)","{雨|あめ}が{三日|みっか}つづいています。","La pluie dure depuis trois jours."),
 W("つづける","つづける","continuer (qqch)","{毎日|まいにち}{日本語|にほんご}の{勉強|べんきょう}をつづけています。","Je continue à étudier le japonais tous les jours."),
 W("{上|あ}がる","あがる","monter, augmenter","{今年|ことし}、{電気|でんき}{代|だい}が{上|あ}がりました。","Cette année, la facture d'électricité a augmenté."),
 W("{上|あ}げる","あげる","lever, augmenter (qqch)","{質問|しつもん}がある{人|ひと}は{手|て}を{上|あ}げてください。","Ceux qui ont une question, levez la main."),
 W("{下|さ}がる","さがる","baisser, descendre","{薬|くすり}を{飲|の}んで、ねつが{下|さ}がりました。","J'ai pris un médicament, la fièvre est tombée."),
 W("{下|さ}げる","さげる","baisser (qqch)","あの{店|みせ}はねだんを{下|さ}げました。","Ce magasin a baissé ses prix."),
 W("{起|お}こす","おこす","réveiller (qqn)","{明日|あした}{六時|ろくじ}に{起|お}こしてください。","Réveille-moi à six heures demain."),
 W("{建|た}てる","たてる","construire","{父|ちち}は{去年|きょねん}{家|いえ}を{建|た}てました。","Mon père a fait construire une maison l'an dernier."),
 W("{建|た}つ","たつ","être construit","{駅|えき}の{前|まえ}に{新|あたら}しいビルが{建|た}ちました。","Un nouvel immeuble a été construit devant la gare."),
 W("ならぶ","ならぶ","être alignés, faire la queue","{店|みせ}の{前|まえ}に{人|ひと}がならんでいます。","Des gens font la queue devant le magasin."),
 W("{売|う}れる","うれる","se vendre","この{本|ほん}はよく{売|う}れています。","Ce livre se vend bien."),
], "sections": [
 {"h": "Les paires を / が (suite de la leçon 27)",
  "p": ["À gauche, quelqu'un **fait** l'action sur quelque chose (を). À droite, la chose **change d'elle-même** (が)."],
  "grid": {"head": ["", "を〜 ↔ が〜"], "rows": [
   ["commencer", "{会議|かいぎ}==を=={始|はじ}める ↔ {会議|かいぎ}==が=={始|はじ}まる"],
   ["arrêter", "{車|くるま}==を=={止|と}める ↔ {車|くるま}==が=={止|と}まる"],
   ["changer", "{色|いろ}==を==かえる ↔ {色|いろ}==が==かわる"],
   ["continuer", "{勉強|べんきょう}==を==つづける ↔ {雨|あめ}==が==つづく"],
   ["monter", "{手|て}==を=={上|あ}げる ↔ ねだん==が=={上|あ}がる"],
   ["baisser", "ねだん==を=={下|さ}げる ↔ ねつ==が=={下|さ}がる"],
   ["réveiller", "{子|こ}ども==を=={起|お}こす ↔ {子|こ}ども==が=={起|お}きる"],
   ["construire", "{家|いえ}==を=={建|た}てる ↔ {家|いえ}==が=={建|た}つ"]]}}
], "pieges": [
 "Un repère : 〜**える** et 〜**す** sont souvent les verbes « je fais » (を) ; 〜**まる**, 〜**がる**, 〜**く** les verbes « ça se fait » (が).",
 "{上|あ}げる (lever, augmenter) a le même son que あげる (donner, leçon 26) : {手|て}を{上|あ}げる ≠ プレゼントをあげる.",
 "かえる (changer) ≠ {帰|かえ}る (rentrer). かわる = ça change.",
 "{起|お}こす = réveiller **quelqu'un** ; {起|お}きる = se réveiller, se lever.",
 "{建|た}てる / {建|た}つ (construire) ≠ {立|た}つ (se lever) : même son.",
 "よく{売|う}れる = se vendre bien ; {売|う}る = vendre (leçon 26)."
], "exercises": [
 C(L,1,["{始|はじ}めます","{始|はじ}まります","つづきます","{上|あ}がります"],jp="では、{会議|かいぎ}を＿。",fr="Bien, commençons la réunion.",uses=["v5-14"]),
 C(L,2,["{始|はじ}まります","{始|はじ}めます","{上|あ}げます","{下|さ}げます"],jp="{明日|あした}は{九時|くじ}から{会議|かいぎ}が＿。",fr="Demain, la réunion commence à neuf heures.",uses=["v5-14"],explain="{会議|かいぎ}**が** : la chose elle-même → {始|はじ}まる."),
 C(L,3,["{止|と}めました","{止|と}まりました","{建|た}ちました","ならびました"],jp="{駅|えき}の{前|まえ}に{車|くるま}を＿。",fr="J'ai garé la voiture devant la gare.",uses=["v5-36"]),
 C(L,4,["かわりました","かえました","{建|た}てました","{起|お}こしました"],jp="この{町|まち}は{十年|じゅうねん}でずいぶん＿。",fr="Cette ville a beaucoup changé en dix ans."),
 C(L,5,["かえました","かわりました","{帰|かえ}りました","つづきました"],jp="かみの{色|いろ}を＿。どうですか。",fr="J'ai changé la couleur de mes cheveux. Ça te plaît ?",uses=["v4-42","v5-24"]),
 C(L,6,["つづいて","つづけて","{始|はじ}めて","{上|あ}げて"],jp="{雨|あめ}が{三日|みっか}＿います。",fr="La pluie dure depuis trois jours.",uses=["v5-25"]),
 C(L,7,["つづけて","つづいて","かわって","{下|さ}がって"],jp="{毎日|まいにち}{日本語|にほんご}の{勉強|べんきょう}を＿います。",fr="Je continue à étudier le japonais tous les jours."),
 C(L,8,["{上|あ}げて","{上|あ}がって","{下|さ}がって","{建|た}って"],jp="{質問|しつもん}がある{人|ひと}は、{手|て}を＿ください。",fr="Ceux qui ont une question, levez la main.",uses=["v5-29"]),
 C(L,9,["{下|さ}がりました","{下|さ}げました","{上|あ}げました","{建|た}ちました"],jp="{薬|くすり}を{飲|の}んで、ねつが＿。",fr="J'ai pris un médicament et la fièvre est tombée.",uses=["v5-23"]),
 C(L,10,["{起|お}こして","{起|お}きて","{止|と}まって","ならんで"],jp="{明日|あした}{六時|ろくじ}に{私|わたし}を＿ください。",fr="Réveille-moi à six heures demain, s'il te plaît.",uses=["v5-02"]),
 C(L,11,["{建|た}てました","{建|た}ちました","{立|た}ちました","{上|あ}がりました"],jp="{父|ちち}は{去年|きょねん}{新|あたら}しい{家|いえ}を＿。",fr="Mon père a fait construire une nouvelle maison l'an dernier."),
 C(L,12,["{建|た}ちました","{建|た}てました","ならべました","{起|お}こしました"],jp="{駅|えき}の{前|まえ}に{大|おお}きいビルが＿。",fr="Un grand immeuble a été construit devant la gare."),
 C(L,13,["ならんで","ならべて","{建|た}てて","{止|と}めて"],jp="あの{店|みせ}はおいしいですから、いつも{人|ひと}がたくさん＿います。",fr="Ce restaurant est bon, alors il y a toujours beaucoup de gens qui font la queue.",uses=["v5-27"]),
 C(L,14,["{売|う}れて","かわって","{起|お}こして","ならべて"],jp="この{本|ほん}はとてもおもしろいですから、よく＿います。",fr="Ce livre est très intéressant, alors il se vend bien.",uses=["v5-26"]),
 C(L,15,["lever","donner","baisser","laver"],q="Dans « {手|て}を{上|あ}げてください », que veut dire {上|あ}げる ?"),
 C(L,16,["ねだんが{上|あ}がりました。","ねだんを{上|あ}がりました。","ねだんが{上|あ}げました。","ねだんが{上|うえ}になりました。"],q="« Le prix a augmenté » se dit…"),
 O(L,17,"Continue à étudier tous les jours.",["{毎日|まいにち}","{勉強|べんきょう}を","つづけて","ください"],uses=["v5-14"]),
 O(L,18,"J'ai garé la voiture devant la gare.",["{駅|えき}の{前|まえ}に","{車|くるま}を","{止|と}めました"],alt=[["{車|くるま}を","{駅|えき}の{前|まえ}に","{止|と}めました"]],uses=["v5-20"]),
]}

# ---------- L48 Paires を / が (2) ----------
L = "v4-48"
l48 = {"id": L, "title": "Je fais / ça se fait (2)", "words": [
 W("{見|み}つかる","みつかる","être trouvé","なくしたかぎが{見|み}つかりました。","J'ai retrouvé la clé que j'avais perdue."),
 W("{見|み}つける","みつける","trouver","{駅|えき}の{近|ちか}くでいいレストランを{見|み}つけました。","J'ai trouvé un bon restaurant près de la gare."),
 W("きまる","きまる","être décidé","{旅行|りょこう}の{日|ひ}がきまりました。","La date du voyage est décidée."),
 W("きめる","きめる","décider","どの{大学|だいがく}に{行|い}くか、まだきめていません。","Je n'ai pas encore décidé dans quelle université aller."),
 W("おちる","おちる","tomber ; échouer","{木|き}からりんごがおちました。","Une pomme est tombée de l'arbre."),
 W("おとす","おとす","faire tomber ; perdre","{電車|でんしゃ}の{中|なか}でさいふをおとしました。","J'ai perdu mon portefeuille dans le train."),
 W("こわれる","こわれる","se casser, tomber en panne","パソコンがこわれました。","L'ordinateur est tombé en panne."),
 W("こわす","こわす","casser (qqch)","{子|こ}どもがおもちゃをこわしました。","L'enfant a cassé le jouet."),
 W("われる","われる","se briser","コップがおちて、われました。","Le verre est tombé et s'est brisé."),
 W("わる","わる","briser (qqch)","おさらをわってしまいました。","J'ai cassé une assiette."),
 W("わく","わく","bouillir","おゆがわきました。","L'eau bout."),
 W("わかす","わかす","faire bouillir","おちゃを{入|い}れますから、おゆをわかします。","Je fais bouillir de l'eau pour le thé."),
 W("かわく","かわく","sécher ; avoir soif (のど)","せんたくものがかわきました。","Le linge a séché."),
 W("ひえる","ひえる","refroidir (ça refroidit)","ビールがよくひえています。","La bière est bien fraîche."),
 W("ひやす","ひやす","mettre au frais","スイカをれいぞうこでひやします。","Je mets la pastèque au frais dans le frigo."),
], "sections": [
 {"h": "Encore des paires を / が",
  "p": ["Même principe qu'à la leçon 47 : を = quelqu'un agit ; が = la chose change d'elle-même."],
  "grid": {"head": ["", "を〜 ↔ が〜"], "rows": [
   ["trouver", "かぎ==を=={見|み}つける ↔ かぎ==が=={見|み}つかる"],
   ["décider", "{日|ひ}==を==きめる ↔ {日|ひ}==が==きまる"],
   ["faire tomber", "さいふ==を==おとす ↔ さいふ==が==おちる"],
   ["casser (machine, objet)", "パソコン==を==こわす ↔ パソコン==が==こわれる"],
   ["briser (verre)", "コップ==を==わる ↔ コップ==が==われる"],
   ["faire bouillir", "おゆ==を==わかす ↔ おゆ==が==わく"],
   ["refroidir", "ビール==を==ひやす ↔ ビール==が==ひえる"]]}}
], "pieges": [
 "こわれる / こわす : une machine, un jouet qui ne marche plus. われる / わる : ce qui se brise en morceaux (verre, assiette, œuf).",
 "おとす = faire tomber **et** perdre : さいふをおとしました = j'ai perdu mon portefeuille.",
 "おちる = tomber d'en haut, et **échouer** : {試験|しけん}**に**おちる.",
 "のどがかわく = avoir soif (la gorge sèche).",
 "Fin en 〜す = souvent « je fais » (を) : おとす, こわす, わかす, ひやす.",
 "〜てしまう ajoute « malheureusement, c'est fait » : おさらをわってしまいました."
], "exercises": [
 C(L,1,["{見|み}つかりました","{見|み}つけました","おとしました","こわしました"],jp="なくしたかぎが＿。よかったです。",fr="J'ai retrouvé la clé que j'avais perdue. Ouf !",uses=["v5-12"]),
 C(L,2,["{見|み}つけました","{見|み}つかりました","きまりました","おちました"],jp="{駅|えき}の{近|ちか}くで、おいしいレストランを＿。",fr="J'ai trouvé un bon restaurant près de la gare.",uses=["v5-04"]),
 C(L,3,["きまりました","きめました","わきました","ひえました"],jp="{旅行|りょこう}の{日|ひ}が＿。{来月|らいげつ}の{五日|いつか}です。",fr="La date du voyage est décidée : le 5 du mois prochain.",uses=["v5-17","v5-33"]),
 C(L,4,["きめて","わいて","ひやして","こわれて"],jp="どの{大学|だいがく}に{行|い}くか、まだ＿いません。",fr="Je n'ai pas encore décidé dans quelle université aller.",uses=["v5-30"]),
 C(L,5,["おちました","おとしました","われました","きまりました"],jp="{木|き}からりんごが＿。",fr="Une pomme est tombée de l'arbre.",uses=["v5-35"]),
 C(L,6,["おとしました","おちました","われました","わきました"],jp="{電車|でんしゃ}の{中|なか}でさいふを＿。こうばんに{行|い}きます。",fr="J'ai perdu mon portefeuille dans le train. Je vais au poste de police.",uses=["v5-32"]),
 C(L,7,["こわれて","こわして","われて","わって"],jp="{古|ふる}いパソコンが＿、もう{動|うご}きません。",fr="Le vieil ordinateur est en panne, il ne marche plus.",uses=["v4-45"]),
 C(L,8,["こわして","こわれて","おちて","きまって"],jp="{子|こ}どもがおもちゃを＿しまいました。",fr="L'enfant a cassé son jouet."),
 C(L,9,["われました","わりました","こわしました","わかしました"],jp="コップがおちて、＿。",fr="Le verre est tombé et s'est brisé.",uses=["v5-34"]),
 C(L,10,["わかします","わきます","ひえます","おちます"],jp="おちゃを{入|い}れますから、おゆを＿。",fr="Je fais bouillir de l'eau pour le thé.",uses=["v5-27"]),
 C(L,11,["わきました","わかしました","ひやしました","おとしました"],jp="おゆが＿から、おちゃを{入|い}れましょう。",fr="L'eau bout, faisons le thé."),
 C(L,12,["かわきます","わきます","ひえます","おちます"],jp="{暑|あつ}い{日|ひ}は、すぐのどが＿。",fr="Les jours de chaleur, on a vite soif.",uses=["v5-25"]),
 C(L,13,["ひやして","ひえて","わいて","かわいて"],jp="パーティーの{前|まえ}に、ビールをれいぞうこで＿おきます。",fr="Avant la fête, je mets la bière au frais dans le frigo.",uses=["v5-22","v5-31"]),
 C(L,14,["おちて","おとして","われて","こわれて"],jp="{試験|しけん}に＿、とてもかなしいです。",fr="J'ai échoué à l'examen, je suis très triste.",uses=["v4-41","v5-29"],explain="{試験|しけん}**に**おちる = échouer à un examen."),
 C(L,15,["perdre (faire tomber)","trouver","casser","acheter"],q="Dans « さいふをおとしました », que veut dire おとす ?"),
 C(L,16,["おさらがわれました。","おさらがこわしました。","おさらをわれました。","おさらがわりました。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-34"]),
 O(L,17,"J'ai perdu mon portefeuille dans le train.",["{電車|でんしゃ}の{中|なか}で","さいふを","おとしました"],alt=[["さいふを","{電車|でんしゃ}の{中|なか}で","おとしました"]],uses=["v5-12"]),
 O(L,18,"La date du voyage est décidée.",["{旅行|りょこう}の","{日|ひ}が","きまりました"],uses=["v5-33"]),
]}

# ---------- L49 Augmenter, diminuer, rester ----------
L = "v4-49"
l49 = {"id": L, "title": "Augmenter, diminuer, rester", "words": [
 W("ふえる","ふえる","augmenter","{日本|にほん}に{来|く}る{外国人|がいこくじん}がふえています。","Les étrangers qui viennent au Japon sont de plus en plus nombreux."),
 W("へる","へる","diminuer","{町|まち}の{人|ひと}がだんだんへっています。","La population de la ville diminue peu à peu."),
 W("{足|た}りる","たりる","suffire","お{金|かね}が{足|た}りません。","Je n'ai pas assez d'argent."),
 W("のこる","のこる","rester (il en reste)","ケーキが{一|ひと}つのこっています。","Il reste un gâteau."),
 W("のこす","のこす","laisser (de côté)","{料理|りょうり}をのこさないで、ぜんぶ{食|た}べてください。","Ne laisse rien dans ton assiette, mange tout."),
 W("なくなる","なくなる","ne plus y en avoir ; disparaître","さとうがなくなりました。{買|か}いに{行|い}きます。","Il n'y a plus de sucre. Je vais en acheter."),
 W("なくす","なくす","perdre (qqch)","かぎをなくしました。","J'ai perdu ma clé."),
 W("{十分|じゅうぶん}","じゅうぶん","assez, suffisamment","{時間|じかん}は{十分|じゅうぶん}あります。","On a largement le temps."),
 W("ちょうど","ちょうど","juste, pile","{今|いま}、ちょうど{三時|さんじ}です。","Il est trois heures pile."),
 W("ずいぶん","ずいぶん","très, beaucoup","この{町|まち}はずいぶんかわりましたね。","Cette ville a beaucoup changé, hein."),
 W("だんだん","だんだん","peu à peu","だんだん{寒|さむ}くなってきました。","Il commence à faire de plus en plus froid."),
 W("ほとんど","ほとんど","presque (tout)","{宿題|しゅくだい}はほとんど{終|お}わりました。","J'ai presque fini mes devoirs."),
 W("{大分|だいぶ}","だいぶ","pas mal, nettement","かぜは{大分|だいぶ}よくなりました。","Mon rhume va nettement mieux."),
 W("〜ずつ","〜ずつ","… chacun, … à la fois","{毎日|まいにち}{漢字|かんじ}を{五|いつ}つずつおぼえます。","Je retiens cinq kanji par jour."),
 W("やっと","やっと","enfin","{一時間|いちじかん}{待|ま}って、やっとバスが{来|き}ました。","Après une heure d'attente, le bus est enfin arrivé."),
], "sections": [
 {"h": "Plus, moins, il en reste",
  "p": ["Encore des paires が / を, et quelques adverbes de quantité."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["augmenter / diminuer", "ふえる ↔ へる"],
   ["suffire", "{足|た}りる : お{金|かね}が{足|た}りない = pas assez d'argent"],
   ["rester / laisser", "のこる (が) ↔ のこす (を)"],
   ["ne plus y en avoir / perdre", "なくなる (が) ↔ なくす (を)"],
   ["peu à peu", "だんだん · 〜ずつ"]]}}
], "pieges": [
 "{十分|じゅうぶん} (assez) ≠ {十分|じゅっぷん} (dix minutes) : même écriture, lecture différente !",
 "{足|た}りる est du groupe 2 : {足|た}りない, {足|た}りません.",
 "なくなる = il n'y en a plus (épuisé ou disparu) ; なくす = perdre quelque chose.",
 "ほとんど = presque tout ; avec un négatif, presque pas : ほとんど{分|わ}かりません.",
 "やっと = enfin (après une longue attente) ; だんだん = peu à peu, de plus en plus.",
 "〜ずつ = … chacun, … à la fois : {一人|ひとり}{二|ふた}つずつ = deux par personne."
], "exercises": [
 C(L,1,["ふえて","へって","{足|た}りて","のこして"],jp="{日本|にほん}に{来|く}る{外国人|がいこくじん}が{毎年|まいとし}＿いますから、ホテルがいつもいっぱいです。",fr="Les étrangers qui viennent au Japon sont plus nombreux chaque année, alors les hôtels sont toujours pleins.",uses=["v5-33","v5-34","v5-38"]),
 C(L,2,["へって","ふえて","なくして","のこして"],jp="{子|こ}どもが{少|すく}なくなって、{学校|がっこう}の{学生|がくせい}が＿います。",fr="Il y a moins d'enfants, alors le nombre d'élèves diminue."),
 C(L,3,["{足|た}り","なくなり","へり","なくし"],jp="お{金|かね}が＿ませんから、{車|くるま}は{買|か}えません。",fr="Je n'ai pas assez d'argent, je ne peux pas acheter de voiture.",uses=["v5-07"]),
 C(L,4,["のこって","のこして","なくなって","へって"],jp="ケーキがまだ{一|ひと}つ＿います。だれが{食|た}べますか。",fr="Il reste encore un gâteau. Qui le mange ?",uses=["v5-08"]),
 C(L,5,["のこさ","のこら","なくなら","ふえ"],jp="{料理|りょうり}を＿ないで、ぜんぶ{食|た}べてください。",fr="Ne laisse rien, mange tout.",uses=["v5-07"]),
 C(L,6,["なくなりました","なくしました","のこりました","ふえました"],jp="さとうが＿から、{買|か}いに{行|い}きます。",fr="Il n'y a plus de sucre, je vais en acheter.",uses=["v5-34"]),
 C(L,7,["なくして","なくなって","へって","ふえて"],jp="{駅|えき}でかぎを＿しまいました。",fr="J'ai perdu ma clé à la gare.",uses=["v5-12"]),
 C(L,8,["{十分|じゅうぶん}","やっと","だんだん","ほとんど"],jp="{電車|でんしゃ}まで{時間|じかん}は＿あります。ゆっくり{行|い}きましょう。",fr="On a largement le temps avant le train. Allons-y tranquillement.",uses=["v5-37"]),
 C(L,9,["じゅうぶん","じゅっぷん","じっぷん","とおぶん"],q="Dans « {時間|じかん}は十分あります » (on a largement le temps), comment se lit **十分** ?",uses=["v5-16"]),
 C(L,10,["ちょうど","だんだん","ほとんど","{十分|じゅうぶん}"],jp="{今|いま}、＿{三時|さんじ}です。",fr="Il est trois heures pile.",uses=["v5-16"]),
 C(L,11,["だんだん","ちょうど","ほとんど","ずつ"],jp="{冬|ふゆ}になって、＿{寒|さむ}くなってきました。",fr="L'hiver arrive, il fait de plus en plus froid.",uses=["v5-25"]),
 C(L,12,["ほとんど","ちょうど","だんだん","やっと"],jp="{宿題|しゅくだい}は＿{終|お}わりました。あと{一|ひと}つだけです。",fr="J'ai presque fini mes devoirs. Il n'en reste qu'un.",uses=["v5-29"]),
 C(L,13,["nettement, pas mal","exactement","enfin","à peine"],q="Dans « かぜは{大分|だいぶ}よくなりました », que veut dire {大分|だいぶ} ?"),
 C(L,14,["ずつ","ちょうど","ほとんど","だんだん"],jp="{毎日|まいにち}{漢字|かんじ}を{五|いつ}つ＿おぼえます。",fr="Je retiens cinq kanji par jour.",uses=["v5-28"]),
 C(L,15,["やっと","ちょうど","ずいぶん","ほとんど"],jp="{一時間|いちじかん}{待|ま}って、＿バスが{来|き}ました。",fr="Après une heure d'attente, le bus est enfin arrivé.",uses=["v5-36"]),
 C(L,16,["へる","のこる","なくす","{足|た}りる"],q="Contraire de **ふえる** ?"),
 O(L,17,"Je n'ai pas assez d'argent pour acheter une voiture.",["{車|くるま}を{買|か}う","お{金|かね}が","{足|た}りません"],uses=["v5-07"]),
 O(L,18,"Il reste encore un gâteau.",["ケーキが","まだ","{一|ひと}つ","のこっています"],alt=[["まだ","ケーキが","{一|ひと}つ","のこっています"]],uses=["v5-08"]),
]}

# ---------- L50 Circulation ----------
L = "v4-50"
l50 = {"id": L, "title": "Train et circulation", "words": [
 W("{乗|の}りかえる","のりかえる","changer (de train)","{東京|とうきょう}{駅|えき}でちかてつに{乗|の}りかえます。","Je prends la correspondance pour le métro à la gare de Tokyo."),
 W("おくれる","おくれる","être en retard","{電車|でんしゃ}がおくれて、{会社|かいしゃ}におくれました。","Le train avait du retard, je suis arrivé en retard au bureau."),
 W("{間|ま}に{合|あ}う","まにあう","arriver à temps","{走|はし}って、{電車|でんしゃ}に{間|ま}に{合|あ}いました。","J'ai couru et j'ai eu le train."),
 W("しんごう","しんごう","feu (de circulation)","しんごうが{赤|あか}のときは、わたらないでください。","Ne traversez pas quand le feu est rouge."),
 W("こうさてん","こうさてん","carrefour","つぎのこうさてんを{右|みぎ}にまがってください。","Tournez à droite au prochain carrefour."),
 W("じこ","じこ","accident","ゆきの{日|ひ}は{車|くるま}のじこが{多|おお}いです。","Les jours de neige, il y a beaucoup d'accidents de voiture."),
 W("こむ","こむ","être bondé","{朝|あさ}の{電車|でんしゃ}はとてもこんでいます。","Le train du matin est bondé."),
 W("{空|す}く","すく","être peu fréquenté","{日曜日|にちようび}の{朝|あさ}は{道|みち}が{空|す}いています。","Le dimanche matin, les rues sont vides."),
 W("あぶない","あぶない","dangereux","{道|みち}で{遊|あそ}ぶのはあぶないです。","Jouer dans la rue, c'est dangereux."),
 W("あんぜん","あんぜん","sûr, sans danger","この{町|まち}は{夜|よる}もあんぜんです。","Cette ville est sûre, même la nuit."),
 W("{急行|きゅうこう}","きゅうこう","(train) express","{急行|きゅうこう}は{小|ちい}さい{駅|えき}には{止|と}まりません。","L'express ne s'arrête pas aux petites gares."),
 W("{特急|とっきゅう}","とっきゅう","express limité","{特急|とっきゅう}に{乗|の}ると、{一時間|いちじかん}で{着|つ}きます。","Avec l'express limité, on arrive en une heure."),
 W("{乗|の}り{物|もの}","のりもの","moyen de transport","{子|こ}どもは{乗|の}り{物|もの}が{大好|だいす}きです。","Les enfants adorent tout ce qui roule."),
 W("せき","せき","place (assise)","すみません、このせきはあいていますか。","Excusez-moi, cette place est libre ?"),
 W("ちゅうしゃじょう","ちゅうしゃじょう","parking","{車|くるま}はちゅうしゃじょうに{止|と}めてください。","Garez la voiture sur le parking."),
], "sections": [
 {"h": "Prendre le train, la route",
  "p": ["Les particules changent tout : retenez les expressions en entier."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["changer pour", "〜で 〜==に=={乗|の}りかえる"],
   ["être en retard à", "〜==に==おくれる"],
   ["arriver à temps pour", "〜==に=={間|ま}に{合|あ}う"],
   ["bondé / vide", "こんでいる / {空|す}いている"],
   ["le feu passe au vert", "しんごう==が=={青|あお}になる"]]}}
], "pieges": [
 "{会社|かいしゃ}**に**おくれる = arriver en retard au bureau ; {電車|でんしゃ}**が**おくれる = le train a du retard.",
 "〜**に**{間|ま}に{合|あ}う = arriver à temps pour : {電車|でんしゃ}に{間|ま}に{合|あ}った = j'ai eu le train.",
 "こむ et {空|す}く s'emploient surtout en ている : こんでいる (bondé), {空|す}いている (peu de monde).",
 "Une **place** libre : せきが**あいている** ({空|あ}く). すいている, c'est « peu de monde ».",
 "Le feu vert se dit {青|あお} : しんごうが{青|あお}になったら、わたります.",
 "{急行|きゅうこう} (express) s'arrête moins souvent ; {特急|とっきゅう} encore moins (et coûte plus cher)."
], "exercises": [
 C(L,1,["{乗|の}りかえます","{降|お}ります","すきます","こみます"],jp="{東京|とうきょう}{駅|えき}で、JRからちかてつに＿。",fr="À la gare de Tokyo, je passe de la ligne JR au métro.",uses=["v5-15"]),
 C(L,2,["おくれて","{間|ま}に{合|あ}って","すいて","{乗|の}りかえて"],jp="{電車|でんしゃ}が{三十分|さんじゅっぷん}＿、{会議|かいぎ}に{間|ま}に{合|あ}いませんでした。",fr="Le train avait trente minutes de retard, je n'ai pas pu arriver à temps à la réunion."),
 C(L,3,["{間|ま}に{合|あ}いました","おくれました","こみました","すきました"],jp="{走|はし}って、{電車|でんしゃ}に＿。よかったです。",fr="J'ai couru et j'ai eu le train. Ouf !",uses=["v5-15"]),
 C(L,4,["しんごう","こうさてん","じこ","せき"],jp="＿が{赤|あか}のときは、{道|みち}をわたらないでください。",fr="Ne traversez pas la rue quand le feu est rouge.",uses=["v5-24","v5-32"]),
 C(L,5,["こうさてん","じこ","せき","{急行|きゅうこう}"],jp="つぎの＿を{右|みぎ}にまがってください。",fr="Tournez à droite au prochain carrefour.",uses=["v5-32"]),
 C(L,6,["じこ","しんごう","せき","{乗|の}り{物|もの}"],jp="ゆきの{日|ひ}は{車|くるま}の＿が{多|おお}いですから、{気|き}をつけてください。",fr="Les jours de neige, il y a beaucoup d'accidents de voiture : soyez prudents.",uses=["v5-25"]),
 C(L,7,["こんで","すいて","おくれて","{間|ま}に{合|あ}って"],jp="{朝|あさ}の{電車|でんしゃ}はとても＿いて、すわれません。",fr="Le train du matin est bondé, on ne peut pas s'asseoir.",uses=["v5-36"]),
 C(L,8,["{空|す}いて","こんで","あぶなくて","おくれて"],jp="{日曜日|にちようび}の{朝|あさ}は{道|みち}が＿いますから、{車|くるま}ですぐ{着|つ}きます。",fr="Le dimanche matin, les rues sont vides, alors on arrive vite en voiture."),
 C(L,9,["あぶない","あんぜん","こんで","すいて"],jp="{車|くるま}が{多|おお}いですから、{子|こ}どもが{道|みち}で{遊|あそ}ぶのは＿です。",fr="Il y a beaucoup de voitures, alors c'est dangereux pour les enfants de jouer dans la rue.",uses=["v5-31"]),
 C(L,10,["あんぜん","あぶない","じこ","{特急|とっきゅう}"],jp="この{町|まち}は{夜|よる}も＿ですから、{一人|ひとり}で{歩|ある}いてもだいじょうぶです。",fr="Cette ville est sûre même la nuit, on peut s'y promener seul."),
 C(L,11,["{急行|きゅうこう}","{乗|の}り{物|もの}","しんごう","ちゅうしゃじょう"],jp="＿は{小|ちい}さい{駅|えき}には{止|と}まりません。",fr="L'express ne s'arrête pas aux petites gares.",uses=["v5-36"]),
 C(L,12,["あいて","すいて","こんで","おくれて"],jp="すみません、このせきは＿いますか。— はい、どうぞ。",fr="Excusez-moi, cette place est libre ? — Oui, je vous en prie.",explain="Une place libre : あいている. すいている = peu de monde (un train, une rue)."),
 C(L,13,["ちゅうしゃじょう","こうさてん","しんごう","せき"],jp="{車|くるま}は＿に{止|と}めてください。",fr="Garez la voiture sur le parking.",uses=["v4-47"]),
 C(L,14,["{乗|の}り{物|もの}","じこ","しんごう","せき"],jp="{子|こ}どもは{電車|でんしゃ}やバスなどの＿が{大好|だいす}きです。",fr="Les enfants adorent les trains, les bus et tout ce qui roule."),
 C(L,15,["とっきゅう","とくきゅう","とっきょう","とくいそぎ"],q=LECT+"**特急** ?"),
 C(L,16,["{会社|かいしゃ}におくれました。","{会社|かいしゃ}をおくれました。","{会社|かいしゃ}がおくれました。","{会社|かいしゃ}におくりました。"],q="« Je suis arrivé en retard au bureau » se dit…",explain="Être en retard **à** : 〜におくれる."),
 O(L,17,"Je prends la correspondance pour le métro à la gare de Tokyo.",["{東京|とうきょう}{駅|えき}で","ちかてつに","{乗|の}りかえます"],alt=[["ちかてつに","{東京|とうきょう}{駅|えき}で","{乗|の}りかえます"]],uses=["v5-15"]),
 O(L,18,"J'ai couru et j'ai eu le train de justesse.",["{走|はし}って、","{電車|でんしゃ}に","{間|ま}に{合|あ}いました"],uses=["v5-15"]),
]}

TC, TO, XC, XO = make_block("v4-b10", "v4-x05")
test = [
 TC(1,["つづいて","つづけて","{始|はじ}めて","{集|あつ}めて"],jp="{雨|あめ}が{一週間|いっしゅうかん}＿います。",fr="La pluie dure depuis une semaine.",uses=["v4-47"]),
 TC(2,["{起|お}こします","{起|お}きます","{上|あ}げます","{建|た}てます"],jp="{毎朝|まいあさ}{七時|しちじ}に{子|こ}どもを＿。",fr="Tous les matins, je réveille les enfants à sept heures.",uses=["v4-47"]),
 TC(3,["{足|た}り","なくなり","のこし","わき"],jp="お{金|かね}が＿ませんでしたから、{安|やす}いほうを{買|か}いました。",fr="Je n'avais pas assez d'argent, alors j'ai acheté le moins cher.",uses=["v4-49"]),
 TC(4,["おくれます","{間|ま}に{合|あ}います","すきます","{乗|の}りかえます"],jp="{急|いそ}がないと、{電車|でんしゃ}に＿よ。",fr="Si tu ne te dépêches pas, tu vas rater le train (tu seras en retard).",uses=["v4-50"]),
 TC(5,["わって","われて","こわれて","わいて"],jp="コップを＿しまいました。ごめんなさい。",fr="J'ai cassé un verre. Pardon.",uses=["v4-48"]),
 TC(6,["ふえて","へって","なくして","{足|た}りて"],jp="{日本|にほん}に{住|す}む{外国人|がいこくじん}が＿いますから、{英語|えいご}のメニューも{多|おお}くなりました。",fr="Il y a de plus en plus d'étrangers qui vivent au Japon, alors les menus en anglais sont plus nombreux.",uses=["v4-49"]),
 TC(7,["{電車|でんしゃ}がこんでいます。","{電車|でんしゃ}をこんでいます。","{電車|でんしゃ}がすいています。","{電車|でんしゃ}がこまっています。"],q="« Le train est bondé » se dit…",uses=["v4-50"]),
 TC(8,["{集|あつ}まり","{集|あつ}め","{通|かよ}い","{見|み}つかり"],jp="{旅行|りょこう}の{前|まえ}に、みんなで{駅|えき}に＿ました。",fr="Avant le voyage, nous nous sommes tous rassemblés à la gare.",uses=["v4-46"]),
 TC(9,["{見|み}つかりました","{見|み}つけました","おとしました","おちました"],jp="なくしたさいふが＿。こうばんにありました。",fr="Le portefeuille que j'avais perdu a été retrouvé. Il était au poste de police.",uses=["v4-48"]),
 TC(10,["{始|はじ}まります","{始|はじ}めます","つづけます","{上|あ}げます"],jp="{明日|あした}は{三時|さんじ}から{会議|かいぎ}が＿。",fr="Demain, la réunion commence à trois heures.",uses=["v4-47"]),
 TC(11,["{間|ま}に{合|あ}いませんでした","{間|ま}に{合|あ}いました","{乗|の}りかえました","すきました"],jp="{走|はし}りましたが、バスに＿。つぎのバスは{三十分|さんじゅっぷん}{後|ご}です。",fr="J'ai couru, mais j'ai raté le bus. Le prochain est dans trente minutes.",uses=["v4-50"]),
 TC(12,["assez","dix minutes","dix fois","dix heures"],q="Dans « {時間|じかん}は十分あります », que veut dire 十分 ?",uses=["v4-49"]),
 TC(13,["むかえ","{見送|みおく}り","{集|あつ}め","{通|かよ}い"],jp="{父|ちち}が{今日|きょう}アメリカから{帰|かえ}ってきますから、くうこうまで＿に{行|い}きます。",fr="Mon père rentre des États-Unis aujourd'hui, alors je vais le chercher à l'aéroport.",uses=["v4-46"]),
 TO(14,"Le bus part à huit heures.",["バスは","{八時|はちじ}に","{出発|しゅっぱつ}します"],alt=[["{八時|はちじ}に","バスは","{出発|しゅっぱつ}します"]],uses=["v4-46"]),
 TC(15,["ひえて","ひやして","わいて","かわいて"],jp="ビールがよく＿いて、おいしいです。",fr="La bière est bien fraîche, elle est bonne.",uses=["v4-48"]),
 TC(16,["こんでいます","すいています","あんぜんです","{間|ま}に{合|あ}います"],jp="{道|みち}が＿から、{車|くるま}より{電車|でんしゃ}のほうが{早|はや}いです。",fr="Les routes sont encombrées, alors le train est plus rapide que la voiture.",uses=["v4-50"]),
]
exam = [
 XC(1,["{子|こ}どもが{帰|かえ}ってこないので、{母|はは}は{心配|しんぱい}しています。","{子|こ}どもが{帰|かえ}ってこないので、{母|はは}は{安心|あんしん}しています。","{子|こ}どもが{帰|かえ}ってこないので、{母|はは}は{心配|しんぱい}にしています。","{子|こ}どもが{帰|かえ}ってこないので、{母|はは}は{心配|しんぱい}いています。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v4-41"]),
 XC(2,["おくれました","{間|ま}に{合|あ}いました","{始|はじ}めました","{乗|の}りかえました"],jp="{電車|でんしゃ}がとまって、{会議|かいぎ}に{三十分|さんじゅっぷん}＿。みんなを{待|ま}たせてしまいました。",fr="Le train s'est arrêté, je suis arrivé à la réunion avec trente minutes de retard. J'ai fait attendre tout le monde.",uses=["v4-50"]),
 XC(3,["なくなりました","なくしました","{見|み}つかりました","ふえました"],jp="{急|きゅう}に{雨|あめ}が{降|ふ}って、{試合|しあい}が＿。ざんねんです。",fr="Il s'est mis à pleuvoir d'un coup, le match a été annulé. C'est dommage.",uses=["v4-41","v4-49"]),
 XC(4,["{主人|しゅじん}は{毎朝|まいあさ}{運動|うんどう}しています。","ご{主人|しゅじん}は{毎朝|まいあさ}{運動|うんどう}しています。","おっとさんは{毎朝|まいあさ}{運動|うんどう}しています。","{主人|しゅじん}は{毎朝|まいあさ}{運動|うんどう}がしています。"],q="Mme Tanaka te parle de **son** mari. Elle dit :",uses=["v4-43","v4-45"]),
 XC(5,["やせました","なおりました","かわきました","{集|あつ}まりました"],jp="{毎日|まいにち}{走|はし}って、{五|ご}キロ＿。{体|からだ}のぐあいもいいです。",fr="J'ai couru tous les jours et j'ai perdu cinq kilos. Je me sens aussi en meilleure forme.",uses=["v4-42","v4-44"]),
 XC(6,["きゅうきゅうしゃ","おみまい","{歯医者|はいしゃ}","{特急|とっきゅう}"],jp="{夜|よる}、{父|ちち}が{急|きゅう}にたおれましたから、＿をよびました。",fr="La nuit, mon père s'est effondré d'un coup, alors j'ai appelé une ambulance.",uses=["v4-44","v4-45"]),
 XC(7,["おちなくて","おちて","おとして","われなくて"],jp="{弟|おとうと}が{試験|しけん}に＿、{母|はは}は{安心|あんしん}しました。",fr="Mon petit frère n'a pas échoué à l'examen, ma mère a été soulagée.",uses=["v4-41","v4-48"]),
 XO(8,"J'ai trouvé une bonne école près de chez moi.",["{家|いえ}の{近|ちか}くで","いい{学校|がっこう}を","{見|み}つけました"],alt=[["いい{学校|がっこう}を","{家|いえ}の{近|ちか}くで","{見|み}つけました"]],uses=["v4-48"]),
 XC(9,["J'ai accompagné mon ami à la gare pour son départ.","Je suis allé chercher mon ami à la gare.","J'ai croisé mon ami par hasard à la gare.","J'ai attendu mon ami à la gare."],q="Que veut dire : {駅|えき}で{友|とも}だちを{見送|みおく}りました。",uses=["v4-46"]),
 XC(10,["{空|す}いて","こんで","おくれて","{間|ま}に{合|あ}って"],jp="このレストランはいつもこんでいますが、{今日|きょう}は＿います。",fr="Ce restaurant est toujours bondé, mais aujourd'hui il y a peu de monde.",uses=["v4-50"]),
 XC(11,["たおれて","おちて","おとして","こわして"],jp="{風|かぜ}で{大|おお}きい{木|き}が＿、{道|みち}が{通|とお}れません。",fr="Un grand arbre est tombé à cause du vent, on ne peut pas passer dans la rue.",uses=["v4-45","v4-46"]),
 XC(12,["にて","かわって","{通|かよ}って","{集|あつ}まって"],jp="{兄|あに}はお{父|とう}さんによく＿います。{顔|かお}もせもそっくりです。",fr="Mon grand frère ressemble beaucoup à notre père : le visage, la taille, tout pareil.",uses=["v4-42"],star={"jp":"にる","kana":"にる","fr":"ressembler (à)"}),
 XC(13,["だんだん","ちょうど","{急行|きゅうこう}","ずつ"],jp="{毎日|まいにち}れんしゅうをつづけて、ピアノが＿{上手|じょうず}になりました。",fr="En continuant à m'exercer tous les jours, je suis peu à peu devenu bon au piano.",uses=["v4-47","v4-49"]),
 XC(14,["{三|みっ}つ","{六|むっ}つ","{一|ひと}つ","{二|ふた}つ"],q="ケーキが{六|むっ}つありました。{三人|さんにん}が{一|ひと}つずつ{食|た}べました。いくつのこっていますか。",uses=["v4-49"]),
 XC(15,["{通|かよ}って","{集|あつ}まって","{進|すす}んで","{出発|しゅっぱつ}して"],jp="{毎日|まいにち}{電車|でんしゃ}で{会社|かいしゃ}に＿います。とちゅうで{一度|いちど}{乗|の}りかえます。",fr="Je vais au bureau en train tous les jours. Je change une fois en route.",uses=["v4-46","v4-50"]),
]
bloc = {"id": "v4-b10", "level": "N4", "title": "Bouger et changer : déplacements, paires を / が, quantités, circulation",
        "lessons": [l46, l47, l48, l49, l50], "test": test, "examTest": exam}
save_n4(bloc, sys.argv[1])
