import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L76 Verbes N4 (1) ----------
L = "v4-76"
l76 = {"id": L, "title": "Verbes N4 (1)", "words": [
 W("{思|おも}い{出|だ}す","おもいだす","se rappeler","この{歌|うた}を{聞|き}くと、{子|こ}どものころを{思|おも}い{出|だ}します。","Quand j'écoute cette chanson, je me rappelle mon enfance."),
 W("かんじる","かんじる","sentir, ressentir","{朝|あさ}、{少|すこ}しさむさをかんじました。","Ce matin, j'ai senti un peu de froid."),
 W("しんじる","しんじる","croire","{田中|たなか}さんの{話|はなし}をしんじています。","Je crois ce que dit M. Tanaka."),
 W("さがす","さがす","chercher (un objet)","なくしたかぎをさがしています。","Je cherche la clé que j'ai perdue."),
 W("そだてる","そだてる","élever","{母|はは}は{一人|ひとり}で{子|こ}どもを{三人|さんにん}そだてました。","Ma mère a élevé seule trois enfants."),
 W("うえる","うえる","planter","にわに{木|き}をうえました。","J'ai planté un arbre dans le jardin."),
 W("かう","かう","avoir (un animal)","{犬|いぬ}を{二|に}ひきかっています。","J'ai deux chiens."),
 W("たずねる","たずねる","rendre visite ; demander","{先生|せんせい}のおたくをたずねました。","J'ai rendu visite au professeur chez lui."),
 W("なれる","なれる","s'habituer","{日本|にほん}のせいかつにもうなれました。","Je me suis déjà habitué à la vie au Japon."),
 W("つかまえる","つかまえる","attraper","けいさつがどろぼうをつかまえました。","La police a attrapé le voleur."),
 W("にげる","にげる","s'enfuir","ねこが{外|そと}へにげてしまいました。","Le chat s'est enfui dehors."),
 W("{合|あ}う","あう","aller bien, convenir","このくつは{私|わたし}の{足|あし}に{合|あ}いません。","Ces chaussures ne me vont pas."),
 W("はる","はる","coller","{手紙|てがみ}に{切手|きって}をはります。","Je colle un timbre sur la lettre."),
 W("おれる","おれる","se casser (branche, os)","{風|かぜ}で{木|き}がおれました。","L'arbre s'est cassé à cause du vent."),
 W("{楽|たの}しむ","たのしむ","profiter, s'amuser","{旅行|りょこう}を{楽|たの}しんでください。","Profitez bien de votre voyage."),
], "sections": [
 {"h": "Des verbes faciles à confondre",
  "p": ["Même son, sens différent : regardez bien les kanji et la particule."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["chercher un objet / une information", "さがす / しらべる (leçon 66)"],
   ["avoir un animal / acheter", "かう / {買|か}う"],
   ["convenir à / rencontrer", "〜==に=={合|あ}う / 〜==に=={会|あ}う"],
   ["s'habituer à", "〜==に==なれる"],
   ["coller / printemps", "はる / {春|はる}"],
   ["se rappeler", "{思|おも}い{出|だ}す"]]}}
], "pieges": [
 "さがす = chercher ce qu'on n'a pas (objet, travail, personne) ; しらべる = chercher une **information**.",
 "かう (avoir un animal) a le même son que {買|か}う (acheter) : {犬|いぬ}をかっています = j'ai un chien.",
 "{合|あ}う (aller bien, convenir) ≠ {会|あ}う (rencontrer) : くつが{足|あし}に{合|あ}う.",
 "〜**に**なれる = s'habituer **à** : {仕事|しごと}になれる.",
 "たずねる = rendre visite **et** demander ({道|みち}をたずねる).",
 "おれる (ça se casse, が) / おる (je casse, を) : {木|き}がおれる / ほねをおる."
], "exercises": [
 C(L,1,["{思|おも}い{出|だ}します","わすれます","かんじます","しんじます"],jp="この{写真|しゃしん}を{見|み}ると、{子|こ}どものころを＿。",fr="Quand je regarde cette photo, je me rappelle mon enfance.",uses=["v5-28"]),
 C(L,2,["さがして","しらべて","そだてて","うえて"],jp="なくしたかぎを＿いますが、まだ{見|み}つかりません。",fr="Je cherche la clé que j'ai perdue, mais je ne l'ai pas encore trouvée.",uses=["v4-48","v4-49"]),
 C(L,3,["しんじて","にげて","かって","はって"],jp="{田中|たなか}さんはうそをつかない{人|ひと}ですから、{田中|たなか}さんの{話|はなし}を＿います。",fr="M. Tanaka ne ment jamais, alors je crois ce qu'il dit.",uses=["v4-53"]),
 C(L,4,["そだてました","うえました","かいました","つかまえました"],jp="{母|はは}は{一人|ひとり}で{子|こ}どもを{三人|さんにん}＿。",fr="Ma mère a élevé seule trois enfants.",uses=["v5-21"]),
 C(L,5,["うえました","しんじました","はりました","にげました"],jp="{春|はる}に、にわに{花|はな}を＿。",fr="Au printemps, j'ai planté des fleurs dans le jardin.",uses=["v5-22","v5-35"]),
 C(L,6,["かって","うえて","はって","しんじて"],jp="うちでは{犬|いぬ}を{二|に}ひき＿います。",fr="Chez nous, on a deux chiens.",uses=["v5-35"],star={"jp":"かう","kana":"かう","fr":"avoir (un animal)"}),
 C(L,7,["たずねました","にげました","つかまえました","はりました"],jp="{昨日|きのう}、{先生|せんせい}のおたくを＿。",fr="Hier, j'ai rendu visite au professeur chez lui.",uses=["v4-71"]),
 C(L,8,["なれました","にげました","そだてました","おれました"],jp="{日本|にほん}に{来|き}て{一年|いちねん}です。{日本|にほん}のせいかつにもう＿。",fr="Ça fait un an que je suis au Japon. Je me suis déjà habitué à la vie ici.",uses=["v4-68"]),
 C(L,9,["つかまえました","にげました","かいました","うえました"],jp="けいさつがどろぼうを＿。",fr="La police a attrapé le voleur.",uses=["v4-59"]),
 C(L,10,["にげて","つかまえて","かって","しんじて"],jp="ドアが{開|あ}いていて、ねこが{外|そと}へ＿しまいました。",fr="La porte était ouverte, le chat s'est enfui dehors.",uses=["v5-27"]),
 C(L,11,["{合|あ}い","{会|あ}い","{思|おも}い{出|だ}し","かんじ"],jp="このくつは{小|ちい}さくて、{足|あし}に＿ません。",fr="Ces chaussures sont trop petites, elles ne me vont pas.",uses=["v5-13"]),
 C(L,12,["はって","おって","うえて","そだてて"],jp="{手紙|てがみ}に{切手|きって}を＿{出|だ}します。",fr="Je colle un timbre sur la lettre et je la poste.",uses=["v4-59"],star={"jp":"はる","kana":"はる","fr":"coller"}),
 C(L,13,["おれて","にげて","かんじて","なれて"],jp="{強|つよ}い{風|かぜ}で、{古|ふる}い{木|き}が＿しまいました。",fr="Avec le vent fort, le vieil arbre s'est cassé.",uses=["v5-25"]),
 C(L,14,["{楽|たの}しんで","しんじて","さがして","つかまえて"],jp="{旅行|りょこう}を＿きてください。",fr="Profitez bien de votre voyage.",uses=["v5-33"]),
 C(L,15,["かんじます","しんじます","なれます","はります"],jp="{朝|あさ}、{窓|まど}を{開|あ}けると、すずしい{秋|あき}を＿。",fr="Le matin, quand j'ouvre la fenêtre, je sens la fraîcheur de l'automne.",uses=["v5-25"]),
 C(L,16,["avoir (élever) un animal","acheter","chercher","promener"],q="Dans « {犬|いぬ}をかっています », que veut dire かう ?"),
 C(L,17,["さがす : un objet, une personne ; しらべる : une information","さがす : une information ; しらべる : un objet","Aucune","さがす s'emploie seulement au passé"],q="Quelle différence entre さがす et しらべる ?",uses=["v4-66"]),
 O(L,18,"Je cherche la clé que j'ai perdue.",["なくした","かぎを","さがしています"],uses=["v4-49"]),
]}

# ---------- L77 Verbes N4 (2) ----------
L = "v4-77"
l77 = {"id": L, "title": "Verbes N4 (2)", "words": [
 W("てつだう","てつだう","aider","{母|はは}の{料理|りょうり}をてつだいました。","J'ai aidé ma mère à cuisiner."),
 W("ほめる","ほめる","féliciter, faire des compliments","{先生|せんせい}に{作文|さくぶん}をほめられました。","Le professeur m'a félicité pour ma rédaction."),
 W("しかる","しかる","gronder","{宿題|しゅくだい}をしなかったので、{父|ちち}にしかられました。","Je n'avais pas fait mes devoirs, mon père m'a grondé."),
 W("さわぐ","さわぐ","faire du bruit, chahuter","{教室|きょうしつ}でさわがないでください。","Ne faites pas de bruit en classe."),
 W("やくに{立|た}つ","やくにたつ","être utile","このじしょはとてもやくに{立|た}ちます。","Ce dictionnaire est très utile."),
 W("{気|き}がつく","きがつく","se rendre compte","かさをわすれたことに{気|き}がつきました。","Je me suis rendu compte que j'avais oublié mon parapluie."),
 W("えんりょする","えんりょする","se retenir (par politesse)","えんりょしないで、たくさん{食|た}べてください。","Ne vous gênez pas, mangez bien."),
 W("がまんする","がまんする","supporter, se retenir","いたいですが、がまんします。","Ça fait mal, mais je supporte."),
 W("しょうたいする","しょうたいする","inviter","{友|とも}だちをパーティーにしょうたいしました。","J'ai invité des amis à la fête."),
 W("うける","うける","passer (un examen), recevoir","{来月|らいげつ}、{日本語|にほんご}の{試験|しけん}をうけます。","Le mois prochain, je passe l'examen de japonais."),
 W("おどろく","おどろく","être surpris","そのニュースを{聞|き}いて、おどろきました。","J'ai été surpris en entendant cette nouvelle."),
 W("つれる","つれる","emmener (qqn)","{子|こ}どもを{公園|こうえん}につれて{行|い}きます。","J'emmène les enfants au parc."),
 W("はこぶ","はこぶ","transporter","このにもつを{二|に}かいへはこんでください。","Montez ces bagages au premier étage, s'il vous plaît."),
 W("ぬれる","ぬれる","se mouiller","{雨|あめ}で{服|ふく}がぬれました。","Mes vêtements sont mouillés à cause de la pluie."),
 W("ねむる","ねむる","dormir (sommeil)","{赤|あか}ちゃんはよくねむっています。","Le bébé dort profondément."),
], "sections": [
 {"h": "Verbe et particule",
  "p": ["Ces verbes s'apprennent avec leur construction."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["aider à", "〜==を==てつだう"],
   ["être félicité / grondé par", "〜==に==ほめられる / しかられる"],
   ["passer un examen", "{試験|しけん}==を==うける"],
   ["emmener quelqu'un", "〜==を==つれて{行|い}く"],
   ["se rendre compte de", "〜==に=={気|き}がつく"],
   ["ne vous gênez pas", "えんりょしないで"]]}}
], "pieges": [
 "{試験|しけん}**を**うける = passer (présenter) un examen ; ごうかくする = le réussir.",
 "つれて{行|い}く = emmener **une personne, un animal** ; {持|も}って{行|い}く = emporter **un objet**.",
 "えんりょしないで = ne vous gênez pas (invitation à se servir, à parler).",
 "〜**に**{気|き}がつく = se rendre compte **de**.",
 "ねむる = dormir (être endormi) ; ねる = se coucher, dormir.",
 "ほめられる / しかられる : au passif, celui qui félicite ou gronde prend **に**."
], "exercises": [
 C(L,1,["てつだいます","しかります","さわぎます","ぬれます"],jp="{母|はは}が{一人|ひとり}で{料理|りょうり}をしていますから、＿。",fr="Ma mère cuisine toute seule, alors je l'aide.",uses=["v5-14"]),
 C(L,2,["ほめられました","しかられました","てつだわれました","はこばれました"],jp="{作文|さくぶん}がよくできて、{先生|せんせい}に＿。",fr="Ma rédaction était réussie, le professeur m'a félicité.",uses=["v5-29"],star={"jp":"ほめる","kana":"ほめる","fr":"féliciter, faire des compliments"}),
 C(L,3,["しかられました","ほめられました","ねむりました","うけました"],jp="{宿題|しゅくだい}をしなかったので、{父|ちち}に＿。",fr="Je n'avais pas fait mes devoirs, mon père m'a grondé.",uses=["v5-29"],star={"jp":"しかる","kana":"しかる","fr":"gronder"}),
 C(L,4,["さわが","ほめ","がまんし","おどろか"],jp="{図書館|としょかん}では＿ないでください。",fr="Ne faites pas de bruit à la bibliothèque.",uses=["v5-04"]),
 C(L,5,["やくに{立|た}ちます","{気|き}がつきます","がまんします","つれます"],jp="このじしょはとても＿。",fr="Ce dictionnaire est très utile.",uses=["v5-12"]),
 C(L,6,["{気|き}がつきました","えんりょしました","がまんしました","ほめました"],jp="{駅|えき}に{着|つ}いてから、かさをわすれたことに＿。",fr="Une fois à la gare, je me suis rendu compte que j'avais oublié mon parapluie.",uses=["v5-28"]),
 C(L,7,["えんりょ","しょうたい","てつだい","さわぎ"],jp="＿しないで、たくさん{食|た}べてください。",fr="Ne vous gênez pas, mangez bien."),
 C(L,8,["がまん","えんりょ","しょうたい","さわぎ"],jp="ちゅうしゃはいたいですが、ちょっと＿してください。すぐ{終|お}わりますから。",fr="La piqûre fait mal, mais tenez bon un instant : ce sera vite fini.",uses=["v4-44"]),
 C(L,9,["しょうたい","がまん","えんりょ","ほめ"],jp="{友|とも}だちをたんじょうびのパーティーに＿しました。",fr="J'ai invité des amis à ma fête d'anniversaire.",uses=["v5-31"]),
 C(L,10,["うけます","ごうかくします","ねむります","はこびます"],jp="{来月|らいげつ}、{日本語|にほんご}の{試験|しけん}を＿。",fr="Le mois prochain, je passe l'examen de japonais.",uses=["v4-52"]),
 C(L,11,["おどろきました","ほめました","てつだいました","しかりました"],jp="{急|きゅう}に{大|おお}きい{音|おと}がして、＿。",fr="Il y a eu un grand bruit d'un coup, j'ai été surpris.",uses=["v4-55"]),
 C(L,12,["つれて","{持|も}って","ほめて","ぬれて"],jp="{日曜日|にちようび}は{子|こ}どもを{公園|こうえん}に＿{行|い}きます。",fr="Le dimanche, j'emmène les enfants au parc.",uses=["v5-04"]),
 C(L,13,["はこんで","つれて","ねむって","さわいで"],jp="このにもつを{二|に}かいへ＿ください。{重|おも}いですから、{二人|ふたり}で。",fr="Montez ces bagages au premier étage, s'il vous plaît. Ils sont lourds : à deux.",uses=["v5-22","v5-24"]),
 C(L,14,["ぬれました","ねむりました","はこびました","がまんしました"],jp="かさがなかったので、{雨|あめ}で{服|ふく}が＿。",fr="Je n'avais pas de parapluie, mes vêtements sont mouillés.",uses=["v5-25"]),
 C(L,15,["ねむって","しかって","はこんで","てつだって"],jp="{赤|あか}ちゃんがよく＿います。{静|しず}かにしてください。",fr="Le bébé dort profondément. Silence, s'il vous plaît.",uses=["v4-43"]),
 C(L,16,["ne vous gênez pas","ne bougez pas","ne vous inquiétez pas","ne parlez pas"],q="Que veut dire **えんりょしないで** ?"),
 C(L,17,["{日本語|にほんご}の{試験|しけん}をうけます。","{日本語|にほんご}の{試験|しけん}にうけます。","{日本語|にほんご}の{試験|しけん}がうけます。","{日本語|にほんご}の{試験|しけん}をうかります。"],q="« Je passe l'examen de japonais » se dit…"),
 O(L,18,"J'ai aidé ma mère à cuisiner.",["{母|はは}の","{料理|りょうり}を","てつだいました"],uses=["v5-14"]),
]}

# ---------- L78 Adjectifs N4 ----------
L = "v4-78"
l78 = {"id": L, "title": "Adjectifs N4", "words": [
 W("あさい","あさい","peu profond","この{川|かわ}はあさいですから、{子|こ}どもも{遊|あそ}べます。","Cette rivière est peu profonde, les enfants peuvent y jouer."),
 W("うすい","うすい","mince ; léger, fade","このスープは{味|あじ}がうすいです。","Cette soupe est fade."),
 W("おかしい","おかしい","bizarre ; drôle","このパソコンはちょっとおかしいです。","Cet ordinateur a quelque chose de bizarre."),
 W("かたい","かたい","dur","このパンはかたくて、{食|た}べにくいです。","Ce pain est dur, il est difficile à manger."),
 W("こまかい","こまかい","menu, fin ; petite (monnaie)","こまかいお{金|かね}がありますか。","Vous avez de la monnaie ?"),
 W("すごい","すごい","incroyable","あの{人|ひと}は{五|いつ}つのことばが{話|はな}せます。すごいですね。","Cette personne parle cinq langues. Incroyable !"),
 W("すばらしい","すばらしい","magnifique, formidable","{山|やま}の{上|うえ}からのけしきはすばらしかったです。","La vue du haut de la montagne était magnifique."),
 W("{正|ただ}しい","ただしい","juste, correct","{正|ただ}しい{答|こた}えをえらんでください。","Choisissez la bonne réponse."),
 W("めずらしい","めずらしい","rare, inhabituel","{東京|とうきょう}でゆきが{降|ふ}るのはめずらしいです。","Il est rare qu'il neige à Tokyo."),
 W("ふかい","ふかい","profond","この{池|いけ}はふかいですから、{泳|およ}がないでください。","Cet étang est profond, ne vous y baignez pas."),
 W("やわらかい","やわらかい","mou, tendre","このパンはやわらかくておいしいです。","Ce pain est moelleux et bon."),
 W("ねむい","ねむい","avoir sommeil","{昨日|きのう}あまりねなかったので、ねむいです。","Je n'ai pas beaucoup dormi hier, j'ai sommeil."),
 W("{不便|ふべん}","ふべん","pas pratique","{駅|えき}から{遠|とお}くて、{不便|ふべん}です。","C'est loin de la gare, ce n'est pas pratique."),
 W("ふくざつ","ふくざつ","compliqué","この{問題|もんだい}はふくざつで、よく{分|わ}かりません。","Ce problème est compliqué, je ne comprends pas bien."),
 W("むり","むり","impossible, excessif","{一日|いちにち}でぜんぶ{読|よ}むのはむりです。","C'est impossible de tout lire en un jour."),
], "sections": [
 {"h": "Les contraires",
  "p": ["Beaucoup de ces adjectifs vont par paires."],
  "grid": {"head": ["", "sens"], "rows": [
   ["あさい ↔ ふかい", "peu profond ↔ profond"],
   ["かたい ↔ やわらかい", "dur ↔ mou, tendre"],
   ["うすい ↔ あつい", "mince ↔ épais (un autre あつい !)"],
   ["{便利|べんり} ↔ {不便|ふべん}", "pratique ↔ pas pratique"],
   ["かんたん ↔ ふくざつ", "simple ↔ compliqué"],
   ["{正|ただ}しい ↔ まちがっている", "juste ↔ faux"]]}}
], "pieges": [
 "うすい = mince (un livre), léger ou fade (un goût, une couleur).",
 "おかしい = bizarre, qui cloche… **ou** drôle (comme おもしろい).",
 "こまかいお{金|かね} = la petite monnaie.",
 "すごい = incroyable (oral, en bien comme en mal) ; すばらしい = magnifique (toujours en bien).",
 "むり = impossible, trop dur (adjectif en な). むりをしないで = ne force pas.",
 "ねむい = avoir sommeil (adjectif) ; ねむる = dormir (verbe, leçon 77)."
], "exercises": [
 C(L,1,["あさい","ふかい","かたい","ねむい"],jp="この{川|かわ}は＿ですから、{子|こ}どもが{遊|あそ}んでもあんぜんです。",fr="Cette rivière est peu profonde, les enfants peuvent y jouer sans danger.",uses=["v4-50","v5-31"]),
 C(L,2,["ふかい","ねむい","やわらかい","めずらしい"],jp="この{池|いけ}はとても＿ですから、{泳|およ}がないでください。",fr="Cet étang est très profond, ne vous y baignez pas.",uses=["v5-31","v5-35"]),
 C(L,3,["かたく","やわらかく","ねむく","ふかく"],jp="このパンは＿て、{食|た}べにくいです。",fr="Ce pain est dur, il est difficile à manger.",uses=["v5-06"]),
 C(L,4,["うすい","こまかい","かたい","ねむい"],jp="このスープは{味|あじ}が＿です。しおを{入|い}れてください。",fr="Cette soupe est fade. Ajoutez du sel.",uses=["v4-58"]),
 C(L,5,["こまかい","うすい","やわらかい","すばらしい"],jp="すみません、＿お{金|かね}がありませんから、{一万円|いちまんえん}でいいですか。",fr="Désolé, je n'ai pas de monnaie : je peux vous donner un billet de dix mille yens ?",uses=["v5-07"]),
 C(L,6,["すごい","ねむい","あさい","{不便|ふべん}"],jp="あの{人|ひと}は{五|いつ}つのことばが{話|はな}せます。＿ですね。",fr="Cette personne parle cinq langues. Incroyable !",uses=["v4-53"]),
 C(L,7,["すばらしかったです","ねむかったです","ふかかったです","かたかったです"],jp="{山|やま}の{上|うえ}からのけしきは＿。",fr="La vue du haut de la montagne était magnifique.",uses=["v4-62"]),
 C(L,8,["{正|ただ}しい","やわらかい","ねむい","あさい"],jp="＿{答|こた}えをえらんでください。",fr="Choisissez la bonne réponse.",uses=["v4-65","v5-40"]),
 C(L,9,["めずらしい","やわらかい","あさい","ねむい"],jp="{東京|とうきょう}で{四月|しがつ}にゆきが{降|ふ}るのは＿です。",fr="Il est rare qu'il neige à Tokyo en avril.",uses=["v5-25"]),
 C(L,10,["やわらかく","ふかく","ねむく","あさく"],jp="このパンは＿て、おいしいです。",fr="Ce pain est moelleux et bon.",uses=["v5-06"]),
 C(L,11,["ねむい","すごい","めずらしい","かたい"],jp="{昨日|きのう}あまりねなかったので、{今日|きょう}はとても＿です。",fr="Je n'ai pas beaucoup dormi hier, alors aujourd'hui j'ai très sommeil."),
 C(L,12,["{不便|ふべん}","{便利|べんり}","やわらかい","すばらしい"],jp="このアパートは{駅|えき}から{遠|とお}くて、ちょっと＿です。",fr="Cet appartement est loin de la gare, ce n'est pas très pratique.",uses=["v5-19","v5-22"]),
 C(L,13,["ふくざつ","かんたん","めずらしい","ねむい"],jp="この{問題|もんだい}は＿で、よく{分|わ}かりません。",fr="Ce problème est compliqué, je ne comprends pas bien.",uses=["v5-19","v5-29"]),
 C(L,14,["むり","やわらかい","あさい","ねむい"],jp="{一日|いちにち}で{本|ほん}を{十|じゅっ}さつ{読|よ}むのは＿です。",fr="Lire dix livres en un jour, c'est impossible.",uses=["v5-38"]),
 C(L,15,["おかしい","すばらしい","ねむい","あさい"],jp="このパソコンはちょっと＿です。すぐ{止|と}まります。",fr="Cet ordinateur a un problème : il s'arrête tout le temps.",uses=["v4-66"]),
 C(L,16,["あさい","うすい","かるい","ひくい"],q="Contraire de **ふかい** ?"),
 C(L,17,["やわらかい","うすい","あさい","かるい"],q="Contraire de **かたい** ?"),
 O(L,18,"C'est impossible de tout lire en un jour.",["{一日|いちにち}で","ぜんぶ{読|よ}むのは","むり","です"],uses=["v5-38"]),
]}

# ---------- L79 Paires piégeuses du N4 ----------
L = "v4-79"
l79 = {"id": L, "title": "Paires piégeuses du N4", "words": [
 W("おそわる","おそわる","apprendre (de quelqu'un)","{田中|たなか}{先生|せんせい}に{日本語|にほんご}をおそわりました。","J'ai appris le japonais avec le professeur Tanaka."),
 W("{代|か}わる","かわる","remplacer","{部長|ぶちょう}に{代|か}わって、{私|わたし}が{説明|せつめい}します。","J'explique à la place du chef."),
 W("すむ","すむ","se terminer","{宿題|しゅくだい}がすんだら、{遊|あそ}んでもいいです。","Quand tes devoirs seront finis, tu pourras jouer."),
 W("くらす","くらす","vivre (au quotidien)","そぼはいなかで{一人|ひとり}でくらしています。","Ma grand-mère vit seule à la campagne."),
 W("わかれる","わかれる","se séparer, se quitter","{駅|えき}で{友|とも}だちとわかれました。","J'ai quitté mon ami à la gare."),
 W("{学|まな}ぶ","まなぶ","étudier, apprendre","{大学|だいがく}で{日本|にほん}のぶんかを{学|まな}びました。","J'ai étudié la culture japonaise à l'université."),
 W("{乗|の}せる","のせる","faire monter, emmener (en voiture)","{駅|えき}まで{車|くるま}に{乗|の}せてください。","Emmène-moi en voiture jusqu'à la gare, s'il te plaît."),
 W("{降|お}ろす","おろす","déposer, faire descendre","{駅|えき}の{前|まえ}で{降|お}ろしてください。","Déposez-moi devant la gare, s'il vous plaît."),
 W("きけん","きけん","danger, dangereux","この{川|かわ}で{泳|およ}ぐのはきけんです。","Il est dangereux de se baigner dans cette rivière."),
 W("しつれい","しつれい","impoli","{人|ひと}の{話|はなし}を{聞|き}かないのはしつれいです。","Ne pas écouter les autres, c'est impoli."),
 W("たしか","たしか","si je me souviens bien ; sûr","たしか、{会議|かいぎ}は{三時|さんじ}からでした。","Si je me souviens bien, la réunion était à trois heures."),
 W("てきとう","てきとう","approprié ; au hasard","てきとうなことばをえらんでください。","Choisissez le mot qui convient."),
 W("さかん","さかん","florissant, populaire","この{町|まち}はやきゅうがさかんです。","Le baseball est très pratiqué dans cette ville."),
 W("これから","これから","à partir de maintenant","これから{会議|かいぎ}を{始|はじ}めます。","Nous allons maintenant commencer la réunion."),
 W("ゆれる","ゆれる","trembler, bouger","じしんで{家|いえ}がゆれました。","La maison a tremblé à cause du séisme."),
], "sections": [
 {"h": "Les nouvelles paires",
  "p": ["Le N4 ajoute encore quelques paires à ne pas confondre."],
  "grid": {"head": ["", "différence"], "rows": [
   ["{教|おし}える / おそわる", "enseigner / apprendre (de quelqu'un)"],
   ["{住|す}む / くらす / すむ", "habiter / vivre au quotidien / se terminer"],
   ["{乗|の}る / {乗|の}せる", "monter / faire monter quelqu'un"],
   ["{降|お}りる / {降|お}ろす", "descendre / déposer quelqu'un"],
   ["かわる / {代|か}わる", "changer / remplacer"],
   ["あぶない / きけん", "dangereux (oral) / danger (écrit, panneaux)"]]}}
], "pieges": [
 "〜**に**おそわる = apprendre **de** quelqu'un (comme 〜に{習|なら}う).",
 "すむ (se terminer) a le même son que {住|す}む (habiter) : {宿題|しゅくだい}がすむ / {東京|とうきょう}に{住|す}む.",
 "{乗|の}せる / {降|お}ろす : je fais monter, je dépose **quelqu'un d'autre**.",
 "たしか (adverbe) = « si je me souviens bien » ; たしかな = sûr, fiable.",
 "てきとう = approprié… **ou** fait n'importe comment, selon le ton !",
 "しつれい (adj.) = impoli ; しつれいします = excusez-moi (formule)."
], "exercises": [
 C(L,1,["おそわりました","{教|おし}えました","くらしました","わかれました"],jp="{私|わたし}は{田中|たなか}{先生|せんせい}に{日本語|にほんご}を＿。{先生|せんせい}の{説明|せつめい}はとても{分|わ}かりやすかったです。",fr="J'ai appris le japonais avec le professeur Tanaka. Ses explications étaient très claires.",uses=["v4-53"]),
 C(L,2,["{代|か}わって","すんで","わかれて","くらして"],jp="{部長|ぶちょう}がいませんから、{部長|ぶちょう}に＿、{私|わたし}が{説明|せつめい}します。",fr="Le chef n'est pas là, alors j'explique à sa place.",uses=["v4-51","v4-53"]),
 C(L,3,["すんだ","{住|す}んだ","くらした","わかれた"],jp="{宿題|しゅくだい}が＿ら、{遊|あそ}びに{行|い}ってもいいです。",fr="Quand tes devoirs seront finis, tu pourras aller jouer.",uses=["v5-29"],star={"jp":"すむ","kana":"すむ","fr":"se terminer"}),
 C(L,4,["くらして","わかれて","{乗|の}せて","おそわって"],jp="そぼはいなかで{一人|ひとり}で＿います。",fr="Ma grand-mère vit seule à la campagne.",uses=["v4-43","v4-69"]),
 C(L,5,["わかれて","くらして","{乗|の}せて","{降|お}ろして"],jp="{駅|えき}で{友|とも}だちと＿、{一人|ひとり}で{家|いえ}に{帰|かえ}りました。",fr="J'ai quitté mon ami à la gare et je suis rentré seul."),
 C(L,6,["{学|まな}びました","くらしました","わかれました","{降|お}ろしました"],jp="{大学|だいがく}で{日本|にほん}のぶんかを＿。",fr="J'ai étudié la culture japonaise à l'université.",uses=["v4-64"]),
 C(L,7,["{乗|の}せて","{乗|の}って","{降|お}ろして","くらして"],jp="{駅|えき}まで{私|わたし}を{車|くるま}に＿くれませんか。",fr="Tu pourrais m'emmener en voiture jusqu'à la gare ?",uses=["v5-15"]),
 C(L,8,["{降|お}ろして","{乗|の}せて","{降|お}りて","わかれて"],q="Tu es dans un taxi.",jp="すみません、{駅|えき}の{前|まえ}で＿ください。そこで{降|お}ります。",fr="Excusez-moi, déposez-moi devant la gare. Je descends là.",uses=["v5-15"]),
 C(L,9,["きけん","さかん","たしか","しつれい"],jp="この{川|かわ}はふかくて、{泳|およ}ぐのは＿です。",fr="Cette rivière est profonde, il est dangereux de s'y baigner.",uses=["v4-78"]),
 C(L,10,["しつれい","さかん","たしか","すばらしい"],jp="{人|ひと}が{話|はな}しているときに、けいたいを{見|み}るのは＿です。",fr="Regarder son portable pendant que quelqu'un parle, c'est impoli.",uses=["v4-66"]),
 C(L,11,["たしか","てきとう","さかん","しつれい"],jp="＿、{会議|かいぎ}は{三時|さんじ}からだったと{思|おも}います。",fr="Si je me souviens bien, la réunion était à trois heures.",uses=["v4-51"]),
 C(L,12,["てきとう","さかん","きけん","しつれい"],jp="（　）に＿なことばを{入|い}れてください。",fr="Mettez le mot qui convient entre les parenthèses.",uses=["v5-29"]),
 C(L,13,["さかん","しつれい","きけん","てきとう"],jp="この{町|まち}はサッカーが＿で、{子|こ}どもたちはみんなサッカーをします。",fr="Le foot est très populaire dans cette ville : tous les enfants y jouent.",uses=["v5-31"]),
 C(L,14,["これから","たしか","さっき","むかし"],jp="＿{会議|かいぎ}を{始|はじ}めます。みなさん、すわってください。",fr="Nous allons maintenant commencer la réunion. Asseyez-vous, tout le monde.",uses=["v4-54","v4-64"]),
 C(L,15,["ゆれました","わかれました","くらしました","{降|お}ろしました"],jp="じしんで{家|いえ}が{大|おお}きく＿。",fr="La maison a beaucoup tremblé à cause du séisme.",uses=["v4-63"]),
 C(L,16,["apprendre (de quelqu'un)","enseigner","se faire gronder","se tromper"],q="Que veut dire **おそわる** ?"),
 C(L,17,["se terminer","habiter","vivre","se tromper"],q="Dans « {宿題|しゅくだい}がすみました », que veut dire すむ ?"),
 O(L,18,"Emmène-moi en voiture jusqu'à la gare, s'il te plaît.",["{駅|えき}まで","{車|くるま}に","{乗|の}せて","ください"],alt=[["{車|くるま}に","{駅|えき}まで","{乗|の}せて","ください"]],uses=["v5-15"]),
]}

# ---------- L80 Mots composés ----------
L = "v4-80"
l80 = {"id": L, "title": "Suffixes et mots composés", "words": [
 W("〜{中|ちゅう}","〜ちゅう","en cours de …","{田中|たなか}さんは{今|いま}、{電話|でんわ}{中|ちゅう}です。","M. Tanaka est au téléphone en ce moment."),
 W("〜{中|じゅう}","〜じゅう","pendant tout …","{昨日|きのう}は{一日中|いちにちじゅう}{雨|あめ}でした。","Il a plu toute la journée hier."),
 W("〜{始|はじ}める","〜はじめる","commencer à …","{雨|あめ}が{降|ふ}り{始|はじ}めました。","Il a commencé à pleuvoir."),
 W("〜{終|お}わる","〜おわる","finir de …","この{本|ほん}をやっと{読|よ}み{終|お}わりました。","J'ai enfin fini de lire ce livre."),
 W("〜やすい","〜やすい","facile à …","このペンは{書|か}きやすいです。","Ce stylo écrit bien (il est facile à utiliser)."),
 W("〜にくい","〜にくい","difficile à …","この{漢字|かんじ}はおぼえにくいです。","Ce kanji est difficile à retenir."),
 W("〜すぎる","〜すぎる","trop …","{昨日|きのう}は{食|た}べすぎました。","Hier, j'ai trop mangé."),
 W("〜{出|だ}す","〜だす","se mettre (soudain) à …","{急|きゅう}に{子|こ}どもがなき{出|だ}しました。","D'un coup, l'enfant s'est mis à pleurer."),
 W("〜つづける","〜つづける","continuer à …","{三時間|さんじかん}{歩|ある}きつづけました。","J'ai marché trois heures sans m'arrêter."),
 W("〜なおす","〜なおす","refaire","まちがえたので、{書|か}きなおしました。","Je m'étais trompé, alors j'ai réécrit."),
 W("〜{合|あ}う","〜あう","… ensemble, l'un l'autre","{友|とも}だちと{話|はな}し{合|あ}って、きめました。","On en a discuté ensemble, mon ami et moi, et on a décidé."),
 W("〜{目|め}","〜め","…ième","{二|ふた}つ{目|め}の{駅|えき}で{降|お}りてください。","Descendez à la deuxième gare."),
 W("〜せい","〜せい","fabriqué en …","これは{日本|にほん}せいの{時計|とけい}です。","C'est une montre fabriquée au Japon."),
 W("〜{料|りょう}","〜りょう","frais de …","{入場料|にゅうじょうりょう}は{五百円|ごひゃくえん}です。","L'entrée coûte cinq cents yens."),
 W("〜{者|しゃ}","〜しゃ","… (personne)","しょうらい、{研究者|けんきゅうしゃ}になりたいです。","Plus tard, je veux devenir chercheur."),
], "sections": [
 {"h": "Radical du verbe + suffixe",
  "p": ["On prend le radical de la forme ます : {読|よ}み（ます）→ {読|よ}み{始|はじ}める, {読|よ}みやすい, {読|よ}みすぎる."],
  "grid": {"head": ["", "sens"], "rows": [
   ["〜{始|はじ}める · 〜{出|だ}す", "commencer à (出す : d'un coup)"],
   ["〜{終|お}わる · 〜つづける", "finir de · continuer à"],
   ["〜やすい · 〜にくい", "facile à · difficile à"],
   ["〜すぎる", "trop (aussi après un adjectif : {高|たか}すぎる)"],
   ["〜なおす", "refaire"],
   ["〜{合|あ}う", "l'un l'autre, ensemble"]]}}
], "pieges": [
 "Radical de la forme ます + suffixe : {書|か}き + やすい = {書|か}きやすい.",
 "〜{中|ちゅう} = en cours de ({会議|かいぎ}{中|ちゅう}) ; 〜{中|じゅう} = pendant tout ({一日中|いちにちじゅう}, {世界中|せかいじゅう}).",
 "〜{出|だ}す = se mettre **soudain** à : なき{出|だ}す = éclater en sanglots.",
 "〜すぎる marche aussi avec les adjectifs : {高|たか}すぎる = trop cher (い tombe).",
 "〜{目|め} = rang : {二|ふた}つ{目|め}, {三人目|さんにんめ} (comme 〜ばんめ, leçon 70).",
 "〜せい = fabriqué en ({日本|にほん}せい) ; 〜{料|りょう} = frais ({入場料|にゅうじょうりょう}) ; 〜{者|しゃ} = la personne ({研究者|けんきゅうしゃ})."
], "exercises": [
 C(L,1,["{中|ちゅう}","{目|め}","せい","{料|りょう}"],jp="{田中|たなか}さんは{今|いま}、{会議|かいぎ}＿です。あとで{電話|でんわ}してください。",fr="M. Tanaka est en réunion. Rappelez plus tard, s'il vous plaît.",uses=["v4-51"]),
 C(L,2,["{中|じゅう}","{目|め}","せい","{者|しゃ}"],jp="{昨日|きのう}は{一日|いちにち}＿{雨|あめ}でした。",fr="Il a plu toute la journée hier.",uses=["v5-38"]),
 C(L,3,["{始|はじ}め","{終|お}わり","なおし","{合|あ}い"],jp="{雨|あめ}が{降|ふ}り＿ましたから、かさをさしました。",fr="Il a commencé à pleuvoir, alors j'ai ouvert mon parapluie.",uses=["v5-25"]),
 C(L,4,["{終|お}わりました","つづけました","すぎました","{合|あ}いました"],jp="この{本|ほん}をやっと{読|よ}み＿。{三週間|さんしゅうかん}かかりました。",fr="J'ai enfin fini de lire ce livre. Ça m'a pris trois semaines.",uses=["v4-49"]),
 C(L,5,["やすい","すぎ","{終|お}わり","{出|だ}し"],jp="このペンはとても{書|か}き＿です。",fr="Ce stylo écrit très bien."),
 C(L,6,["にくい","やすい","すぎ","なおし"],jp="この{漢字|かんじ}はかたちがふくざつで、おぼえ＿です。",fr="Ce kanji a une forme compliquée, il est difficile à retenir.",uses=["v4-75","v4-78"]),
 C(L,7,["すぎ","やす","にく","{合|あ}い"],jp="{昨日|きのう}はケーキを{食|た}べ＿て、おなかがいたいです。",fr="J'ai mangé trop de gâteau hier, j'ai mal au ventre.",uses=["v5-23"]),
 C(L,8,["{出|だ}し","やすく","すぎ","なおし"],jp="{急|きゅう}に{子|こ}どもがなき＿ました。",fr="D'un coup, l'enfant s'est mis à pleurer.",uses=["v4-41","v4-55"]),
 C(L,9,["つづけ","{始|はじ}め","なおし","{合|あ}っ"],jp="{三時間|さんじかん}{歩|ある}き＿て、つかれました。",fr="J'ai marché trois heures sans m'arrêter, je suis fatigué.",uses=["v5-36"]),
 C(L,10,["なおし","すぎ","{出|だ}し","{合|あ}い"],jp="{答|こた}えをまちがえたので、{書|か}き＿ました。",fr="Je m'étais trompé de réponse, alors j'ai réécrit.",uses=["v4-75"]),
 C(L,11,["{合|あ}っ","すぎ","にくく","{出|だ}し"],jp="{友|とも}だちと{話|はな}し＿て、{旅行|りょこう}の{場所|ばしょ}をきめました。",fr="On en a discuté ensemble, mon ami et moi, et on a choisi la destination du voyage.",uses=["v4-48","v4-69"]),
 C(L,12,["{目|め}","{中|ちゅう}","{料|りょう}","せい"],jp="{二|ふた}つ＿の{駅|えき}で{降|お}りてください。",fr="Descendez à la deuxième gare.",uses=["v5-15"]),
 C(L,13,["せい","{中|ちゅう}","{料|りょう}","{目|め}"],jp="この{時計|とけい}は{日本|にほん}＿です。とてもいいです。",fr="Cette montre est fabriquée au Japon. Elle est très bien.",uses=["v5-12"]),
 C(L,14,["{料|りょう}","{中|ちゅう}","せい","{目|め}"],jp="このてんらんかいの{入場|にゅうじょう}＿は{五百円|ごひゃくえん}です。",fr="L'entrée de cette exposition coûte cinq cents yens.",uses=["v4-61"]),
 C(L,15,["{者|しゃ}","{料|りょう}","{目|め}","{中|ちゅう}"],jp="しょうらい、{研究|けんきゅう}＿になりたいです。",fr="Plus tard, je veux devenir chercheur.",uses=["v4-52","v4-54"]),
 C(L,16,["facile à lire","difficile à lire","trop lire","commencer à lire"],q="Que veut dire **{読|よ}みやすい** ?"),
 C(L,17,["trop cher","pas assez cher","de plus en plus cher","facile à acheter"],q="Que veut dire **{高|たか}すぎる** ?"),
 O(L,18,"J'ai trop mangé hier, j'ai mal au ventre.",["{昨日|きのう}は","{食|た}べすぎて、","おなかが","いたいです"],uses=["v5-23"]),
]}

TC, TO, XC, XO = make_block("v4-b16", "v4-x08")
test = [
 TC(1,["さがして","しらべて","そだてて","にげて"],jp="なくしたさいふを{一時間|いちじかん}＿いますが、{見|み}つかりません。",fr="Ça fait une heure que je cherche le portefeuille que j'ai perdu, sans le trouver.",uses=["v4-76"]),
 TC(2,["てつだいました","しかりました","ほめました","おどろきました"],jp="{母|はは}の{引|ひ}っこしを＿。にもつが{多|おお}くて、たいへんでした。",fr="J'ai aidé ma mère à déménager. Il y avait beaucoup d'affaires, c'était dur.",uses=["v4-77"]),
 TC(3,["やわらかく","かたく","ねむく","ふかく"],jp="このパンは＿て、{小|ちい}さい{子|こ}どもも{食|た}べやすいです。",fr="Ce pain est moelleux, même les petits enfants le mangent facilement.",uses=["v4-78","v4-80"]),
 TC(4,["{降|お}ろして","{降|お}りて","くらして","すんで"],q="Tu es dans un taxi.",jp="すみません、{駅|えき}で＿ください。",fr="Excusez-moi, déposez-moi à la gare.",uses=["v4-79"]),
 TC(5,["にくい","やすい","すぎ","{出|だ}し"],jp="この{漢字|かんじ}はかたちがふくざつで、{書|か}き＿です。",fr="Ce kanji a une forme compliquée, il est difficile à écrire.",uses=["v4-80"]),
 TC(6,["かって","{買|か}って","うえて","はって"],jp="うちでは、ねこを{二|に}ひき＿います。かわいいです。",fr="Chez nous, on a deux chats. Ils sont mignons.",uses=["v4-76"],star={"jp":"かう","kana":"かう","fr":"avoir (un animal)"}),
 TC(7,["うける","ごうかくする","はこぶ","ねむる"],jp="{来月|らいげつ}、{日本語|にほんご}の{試験|しけん}を＿つもりです。",fr="J'ai l'intention de passer l'examen de japonais le mois prochain.",uses=["v4-77"]),
 TC(8,["ふかい","うすい","かるい","ひくい"],q="Contraire de **あさい** ?",uses=["v4-78"]),
 TC(9,["すんだ","{住|す}んだ","くらした","わかれた"],jp="{宿題|しゅくだい}が＿ら、テレビを{見|み}てもいいですよ。",fr="Quand tes devoirs seront finis, tu pourras regarder la télé.",uses=["v4-79"],star={"jp":"すむ","kana":"すむ","fr":"se terminer"}),
 TC(10,["ほめられて","しかられて","てつだわれて","はこばれて"],jp="{先生|せんせい}に{作文|さくぶん}を＿、うれしかったです。",fr="Le professeur m'a félicité pour ma rédaction, j'étais content.",uses=["v4-77"],star={"jp":"ほめる","kana":"ほめる","fr":"féliciter, faire des compliments"}),
 TC(11,["いちにちじゅう","いちにちちゅう","ついたちじゅう","ひとひなか"],q=LECT+"**一日中** ?",uses=["v4-80"],star={"jp":"{一日中|いちにちじゅう}","kana":"いちにちじゅう","fr":"toute la journée"}),
 TC(12,["なれました","にげました","おれました","かいました"],jp="{日本|にほん}のせいかつにもう＿か。",fr="Tu t'es déjà habitué à la vie au Japon ?",uses=["v4-76"]),
 TC(13,["むり","やわらかい","あさい","ねむい"],jp="{一週間|いっしゅうかん}で{本|ほん}を{二十|にじゅっ}さつ{読|よ}むのは＿です。",fr="Lire vingt livres en une semaine, c'est impossible.",uses=["v4-78"]),
 TO(14,"J'ai marché trois heures sans m'arrêter, je suis fatigué.",["{三時間|さんじかん}","{歩|ある}きつづけて、","つかれました"],uses=["v4-80"]),
 TC(15,["ゆれました","わかれました","おれました","にげました"],jp="じしんで{家|いえ}が＿。こわかったです。",fr="La maison a tremblé avec le séisme. J'ai eu peur.",uses=["v4-79"]),
 TC(16,["しつれい","さかん","てきとう","たしか"],jp="{人|ひと}の{家|いえ}に{入|はい}るとき、くつをぬがないのは＿です。",fr="Ne pas enlever ses chaussures en entrant chez quelqu'un, c'est impoli.",uses=["v4-79"]),
]
exam = [
 XC(1,["{先生|せんせい}は{明日|あした}{京都|きょうと}へいらっしゃいます。","{先生|せんせい}は{明日|あした}{京都|きょうと}へまいります。","{先生|せんせい}は{明日|あした}{京都|きょうと}へいらっしゃります。","{先生|せんせい}は{明日|あした}{京都|きょうと}をいらっしゃいます。"],q="Tu parles de ton professeur à un camarade de classe. Une seule phrase convient. Laquelle ?",uses=["v4-71","v4-72"]),
 XC(2,["おかしい","すばらしい","やわらかい","あさい"],jp="{田中|たなか}さんのようすが＿です。{朝|あさ}から{何|なに}も{話|はな}しません。",fr="M. Tanaka a l'air bizarre. Il n'a rien dit depuis ce matin.",uses=["v4-75","v4-78"]),
 XC(3,["けっか","もくてき","ほうほう","かたち"],jp="{試験|しけん}の＿が{悪|わる}かったので、もう{一度|いちど}うけます。",fr="Mes résultats à l'examen étaient mauvais, alors je le repasse.",uses=["v4-75","v4-77"]),
 XC(4,["ねて","さわいで","はこんで","おどろいて"],jp="{昨日|きのう}はねつがあって、{一日中|いちにちじゅう}＿いました。",fr="Hier j'avais de la fièvre, je suis resté couché toute la journée.",uses=["v4-80"]),
 XC(5,["environ 30 %","environ 3 %","environ 65 %","environ 13 %"],q="{日本|にほん}の{人口|じんこう}の{三十|さんじゅう}パーセントぐらいが{六十五|ろくじゅうご}さい{以上|いじょう}です。 Quelle part des Japonais a 65 ans ou plus ?",uses=["v4-68","v4-70"]),
 XC(6,["うかがって","いらっしゃって","めしあがって","くださって"],jp="{来週|らいしゅう}、{先生|せんせい}のおたくに＿もよろしいでしょうか。",fr="Me permettez-vous de passer chez vous la semaine prochaine, professeur ?",uses=["v4-71","v4-72"]),
 XC(7,["{代|か}わって","すんで","くらして","わかれて"],jp="{部長|ぶちょう}が{病気|びょうき}でしたから、{部長|ぶちょう}に＿、{私|わたし}が{会議|かいぎ}で{説明|せつめい}しました。",fr="Le chef était malade, alors c'est moi qui ai fait la présentation à la réunion à sa place.",uses=["v4-75","v4-79"]),
 XO(8,"Ce dictionnaire est facile à utiliser et très utile.",["このじしょは","{使|つか}いやすくて、","とても","やくに{立|た}ちます"],uses=["v4-77","v4-80"]),
 XC(9,["À cause du typhon, le match a été reporté à la semaine prochaine.","Malgré le typhon, le match a lieu cette semaine.","Grâce au typhon, on a gagné le match.","Le typhon arrivera la semaine prochaine, pendant le match."],q="Que veut dire : {台風|たいふう}のため、{試合|しあい}は{来週|らいしゅう}になりました。",uses=["v4-63","v4-75"]),
 XC(10,["かしこまりました","おじゃまします","おかげさまで","どういたしまして"],q="Au restaurant. Le client : « コーヒーをおねがいします。» Que répond l'employé ?",uses=["v4-73"]),
 XC(11,["きけん","さかん","たしか","やわらかい"],jp="この{道|みち}は{夜|よる}{暗|くら}くて、{一人|ひとり}で{歩|ある}くのは＿です。",fr="Cette rue est sombre la nuit, il est dangereux d'y marcher seul.",uses=["v4-79"]),
 XC(12,["なれて","にげて","おれて","かって"],jp="{先週|せんしゅう}から{新|あたら}しい{仕事|しごと}を{始|はじ}めましたが、まだ＿いません。",fr="J'ai commencé un nouveau travail la semaine dernière, mais je ne m'y suis pas encore habitué.",uses=["v4-76"]),
 XC(13,["ほうほう","けっか","かたち","けしき"],jp="{母|はは}は{料理|りょうり}の{時間|じかん}を{短|みじか}くする＿をいろいろ{考|かんが}えています。",fr="Ma mère cherche toutes sortes de moyens de passer moins de temps à cuisiner.",uses=["v4-75"]),
 XC(14,["めずらしい","ふかい","やわらかい","あさい"],jp="ゆかたは{夏|なつ}に{着|き}るものです。{冬|ふゆ}にゆかたを{着|き}る{人|ひと}は＿です。",fr="Le yukata se porte en été. Les gens qui en portent en hiver sont rares.",uses=["v4-64","v4-78"]),
 XC(15,["Quand tu auras fini tes devoirs, tu pourras aller jouer.","Si tu habites ici, tu peux aller jouer.","Fais tes devoirs en jouant.","Tu ne pourras pas aller jouer avant demain."],q="Que veut dire : {宿題|しゅくだい}がすんだら、{遊|あそ}びに{行|い}ってもいいです。",uses=["v4-79"]),
]
# Suffixes de la leçon 80 : sans épingle explicite, le moteur prendrait 中 « dedans », 目 « œil »
# ou un fragment (やすい) avec la traduction de toute la phrase. On épingle le suffixe lui-même.
from common import plain, reading
for e in l80["exercises"] + test:
    if "star" in e or e.get("type") != "choice" or "＿" not in e.get("jp", ""):
        continue
    ans = e["choices"][e["a"]]
    for w in l80["words"]:
        if plain(w["jp"]).lstrip("〜") == plain(ans) and w["kana"].lstrip("〜") == reading(ans):
            e["star"] = {"jp": w["jp"], "kana": w["kana"], "fr": w["fr"]}

bloc = {"id": "v4-b16", "level": "N4", "title": "Consolider le N4 : verbes, adjectifs, paires, mots composés",
        "lessons": [l76, l77, l78, l79, l80], "test": test, "examTest": exam}
save_n4(bloc, sys.argv[1])
