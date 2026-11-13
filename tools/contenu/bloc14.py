import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L66 Technologie ----------
L = "v4-66"
l66 = {"id": L, "title": "Appareils et technologie", "words": [
 W("パソコン","パソコン","ordinateur","{毎日|まいにち}パソコンで{仕事|しごと}をします。","Je travaille sur ordinateur tous les jours."),
 W("きかい","きかい","machine","{工場|こうじょう}の{大|おお}きいきかいが{動|うご}かなくなりました。","La grande machine de l'usine ne marche plus."),
 W("{電池|でんち}","でんち","pile, batterie","{時計|とけい}の{電池|でんち}がなくなりました。","La pile de la montre est à plat."),
 W("スイッチ","スイッチ","interrupteur","スイッチをおすと、{電気|でんき}がつきます。","Quand on appuie sur l'interrupteur, la lumière s'allume."),
 W("インターネット","インターネット","Internet","インターネットでホテルをよやくしました。","J'ai réservé l'hôtel sur Internet."),
 W("がめん","がめん","écran","パソコンのがめんが{暗|くら}くなりました。","L'écran de l'ordinateur s'est assombri."),
 W("エアコン","エアコン","climatisation","{暑|あつ}いですから、エアコンをつけましょう。","Il fait chaud, allumons la clim."),
 W("せんたくき","せんたくき","machine à laver","せんたくきがこわれて、{服|ふく}が{洗|あら}えません。","La machine à laver est en panne, je ne peux pas laver mes vêtements."),
 W("けいたい","けいたい","téléphone portable","けいたいで{写真|しゃしん}をとりました。","J'ai pris une photo avec mon portable."),
 W("ビデオ","ビデオ","vidéo","{旅行|りょこう}のビデオを{見|み}せてください。","Montre-moi la vidéo du voyage."),
 W("{文字|もじ}","もじ","caractère, lettre (écrite)","がめんの{文字|もじ}が{小|ちい}さくて{読|よ}めません。","Les caractères à l'écran sont trop petits, je n'arrive pas à lire."),
 W("しらべる","しらべる","chercher (une information)","{分|わ}からないことばをじしょでしらべます。","Je cherche les mots que je ne connais pas dans le dictionnaire."),
 W("{電子|でんし}レンジ","でんしレンジ","four à micro-ondes","おべんとうを{電子|でんし}レンジであたためます。","Je réchauffe mon bentō au micro-ondes."),
 W("{自動|じどう}","じどう","automatique","この{店|みせ}のドアは{自動|じどう}で{開|あ}きます。","La porte de ce magasin s'ouvre automatiquement."),
 W("ボタン","ボタン","bouton","このボタンをおしてください。","Appuyez sur ce bouton."),
], "sections": [
 {"h": "Utiliser les appareils",
  "p": ["Les verbes des appareils, presque tous déjà vus en N5."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["allumer / éteindre", "エアコン==を==つける / {消|け}す"],
   ["appuyer sur", "ボタン==を==おす"],
   ["chercher une info", "インターネット==で==しらべる"],
   ["la pile est vide", "{電池|でんち}==が==なくなる"],
   ["automatiquement", "{自動|じどう}==で=={開|あ}く"]]}}
], "pieges": [
 "しらべる = chercher une **information** (dictionnaire, Internet) ; さがす (leçon 76) = chercher un **objet**.",
 "けいたい = téléphone portable (on dit aussi スマホ).",
 "{文字|もじ} = caractère, lettre ; {字|じ} (leçon 29) = écriture, caractère.",
 "{電池|でんち}がなくなる = la pile est à plat (なくなる, leçon 49).",
 "Appareils en panne : こわれる (leçon 48). Ils « marchent » : {動|うご}く (leçon 45)."
], "exercises": [
 C(L,1,["パソコン","エアコン","せんたくき","{電池|でんち}"],jp="{毎日|まいにち}＿で{仕事|しごと}のメールを{書|か}きます。",fr="Tous les jours, j'écris mes mails de travail sur ordinateur.",uses=["v4-53"]),
 C(L,2,["きかい","{文字|もじ}","インターネット","{自動|じどう}"],jp="{工場|こうじょう}の{大|おお}きい＿が{動|うご}かなくなりました。",fr="La grande machine de l'usine ne marche plus.",uses=["v4-45","v5-30"]),
 C(L,3,["{電池|でんち}","がめん","{文字|もじ}","インターネット"],jp="{時計|とけい}が{止|と}まりました。＿がなくなったのでしょう。",fr="Ma montre s'est arrêtée. La pile doit être à plat.",uses=["v4-49","v5-36"]),
 C(L,4,["スイッチ","ビデオ","{文字|もじ}","インターネット"],jp="＿をおすと、{電気|でんき}がつきます。",fr="Quand on appuie sur l'interrupteur, la lumière s'allume.",uses=["v5-27","v5-40"]),
 C(L,5,["インターネット","エアコン","せんたくき","{電池|でんち}"],jp="＿でホテルをよやくしました。{安|やす}かったです。",fr="J'ai réservé l'hôtel sur Internet. C'était bon marché.",uses=["v4-54"]),
 C(L,6,["がめん","スイッチ","{電池|でんち}","インターネット"],jp="パソコンの＿が{暗|くら}くて、よく{見|み}えません。",fr="L'écran de l'ordinateur est sombre, on ne voit pas bien.",uses=["v5-24","v5-40"]),
 C(L,7,["エアコン","せんたくき","{電池|でんち}","{文字|もじ}"],jp="{暑|あつ}いですから、＿をつけましょう。",fr="Il fait chaud, allumons la clim.",uses=["v5-25","v5-27"]),
 C(L,8,["せんたくき","エアコン","{電子|でんし}レンジ","けいたい"],jp="＿がこわれて、{服|ふく}が{洗|あら}えません。",fr="La machine à laver est en panne, je ne peux pas laver mes vêtements.",uses=["v4-48"]),
 C(L,9,["けいたい","エアコン","せんたくき","{電子|でんし}レンジ"],jp="{電車|でんしゃ}の{中|なか}では、＿で{話|はな}さないでください。",fr="Ne téléphonez pas avec votre portable dans le train, s'il vous plaît.",uses=["v5-15"]),
 C(L,10,["ビデオ","{電池|でんち}","スイッチ","せんたくき"],jp="{旅行|りょこう}の＿を{見|み}せてください。",fr="Montre-moi la vidéo du voyage.",uses=["v5-26"]),
 C(L,11,["{文字|もじ}","スイッチ","{電池|でんち}","エアコン"],jp="がめんの＿が{小|ちい}さくて{読|よ}めません。",fr="Les caractères à l'écran sont trop petits, je n'arrive pas à lire."),
 C(L,12,["しらべて","おして","つけて","こわして"],jp="{分|わ}からないことばは、じしょで＿ください。",fr="Cherchez les mots que vous ne connaissez pas dans le dictionnaire.",uses=["v5-29"]),
 C(L,13,["{電子|でんし}レンジ","せんたくき","エアコン","けいたい"],jp="つめたいおべんとうを＿であたためます。",fr="Je réchauffe mon bentō froid au micro-ondes.",uses=["v5-34"]),
 C(L,14,["{自動|じどう}","{文字|もじ}","がめん","ビデオ"],jp="この{店|みせ}のドアは＿で{開|あ}きます。",fr="La porte de ce magasin s'ouvre automatiquement.",uses=["v5-27"]),
 C(L,15,["chercher (une information)","envoyer","réparer","allumer"],q="Que veut dire **しらべる** ?"),
 C(L,16,["でんち","でんいけ","でんし","てんち"],q=LECT+"**電池** ?"),
 O(L,17,"J'ai cherché le mot sur Internet.",["インターネットで","ことばを","しらべました"],alt=[["ことばを","インターネットで","しらべました"]],uses=["v5-29"]),
 O(L,18,"Allume la clim, s'il te plaît.",["エアコンを","つけて","ください"],uses=["v5-27"]),
]}

# ---------- L67 Médias et actualité ----------
L = "v4-67"
l67 = {"id": L, "title": "Médias et actualité", "words": [
 W("ばんぐみ","ばんぐみ","émission","{好|す}きなテレビのばんぐみは{何|なん}ですか。","Quelle est ton émission de télé préférée ?"),
 W("ほうそうする","ほうそうする","diffuser (radio, télé)","その{試合|しあい}は{夜|よる}{九時|くじ}からテレビでほうそうします。","Le match est diffusé à la télé à partir de 21 heures."),
 W("{新聞社|しんぶんしゃ}","しんぶんしゃ","journal (l'entreprise)","{兄|あに}は{新聞社|しんぶんしゃ}で{働|はたら}いています。","Mon grand frère travaille pour un journal."),
 W("きじ","きじ","article","{新聞|しんぶん}でおもしろいきじを{読|よ}みました。","J'ai lu un article intéressant dans le journal."),
 W("ざっし","ざっし","magazine","{電車|でんしゃ}の{中|なか}でざっしを{読|よ}みます。","Je lis un magazine dans le train."),
 W("アナウンサー","アナウンサー","présentateur","アナウンサーがニュースを{読|よ}んでいます。","Le présentateur lit les informations."),
 W("ラジオ","ラジオ","radio","{車|くるま}の{中|なか}でラジオを{聞|き}きます。","J'écoute la radio en voiture."),
 W("じけん","じけん","affaire, incident","{昨日|きのう}、この{町|まち}で{大|おお}きいじけんがありました。","Hier, il y a eu une grosse affaire dans cette ville."),
 W("ドラマ","ドラマ","série (télévisée)","{毎週|まいしゅう}{日本|にほん}のドラマを{見|み}ています。","Je regarde une série japonaise toutes les semaines."),
 W("はっぴょうする","はっぴょうする","annoncer, présenter","{授業|じゅぎょう}で{研究|けんきゅう}をはっぴょうしました。","J'ai présenté mes recherches en cours."),
 W("きしゃ","きしゃ","journaliste","きしゃが{有名人|ゆうめいじん}に{質問|しつもん}をしました。","Un journaliste a posé une question à une célébrité."),
 W("じょうほう","じょうほう","information(s)","インターネットでいろいろなじょうほうを{集|あつ}めます。","Je rassemble toutes sortes d'informations sur Internet."),
 W("こうこく","こうこく","publicité","{新|あたら}しい{車|くるま}のこうこくをテレビで{見|み}ました。","J'ai vu une pub pour une nouvelle voiture à la télé."),
 W("{有名人|ゆうめいじん}","ゆうめいじん","célébrité","この{店|みせ}には{有名人|ゆうめいじん}がよく{来|き}ます。","Des célébrités viennent souvent dans ce restaurant."),
 W("わだい","わだい","sujet (de conversation)","{今|いま}、そのドラマがわだいになっています。","En ce moment, tout le monde parle de cette série."),
], "sections": [
 {"h": "Les médias",
  "p": ["Le vocabulaire de la télé, de la radio et des journaux."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["émission / série", "ばんぐみ / ドラマ"],
   ["diffuser", "ほうそうする"],
   ["article / magazine", "きじ / ざっし"],
   ["journaliste / présentateur", "きしゃ / アナウンサー"],
   ["présenter (un exposé)", "はっぴょうする"],
   ["faire parler de soi", "わだい==に==なる"]]}}
], "pieges": [
 "ばんぐみ = une émission ; ニュース = les informations ; ドラマ = une série.",
 "きじ = un article ; ざっし = un magazine ; {新聞|しんぶん} = un journal ; {新聞社|しんぶんしゃ} = l'entreprise de presse.",
 "はっぴょうする = annoncer officiellement, présenter un exposé.",
 "じけん = une affaire, un incident (souvent un crime) ; じこ (leçon 50) = un accident.",
 "じょうほう = information(s), renseignements.",
 "わだいになる = être le sujet du moment, faire parler de soi."
], "exercises": [
 C(L,1,["ばんぐみ","ざっし","きじ","きしゃ"],jp="{好|す}きなテレビの＿は{何|なん}ですか。— ニュースです。",fr="Quelle est ton émission de télé préférée ? — Les informations.",uses=["v5-28"]),
 C(L,2,["ほうそう","こうこく","じけん","わだい"],jp="その{試合|しあい}は、{今夜|こんや}{九時|くじ}からテレビで＿します。",fr="Le match est diffusé à la télé ce soir à partir de 21 heures.",uses=["v4-61"]),
 C(L,3,["{新聞社|しんぶんしゃ}","ドラマ","アナウンサー","じけん"],jp="{兄|あに}は＿で{働|はたら}いていて、きじを{書|か}いています。",fr="Mon grand frère travaille pour un journal, il écrit des articles.",uses=["v5-14"]),
 C(L,4,["きじ","ばんぐみ","ラジオ","アナウンサー"],jp="{新聞|しんぶん}でおもしろい＿を{読|よ}みました。",fr="J'ai lu un article intéressant dans le journal.",uses=["v5-12"]),
 C(L,5,["ざっし","ラジオ","ドラマ","ばんぐみ"],jp="{電車|でんしゃ}の{中|なか}で＿を{読|よ}みます。",fr="Je lis un magazine dans le train.",uses=["v5-15"]),
 C(L,6,["アナウンサー","きじ","じけん","ざっし"],jp="＿がテレビでニュースを{読|よ}んでいます。",fr="Le présentateur lit les informations à la télé.",uses=["v5-28"]),
 C(L,7,["ラジオ","ざっし","きじ","{新聞社|しんぶんしゃ}"],jp="{車|くるま}を{運転|うんてん}しながら、＿を{聞|き}きます。",fr="J'écoute la radio en conduisant.",uses=["v5-15"]),
 C(L,8,["じけん","ドラマ","ばんぐみ","こうこく"],jp="{昨日|きのう}、この{町|まち}で{大|おお}きい＿がありました。けいさつがたくさん{来|き}ました。",fr="Hier, il y a eu une grosse affaire dans cette ville. Beaucoup de policiers sont venus.",uses=["v4-59"]),
 C(L,9,["ドラマ","ラジオ","じけん","きしゃ"],jp="{毎週|まいしゅう}{日本|にほん}の＿を{見|み}て、{日本語|にほんご}を{勉強|べんきょう}しています。",fr="Je regarde une série japonaise toutes les semaines pour étudier le japonais.",uses=["v5-38"]),
 C(L,10,["はっぴょう","ほうそう","こうこく","わだい"],jp="{授業|じゅぎょう}で、{自分|じぶん}の{研究|けんきゅう}をみんなの{前|まえ}で＿しました。",fr="En cours, j'ai présenté mes recherches devant tout le monde.",uses=["v4-52","v5-39"]),
 C(L,11,["きしゃ","じけん","ばんぐみ","ざっし"],jp="＿が{有名人|ゆうめいじん}に{質問|しつもん}をしています。",fr="Un journaliste pose une question à une célébrité.",uses=["v5-29"]),
 C(L,12,["じょうほう","アナウンサー","じけん","ラジオ"],jp="インターネットでいろいろな＿を{集|あつ}めます。",fr="Je rassemble toutes sortes d'informations sur Internet.",uses=["v4-46","v4-66"]),
 C(L,13,["こうこく","じけん","きしゃ","アナウンサー"],jp="{新|あたら}しい{車|くるま}の＿をテレビで{見|み}て、ほしくなりました。",fr="J'ai vu une pub pour une nouvelle voiture à la télé, et j'en ai eu envie."),
 C(L,14,["{有名人|ゆうめいじん}","ばんぐみ","こうこく","じょうほう"],jp="この{店|みせ}には＿がよく{来|き}ます。テレビで{見|み}る{人|ひと}たちです。",fr="Des célébrités viennent souvent dans ce restaurant : des gens qu'on voit à la télé."),
 C(L,15,["わだい","じけん","ほうそう","こうこく"],jp="{今|いま}、そのドラマがとても＿になっています。みんな{見|み}ています。",fr="En ce moment, tout le monde parle de cette série. Tout le monde la regarde."),
 C(L,16,["un magazine","un article","une émission","un journal télévisé"],q="Que veut dire **ざっし** ?"),
 C(L,17,["しんぶんしゃ","しんもんしゃ","しんぶんじゃ","あたらしゃ"],q=LECT+"**新聞社** ?"),
 O(L,18,"Le match sera diffusé à la télé ce soir.",["{試合|しあい}は","{今夜|こんや}","テレビで","ほうそうされます"],alt=[["{今夜|こんや}","{試合|しあい}は","テレビで","ほうそうされます"]],uses=["v4-61"]),
]}

# ---------- L68 Société ----------
L = "v4-68"
l68 = {"id": L, "title": "Société, économie, sciences", "words": [
 W("{社会|しゃかい}","しゃかい","société","{子|こ}どもは{学校|がっこう}で{社会|しゃかい}のことを{習|なら}います。","À l'école, les enfants apprennent comment fonctionne la société."),
 W("けいざい","けいざい","économie","{大学|だいがく}でけいざいを{勉強|べんきょう}しています。","J'étudie l'économie à l'université."),
 W("せいじ","せいじ","politique","せいじのニュースはむずかしいです。","Les nouvelles politiques sont difficiles."),
 W("こくさい","こくさい","international","{京都|きょうと}でこくさい{会議|かいぎ}がありました。","Il y a eu une conférence internationale à Kyoto."),
 W("ほうりつ","ほうりつ","loi","{日本|にほん}のほうりつでは、{二十|はたち}さいからお{酒|さけ}が{飲|の}めます。","Selon la loi japonaise, on peut boire de l'alcool à partir de vingt ans."),
 W("せんそう","せんそう","guerre","おじいさんはせんそうの{話|はなし}をしてくれました。","Grand-père m'a raconté la guerre."),
 W("へいわ","へいわ","paix ; paisible","{世界|せかい}がへいわになってほしいです。","Je voudrais que le monde soit en paix."),
 W("{人口|じんこう}","じんこう","population","{東京|とうきょう}の{人口|じんこう}はとても{多|おお}いです。","La population de Tokyo est très nombreuse."),
 W("{産業|さんぎょう}","さんぎょう","industrie, secteur économique","この{町|まち}の{大事|だいじ}な{産業|さんぎょう}はかんこうです。","Le secteur important de cette ville, c'est le tourisme."),
 W("{工業|こうぎょう}","こうぎょう","industrie (fabrication)","この{地方|ちほう}は{工業|こうぎょう}がさかんです。","L'industrie est florissante dans cette région."),
 W("せいかつ","せいかつ","vie (quotidienne)","{日本|にほん}でのせいかつにもうなれました。","Je me suis déjà habitué à la vie au Japon."),
 W("{医学|いがく}","いがく","médecine (science)","{兄|あに}は{大学|だいがく}で{医学|いがく}を{勉強|べんきょう}しています。","Mon grand frère étudie la médecine à l'université."),
 W("かがく","かがく","science(s)","{子|こ}どものとき、かがくが{好|す}きでした。","Enfant, j'aimais les sciences."),
 W("ぎじゅつ","ぎじゅつ","technique, technologie","{日本|にほん}の{車|くるま}のぎじゅつはすばらしいです。","La technologie automobile japonaise est formidable."),
 W("ぼうえき","ぼうえき","commerce extérieur","{日本|にほん}は{外国|がいこく}とぼうえきをしています。","Le Japon commerce avec l'étranger."),
], "sections": [
 {"h": "Les grands domaines",
  "p": ["Des mots qu'on rencontre dans les informations et les textes du JLPT."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["économie / politique", "けいざい / せいじ"],
   ["loi", "ほうりつ"],
   ["guerre / paix", "せんそう / へいわ"],
   ["industrie / commerce extérieur", "{産業|さんぎょう}, {工業|こうぎょう} / ぼうえき"],
   ["sciences / technique / médecine", "かがく / ぎじゅつ / {医学|いがく}"],
   ["vie quotidienne", "せいかつ"]]}}
], "pieges": [
 "せいかつ = la vie de tous les jours, le mode de vie : {日本|にほん}でのせいかつ.",
 "{人口|じんこう} = la population (le nombre d'habitants) : {人口|じんこう}が{多|おお}い / {少|すく}ない.",
 "こくさい = international, presque toujours devant un nom : こくさい{会議|かいぎ}.",
 "{工業|こうぎょう} (fabrication) fait partie des {産業|さんぎょう} (toutes les activités économiques).",
 "へいわ est un adjectif en な : へいわな{世界|せかい}, へいわになる.",
 "{二十|はたち}さい : vingt ans se lit はたち."
], "exercises": [
 C(L,1,["けいざい","せんそう","{人口|じんこう}","へいわ"],jp="{大学|だいがく}で＿を{勉強|べんきょう}して、{銀行|ぎんこう}で{働|はたら}きたいです。",fr="Je veux étudier l'économie à l'université, puis travailler dans une banque.",uses=["v5-14"]),
 C(L,2,["la politique","l'économie","la société","la loi"],q="Que veut dire **せいじ** ?"),
 C(L,3,["こくさい","せいかつ","へいわ","{人口|じんこう}"],jp="{京都|きょうと}で＿{会議|かいぎ}があって、いろいろな{国|くに}の{人|ひと}が{来|き}ました。",fr="Il y a eu une conférence internationale à Kyoto : des gens de nombreux pays sont venus.",uses=["v4-51","v5-37"]),
 C(L,4,["ほうりつ","かがく","ぎじゅつ","{医学|いがく}"],jp="{日本|にほん}の＿では、{二十|はたち}さいからお{酒|さけ}が{飲|の}めます。",fr="Selon la loi japonaise, on peut boire de l'alcool à partir de vingt ans.",uses=["v5-06"]),
 C(L,5,["せんそう","へいわ","かがく","ぼうえき"],jp="おじいさんは＿の{話|はなし}をしてくれました。とてもかなしい{話|はなし}でした。",fr="Grand-père m'a raconté la guerre. C'était une histoire très triste.",uses=["v4-41","v5-28"]),
 C(L,6,["へいわ","せんそう","{人口|じんこう}","けいざい"],jp="{世界|せかい}が＿になってほしいです。",fr="Je voudrais que le monde soit en paix."),
 C(L,7,["{人口|じんこう}","ほうりつ","せいじ","へいわ"],jp="{東京|とうきょう}は＿が{多|おお}くて、{電車|でんしゃ}がいつもこんでいます。",fr="Tokyo est très peuplé, les trains sont toujours bondés.",uses=["v4-50"]),
 C(L,8,["{産業|さんぎょう}","{工業|こうぎょう}","せいじ","{医学|いがく}"],jp="この{町|まち}のいちばん{大事|だいじ}な＿はかんこうです。",fr="Le secteur économique le plus important de cette ville, c'est le tourisme.",uses=["v4-62"]),
 C(L,9,["{工業|こうぎょう}","{医学|いがく}","へいわ","せんそう"],jp="この{地方|ちほう}には{工場|こうじょう}が{多|おお}くて、＿がさかんです。",fr="Il y a beaucoup d'usines dans cette région : l'industrie y est florissante.",uses=["v4-62","v5-30"]),
 C(L,10,["せいかつ","せいじ","{人口|じんこう}","ぼうえき"],jp="{日本|にほん}での＿にもうなれましたか。",fr="Tu t'es habitué à la vie au Japon ?"),
 C(L,11,["{医学|いがく}","{工業|こうぎょう}","けいざい","せいじ"],jp="{兄|あに}は{医者|いしゃ}になりたいですから、{大学|だいがく}で＿を{勉強|べんきょう}しています。",fr="Mon grand frère veut devenir médecin, alors il étudie la médecine à l'université.",uses=["v5-30"]),
 C(L,12,["かがく","せいじ","ほうりつ","けいざい"],jp="{子|こ}どものとき、＿が{好|す}きで、ほしやむしのことをよくしらべました。",fr="Enfant, j'aimais les sciences : je faisais souvent des recherches sur les étoiles et les insectes.",uses=["v4-63","v4-66"]),
 C(L,13,["ぎじゅつ","せんそう","{人口|じんこう}","へいわ"],jp="{日本|にほん}の{車|くるま}の＿はすばらしいです。",fr="La technologie automobile japonaise est formidable."),
 C(L,14,["ぼうえき","せんそう","せいかつ","{医学|いがく}"],jp="{日本|にほん}は{外国|がいこく}と＿をして、{車|くるま}を{売|う}っています。",fr="Le Japon commerce avec l'étranger : il y vend des voitures.",uses=["v5-26"]),
 C(L,15,["じんこう","ひとくち","にんこう","じんぐち"],q=LECT+"**人口** ?"),
 C(L,16,["へいわ","けいざい","せいじ","こくさい"],q="Contraire de **せんそう** ?"),
 C(L,17,["la société","l'entreprise","la politique","la ville"],q="Que veut dire **{社会|しゃかい}** ?"),
 O(L,18,"J'étudie l'économie à l'université.",["{大学|だいがく}で","けいざいを","{勉強|べんきょう}しています"],alt=[["けいざいを","{大学|だいがく}で","{勉強|べんきょう}しています"]],uses=["v5-14"]),
]}

# ---------- L69 Lieux et territoire ----------
L = "v4-69"
l69 = {"id": L, "title": "Lieux et territoire", "words": [
 W("{県|けん}","けん","préfecture","{日本|にほん}には{県|けん}が{四十三|よんじゅうさん}あります。","Le Japon compte quarante-trois préfectures en 県."),
 W("{市|し}","し","ville (commune)","{大阪|おおさか}{市|し}に{住|す}んでいます。","J'habite dans la ville d'Osaka."),
 W("{村|むら}","むら","village","そぼは{山|やま}の{中|なか}の{小|ちい}さい{村|むら}に{住|す}んでいます。","Ma grand-mère vit dans un petit village de montagne."),
 W("こうがい","こうがい","banlieue","{東京|とうきょう}のこうがいに{家|いえ}を{建|た}てました。","J'ai fait construire une maison en banlieue de Tokyo."),
 W("{世界|せかい}","せかい","monde","{世界|せかい}でいちばん{高|たか}い{山|やま}はどこですか。","Où est la plus haute montagne du monde ?"),
 W("いなか","いなか","campagne ; région natale","{夏休|なつやす}みはいなかのそぼの{家|いえ}へ{行|い}きます。","Pendant les vacances d'été, je vais chez ma grand-mère à la campagne."),
 W("{区|く}","く","arrondissement","{東京|とうきょう}には{二十三|にじゅうさん}の{区|く}があります。","Tokyo compte vingt-trois arrondissements."),
 W("{近所|きんじょ}","きんじょ","voisinage, quartier","{近所|きんじょ}に{大|おお}きいスーパーができました。","Un grand supermarché a ouvert dans le quartier."),
 W("{場所|ばしょ}","ばしょ","endroit, lieu","{会議|かいぎ}の{場所|ばしょ}を{教|おし}えてください。","Indiquez-moi le lieu de la réunion."),
 W("へん","へん","coin, environs","このへんに{銀行|ぎんこう}はありますか。","Y a-t-il une banque dans le coin ?"),
 W("がわ","がわ","côté","{道|みち}の{右|みぎ}がわを{歩|ある}いてください。","Marchez du côté droit de la rue."),
 W("さか","さか","pente, côte","この{道|みち}はさかが{多|おお}いです。","Cette route a beaucoup de côtes."),
 W("{通|とお}り","とおり","rue, avenue","この{通|とお}りはいつもにぎやかです。","Cette rue est toujours animée."),
 W("{会場|かいじょう}","かいじょう","lieu (d'un événement)","パーティーの{会場|かいじょう}はホテルの{二|に}かいです。","La fête a lieu au premier étage de l'hôtel."),
 W("{都市|とし}","とし","grande ville","{大阪|おおさか}は{日本|にほん}の{大|おお}きい{都市|とし}の{一|ひと}つです。","Osaka est l'une des grandes villes du Japon."),
], "sections": [
 {"h": "Du plus grand au plus petit",
  "p": ["Comme pour une adresse japonaise, on va du plus grand au plus petit. Tokyo compte 23 {区|く}."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["monde / pays", "{世界|せかい} / {国|くに}"],
   ["préfecture", "〜{県|けん}"],
   ["ville / arrondissement", "〜{市|し} / 〜{区|く}"],
   ["village / campagne", "{村|むら} / いなか"],
   ["banlieue / grande ville", "こうがい / {都市|とし}"],
   ["quartier / dans le coin", "{近所|きんじょ} / このへん"]]}}
], "pieges": [
 "このへん = par ici, dans le coin. (へん veut aussi dire « bizarre » : へんな{人|ひと}.)",
 "〜がわ = le côté : {右|みぎ}がわ, {左|ひだり}がわ.",
 "{近所|きんじょ} = le voisinage : {近所|きんじょ}の{人|ひと} = les voisins.",
 "いなか = la campagne, **et** la région d'où l'on vient.",
 "{通|とお}り = rue, avenue (nom) ; {通|とお}る = passer (verbe, leçon 46).",
 "{場所|ばしょ} = un lieu précis ; {会場|かいじょう} = le lieu d'un événement."
], "exercises": [
 C(L,1,["{市|し}","{区|く}","{村|むら}","{世界|せかい}"],jp="{大阪|おおさか}＿に{住|す}んでいます。",fr="J'habite dans la ville d'Osaka.",uses=["v5-36"]),
 C(L,2,["{村|むら}","{世界|せかい}","{区|く}","{会場|かいじょう}"],jp="そぼは{山|やま}の{中|なか}の{小|ちい}さい＿に{住|す}んでいます。",fr="Ma grand-mère vit dans un petit village de montagne.",uses=["v4-43","v5-36"]),
 C(L,3,["こうがい","{世界|せかい}","さか","がわ"],jp="{東京|とうきょう}の＿に{家|いえ}を{建|た}てました。{会社|かいしゃ}まで{電車|でんしゃ}で{一時間|いちじかん}です。",fr="J'ai fait construire une maison en banlieue de Tokyo. J'ai une heure de train jusqu'au bureau.",uses=["v4-47"]),
 C(L,4,["{世界|せかい}","{近所|きんじょ}","{場所|ばしょ}","{会場|かいじょう}"],jp="＿でいちばん{高|たか}い{山|やま}は、{日本|にほん}にはありません。",fr="La plus haute montagne du monde n'est pas au Japon.",uses=["v5-35","v5-37"]),
 C(L,5,["いなか","{都市|とし}","{区|く}","{会場|かいじょう}"],jp="{夏休|なつやす}みは、＿のそぼの{家|いえ}へ{行|い}きます。{山|やま}と{川|かわ}がきれいです。",fr="Pendant les vacances d'été, je vais chez ma grand-mère à la campagne. Les montagnes et la rivière sont magnifiques.",uses=["v4-43","v5-35"]),
 C(L,6,["{区|く}","{県|けん}","{村|むら}","{世界|せかい}"],jp="{東京|とうきょう}には{二十三|にじゅうさん}の＿があります。",fr="Tokyo compte vingt-trois arrondissements."),
 C(L,7,["{近所|きんじょ}","{世界|せかい}","さか","がわ"],jp="＿に{大|おお}きいスーパーができて、{便利|べんり}になりました。",fr="Un grand supermarché a ouvert dans le quartier, c'est devenu pratique.",uses=["v5-19","v5-32"]),
 C(L,8,["{場所|ばしょ}","{世界|せかい}","いなか","{村|むら}"],jp="{会議|かいぎ}の＿と{時間|じかん}を{教|おし}えてください。",fr="Indiquez-moi le lieu et l'heure de la réunion.",uses=["v4-51"]),
 C(L,9,["へん","がわ","さか","{世界|せかい}"],jp="すみません、この＿に{銀行|ぎんこう}はありますか。",fr="Excusez-moi, y a-t-il une banque dans le coin ?",uses=["v5-04"]),
 C(L,10,["がわ","へん","さか","{場所|ばしょ}"],jp="{日本|にほん}では、{車|くるま}は{道|みち}の{左|ひだり}＿を{走|はし}ります。",fr="Au Japon, les voitures roulent du côté gauche de la route.",uses=["v5-20"]),
 C(L,11,["さか","{近所|きんじょ}","{県|けん}","{会場|かいじょう}"],jp="この{道|みち}は＿が{多|おお}いですから、{自転車|じてんしゃ}はたいへんです。",fr="Cette route a beaucoup de côtes, c'est dur à vélo.",uses=["v5-37"]),
 C(L,12,["{通|とお}り","{世界|せかい}","がわ","いなか"],jp="この＿はお{店|みせ}がたくさんあって、いつもにぎやかです。",fr="Cette rue a beaucoup de boutiques, elle est toujours animée.",uses=["v5-19"]),
 C(L,13,["{会場|かいじょう}","{都市|とし}","{県|けん}","{村|むら}"],jp="パーティーの＿はホテルの{二|に}かいです。",fr="La fête a lieu au premier étage de l'hôtel.",uses=["v5-31"]),
 C(L,14,["{都市|とし}","{村|むら}","{近所|きんじょ}","がわ"],jp="{大阪|おおさか}は{日本|にほん}の{大|おお}きい＿の{一|ひと}つです。",fr="Osaka est l'une des grandes villes du Japon."),
 C(L,15,["par ici, dans le coin","bizarre","de ce côté-ci","ce chemin"],q="Que veut dire **このへん** ?"),
 C(L,16,["きんじょ","ちかしょ","きんしょ","ちかところ"],q=LECT+"**近所** ?"),
 C(L,17,["la campagne","la banlieue","la frontière","le centre-ville"],q="Que veut dire **いなか** ?"),
 O(L,18,"Y a-t-il une poste dans le coin ?",["このへんに","ゆうびんきょくは","ありますか"],uses=["v5-32"]),
]}

# ---------- L70 Mesures et quantités ----------
L = "v4-70"
l70 = {"id": L, "title": "Mesures et quantités", "words": [
 W("〜ばい","〜ばい","… fois plus","{兄|あに}はいつも{私|わたし}の{二|に}ばい{食|た}べます。","Mon grand frère mange toujours deux fois plus que moi."),
 W("{以上|いじょう}","いじょう","… et plus, au moins","{二十|はたち}さい{以上|いじょう}の{人|ひと}はお{酒|さけ}が{飲|の}めます。","Les personnes de vingt ans et plus peuvent boire de l'alcool."),
 W("{以下|いか}","いか","… et moins","{六|ろく}さい{以下|いか}の{子|こ}どもはお{金|かね}がいりません。","C'est gratuit pour les enfants de six ans et moins."),
 W("{合計|ごうけい}","ごうけい","total","{合計|ごうけい}で{三千円|さんぜんえん}です。","Ça fait trois mille yens au total."),
 W("キロ","キロ","kilo(mètre, gramme)","{駅|えき}から{家|いえ}まで{二|に}キロあります。","Il y a deux kilomètres de la gare à chez moi."),
 W("メートル","メートル","mètre","この{木|き}は{十|じゅう}メートルぐらいあります。","Cet arbre fait environ dix mètres."),
 W("グラム","グラム","gramme","{肉|にく}を{五百|ごひゃく}グラムください。","Cinq cents grammes de viande, s'il vous plaît."),
 W("センチ","センチ","centimètre","{兄|あに}はせが{百八十|ひゃくはちじゅう}センチあります。","Mon grand frère mesure un mètre quatre-vingts."),
 W("{重|おも}さ","おもさ","poids","このにもつの{重|おも}さはどのぐらいですか。","Combien pèsent ces bagages ?"),
 W("{長|なが}さ","ながさ","longueur","この{川|かわ}の{長|なが}さは{三百|さんびゃく}キロです。","Cette rivière fait trois cents kilomètres de long."),
 W("{高|たか}さ","たかさ","hauteur","ふじさんの{高|たか}さは{三千七百|さんぜんななひゃく}メートルぐらいです。","Le mont Fuji fait environ 3 700 mètres de haut."),
 W("{大|おお}きさ","おおきさ","taille, grandeur","このくつの{大|おお}きさはちょうどいいです。","Ces chaussures sont juste à ma taille."),
 W("かず","かず","nombre","{学生|がくせい}のかずがへっています。","Le nombre d'étudiants diminue."),
 W("〜ばんめ","〜ばんめ","…ième (rang)","{右|みぎ}から{三|さん}ばんめの{人|ひと}が{私|わたし}の{兄|あに}です。","La troisième personne en partant de la droite, c'est mon grand frère."),
 W("パーセント","パーセント","pour cent","{日本|にほん}の{人口|じんこう}の{三十|さんじゅう}パーセントぐらいは{六十五|ろくじゅうご}さい{以上|いじょう}です。","Environ trente pour cent de la population japonaise a soixante-cinq ans ou plus."),
], "sections": [
 {"h": "Mesurer et comparer",
  "p": ["Un adjectif en い devient un nom en remplaçant い par **さ** : {重|おも}い → {重|おも}さ."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["adjectif → nom", "{重|おも}い → {重|おも}==さ== · {長|なが}い → {長|なが}==さ== · {高|たか}い → {高|たか}==さ=="],
   ["deux fois, trois fois plus", "{二|に}ばい · {三|さん}ばい"],
   ["… et plus / … et moins", "〜{以上|いじょう} / 〜{以下|いか} (le nombre est compris)"],
   ["le troisième", "{三|さん}ばんめ"],
   ["au total", "{合計|ごうけい}で"]]}}
], "pieges": [
 "Adjectif en い → nom en 〜さ : {重|おも}い → {重|おも}さ (le poids), {大|おお}きい → {大|おお}きさ (la taille).",
 "〜{以上|いじょう} et 〜{以下|いか} **incluent** le nombre : {六|ろく}さい{以下|いか} = six ans et moins.",
 "〜ばい = … fois **plus** ({二|に}ばい = le double) ; 〜{度|ど} (leçon 38) = … fois (fréquence).",
 "〜ばんめ = le rang : {一|いち}ばんめ, {二|に}ばんめ… ≠ いちばん (le plus, leçon 37).",
 "キロ = kilomètre **ou** kilogramme : c'est le contexte qui décide.",
 "かず = le nombre, la quantité de choses : かずが{多|おお}い / へる."
], "exercises": [
 C(L,1,["ばい","ど","ばんめ","パーセント"],jp="{兄|あに}はいつも{私|わたし}の{二|に}＿{食|た}べます。",fr="Mon grand frère mange toujours deux fois plus que moi.",uses=["v5-21"]),
 C(L,2,["{以上|いじょう}","{以下|いか}","{合計|ごうけい}","ばんめ"],jp="{日本|にほん}では、{二十|はたち}さい＿の{人|ひと}はお{酒|さけ}が{飲|の}めます。",fr="Au Japon, les personnes de vingt ans et plus peuvent boire de l'alcool.",uses=["v4-68"]),
 C(L,3,["{以下|いか}","{以上|いじょう}","{合計|ごうけい}","かず"],jp="{六|ろく}さい＿の{小|ちい}さい{子|こ}どもは、お{金|かね}がいりません。",fr="C'est gratuit pour les petits enfants de six ans et moins.",uses=["v5-36"]),
 C(L,4,["{合計|ごうけい}","{以上|いじょう}","ばい","かず"],jp="コーヒーとケーキで、＿{千二百円|せんにひゃくえん}です。",fr="Café et gâteau : mille deux cents yens au total.",uses=["v5-07"]),
 C(L,5,["キロ","グラム","パーセント","ばんめ"],jp="{駅|えき}から{家|いえ}まで{二|に}＿あります。{歩|ある}いて{三十分|さんじゅっぷん}です。",fr="Il y a deux kilomètres de la gare à chez moi : trente minutes à pied.",uses=["v5-15"]),
 C(L,6,["グラム","メートル","センチ","パーセント"],jp="{肉|にく}を{五百|ごひゃく}＿ください。",fr="Cinq cents grammes de viande, s'il vous plaît.",uses=["v5-06"]),
 C(L,7,["センチ","グラム","キロ","パーセント"],jp="{兄|あに}はせが{百八十|ひゃくはちじゅう}＿あります。",fr="Mon grand frère mesure un mètre quatre-vingts.",uses=["v4-42"]),
 C(L,8,["{重|おも}さ","{長|なが}さ","{高|たか}さ","かず"],jp="このにもつの＿は{二十|にじゅう}キロです。{重|おも}いです。",fr="Ces bagages pèsent vingt kilos. C'est lourd.",uses=["v5-24","v5-33"]),
 C(L,9,["{長|なが}さ","{重|おも}さ","{大|おお}きさ","かず"],jp="この{川|かわ}の＿は{三百|さんびゃく}キロです。",fr="Cette rivière fait trois cents kilomètres de long.",uses=["v5-35"]),
 C(L,10,["{高|たか}さ","{重|おも}さ","かず","パーセント"],jp="ふじさんの＿は{三千七百|さんぜんななひゃく}メートルぐらいです。",fr="Le mont Fuji fait environ 3 700 mètres de haut.",uses=["v5-35"]),
 C(L,11,["{大|おお}きさ","かず","パーセント","ばんめ"],jp="このくつは＿がちょうどいいです。{買|か}います。",fr="Ces chaussures sont juste à ma taille. Je les prends.",uses=["v4-49"]),
 C(L,12,["かず","{重|おも}さ","{高|たか}さ","{長|なが}さ"],jp="{学生|がくせい}の＿が{毎年|まいとし}へっています。",fr="Le nombre d'étudiants diminue chaque année.",uses=["v4-49"]),
 C(L,13,["ばんめ","ばい","パーセント","グラム"],jp="{右|みぎ}から{三|さん}＿の{人|ひと}が{私|わたし}の{兄|あに}です。",fr="La troisième personne en partant de la droite, c'est mon grand frère.",uses=["v5-20"]),
 C(L,14,["パーセント","ばんめ","ばい","グラム"],jp="{日本|にほん}の{人口|じんこう}の{三十|さんじゅう}＿ぐらいは、{六十五|ろくじゅうご}さい{以上|いじょう}です。",fr="Environ trente pour cent de la population japonaise a soixante-cinq ans ou plus.",uses=["v4-68"]),
 C(L,15,["{重|おも}さ","{重|おも}い","{重|おも}く","{重|おも}かった"],q="« Le poids » se dit…"),
 C(L,16,["trois fois plus","le troisième","trois fois (fréquence)","trois pour cent"],q="Que veut dire **{三|さん}ばい** ?"),
 C(L,17,["Oui","Non"],q="« {六|ろく}さい{以下|いか} » (six ans et moins) : un enfant de six ans est-il compris ?"),
 O(L,18,"Ça fait trois mille yens au total.",["{合計|ごうけい}で","{三千円|さんぜんえん}","です"],uses=["v5-07"]),
]}

TC, TO, XC, XO = make_block("v4-b14", "v4-x07")
test = [
 TC(1,["しらべます","おします","つけます","こわします"],jp="{分|わ}からないことは、インターネットで＿。",fr="Ce que je ne sais pas, je le cherche sur Internet.",uses=["v4-66"]),
 TC(2,["ほうそう","わだい","じけん","ざっし"],jp="{今夜|こんや}、サッカーの{試合|しあい}をテレビで＿します。",fr="Ce soir, le match de foot est diffusé à la télé.",uses=["v4-67"]),
 TC(3,["へいわ","せんそう","{人口|じんこう}","ぼうえき"],jp="{世界|せかい}が＿になるように、みんなでがんばりましょう。",fr="Faisons tous de notre mieux pour que le monde soit en paix.",uses=["v4-68"]),
 TC(4,["へん","がわ","さか","{世界|せかい}"],jp="すみません、この＿にコンビニはありますか。",fr="Excusez-moi, y a-t-il une supérette dans le coin ?",uses=["v4-69"]),
 TC(5,["{重|おも}さ","{長|なが}さ","{高|たか}さ","かず"],jp="このにもつの＿は{十五|じゅうご}キロです。",fr="Ces bagages pèsent quinze kilos.",uses=["v4-70"]),
 TC(6,["{電池|でんち}","がめん","{文字|もじ}","ボタン"],jp="{時計|とけい}が{止|と}まりました。＿をかえなければなりません。",fr="Ma montre s'est arrêtée. Je dois changer la pile.",uses=["v4-66"]),
 TC(7,["きじ","ばんぐみ","アナウンサー","ラジオ"],jp="{新聞|しんぶん}でおもしろい＿を{読|よ}みました。",fr="J'ai lu un article intéressant dans le journal.",uses=["v4-67"]),
 TC(8,["いがく","いかく","いいがく","いまなび"],q=LECT+"**医学** ?",uses=["v4-68"]),
 TC(9,["{村|むら}","{世界|せかい}","{会場|かいじょう}","{区|く}"],jp="そぼはいなかの{小|ちい}さい＿に{住|す}んでいます。",fr="Ma grand-mère vit dans un petit village à la campagne.",uses=["v4-69"]),
 TC(10,["{以下|いか}","{以上|いじょう}","{合計|ごうけい}","ばい"],jp="{六|ろく}さい＿の{小|ちい}さい{子|こ}どもは、バスのお{金|かね}がいりません。",fr="Les petits enfants de six ans et moins ne paient pas le bus.",uses=["v4-70"]),
 TC(11,["エアコン","せんたくき","{電池|でんち}","{文字|もじ}"],jp="{暑|あつ}いですから、＿をつけてもいいですか。",fr="Il fait chaud, je peux allumer la clim ?",uses=["v4-66"]),
 TC(12,["わだい","じけん","ほうそう","こうこく"],jp="{有名|ゆうめい}な{歌手|かしゅ}がけっこんして、{今|いま}とても＿になっています。",fr="Un chanteur célèbre s'est marié : tout le monde en parle en ce moment.",uses=["v4-67"]),
 TC(13,["{工業|こうぎょう}","{医学|いがく}","せんそう","へいわ"],jp="この{地方|ちほう}は{工場|こうじょう}が{多|おお}くて、＿がさかんです。",fr="Il y a beaucoup d'usines dans cette région : l'industrie y est florissante.",uses=["v4-68"]),
 TO(14,"Y a-t-il une banque dans le coin ?",["このへんに","{銀行|ぎんこう}は","ありますか"],uses=["v4-69"]),
 TC(15,["ばんめ","ばい","パーセント","センチ"],jp="{右|みぎ}から{二|に}＿の{人|ひと}が{田中|たなか}さんです。",fr="La deuxième personne en partant de la droite, c'est M. Tanaka.",uses=["v4-70"]),
 TC(16,["des informations, des renseignements","un incident","une publicité","une émission"],q="Que veut dire **じょうほう** ?",uses=["v4-67"]),
]
exam = [
 XC(1,["きょうみ","しゅみ","{人気|にんき}","わだい"],jp="{日本|にほん}のぶんかに＿があって、{毎年|まいとし}おまつりを{見物|けんぶつ}しに{行|い}きます。",fr="Je m'intéresse à la culture japonaise : tous les ans, je vais voir des fêtes traditionnelles.",uses=["v4-61","v4-64"]),
 XC(2,["{天気|てんき}よほう","こうこく","ドラマ","しゅみ"],jp="{台風|たいふう}が{来|く}るそうです。＿をよく{聞|き}いて、{外|そと}に{出|で}ないでください。",fr="Il paraît qu'un typhon arrive. Écoutez bien la météo et ne sortez pas.",uses=["v4-63","v4-67"]),
 XC(3,["{京都|きょうと}の{旅館|りょかん}に{三日|みっか}とまりました。","{京都|きょうと}の{旅館|りょかん}を{三日|みっか}とまりました。","{京都|きょうと}の{旅館|りょかん}に{三日|みっか}とめました。","{京都|きょうと}の{旅館|りょかん}が{三日|みっか}とまりました。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v4-62"]),
 XC(4,["かつ","まける","えらぶ","おうえんする"],jp="{試合|しあい}に＿ために、{毎日|まいにち}れんしゅうしています。",fr="Je m'entraîne tous les jours pour gagner le match.",uses=["v4-65"],star={"jp":"かつ","kana":"かつ","fr":"gagner"}),
 XC(5,["ばい","ばんめ","パーセント","{以下|いか}"],jp="この{町|まち}の{人口|じんこう}は、{十年前|じゅうねんまえ}の{二|に}＿になりました。{人|ひと}がとてもふえました。",fr="La population de cette ville a doublé en dix ans. Elle a énormément augmenté.",uses=["v4-68","v4-70"]),
 XC(6,["{文字|もじ}","ボタン","{電池|でんち}","スイッチ"],jp="けいたいのがめんの＿が{小|ちい}さくて{読|よ}めませんから、{大|おお}きくしました。",fr="Les caractères sur l'écran du portable étaient trop petits, alors je les ai agrandis.",uses=["v4-66"]),
 XC(7,["じんじゃ","みなと","くうこう","{工業|こうぎょう}"],jp="お{正月|しょうがつ}には、{着物|きもの}を{着|き}て＿へ{行|い}きます。",fr="Au Nouvel An, je vais au sanctuaire en kimono.",uses=["v4-62","v4-64"]),
 XO(8,"J'ai vu une pub pour une nouvelle voiture à la télé.",["{新|あたら}しい{車|くるま}の","こうこくを","テレビで","{見|み}ました"],alt=[["テレビで","{新|あたら}しい{車|くるま}の","こうこくを","{見|み}ました"]],uses=["v4-67"]),
 XC(9,["la vue et l'air","la nourriture et l'hôtel","le temps et les gens","le train et la route"],q="{山|やま}の{上|うえ}からのけしきがすばらしくて、{空気|くうき}もきれいでした。 Qu'est-ce qui était bien ?",uses=["v4-62","v4-63"]),
 XC(10,["{火事|かじ}","{台風|たいふう}","ドラマ","しゅみ"],jp="{昨日|きのう}の{夜|よる}、{近所|きんじょ}で＿がありました。{家|いえ}が{一|ひと}つもえました。",fr="Hier soir, il y a eu un incendie dans le quartier. Une maison a brûlé.",uses=["v4-63","v4-69"]),
 XC(11,["はっぴょう","ほうそう","えらび","おうえん"],jp="{兄|あに}は{大学|だいがく}で{医学|いがく}を{研究|けんきゅう}していて、{来月|らいげつ}こくさい{会議|かいぎ}で＿します。",fr="Mon grand frère fait des recherches en médecine à l'université ; le mois prochain, il présente ses travaux à une conférence internationale.",uses=["v4-52","v4-67","v4-68"]),
 XC(12,["Tokyo","Osaka","Les deux, autant","On ne peut pas savoir"],q="{東京|とうきょう}の{人口|じんこう}は{大阪|おおさか}の{三|さん}ばいぐらいです。 Quelle ville a le plus d'habitants ?",uses=["v4-68","v4-70"]),
 XC(13,["おんせん","みずうみ","しま","みなと"],jp="スキーのあとで＿に{入|はい}りました。{体|からだ}があたたまりました。",fr="Après le ski, je suis allé au bain des sources chaudes. Ça m'a réchauffé.",uses=["v4-62","v4-65"]),
 XC(14,["しらべて","はっぴょうして","ほうそうして","えらんで"],jp="インターネットで{旅館|りょかん}のじょうほうを＿、よやくしました。",fr="J'ai cherché des informations sur l'auberge sur Internet, puis j'ai réservé.",uses=["v4-54","v4-62","v4-66","v4-67"]),
 XC(15,["{以上|いじょう}","{以下|いか}","ばんめ","{合計|ごうけい}"],jp="このにもつは{二十|にじゅう}キロ＿ありますから、{一人|ひとり}では{持|も}てません。",fr="Ces bagages pèsent vingt kilos ou plus, on ne peut pas les porter seul.",uses=["v4-70"]),
]
bloc = {"id": "v4-b14", "level": "N4", "title": "Le monde moderne : technologie, médias, société, territoire, mesures",
        "lessons": [l66, l67, l68, l69, l70], "test": test, "examTest": exam}
save_n4(bloc, sys.argv[1])
