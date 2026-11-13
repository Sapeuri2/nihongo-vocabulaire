import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L51 Le travail ----------
L = "v4-51"
l51 = {"id": L, "title": "Au bureau", "words": [
 W("{社長|しゃちょう}","しゃちょう","PDG, patron","{社長|しゃちょう}は{今|いま}、{会議|かいぎ}{中|ちゅう}です。","Le patron est en réunion en ce moment."),
 W("{部長|ぶちょう}","ぶちょう","chef de service","{部長|ぶちょう}にしりょうを{見|み}せました。","J'ai montré les documents au chef de service."),
 W("{社員|しゃいん}","しゃいん","employé (d'une entreprise)","この{会社|かいしゃ}には{社員|しゃいん}が{百人|ひゃくにん}います。","Cette entreprise compte cent employés."),
 W("{会議|かいぎ}","かいぎ","réunion","{明日|あした}の{会議|かいぎ}は{十時|じゅうじ}からです。","La réunion de demain commence à dix heures."),
 W("{会議室|かいぎしつ}","かいぎしつ","salle de réunion","{会議室|かいぎしつ}は{三|さん}がいにあります。","La salle de réunion est au deuxième étage."),
 W("しゅっちょう","しゅっちょう","voyage d'affaires","{来週|らいしゅう}、しゅっちょうで{大阪|おおさか}へ{行|い}きます。","La semaine prochaine, je vais à Osaka pour le travail."),
 W("ざんぎょう","ざんぎょう","heures supplémentaires","{毎日|まいにち}ざんぎょうがあって、たいへんです。","J'ai des heures sup tous les jours, c'est dur."),
 W("きゅうりょう","きゅうりょう","salaire","きゅうりょうは{毎月|まいつき}{二十五日|にじゅうごにち}です。","Le salaire tombe le 25 de chaque mois."),
 W("うけつけ","うけつけ","accueil, réception","{会社|かいしゃ}に{着|つ}いたら、まずうけつけで{名前|なまえ}を{言|い}ってください。","En arrivant, donnez d'abord votre nom à l'accueil."),
 W("めいし","めいし","carte de visite","はじめまして。これは{私|わたし}のめいしです。","Enchanté. Voici ma carte de visite."),
 W("しりょう","しりょう","documents (de travail)","{会議|かいぎ}のしりょうをコピーしてください。","Photocopiez les documents de la réunion, s'il vous plaît."),
 W("つとめる","つとめる","travailler pour","{兄|あに}は{銀行|ぎんこう}につとめています。","Mon grand frère travaille pour une banque."),
 W("やめる","やめる","arrêter, quitter (un emploi)","{父|ちち}は{去年|きょねん}{会社|かいしゃ}をやめました。","Mon père a quitté son entreprise l'an dernier."),
 W("しっぱいする","しっぱいする","échouer, rater","{大事|だいじ}な{会議|かいぎ}でしっぱいしました。","J'ai raté une réunion importante."),
 W("コピーする","コピーする","photocopier","このしりょうを{十|じゅう}まいコピーしてください。","Faites dix copies de ce document, s'il vous plaît."),
], "sections": [
 {"h": "Dans l'entreprise",
  "p": ["On appelle ses supérieurs par leur titre, sans さん : {田中|たなか}{部長|ぶちょう}, {社長|しゃちょう}."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["patron · chef · employé", "{社長|しゃちょう} · {部長|ぶちょう} · {社員|しゃいん}"],
   ["travailler pour", "〜==に==つとめている"],
   ["quitter son emploi", "{会社|かいしゃ}==を==やめる"],
   ["déplacement · heures sup", "しゅっちょう · ざんぎょう"],
   ["en arrivant", "うけつけ · めいし"]]}}
], "pieges": [
 "〜**に**つとめる = travailler **pour** (une entreprise) ; 〜**で**{働|はたら}く = travailler **dans** (un lieu).",
 "やめる = arrêter une activité, quitter un emploi : {会社|かいしゃ}をやめる, たばこをやめる. ≠ {止|と}める (garer, arrêter une machine).",
 "{部長|ぶちょう}, {社長|しゃちょう} sont déjà des titres de respect : pas de さん après ({田中|たなか}{部長|ぶちょう}).",
 "しゅっちょう = voyage pour le travail ; {旅行|りょこう} = voyage d'agrément.",
 "{会議|かいぎ}{中|ちゅう} = en réunion (〜{中|ちゅう} = en cours de…)."
], "exercises": [
 C(L,1,["つとめて","{働|はたら}いて","やめて","しっぱいして"],jp="{兄|あに}は{銀行|ぎんこう}に＿います。",fr="Mon grand frère travaille pour une banque.",uses=["v5-04"],explain="〜**に**つとめる ; avec {働|はたら}く, il faudrait で."),
 C(L,2,["やめて","つとめて","{止|と}めて","コピーして"],jp="{父|ちち}は{去年|きょねん}{会社|かいしゃ}を＿、{今|いま}は{家|いえ}で{本|ほん}を{書|か}いています。",fr="Mon père a quitté son entreprise l'an dernier ; maintenant il écrit des livres chez lui.",uses=["v5-03"]),
 C(L,3,["しゅっちょう","ざんぎょう","きゅうりょう","めいし"],jp="{来週|らいしゅう}、＿で{大阪|おおさか}へ{行|い}きます。{会社|かいしゃ}の{仕事|しごと}です。",fr="La semaine prochaine, je vais à Osaka en déplacement. C'est pour le travail.",uses=["v5-30"]),
 C(L,4,["ざんぎょう","しゅっちょう","うけつけ","{会議室|かいぎしつ}"],jp="{毎日|まいにち}＿があって、{家|いえ}に{帰|かえ}るのは{十時|じゅうじ}ごろです。",fr="J'ai des heures sup tous les jours, je rentre vers dix heures.",uses=["v5-16"]),
 C(L,5,["きゅうりょう","しりょう","めいし","ざんぎょう"],jp="＿は{毎月|まいつき}{二十五日|にじゅうごにち}にもらいます。",fr="Je touche mon salaire le 25 de chaque mois.",uses=["v5-17","v5-38"]),
 C(L,6,["うけつけ","{社長|しゃちょう}","ざんぎょう","きゅうりょう"],jp="{会社|かいしゃ}に{着|つ}いたら、まず＿で{名前|なまえ}を{言|い}ってください。",fr="En arrivant à l'entreprise, donnez d'abord votre nom à l'accueil.",uses=["v5-15"]),
 C(L,7,["めいし","ざんぎょう","{会議|かいぎ}","きゅうりょう"],jp="はじめまして、{田中|たなか}です。これは{私|わたし}の＿です。",fr="Enchanté, je suis Tanaka. Voici ma carte de visite.",uses=["v5-11"]),
 C(L,8,["しりょう","めいし","きゅうりょう","うけつけ"],jp="{会議|かいぎ}の＿を{十|じゅう}まいコピーしてください。",fr="Faites dix copies des documents de la réunion, s'il vous plaît.",uses=["v5-08"]),
 C(L,9,["{会議室|かいぎしつ}","しゅっちょう","{社長|しゃちょう}","きゅうりょう"],jp="{明日|あした}の{会議|かいぎ}は{三|さん}がいの＿でします。",fr="La réunion de demain a lieu dans la salle du deuxième étage.",uses=["v5-22"]),
 C(L,10,["{田中|たなか}{部長|ぶちょう}","{田中|たなか}{部長|ぶちょう}さん","{田中|たなか}さん{部長|ぶちょう}","{部長|ぶちょう}{田中|たなか}さま"],q="Au bureau, comment appelle-t-on M. Tanaka, chef de service ?",explain="Le titre suffit : {田中|たなか}{部長|ぶちょう} (pas de さん en plus)."),
 C(L,11,["しっぱい","コピー","しゅっちょう","ざんぎょう"],jp="{大事|だいじ}な{会議|かいぎ}で{話|はな}すことをわすれて、＿しました。",fr="J'ai oublié ce que je devais dire à une réunion importante : j'ai complètement raté.",uses=["v5-28","v5-39"]),
 C(L,12,["le PDG, le patron","le chef de service","l'employé","le client"],q="Que veut dire **{社長|しゃちょう}** ?"),
 C(L,13,["{社員|しゃいん}","{社長|しゃちょう}","{部長|ぶちょう}","めいし"],jp="この{会社|かいしゃ}には＿が{三百人|さんびゃくにん}います。",fr="Cette entreprise compte trois cents employés.",uses=["v5-07"]),
 C(L,14,["arrêter (une habitude)","garer","acheter","allumer"],q="Dans « たばこをやめました », que veut dire やめる ?"),
 C(L,15,["かいぎしつ","かいぎしち","あいぎしつ","かいぎむろ"],q=LECT+"**会議室** ?"),
 C(L,16,["コピーして","しっぱいして","つとめて","やめて"],jp="{部長|ぶちょう}、このしりょうを＿もいいですか。",fr="Chef, je peux photocopier ce document ?"),
 O(L,17,"Mon grand frère travaille pour une banque.",["{兄|あに}は","{銀行|ぎんこう}に","つとめています"],uses=["v5-04"]),
 O(L,18,"La salle de réunion est au deuxième étage (3がい).",["{会議室|かいぎしつ}は","{三|さん}がいに","あります"],uses=["v5-22"]),
]}

# ---------- L52 Les études ----------
L = "v4-52"
l52 = {"id": L, "title": "Les études", "words": [
 W("{入学|にゅうがく}する","にゅうがくする","entrer (dans une école)","むすめは{来年|らいねん}{小学校|しょうがっこう}に{入学|にゅうがく}します。","Ma fille entre à l'école primaire l'an prochain."),
 W("そつぎょうする","そつぎょうする","terminer ses études (diplôme)","{兄|あに}は{去年|きょねん}{大学|だいがく}をそつぎょうしました。","Mon grand frère a fini l'université l'an dernier."),
 W("ごうかくする","ごうかくする","réussir (un examen)","{試験|しけん}にごうかくして、とてもうれしいです。","J'ai réussi l'examen, je suis très content."),
 W("{研究|けんきゅう}する","けんきゅうする","faire des recherches","{大学|だいがく}で{日本|にほん}のれきしを{研究|けんきゅう}しています。","Je fais des recherches sur l'histoire du Japon à l'université."),
 W("せんもん","せんもん","spécialité","{大学|だいがく}でのせんもんは{何|なん}ですか。— {文学|ぶんがく}です。","Quelle est ta spécialité à l'université ? — La littérature."),
 W("りゅうがくする","りゅうがくする","étudier à l'étranger","{来年|らいねん}、{日本|にほん}にりゅうがくします。","L'an prochain, je pars étudier au Japon."),
 W("{小学校|しょうがっこう}","しょうがっこう","école primaire","{弟|おとうと}は{小学校|しょうがっこう}の{三年生|さんねんせい}です。","Mon petit frère est en troisième année de primaire."),
 W("{中学校|ちゅうがっこう}","ちゅうがっこう","collège","{中学校|ちゅうがっこう}で{英語|えいご}を{習|なら}いました。","J'ai appris l'anglais au collège."),
 W("{高校|こうこう}","こうこう","lycée","{高校|こうこう}までバスで{三十分|さんじゅっぷん}です。","Le lycée est à trente minutes en bus."),
 W("せいと","せいと","élève","この{学校|がっこう}にはせいとが{五百人|ごひゃくにん}います。","Cette école compte cinq cents élèves."),
 W("てん","てん","note, point","{試験|しけん}で{九十|きゅうじゅう}てんをとりました。","J'ai eu 90 points à l'examen."),
 W("ふくしゅうする","ふくしゅうする","réviser (après le cours)","{授業|じゅぎょう}のあとで、ふくしゅうします。","Je révise après le cours."),
 W("よしゅうする","よしゅうする","préparer (avant le cours)","{授業|じゅぎょう}の{前|まえ}に、よしゅうしてください。","Préparez-vous avant le cours."),
 W("こうぎ","こうぎ","cours magistral","{午後|ごご}は{大学|だいがく}でこうぎがあります。","L'après-midi, j'ai un cours à l'université."),
 W("れきし","れきし","histoire","れきしの{本|ほん}を{読|よ}むのが{好|す}きです。","J'aime lire des livres d'histoire."),
], "sections": [
 {"h": "L'école au Japon",
  "p": ["On entre **dans** une école (に) et on **en** sort (を), comme pour le train : {乗|の}る / {降|お}りる."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["6 à 12 ans", "{小学校|しょうがっこう}"],
   ["12 à 15 ans", "{中学校|ちゅうがっこう}"],
   ["15 à 18 ans", "{高校|こうこう}"],
   ["ensuite", "{大学|だいがく}"],
   ["entrer / finir", "〜==に=={入学|にゅうがく}する / 〜==を==そつぎょうする"],
   ["avant / après le cours", "よしゅう / ふくしゅう"]]}}
], "pieges": [
 "〜**に**{入学|にゅうがく}する (entrer **dans**) ; 〜**を**そつぎょうする (sortir **de**).",
 "{試験|しけん}**に**ごうかくする (réussir) ↔ {試験|しけん}**に**おちる (échouer, leçon 48).",
 "せいと = élève (collège, lycée) ; {学生|がくせい} = étudiant. 〜{年生|ねんせい} = élève de … année.",
 "よしゅう se fait **avant** le cours, ふくしゅう **après**.",
 "てんを**とる** = obtenir une note.",
 "りゅうがくする = partir étudier à l'étranger : {日本|にほん}**に**りゅうがくする."
], "exercises": [
 C(L,1,["{入学|にゅうがく}します","そつぎょうします","{研究|けんきゅう}します","よしゅうします"],jp="むすめは{来年|らいねん}、{小学校|しょうがっこう}に＿。",fr="Ma fille entre à l'école primaire l'an prochain.",uses=["v4-43"]),
 C(L,2,["そつぎょうして","{入学|にゅうがく}して","ごうかくして","りゅうがくして"],jp="{兄|あに}は{去年|きょねん}{大学|だいがく}を＿、{今|いま}は{会社|かいしゃ}で{働|はたら}いています。",fr="Mon grand frère a fini l'université l'an dernier ; il travaille maintenant dans une entreprise.",uses=["v5-30"]),
 C(L,3,["ごうかくして","おちて","そつぎょうして","ふくしゅうして"],jp="{試験|しけん}に＿、{来月|らいげつ}から{大学生|だいがくせい}です。",fr="J'ai réussi l'examen : je suis étudiant à partir du mois prochain.",uses=["v4-48","v5-30"]),
 C(L,4,["{研究|けんきゅう}して","ごうかくして","そつぎょうして","{入学|にゅうがく}して"],jp="{大学|だいがく}で{日本|にほん}のれきしを＿います。",fr="Je fais des recherches sur l'histoire du Japon à l'université."),
 C(L,5,["せんもん","てん","せいと","{中学校|ちゅうがっこう}"],jp="{大学|だいがく}での＿は{何|なん}ですか。— {文学|ぶんがく}です。",fr="Quelle est ta spécialité à l'université ? — La littérature.",uses=["v5-09"]),
 C(L,6,["りゅうがく","そつぎょう","よしゅう","ふくしゅう"],jp="{来年|らいねん}、フランスから{日本|にほん}の{大学|だいがく}に＿します。",fr="L'an prochain, je pars de France étudier dans une université japonaise.",uses=["v5-33"]),
 C(L,7,["{小学校|しょうがっこう}","{中学校|ちゅうがっこう}","{高校|こうこう}","{大学|だいがく}"],jp="{弟|おとうと}は{七|なな}さいです。＿の{二年生|にねんせい}です。",fr="Mon petit frère a sept ans. Il est en deuxième année de primaire.",uses=["v5-08"]),
 C(L,8,["せいと","てん","せんもん","こうぎ"],jp="この{学校|がっこう}には＿が{五百人|ごひゃくにん}います。",fr="Cette école compte cinq cents élèves.",uses=["v5-08"]),
 C(L,9,["てん","まい","{人|にん}","さつ"],jp="{試験|しけん}で{九十|きゅうじゅう}＿をとりました。",fr="J'ai eu 90 points à l'examen.",uses=["v5-08","v5-29"]),
 C(L,10,["よしゅう","ふくしゅう","そつぎょう","{入学|にゅうがく}"],jp="{授業|じゅぎょう}の{前|まえ}に＿しておくと、よく{分|わ}かります。",fr="Si on se prépare avant le cours, on comprend bien.",uses=["v5-29"]),
 C(L,11,["ふくしゅう","よしゅう","ごうかく","りゅうがく"],jp="{授業|じゅぎょう}のあとで、{習|なら}ったことを＿します。",fr="Après le cours, je révise ce que j'ai appris.",uses=["v5-28"]),
 C(L,12,["こうぎ","てん","せいと","{小学校|しょうがっこう}"],jp="{午後|ごご}は{大学|だいがく}で{先生|せんせい}の＿を{聞|き}きます。",fr="L'après-midi, j'assiste au cours du professeur à l'université.",uses=["v5-16"]),
 C(L,13,["そつぎょうする","ごうかくする","りゅうがくする","よしゅうする"],q="Contraire de **{入学|にゅうがく}する** ?"),
 C(L,14,["réussir (un examen)","échouer","réviser","s'inscrire"],q="Que veut dire **ごうかくする** ?"),
 C(L,15,["けんきゅう","けんく","けんきょう","げんきゅう"],q=LECT+"**研究** ?"),
 C(L,16,["{高校|こうこう}に{入学|にゅうがく}しました。","{高校|こうこう}を{入学|にゅうがく}しました。","{高校|こうこう}で{入学|にゅうがく}しました。","{高校|こうこう}が{入学|にゅうがく}しました。"],q="« Je suis entré au lycée » se dit…"),
 O(L,17,"Mon grand frère a fini l'université l'an dernier.",["{兄|あに}は","{去年|きょねん}","{大学|だいがく}を","そつぎょうしました"],alt=[["{去年|きょねん}","{兄|あに}は","{大学|だいがく}を","そつぎょうしました"]],uses=["v5-03"]),
 O(L,18,"Je fais des recherches sur l'histoire du Japon à l'université.",["{大学|だいがく}で","{日本|にほん}の","れきしを","{研究|けんきゅう}しています"],alt=[["{日本|にほん}の","れきしを","{大学|だいがく}で","{研究|けんきゅう}しています"]],uses=["v5-30"]),
]}

# ---------- L53 Communiquer ----------
L = "v4-53"
l53 = {"id": L, "title": "Communiquer", "words": [
 W("れんらくする","れんらくする","contacter, prévenir","{明日|あした}、メールでれんらくします。","Je te contacte par mail demain."),
 W("{説明|せつめい}する","せつめいする","expliquer","{先生|せんせい}がことばの{意味|いみ}を{説明|せつめい}しました。","Le professeur a expliqué le sens du mot."),
 W("そうだんする","そうだんする","consulter, demander conseil","{仕事|しごと}のことを{部長|ぶちょう}にそうだんしました。","J'ai demandé conseil au chef de service pour le travail."),
 W("へんじ","へんじ","réponse (lettre, appel)","{手紙|てがみ}を{書|か}きましたが、まだへんじが{来|き}ません。","J'ai écrit une lettre, mais pas encore de réponse."),
 W("つたえる","つたえる","transmettre (un message)","{田中|たなか}さんに、{会議|かいぎ}は{三時|さんじ}からだとつたえてください。","Dites à M. Tanaka que la réunion commence à trois heures."),
 W("あやまる","あやまる","s'excuser","おくれて、{友|とも}だちにあやまりました。","J'étais en retard, je me suis excusé auprès de mon ami."),
 W("ことわる","ことわる","refuser (poliment)","{仕事|しごと}がいそがしいので、パーティーをことわりました。","J'étais débordé de travail, j'ai décliné la fête."),
 W("たのむ","たのむ","demander (un service) ; commander","{店|みせ}の{人|ひと}にコーヒーをたのみました。","J'ai commandé un café au serveur."),
 W("{知|し}らせる","しらせる","informer, faire savoir","{住所|じゅうしょ}がかわったら、{知|し}らせてください。","Si ton adresse change, préviens-moi."),
 W("おれい","おれい","remerciement","{友|とも}だちにおれいの{手紙|てがみ}を{書|か}きました。","J'ai écrit une lettre de remerciement à un ami."),
 W("しょうかいする","しょうかいする","présenter (qqn)","{友|とも}だちを{家族|かぞく}にしょうかいしました。","J'ai présenté mon ami à ma famille."),
 W("あいさつ","あいさつ","salutation","{朝|あさ}、{会社|かいしゃ}の{人|ひと}に「おはようございます」とあいさつします。","Le matin, je salue mes collègues d'un « bonjour »."),
 W("メール","メール","e-mail, message","{毎日|まいにち}たくさんメールが{来|き}ます。","Je reçois beaucoup de mails tous les jours."),
 W("うそ","うそ","mensonge","うそをつかないでください。","Ne mens pas, s'il te plaît."),
 W("{会話|かいわ}","かいわ","conversation","{日本語|にほんご}の{会話|かいわ}はむずかしいです。","La conversation en japonais, c'est difficile."),
], "sections": [
 {"h": "Qui fait quoi à qui ?",
  "p": ["La personne à qui l'on s'adresse prend **に**."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["demander conseil à", "〜==に==そうだんする"],
   ["transmettre à", "〜==に==つたえる"],
   ["s'excuser auprès de", "〜==に==あやまる"],
   ["demander (un service) à", "〜==に==たのむ"],
   ["présenter A à B", "A==を==B==に==しょうかいする"],
   ["mentir", "うそ==を==つく"]]}}
], "pieges": [
 "たのむ = demander un **service**, ou **commander** (au restaurant). Demander une information : {聞|き}く.",
 "ことわる = refuser poliment (une invitation, une demande).",
 "へんじ = réponse à une lettre, un mail, un appel ; {答|こた}え = réponse à une question (examen).",
 "{知|し}らせる = faire savoir ; {知|し}る = savoir.",
 "« Mentir » se dit うそを**つく** (expression toute faite).",
 "あいさつ**を**する = saluer, dire bonjour (ou faire un petit discours)."
], "exercises": [
 C(L,1,["れんらく","あいさつ","うそ","おれい"],jp="{時間|じかん}がきまったら、メールで＿します。",fr="Quand l'heure sera fixée, je te préviendrai par mail.",uses=["v4-48"]),
 C(L,2,["{説明|せつめい}","そうだん","あいさつ","うそ"],jp="{先生|せんせい}がことばの{意味|いみ}を＿しました。よく{分|わ}かりました。",fr="Le professeur a expliqué le sens du mot. J'ai bien compris.",uses=["v5-29"]),
 C(L,3,["そうだん","しょうかい","あいさつ","へんじ"],jp="{仕事|しごと}のことを{部長|ぶちょう}に＿しました。いいアドバイスをもらいました。",fr="J'ai consulté le chef de service à propos du travail. Il m'a donné de bons conseils.",uses=["v4-51"]),
 C(L,4,["へんじ","{答|こた}え","あいさつ","うそ"],jp="{友|とも}だちに{手紙|てがみ}を{書|か}きましたが、まだ＿が{来|き}ません。",fr="J'ai écrit une lettre à un ami, mais il ne m'a pas encore répondu.",uses=["v5-12"],explain="Réponse à une lettre, un mail : へんじ. {答|こた}え, c'est la réponse à une question."),
 C(L,5,["つたえて","あやまって","ことわって","たのんで"],jp="{田中|たなか}さんに、{会議|かいぎ}は{三時|さんじ}からだと＿ください。",fr="Dites à M. Tanaka que la réunion commence à trois heures.",uses=["v4-51"]),
 C(L,6,["あやまりました","ことわりました","しょうかいしました","たのみました"],jp="{三十分|さんじゅっぷん}もおくれて、{友|とも}だちに＿。",fr="J'avais trente minutes de retard, je me suis excusé auprès de mon ami.",uses=["v4-50"]),
 C(L,7,["ことわりました","たのみました","あやまりました","{知|し}らせました"],jp="{仕事|しごと}がいそがしいので、{友|とも}だちのパーティーに{行|い}くのを＿。",fr="J'étais débordé, alors j'ai décliné la fête de mon ami.",uses=["v5-31"]),
 C(L,8,["たのみました","つたえました","れんらくしました","あいさつしました"],jp="レストランで、コーヒーを{二|ふた}つ＿。",fr="Au restaurant, j'ai commandé deux cafés.",uses=["v5-08"]),
 C(L,9,["{知|し}らせて","{知|し}って","あやまって","ことわって"],jp="{住所|じゅうしょ}がかわったら、すぐ＿ください。",fr="Si ton adresse change, préviens-moi tout de suite.",uses=["v4-47","v5-33"]),
 C(L,10,["おれい","うそ","{会話|かいわ}","めいし"],jp="{引|ひ}っこしをてつだってくれた{友|とも}だちに、＿の{手紙|てがみ}を{書|か}きました。",fr="J'ai écrit une lettre de remerciement à l'ami qui m'a aidé à déménager.",uses=["v4-46","v4-51"]),
 C(L,11,["しょうかい","そうだん","れんらく","あいさつ"],jp="{新|あたら}しい{友|とも}だちを{家族|かぞく}に＿しました。",fr="J'ai présenté mon nouvel ami à ma famille.",uses=["v5-21"]),
 C(L,12,["あいさつ","しょうかい","そうだん","おれい"],jp="{朝|あさ}、{会社|かいしゃ}の{人|ひと}に「おはようございます」と＿します。",fr="Le matin, je salue mes collègues d'un « bonjour ».",uses=["v5-11"]),
 C(L,13,["うそ","へんじ","あいさつ","メール"],jp="＿をつかないでください。ほんとうのことを{言|い}ってください。",fr="Ne mens pas. Dis la vérité.",uses=["v5-28"]),
 C(L,14,["{会話|かいわ}","うそ","おれい","へんじ"],jp="{日本語|にほんご}の＿はまだ{下手|へた}ですが、{読|よ}むのは{好|す}きです。",fr="Je suis encore mauvais en conversation japonaise, mais j'aime lire.",uses=["v5-19"]),
 C(L,15,["refuser (poliment)","demander","s'excuser","répondre"],q="Que veut dire **ことわる** ?"),
 C(L,16,["commander","refuser","renverser","boire"],q="Dans « コーヒーをたのみました », que veut dire たのむ ?"),
 O(L,17,"Je te contacte par mail demain.",["{明日|あした}","メールで","れんらく","します"],alt=[["メールで","{明日|あした}","れんらく","します"]],uses=["v5-03"]),
 O(L,18,"J'ai présenté mon ami à ma famille.",["{友|とも}だちを","{家族|かぞく}に","しょうかいしました"],alt=[["{家族|かぞく}に","{友|とも}だちを","しょうかいしました"]],uses=["v5-21"]),
]}

# ---------- L54 Projets et rendez-vous ----------
L = "v4-54"
l54 = {"id": L, "title": "Projets, rendez-vous, moments", "words": [
 W("よてい","よてい","programme, projet","{週末|しゅうまつ}のよていは{何|なん}ですか。","Qu'est-ce que tu as prévu ce week-end ?"),
 W("{計画|けいかく}","けいかく","plan, projet","{夏|なつ}の{旅行|りょこう}の{計画|けいかく}を{立|た}てています。","Je prépare le plan du voyage d'été."),
 W("じゅんび","じゅんび","préparatifs","{旅行|りょこう}のじゅんびはもうできましたか。","Les préparatifs du voyage sont terminés ?"),
 W("{用意|ようい}","ようい","préparation (concrète)","{晩|ばん}ご{飯|はん}の{用意|ようい}ができました。","Le dîner est prêt."),
 W("やくそく","やくそく","promesse, rendez-vous","{友|とも}だちと{三時|さんじ}に{会|あ}うやくそくをしました。","J'ai rendez-vous avec un ami à trois heures."),
 W("{都合|つごう}","つごう","disponibilité, convenance","{明日|あした}は{都合|つごう}が{悪|わる}いです。","Demain, ça ne m'arrange pas."),
 W("よやく","よやく","réservation","レストランをよやくしました。","J'ai réservé au restaurant."),
 W("キャンセル","キャンセル","annulation","ホテルのよやくをキャンセルしました。","J'ai annulé la réservation d'hôtel."),
 W("{今度|こんど}","こんど","la prochaine fois","{今度|こんど}の{日曜日|にちようび}、いっしょに{映画|えいが}を{見|み}ませんか。","Dimanche prochain, on va voir un film ensemble ?"),
 W("この{間|あいだ}","このあいだ","l'autre jour","この{間|あいだ}はありがとうございました。","Merci pour l'autre jour."),
 W("さっき","さっき","tout à l'heure (il y a peu)","さっき{田中|たなか}さんから{電話|でんわ}がありました。","M. Tanaka a téléphoné tout à l'heure."),
 W("さいきん","さいきん","ces derniers temps","さいきん、{仕事|しごと}がいそがしいです。","Ces derniers temps, je suis débordé."),
 W("さいしょ","さいしょ","début, d'abord","さいしょは{日本語|にほんご}がぜんぜん{分|わ}かりませんでした。","Au début, je ne comprenais rien au japonais."),
 W("さいご","さいご","fin, dernier","{映画|えいが}のさいごがよかったです。","La fin du film était bien."),
 W("しょうらい","しょうらい","avenir, plus tard","しょうらい、{医者|いしゃ}になりたいです。","Plus tard, je veux devenir médecin."),
], "sections": [
 {"h": "Avant, maintenant, plus tard",
  "p": ["Des repères de temps très fréquents à l'oral."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["il y a un instant", "さっき"],
   ["l'autre jour", "この{間|あいだ}"],
   ["ces derniers temps", "さいきん"],
   ["la prochaine fois", "{今度|こんど}"],
   ["plus tard (dans la vie)", "しょうらい"],
   ["au début / à la fin", "さいしょ / さいご"]]}}
], "pieges": [
 "{今度|こんど}の{日曜日|にちようび} = dimanche **prochain** ; この{間|あいだ} = l'autre jour (**passé**).",
 "{都合|つごう}がいい / {悪|わる}い = ça m'arrange / ça ne m'arrange pas (pour fixer un rendez-vous).",
 "やくそく = promesse **et** rendez-vous (avec un ami). Chez le médecin, à l'hôtel : よやく (réservation).",
 "{計画|けいかく}を**{立|た}てる** = faire des plans.",
 "じゅんび = les préparatifs en général ; {用意|ようい} = préparer concrètement (repas, affaires). 〜ができる = c'est prêt.",
 "さっき = il y a quelques minutes ; さいきん = ces dernières semaines."
], "exercises": [
 C(L,1,["よてい","さいご","キャンセル","さっき"],jp="{週末|しゅうまつ}の＿は{何|なん}ですか。— {友|とも}だちと{山|やま}に{行|い}きます。",fr="Qu'est-ce que tu as prévu ce week-end ? — Je vais à la montagne avec des amis.",uses=["v5-17"]),
 C(L,2,["{計画|けいかく}","{用意|ようい}","やくそく","{都合|つごう}"],jp="{夏|なつ}の{旅行|りょこう}の＿を{立|た}てています。",fr="Je prépare le plan du voyage d'été.",uses=["v5-33"]),
 C(L,3,["じゅんび","さいご","さっき","しょうらい"],jp="{明日|あした}は{旅行|りょこう}ですね。＿はもうできましたか。",fr="Tu pars en voyage demain. Les préparatifs sont terminés ?",uses=["v5-33"]),
 C(L,4,["{用意|ようい}","{計画|けいかく}","やくそく","{都合|つごう}"],jp="{晩|ばん}ご{飯|はん}の＿ができましたよ。{食|た}べましょう。",fr="Le dîner est prêt ! Mangeons.",uses=["v5-06"]),
 C(L,5,["やくそく","よやく","キャンセル","さいご"],jp="{友|とも}だちと{三時|さんじ}に{駅|えき}で{会|あ}う＿をしました。",fr="J'ai rendez-vous avec un ami à trois heures à la gare.",uses=["v5-02"]),
 C(L,6,["{都合|つごう}","{気分|きぶん}","{計画|けいかく}","よてい"],jp="すみません、{明日|あした}は＿が{悪|わる}いです。{金曜日|きんようび}はどうですか。",fr="Désolé, demain ça ne m'arrange pas. Et vendredi ?",uses=["v5-17"]),
 C(L,7,["よやく","キャンセル","さいご","しょうらい"],jp="{人|ひと}が{多|おお}いレストランですから、{前|まえ}に＿しておきます。",fr="C'est un restaurant très fréquenté, alors je réserve à l'avance.",uses=["v5-05"]),
 C(L,8,["キャンセル","じゅんび","{用意|ようい}","やくそく"],jp="{病気|びょうき}になって、ホテルのよやくを＿しました。",fr="Je suis tombé malade, j'ai annulé la réservation d'hôtel.",uses=["v5-23","v5-33"]),
 C(L,9,["{今度|こんど}","この{間|あいだ}","さっき","さいきん"],jp="＿の{日曜日|にちようび}、いっしょに{映画|えいが}を{見|み}ませんか。",fr="Dimanche prochain, on va voir un film ensemble ?",uses=["v5-31"]),
 C(L,10,["この{間|あいだ}","{今度|こんど}","しょうらい","さいきん"],jp="＿はどうもありがとうございました。とても{楽|たの}しかったです。",fr="Merci beaucoup pour l'autre jour. C'était très agréable.",uses=["v5-37"]),
 C(L,11,["さっき","{今度|こんど}","しょうらい","さいご"],jp="＿{田中|たなか}さんから{電話|でんわ}がありましたよ。{五分|ごふん}ぐらい{前|まえ}です。",fr="M. Tanaka a téléphoné tout à l'heure. Il y a environ cinq minutes.",uses=["v5-16"]),
 C(L,12,["さいきん","さっき","{今度|こんど}","しょうらい"],jp="＿、{仕事|しごと}がとてもいそがしくて、ねる{時間|じかん}がありません。",fr="Ces derniers temps, je suis tellement débordé que je n'ai pas le temps de dormir."),
 C(L,13,["さいしょ","さいご","{今度|こんど}","しょうらい"],jp="＿は{日本語|にほんご}がぜんぜん{分|わ}かりませんでしたが、{今|いま}は{大分|だいぶ}{分|わ}かります。",fr="Au début, je ne comprenais rien au japonais, mais maintenant je comprends pas mal.",uses=["v4-49"]),
 C(L,14,["さいご","よてい","{都合|つごう}","よやく"],jp="{映画|えいが}の＿がとてもかなしくて、ないてしまいました。",fr="La fin du film était si triste que j'ai pleuré.",uses=["v4-41"]),
 C(L,15,["しょうらい","さっき","この{間|あいだ}","さいきん"],jp="＿は{医者|いしゃ}になりたいです。",fr="Plus tard, je veux devenir médecin.",uses=["v5-30"]),
 C(L,16,["{明日|あした}は{都合|つごう}が{悪|わる}いです。","{明日|あした}は{都合|つごう}がないです。","{明日|あした}は{都合|つごう}を{悪|わる}いです。","{明日|あした}は{都合|つごう}が{悪|わる}いします。"],q="« Demain, ça ne m'arrange pas » se dit…"),
 O(L,17,"J'ai réservé un restaurant pour samedi.",["{土曜日|どようび}の","レストランを","よやく","しました"],uses=["v5-17"]),
 O(L,18,"Les préparatifs du voyage sont terminés.",["{旅行|りょこう}の","じゅんびが","できました"],uses=["v5-33"]),
]}

# ---------- L55 Adverbes N4 (1) ----------
L = "v4-55"
l55 = {"id": L, "title": "Adverbes N4 (1)", "words": [
 W("かならず","かならず","sans faute, toujours","{明日|あした}はかならず{来|き}てください。","Venez demain sans faute."),
 W("ずっと","ずっと","tout le temps ; bien plus","{朝|あさ}からずっと{雨|あめ}が{降|ふ}っています。","Il pleut sans arrêt depuis ce matin."),
 W("たまに","たまに","de temps en temps (rarement)","たまにレストランで{晩|ばん}ご{飯|はん}を{食|た}べます。","De temps en temps, je dîne au restaurant."),
 W("なかなか","なかなか","(ne…) pas facilement ; assez","バスがなかなか{来|き}ません。","Le bus n'arrive pas."),
 W("{特|とく}に","とくに","surtout, en particulier","{果物|くだもの}が{好|す}きです。{特|とく}にりんごが{好|す}きです。","J'aime les fruits. Surtout les pommes."),
 W("{急|きゅう}に","きゅうに","soudain","{急|きゅう}に{雨|あめ}が{降|ふ}ってきました。","Il s'est mis à pleuvoir d'un coup."),
 W("きっと","きっと","sûrement","{田中|たなか}さんはきっと{来|き}ますよ。","M. Tanaka viendra sûrement."),
 W("ぜひ","ぜひ","absolument (souhait, invitation)","ぜひ{一度|いちど}{日本|にほん}に{来|き}てください。","Venez absolument au Japon une fois."),
 W("もし","もし","si (hypothèse)","もし{雨|あめ}が{降|ふ}ったら、{行|い}きません。","S'il pleut, je n'y vais pas."),
 W("もうすぐ","もうすぐ","bientôt","もうすぐ{夏休|なつやす}みです。","Ce sont bientôt les vacances d'été."),
 W("そろそろ","そろそろ","il est bientôt temps","もう{十時|じゅうじ}ですね。そろそろ{帰|かえ}ります。","Il est déjà dix heures. Je vais y aller."),
 W("いっしょうけんめい","いっしょうけんめい","de toutes ses forces","{試験|しけん}のために、いっしょうけんめい{勉強|べんきょう}しています。","J'étudie de toutes mes forces pour l'examen."),
 W("とうとう","とうとう","finalement (au bout du compte)","{十年|じゅうねん}かかって、とうとう{家|いえ}ができました。","Au bout de dix ans, la maison est enfin terminée."),
 W("やっぱり","やっぱり","comme je pensais ; finalement","やっぱり{日本|にほん}の{料理|りょうり}はおいしいですね。","La cuisine japonaise, c'est vraiment bon, comme je pensais."),
 W("しっかり","しっかり","bien, solidement","しっかり{食|た}べて、よくねてください。","Mange bien et dors bien."),
], "sections": [
 {"h": "Adverbes qui appellent une certaine fin de phrase",
  "p": ["Ces adverbes vont avec une construction précise : retenez le couple."],
  "grid": {"head": ["", "emploi"], "rows": [
   ["なかなか 〜ない", "ça ne vient pas, pas facilement"],
   ["もし 〜たら", "si…"],
   ["ぜひ 〜てください / 〜たい", "absolument (invitation, souhait)"],
   ["きっと 〜でしょう / 〜と{思|おも}う", "sûrement (je le crois)"],
   ["そろそろ 〜ます", "il est temps de…"]]}}
], "pieges": [
 "なかなか + négatif = « ne … pas facilement » ; + positif = « assez, plutôt » : なかなかおいしい.",
 "きっと = sûrement (supposition) ; かならず = sans faute (certitude, consigne, promesse).",
 "ぜひ ne s'emploie qu'avec un souhait ou une invitation : ぜひ{来|き}てください, ぜひ{行|い}きたい.",
 "やっと (enfin, soulagé, leçon 49) ; とうとう = finalement, au bout du compte (en bien ou en mal).",
 "たまに = de temps en temps (rarement) ; ときどき = parfois (plus souvent).",
 "ずっと = tout le temps, depuis longtemps ; avec une comparaison, « bien plus » : ずっと{大|おお}きい."
], "exercises": [
 C(L,1,["かならず","たまに","なかなか","とうとう"],jp="{明日|あした}の{会議|かいぎ}は{大事|だいじ}ですから、＿{来|き}てください。",fr="La réunion de demain est importante : venez sans faute.",uses=["v4-51"]),
 C(L,2,["ずっと","たまに","ぜひ","もし"],jp="{朝|あさ}から＿{雨|あめ}が{降|ふ}っています。",fr="Il pleut sans arrêt depuis ce matin.",uses=["v5-25"]),
 C(L,3,["たまに","ずっと","かならず","ぜひ"],jp="{毎日|まいにち}{料理|りょうり}をしますが、＿レストランで{食|た}べます。",fr="Je cuisine tous les jours, mais de temps en temps je mange au restaurant.",uses=["v5-14"]),
 C(L,4,["なかなか","そろそろ","ぜひ","しっかり"],jp="バスが＿{来|き}ません。もう{三十分|さんじゅっぷん}{待|ま}っています。",fr="Le bus n'arrive pas. Ça fait déjà trente minutes que j'attends.",uses=["v5-36"]),
 C(L,5,["{特|とく}に","たまに","もし","そろそろ"],jp="{果物|くだもの}はなんでも{好|す}きですが、＿りんごが{好|す}きです。",fr="J'aime tous les fruits, mais surtout les pommes.",uses=["v5-06"]),
 C(L,6,["{急|きゅう}に","ずっと","ぜひ","もし"],jp="いい{天気|てんき}でしたが、＿{雨|あめ}が{降|ふ}ってきました。",fr="Il faisait beau, mais il s'est mis à pleuvoir d'un coup.",uses=["v5-25"]),
 C(L,7,["きっと","たまに","ぜひ","なかなか"],jp="{田中|たなか}さんはまじめな{人|ひと}ですから、＿{来|き}ますよ。",fr="M. Tanaka est quelqu'un de sérieux, il viendra sûrement.",uses=["v4-42"]),
 C(L,8,["ぜひ","たまに","なかなか","とうとう"],jp="{日本|にほん}はとてもいいところです。＿{一度|いちど}{来|き}てください。",fr="Le Japon est un endroit formidable. Venez absolument une fois.",uses=["v5-38"]),
 C(L,9,["もし","ぜひ","きっと","なかなか"],jp="＿{雨|あめ}が{降|ふ}ったら、{試合|しあい}はありません。",fr="S'il pleut, il n'y aura pas de match.",uses=["v5-25"]),
 C(L,10,["もうすぐ","さっき","たまに","{特|とく}に"],jp="＿{夏休|なつやす}みですね。どこへ{行|い}きますか。",fr="Ce sont bientôt les vacances d'été. Où vas-tu ?",uses=["v4-54"]),
 C(L,11,["そろそろ","たまに","ぜひ","ずっと"],jp="もう{十一時|じゅういちじ}ですね。＿{帰|かえ}ります。",fr="Il est déjà onze heures. Je vais y aller.",uses=["v5-16"]),
 C(L,12,["いっしょうけんめい","たまに","もし","ぜひ"],jp="{大学|だいがく}にごうかくしたいですから、{毎日|まいにち}＿{勉強|べんきょう}しています。",fr="Je veux être reçu à l'université, alors j'étudie de toutes mes forces tous les jours.",uses=["v4-52"]),
 C(L,13,["とうとう","たまに","もし","そろそろ"],jp="{十年|じゅうねん}お{金|かね}をためて、＿{自分|じぶん}の{家|いえ}を{建|た}てました。",fr="Après dix ans d'économies, j'ai finalement fait construire ma propre maison.",uses=["v4-47","v5-39"]),
 C(L,14,["やっぱり","もし","たまに","なかなか"],jp="いろいろな{国|くに}の{料理|りょうり}を{食|た}べましたが、＿{日本|にほん}の{料理|りょうり}がいちばんおいしいです。",fr="J'ai goûté la cuisine de plein de pays, mais finalement c'est la japonaise la meilleure.",uses=["v5-37"]),
 C(L,15,["しっかり","もし","なかなか","とうとう"],jp="{病気|びょうき}ですから、＿{食|た}べて、よくねてください。",fr="Tu es malade, alors mange bien et dors bien.",uses=["v5-23"]),
 C(L,16,["assez, plutôt","pas du tout","jamais","enfin"],q="Dans « この{料理|りょうり}はなかなかおいしいです », que veut dire なかなか ?"),
 O(L,17,"Venez absolument chez moi.",["ぜひ","うちに","{来|き}て","ください"],alt=[["うちに","ぜひ","{来|き}て","ください"]],uses=["v5-22"]),
 O(L,18,"Il pleut sans arrêt depuis ce matin.",["{朝|あさ}から","ずっと","{雨|あめ}が","{降|ふ}っています"],alt=[["{朝|あさ}から","{雨|あめ}が","ずっと","{降|ふ}っています"]],uses=["v5-25"]),
]}

TC, TO, XC, XO = make_block("v4-b11")
test = [
 TC(1,["つとめて","やめて","しっぱいして","コピーして"],jp="{父|ちち}は{三十年|さんじゅうねん}、{同|おな}じ{会社|かいしゃ}に＿います。",fr="Mon père travaille pour la même entreprise depuis trente ans.",uses=["v4-51"]),
 TC(2,["そつぎょうして","{入学|にゅうがく}して","ごうかくして","りゅうがくして"],jp="{大学|だいがく}を＿、{銀行|ぎんこう}に{入|はい}りました。",fr="Après avoir fini l'université, je suis entré dans une banque.",uses=["v4-52"]),
 TC(3,["そうだん","しょうかい","あいさつ","うそ"],jp="{大学|だいがく}のことを{先生|せんせい}に＿しました。",fr="J'ai demandé conseil au professeur au sujet de l'université.",uses=["v4-53"]),
 TC(4,["キャンセル","よやく","じゅんび","{用意|ようい}"],jp="{明日|あした}は{都合|つごう}が{悪|わる}くなったので、やくそくを＿してもいいですか。",fr="Demain ne m'arrange plus : est-ce que je peux annuler notre rendez-vous ?",uses=["v4-54"]),
 TC(5,["なかなか","かならず","ぜひ","たまに"],jp="バスが＿{来|き}ませんでしたから、タクシーで{行|い}きました。",fr="Le bus n'arrivait pas, alors j'ai pris un taxi.",uses=["v4-55"]),
 TC(6,["かいぎ","かいき","あいぎ","かいご"],q=LECT+"**会議** ?",uses=["v4-51"]),
 TC(7,["ごうかくして","そつぎょうして","{入学|にゅうがく}して","ふくしゅうして"],jp="{試験|しけん}に＿、とてもうれしいです。",fr="J'ai réussi l'examen, je suis très content.",uses=["v4-52"]),
 TC(8,["しょうかい","れんらく","そうだん","あいさつ"],jp="{部長|ぶちょう}が{新|あたら}しい{社員|しゃいん}をみんなに＿しました。",fr="Le chef de service a présenté le nouvel employé à tout le monde.",uses=["v4-51","v4-53"]),
 TC(9,["{来週|らいしゅう}、しゅっちょうで{大阪|おおさか}へ{行|い}きます。","{来週|らいしゅう}、ざんぎょうで{大阪|おおさか}へ{行|い}きます。","{来週|らいしゅう}、{旅行|りょこう}で{大阪|おおさか}へ{行|い}きます。","{来週|らいしゅう}、しゅっちょうを{大阪|おおさか}へ{行|い}きます。"],q="« La semaine prochaine, je vais à Osaka en voyage d'affaires » se dit…",uses=["v4-51"]),
 TC(10,["もし","きっと","ぜひ","なかなか"],jp="＿{雨|あめ}だったら、{試合|しあい}は{来週|らいしゅう}です。",fr="S'il pleut, le match aura lieu la semaine prochaine.",uses=["v4-55"]),
 TC(11,["ふくしゅう","よしゅう","そつぎょう","しっぱい"],jp="{試験|しけん}の{前|まえ}に、{習|なら}ったことを＿します。",fr="Avant l'examen, je révise ce que j'ai appris.",uses=["v4-52"]),
 TC(12,["しょうらい","さっき","この{間|あいだ}","さいご"],jp="＿は{日本|にほん}で{働|はたら}きたいです。",fr="Plus tard, je veux travailler au Japon.",uses=["v4-54"]),
 TC(13,["しっぱい","コピー","よやく","しゅっちょう"],jp="{大事|だいじ}な{会議|かいぎ}で{社長|しゃちょう}の{名前|なまえ}をまちがえて、＿しました。",fr="À une réunion importante, je me suis trompé de nom pour le patron : quelle gaffe.",uses=["v4-51"]),
 TO(14,"Je te contacte sans faute demain.",["{明日|あした}","かならず","れんらく","します"],alt=[["かならず","{明日|あした}","れんらく","します"]],uses=["v4-53","v4-55"]),
 TC(15,["un mensonge","une réponse","une salutation","un remerciement"],q="Que veut dire **うそ** ?",uses=["v4-53"]),
 TC(16,["へんじ","{答|こた}え","あいさつ","おれい"],jp="{田中|たなか}さんにメールを{送|おく}りましたが、まだ＿がありません。",fr="J'ai envoyé un mail à M. Tanaka, mais il n'a pas encore répondu.",uses=["v4-53"]),
]
bloc = {"id": "v4-b11", "level": "N4", "title": "Travail et études : bureau, études, communiquer, projets, adverbes",
        "lessons": [l51, l52, l53, l54, l55], "test": test}
save_n4(bloc, sys.argv[1])
