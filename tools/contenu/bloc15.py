import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L71 Keigo : respect ----------
L = "v4-71"
l71 = {"id": L, "title": "Keigo : verbes de respect", "words": [
 W("いらっしゃる","いらっしゃる","être, aller, venir (respect)","{社長|しゃちょう}は{今|いま}、{会議室|かいぎしつ}にいらっしゃいます。","Le patron est dans la salle de réunion."),
 W("おっしゃる","おっしゃる","dire (respect)","{先生|せんせい}が{明日|あした}{試験|しけん}があるとおっしゃいました。","Le professeur a dit qu'il y avait un examen demain."),
 W("めしあがる","めしあがる","manger, boire (respect)","どうぞ、めしあがってください。","Je vous en prie, servez-vous."),
 W("なさる","なさる","faire (respect)","{週末|しゅうまつ}は{何|なに}をなさいますか。","Que faites-vous le week-end ?"),
 W("ごらんになる","ごらんになる","voir, regarder (respect)","この{写真|しゃしん}をごらんになりましたか。","Avez-vous vu cette photo ?"),
 W("くださる","くださる","me donner (respect)","{先生|せんせい}がこの{本|ほん}をくださいました。","Le professeur m'a donné ce livre."),
 W("ごぞんじ","ごぞんじ","savoir, connaître (respect)","{田中|たなか}さんをごぞんじですか。","Connaissez-vous M. Tanaka ?"),
 W("おたく","おたく","votre maison (poli)","{先生|せんせい}のおたくはどちらですか。","Où habitez-vous, monsieur le professeur ?"),
 W("〜さま","〜さま","M. / Mme … (très poli)","{山田|やまだ}さま、こちらへどうぞ。","Monsieur Yamada, par ici, je vous prie."),
 W("おいでになる","おいでになる","venir, être (respect)","{明日|あした}は{何時|なんじ}においでになりますか。","À quelle heure venez-vous demain ?"),
 W("ございます","ございます","il y a (très poli)","トイレはあちらにございます。","Les toilettes sont par là."),
 W("いらっしゃいませ","いらっしゃいませ","bienvenue (magasin)","いらっしゃいませ。{何名|なんめい}さまですか。","Bienvenue. Vous êtes combien ?"),
 W("おきゃくさま","おきゃくさま","client (très poli)","おきゃくさま、こちらへどうぞ。","Madame, monsieur, par ici je vous prie."),
 W("お{休|やす}みになる","おやすみになる","se coucher, dormir (respect)","{社長|しゃちょう}はもうお{休|やす}みになりました。","Le patron est déjà couché."),
], "sections": [
 {"h": "Les verbes de respect (そんけいご)",
  "p": ["On les emploie pour ce que fait **l'autre** (client, professeur, supérieur). Jamais pour soi."],
  "grid": {"head": ["verbe simple", "respect"], "rows": [
   ["いる · {行|い}く · {来|く}る", "いらっしゃる"],
   ["{言|い}う", "おっしゃる"],
   ["{食|た}べる · {飲|の}む", "めしあがる"],
   ["する", "なさる"],
   ["{見|み}る", "ごらんになる"],
   ["くれる", "くださる"],
   ["{知|し}っている", "ごぞんじだ"],
   ["ねる", "お{休|やす}みになる"]]}}
], "pieges": [
 "Le respect s'emploie pour ce que fait **l'autre** : {先生|せんせい}が**いらっしゃいます**. Pour soi : leçon 72 (modestie).",
 "Forme ます irrégulière : いらっしゃ**い**ます, おっしゃ**い**ます, なさ**い**ます, くださ**い**ます (pas 〜ります).",
 "ございます = あります en très poli : トイレはあちらに**ございます**. Pour une personne : いらっしゃいます.",
 "ごぞんじですか = vous connaissez ? Pour soi, on répond : はい、{知|し}っています.",
 "おたく = la maison **de l'autre** (poli).",
 "〜さま = さん en plus poli : おきゃくさま, {田中|たなか}さま."
], "exercises": [
 C(L,1,["いらっしゃいます","いらっしゃります","いらっしゃるます","いらっしゃいいます"],jp="{社長|しゃちょう}は{今|いま}、{会議室|かいぎしつ}に＿。",fr="Le patron est dans la salle de réunion.",uses=["v4-51"],explain="Forme ます irrégulière : いらっしゃ**い**ます.",star={"jp":"いらっしゃる","kana":"いらっしゃる","fr":"être, aller, venir (respect)"}),
 C(L,2,["おっしゃいました","めしあがりました","ごらんになりました","くださいました"],jp="{先生|せんせい}が、{明日|あした}{試験|しけん}があると＿。",fr="Le professeur a dit qu'il y avait un examen demain.",uses=["v5-29"]),
 C(L,3,["めしあがって","ごぞんじで","くださって","ございまして"],jp="どうぞ、たくさん＿ください。",fr="Je vous en prie, servez-vous bien."),
 C(L,4,["なさいます","なさります","いたします","ございます"],jp="{先生|せんせい}は{週末|しゅうまつ}{何|なに}を＿か。",fr="Professeur, que faites-vous le week-end ?",uses=["v5-17"]),
 C(L,5,["ごらんになりました","お{休|やす}みになりました","めしあがりました","おっしゃいました"],jp="{部長|ぶちょう}、{昨日|きのう}のしりょうを＿か。",fr="Chef, avez-vous vu les documents d'hier ?",uses=["v4-51"]),
 C(L,6,["くださいました","めしあがりました","いらっしゃいました","おっしゃいました"],jp="{先生|せんせい}がこの{本|ほん}を{私|わたし}に＿。",fr="Le professeur m'a donné ce livre.",uses=["v5-26"]),
 C(L,7,["ごぞんじです","ごらんになります","めしあがります","なさいます"],jp="{田中|たなか}{先生|せんせい}を＿か。— はい、よく{知|し}っています。",fr="Connaissez-vous le professeur Tanaka ? — Oui, très bien.",uses=["v5-28"]),
 C(L,8,["おたく","おきゃくさま","ございます","いらっしゃいませ"],jp="{先生|せんせい}の＿はどちらですか。— {駅|えき}の{近|ちか}くです。",fr="Où est votre maison, professeur ? — Près de la gare.",uses=["v5-09"]),
 C(L,9,["いらっしゃいませ","おじゃまします","ただいま","いただきます"],q="Un client entre dans le restaurant. L'employé dit :",uses=["v5-11"]),
 C(L,10,["ございます","いらっしゃいます","なさいます","おっしゃいます"],jp="トイレはあちらに＿。",fr="Les toilettes sont par là.",explain="Pour une chose, en très poli : ございます. いらっしゃる, c'est pour une personne."),
 C(L,11,["お{休|やす}みになりました","めしあがりました","ごらんになりました","ございました"],jp="{社長|しゃちょう}はもう＿。{明日|あした}の{朝|あさ}お{会|あ}いできます。",fr="Le patron est déjà couché. Vous pourrez le voir demain matin.",uses=["v4-51"]),
 C(L,12,["さま","くださる","ございます","おたく"],jp="{田中|たなか}＿、こちらへどうぞ。",fr="Monsieur Tanaka, par ici je vous prie.",uses=["v5-11"]),
 C(L,13,["おいでになります","おっしゃいます","ごぞんじです","くださいます"],jp="{明日|あした}は{何時|なんじ}にこちらへ＿か。",fr="À quelle heure venez-vous ici demain ?",uses=["v5-16"]),
 C(L,14,["おっしゃる","いらっしゃる","なさる","めしあがる"],q="Forme de respect de **{言|い}う** ?"),
 C(L,15,["めしあがる","ごらんになる","おっしゃる","くださる"],q="Forme de respect de **{食|た}べる** ?"),
 C(L,16,["ごらんになる","めしあがる","なさる","いらっしゃる"],q="Forme de respect de **{見|み}る** ?"),
 C(L,17,["Non : めしあがる est réservé à ce que font les autres.","Oui, c'est très poli.","Oui, mais seulement au restaurant.","Non, il faut dire めしあがりです."],q="Peut-on dire de soi-même : {私|わたし}はコーヒーをめしあがります ?"),
 O(L,18,"Je vous en prie, servez-vous.",["どうぞ","めしあがって","ください"]),
]}

# ---------- L72 Keigo : modestie ----------
L = "v4-72"
l72 = {"id": L, "title": "Keigo : verbes de modestie", "words": [
 W("まいる","まいる","aller, venir (modestie)","{明日|あした}{十時|じゅうじ}にまいります。","Je viendrai demain à dix heures."),
 W("もうす","もうす","dire, s'appeler (modestie)","はじめまして、{田中|たなか}ともうします。","Enchanté, je m'appelle Tanaka."),
 W("いたす","いたす","faire (modestie)","{私|わたくし}がごあんないいたします。","Je vais vous guider."),
 W("いただく","いただく","recevoir ; manger (modestie)","{先生|せんせい}にじしょをいただきました。","Le professeur m'a offert un dictionnaire."),
 W("はいけんする","はいけんする","voir, lire (modestie)","お{手紙|てがみ}をはいけんしました。","J'ai lu votre lettre."),
 W("うかがう","うかがう","rendre visite ; demander (modestie)","{明日|あした}、おたくにうかがってもいいですか。","Puis-je passer chez vous demain ?"),
 W("おる","おる","être (modestie)","{父|ちち}は{今|いま}、{家|いえ}におります。","Mon père est à la maison en ce moment."),
 W("お{目|め}にかかる","おめにかかる","rencontrer (modestie)","{社長|しゃちょう}にお{目|め}にかかりたいです。","Je souhaiterais rencontrer le patron."),
 W("さしあげる","さしあげる","donner (modestie)","{先生|せんせい}に{花|はな}をさしあげました。","J'ai offert des fleurs au professeur."),
 W("ぞんじる","ぞんじる","savoir, connaître (modestie)","{田中|たなか}さんのことはよくぞんじています。","Je connais bien M. Tanaka."),
 W("{私|わたくし}","わたくし","je, moi (très poli)","{私|わたくし}が{田中|たなか}でございます。","C'est moi, Tanaka."),
 W("もうしあげる","もうしあげる","dire (modestie, très poli)","{心|こころ}からおれいをもうしあげます。","Je vous remercie du fond du cœur."),
], "sections": [
 {"h": "Les verbes de modestie (けんじょうご)",
  "p": ["On les emploie pour ce que **je** fais (ou ma famille, mon entreprise) devant quelqu'un qu'on respecte."],
  "grid": {"head": ["verbe simple", "modestie"], "rows": [
   ["{行|い}く · {来|く}る", "まいる"],
   ["{言|い}う", "もうす · もうしあげる"],
   ["する", "いたす"],
   ["もらう · {食|た}べる", "いただく"],
   ["{見|み}る", "はいけんする"],
   ["{聞|き}く · aller chez qqn", "うかがう"],
   ["いる", "おる"],
   ["{会|あ}う", "お{目|め}にかかる"],
   ["あげる", "さしあげる"],
   ["{知|し}っている", "ぞんじている"]]}}
], "pieges": [
 "Même action, deux formes : {先生|せんせい}が**いらっしゃる** (respect) / {私|わたし}が**まいる** (modestie).",
 "Au téléphone avec un client, on parle de **son propre** chef avec la modestie : {部長|ぶちょう}の{田中|たなか}は{会議|かいぎ}に{出|で}て**おります**.",
 "いただきます (avant le repas) vient de いただく : recevoir humblement.",
 "うかがう = « je viens chez vous » **ou** « je vous demande ».",
 "Pour se présenter : 〜**ともうします**.",
 "わたくし = « je » très poli (discours, téléphone professionnel)."
], "exercises": [
 C(L,1,["ともうします","とおっしゃいます","といたします","とまいります"],jp="はじめまして。マリー＿。よろしくおねがいします。",fr="Enchantée. Je m'appelle Marie. Ravie de vous connaître.",uses=["v5-11"]),
 C(L,2,["まいります","いらっしゃいます","めしあがります","ごらんになります"],q="Tu parles à un client.",jp="{明日|あした}{十時|じゅうじ}にそちらへ＿。",fr="Je viendrai chez vous demain à dix heures.",uses=["v4-71"],explain="Pour ce que **je** fais : modestie (まいる)."),
 C(L,3,["いたします","なさいます","まいります","もうします"],jp="{私|わたくし}がごあんない＿。こちらへどうぞ。",fr="Je vais vous guider. Par ici, je vous prie.",uses=["v4-46"]),
 C(L,4,["いただきました","くださいました","さしあげました","もうしました"],jp="{先生|せんせい}にじしょを＿。とても{便利|べんり}です。",fr="Le professeur m'a offert un dictionnaire. Il est très pratique.",uses=["v5-12","v5-19"]),
 C(L,5,["はいけんしました","ごらんになりました","いたしました","まいりました"],jp="{先生|せんせい}のお{手紙|てがみ}を＿。ありがとうございました。",fr="J'ai lu votre lettre, professeur. Merci beaucoup.",uses=["v5-12"]),
 C(L,6,["うかがって","いらっしゃって","めしあがって","はいけんして"],jp="{明日|あした}、{先生|せんせい}のおたくに＿もよろしいですか。",fr="Puis-je passer chez vous demain, professeur ?",uses=["v4-71"]),
 C(L,7,["おります","いらっしゃいます","ございます","なさいます"],q="Au téléphone, un client demande ton père.",jp="{父|ちち}は{今|いま}、{家|いえ}に＿。",fr="Mon père est à la maison en ce moment.",uses=["v4-71"],explain="Sa propre famille, devant quelqu'un d'extérieur : modestie (おる)."),
 C(L,8,["お{目|め}にかかり","ごらんになり","めしあがり","おっしゃり"],jp="{一度|いちど}、{社長|しゃちょう}に＿たいです。",fr="J'aimerais rencontrer le patron une fois.",uses=["v4-51"]),
 C(L,9,["さしあげました","くださいました","まいりました","めしあがりました"],jp="{先生|せんせい}のたんじょうびに、{私|わたし}は{花|はな}を＿。",fr="Pour l'anniversaire du professeur, je lui ai offert des fleurs.",uses=["v5-17","v5-35"]),
 C(L,10,["ぞんじて","ごぞんじで","もうして","いたして"],jp="その{方|かた}のことは、よく＿おります。",fr="Je connais bien cette personne.",uses=["v5-39"]),
 C(L,11,["わたくし","わたし","ぼく","おれ"],q="Comment dit-on « je » de la façon la plus polie (discours, téléphone professionnel) ?"),
 C(L,12,["もうしあげます","おっしゃいます","めしあがります","いらっしゃいます"],jp="{心|こころ}からおれいを＿。",fr="Je vous remercie du fond du cœur.",uses=["v4-53"]),
 C(L,13,["{行|い}く / {来|く}る","{言|い}う","{見|み}る","する"],q="まいる est la forme de modestie de…"),
 C(L,14,["{見|み}る","{聞|き}く","{会|あ}う","{書|か}く"],q="はいけんする est la forme de modestie de…"),
 C(L,15,["demander (poliment)","rendre visite","attendre","entendre"],q="Dans « ちょっとうかがいますが、{駅|えき}はどこですか », que veut dire うかがう ?"),
 C(L,16,["moi (celui qui parle)","la personne à qui je parle","mon patron","un client"],q="Qui fait l'action dans « {明日|あした}そちらへまいります » ?"),
 O(L,17,"Je viendrai demain à dix heures.",["{明日|あした}","{十時|じゅうじ}に","まいります"],uses=["v5-16"]),
]}

# ---------- L73 Formules polies ----------
L = "v4-73"
l73 = {"id": L, "title": "Formules polies N4", "words": [
 W("おまたせしました","おまたせしました","désolé de vous avoir fait attendre","おまたせしました。コーヒーです。","Désolé pour l'attente. Voici votre café."),
 W("おかげさまで","おかげさまで","grâce à vous (réponse polie)","お{元気|げんき}ですか。— はい、おかげさまで。","Vous allez bien ? — Oui, merci."),
 W("かしこまりました","かしこまりました","bien compris (employé → client)","コーヒーを{二|ふた}つおねがいします。— かしこまりました。","Deux cafés, s'il vous plaît. — Bien, monsieur."),
 W("しょうちしました","しょうちしました","entendu, bien compris","{明日|あした}{九時|くじ}に{来|き}てください。— しょうちしました。","Venez demain à neuf heures. — Entendu."),
 W("もうしわけありません","もうしわけありません","je suis vraiment désolé","おそくなって、もうしわけありません。","Je suis vraiment désolé d'être en retard."),
 W("おせわになりました","おせわになりました","merci pour tout (votre aide)","{三年間|さんねんかん}、おせわになりました。","Merci pour tout pendant ces trois années."),
 W("おつかれさまでした","おつかれさまでした","merci pour votre travail","{今日|きょう}もおつかれさまでした。","Merci pour votre travail aujourd'hui encore."),
 W("いってらっしゃい","いってらっしゃい","à tout à l'heure (à qui part)","いってきます。— いってらっしゃい。","J'y vais ! — À tout à l'heure !"),
 W("おかえりなさい","おかえりなさい","bon retour (à qui rentre)","ただいま。— おかえりなさい。","Je suis rentré ! — Bon retour !"),
 W("おめでとうございます","おめでとうございます","félicitations","ごけっこん、おめでとうございます。","Félicitations pour votre mariage."),
 W("よろしくおねがいします","よろしくおねがいします","ravi de vous connaître ; je compte sur vous","はじめまして。マリーです。よろしくおねがいします。","Enchantée, je suis Marie. Ravie de vous connaître."),
 W("おじゃまします","おじゃまします","je vous dérange (en entrant chez qqn)","どうぞ、{入|はい}ってください。— おじゃまします。","Entrez, je vous en prie. — Merci, je vous dérange."),
 W("おさきにしつれいします","おさきにしつれいします","je pars avant vous (excusez-moi)","{仕事|しごと}が{終|お}わりました。おさきにしつれいします。","J'ai fini mon travail. Je vous laisse, bonne soirée."),
 W("どういたしまして","どういたしまして","de rien","ありがとうございました。— どういたしまして。","Merci beaucoup. — De rien."),
 W("ようこそ","ようこそ","bienvenue","{日本|にほん}へようこそ。","Bienvenue au Japon."),
], "sections": [
 {"h": "Qui dit quoi, et quand ?",
  "p": ["Ces formules se disent dans des situations précises : apprenez la situation avec la phrase."],
  "grid": {"head": ["situation", "formule"], "rows": [
   ["on a fait attendre", "おまたせしました"],
   ["employé → client : « bien reçu »", "かしこまりました · しょうちしました"],
   ["on quitte le travail avant les autres", "おさきにしつれいします → おつかれさまでした"],
   ["on entre chez quelqu'un", "おじゃまします"],
   ["on part après une longue aide", "おせわになりました"],
   ["grandes excuses", "もうしわけありません"]]}}
], "pieges": [
 "かしこまりました (très poli, employé → client) ≈ しょうちしました ≈ {分|わ}かりました.",
 "おかげさまで = « grâce à vous » : la réponse polie à « vous allez bien ? ».",
 "おつかれさまでした = merci pour votre travail (entre collègues, en fin de journée).",
 "おじゃまします = « je vous dérange » : en entrant chez quelqu'un.",
 "もうしわけありません = すみません en beaucoup plus poli.",
 "いってきます → **いってらっしゃい** ; ただいま → **おかえりなさい** (leçon 11)."
], "exercises": [
 C(L,1,["おまたせしました","おかえりなさい","いってらっしゃい","おじゃまします"],jp="＿。コーヒーとケーキです。",fr="Désolé pour l'attente. Voici le café et le gâteau.",uses=["v5-06"]),
 C(L,2,["おかげさまで","おまたせしました","おじゃまします","ようこそ"],jp="お{元気|げんき}ですか。— はい、＿、{元気|げんき}です。",fr="Vous allez bien ? — Oui, grâce à vous, je vais bien.",uses=["v5-19"]),
 C(L,3,["かしこまりました","おかげさまで","おつかれさまでした","おめでとうございます"],jp="コーヒーを{二|ふた}つおねがいします。— ＿。",fr="Deux cafés, s'il vous plaît. — Bien, monsieur.",uses=["v5-11"]),
 C(L,4,["もうしわけありません","おかげさまで","ようこそ","いってらっしゃい"],jp="{会議|かいぎ}におくれて、＿。",fr="Je suis vraiment désolé d'être arrivé en retard à la réunion.",uses=["v4-50","v4-51"]),
 C(L,5,["おせわになりました","おじゃまします","おまたせしました","おかえりなさい"],jp="{今日|きょう}で{会社|かいしゃ}をやめます。{三年間|さんねんかん}、＿。",fr="Je quitte l'entreprise aujourd'hui. Merci pour tout pendant ces trois années.",uses=["v4-51"]),
 C(L,6,["おつかれさまでした","いただきます","おかげさまで","ようこそ"],jp="「おさきにしつれいします。」「＿。」",fr="« Je vous laisse, bonne soirée. » « Merci pour ton travail ! »"),
 C(L,7,["おじゃまします","おまたせしました","おかえりなさい","おつかれさまでした"],q="Tu entres chez un ami qui t'a invité. Tu dis :"),
 C(L,8,["おめでとうございます","おかげさまで","もうしわけありません","おじゃまします"],q="Ton ami se marie. Tu lui dis :",uses=["v4-64"]),
 C(L,9,["どういたしまして","おかげさまで","よろしくおねがいします","ようこそ"],q="Quelqu'un te remercie : ありがとうございました. Tu réponds :"),
 C(L,10,["{日本|にほん}へようこそ。","{日本|にほん}へおじゃまします。","{日本|にほん}へおかえりなさい。","{日本|にほん}へおまたせしました。"],q="Tu accueilles un visiteur étranger au Japon. Tu dis :"),
 C(L,11,["いってらっしゃい","おかえりなさい","ただいま","いただきます"],q="Ton fils part à l'école : いってきます！ Tu réponds :",uses=["v5-11"]),
 C(L,12,["おさきにしつれいします","おまたせしました","ようこそ","いただきます"],q="Tu quittes le bureau avant tes collègues. Tu dis :"),
 C(L,13,["しょうちしました","おかげさまで","おめでとうございます","どういたしまして"],jp="{明日|あした}は{八時|はちじ}に{来|き}てください。— ＿。",fr="Venez demain à huit heures. — Entendu.",uses=["v5-16"]),
 C(L,14,["よろしくおねがいします","おまたせしました","おせわになりました","おかえりなさい"],jp="はじめまして、{田中|たなか}です。どうぞ＿。",fr="Enchanté, je m'appelle Tanaka. Ravi de vous connaître.",uses=["v5-11"]),
 C(L,15,["Je suis vraiment désolé (très poli).","Je n'ai rien à dire.","Merci beaucoup.","Ce n'est pas grave."],q="Que veut dire **もうしわけありません** ?"),
 C(L,16,["Grâce à vous (réponse polie).","Bon appétit.","Bienvenue.","Désolé pour l'attente."],q="Que veut dire **おかげさまで** ?"),
 C(L,17,["かしこまりました","おじゃまします","どういたしまして","おかえりなさい"],q="Un client passe sa commande. Que lui répond l'employé ?"),
]}

# ---------- L74 Mots abstraits (1) ----------
L = "v4-74"
l74 = {"id": L, "title": "Raisons, avis, intentions", "words": [
 W("りゆう","りゆう","raison","{会社|かいしゃ}をやめたりゆうを{教|おし}えてください。","Dites-moi pourquoi vous avez quitté l'entreprise."),
 W("{意見|いけん}","いけん","avis, opinion","みんなの{意見|いけん}を{聞|き}きましょう。","Écoutons l'avis de chacun."),
 W("けいけん","けいけん","expérience (vécue)","{外国|がいこく}で{働|はたら}いたけいけんがあります。","J'ai déjà travaillé à l'étranger."),
 W("しゅうかん","しゅうかん","habitude, coutume","{毎朝|まいあさ}{走|はし}るしゅうかんがあります。","J'ai l'habitude de courir tous les matins."),
 W("きそく","きそく","règlement","この{学校|がっこう}はきそくがきびしいです。","Le règlement de cette école est strict."),
 W("げんいん","げんいん","cause","じこのげんいんはまだ{分|わ}かりません。","On ne connaît pas encore la cause de l'accident."),
 W("{考|かんが}え","かんがえ","idée, pensée","それはいい{考|かんが}えですね。","C'est une bonne idée."),
 W("つもり","つもり","intention","{来年|らいねん}{日本|にほん}へ{行|い}くつもりです。","J'ai l'intention d'aller au Japon l'an prochain."),
 W("ひつよう","ひつよう","nécessaire","{日本|にほん}へ{行|い}くとき、ビザはひつようですか。","Faut-il un visa pour aller au Japon ?"),
 W("{特別|とくべつ}","とくべつ","spécial","{今日|きょう}は{特別|とくべつ}な{日|ひ}です。","Aujourd'hui est un jour spécial."),
 W("ふつう","ふつう","normal, d'habitude","ふつうは{七時|しちじ}に{起|お}きます。","D'habitude, je me lève à sept heures."),
 W("じゆう","じゆう","libre, liberté","この{部屋|へや}はじゆうに{使|つか}ってください。","Utilisez cette pièce librement."),
 W("はんたい","はんたい","opposition, contre","{父|ちち}は{私|わたし}の{計画|けいかく}にはんたいしました。","Mon père s'est opposé à mon projet."),
 W("さんせい","さんせい","accord, pour","その{意見|いけん}にさんせいです。","Je suis d'accord avec cet avis."),
 W("ゆめ","ゆめ","rêve","しょうらいのゆめは{医者|いしゃ}になることです。","Mon rêve, c'est de devenir médecin plus tard."),
], "sections": [
 {"h": "Donner son avis",
  "p": ["Des mots indispensables pour parler de ses idées et de ses projets."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["je suis pour / contre", "〜==に==さんせいです / 〜==に==はんたいです"],
   ["à mon avis…", "{私|わたし}の{意見|いけん}は…"],
   ["la raison, c'est…", "〜のりゆうは…"],
   ["j'ai l'intention de…", "(verbe) ==つもり==です"],
   ["c'est nécessaire", "〜==が==ひつようです"],
   ["d'habitude", "ふつうは…"]]}}
], "pieges": [
 "〜**に**さんせい / 〜**に**はんたい : être pour / contre **quelque chose**.",
 "つもり = intention : {行|い}く**つもり**です (forme dictionnaire + つもり).",
 "ひつよう = nécessaire (adjectif en な) : ひつような{物|もの}. Rappel : いる = avoir besoin (leçon 36).",
 "けいけん = expérience vécue : 〜**た**けいけんがある = avoir déjà fait.",
 "しゅうかん = habitude (personnelle) ou coutume (d'un pays).",
 "{特別|とくべつ} (spécial) ↔ ふつう (normal) ; じゆう (libre) : adjectifs en な."
], "exercises": [
 C(L,1,["りゆう","ゆめ","きそく","つもり"],jp="{会社|かいしゃ}をやめた＿を{教|おし}えてください。",fr="Dites-moi pourquoi vous avez quitté l'entreprise.",uses=["v4-51"]),
 C(L,2,["{意見|いけん}","きそく","げんいん","しゅうかん"],jp="みんなの＿を{聞|き}いてから、きめましょう。",fr="Écoutons l'avis de chacun avant de décider.",uses=["v4-48"]),
 C(L,3,["けいけん","さんせい","きそく","じゆう"],jp="{外国|がいこく}で{働|はたら}いた＿がありますか。",fr="Avez-vous déjà travaillé à l'étranger ?",uses=["v5-33"]),
 C(L,4,["しゅうかん","けいけん","ゆめ","はんたい"],jp="{日本|にほん}では、{家|いえ}に{入|はい}るとき、くつをぬぐ＿があります。",fr="Au Japon, on a la coutume d'enlever ses chaussures en entrant dans une maison.",uses=["v5-13"]),
 C(L,5,["きそく","ゆめ","{考|かんが}え","じゆう"],jp="この{学校|がっこう}は＿がきびしくて、けいたいを{使|つか}ってはいけません。",fr="Le règlement de cette école est strict : on n'a pas le droit d'utiliser son portable.",uses=["v4-42","v4-66"]),
 C(L,6,["げんいん","ゆめ","しゅうかん","さんせい"],jp="じこの＿はまだ{分|わ}かりません。けいさつがしらべています。",fr="On ne connaît pas encore la cause de l'accident. La police enquête.",uses=["v4-50","v4-59"]),
 C(L,7,["{考|かんが}え","げんいん","きそく","けいけん"],jp="それはいい＿ですね。そうしましょう。",fr="C'est une bonne idée. Faisons comme ça."),
 C(L,8,["つもり","けいけん","きそく","ひつよう"],jp="{来年|らいねん}、{日本|にほん}の{大学|だいがく}に{入|はい}る＿です。",fr="J'ai l'intention d'entrer dans une université japonaise l'an prochain.",uses=["v5-30"]),
 C(L,9,["ひつよう","{特別|とくべつ}","ふつう","じゆう"],jp="{日本|にほん}に{三|さん}か{月|げつ}{以上|いじょう}いるときは、ビザが＿です。",fr="Pour rester plus de trois mois au Japon, il faut un visa.",uses=["v4-70"]),
 C(L,10,["{特別|とくべつ}","ふつう","ひつよう","はんたい"],jp="{今日|きょう}は{母|はは}のたんじょうびですから、＿な{料理|りょうり}を{作|つく}ります。",fr="Aujourd'hui, c'est l'anniversaire de ma mère, alors je prépare un plat spécial.",uses=["v5-17"]),
 C(L,11,["ふつう","{特別|とくべつ}","じゆう","はんたい"],jp="＿は{七時|しちじ}に{起|お}きますが、{日曜日|にちようび}はおそくまでねます。",fr="D'habitude, je me lève à sept heures, mais le dimanche je dors tard.",uses=["v5-16"]),
 C(L,12,["じゆう","けいけん","げんいん","ゆめ"],jp="この{部屋|へや}は＿に{使|つか}ってください。",fr="Utilisez cette pièce librement.",uses=["v5-27"]),
 C(L,13,["はんたい","さんせい","けいけん","ゆめ"],jp="{父|ちち}は{私|わたし}がりゅうがくすることに＿しました。「あぶない」と{言|い}いました。",fr="Mon père s'est opposé à mon départ pour étudier à l'étranger. Il a dit : « C'est dangereux. »",uses=["v4-50","v4-52"]),
 C(L,14,["さんせい","はんたい","りゆう","げんいん"],jp="その{意見|いけん}に＿です。とてもいい{考|かんが}えだと{思|おも}います。",fr="Je suis d'accord avec cet avis. Je trouve que c'est une très bonne idée.",uses=["v5-28"]),
 C(L,15,["ゆめ","きそく","げんいん","しゅうかん"],jp="しょうらいの＿は{医者|いしゃ}になることです。",fr="Mon rêve, c'est de devenir médecin plus tard.",uses=["v4-54"]),
 C(L,16,["はんたい","{意見|いけん}","りゆう","ふつう"],q="Contraire de **さんせい** ?"),
 C(L,17,["ふつう","じゆう","ひつよう","はんたい"],q="Contraire de **{特別|とくべつ}** ?"),
 O(L,18,"J'ai l'intention d'aller au Japon l'an prochain.",["{来年|らいねん}","{日本|にほん}へ","{行|い}く","つもりです"],alt=[["{日本|にほん}へ","{来年|らいねん}","{行|い}く","つもりです"]],uses=["v5-03"]),
]}

# ---------- L75 Mots abstraits (2) ----------
L = "v4-75"
l75 = {"id": L, "title": "Moyens, buts, résultats", "words": [
 W("ほうほう","ほうほう","méthode, moyen","{日本語|にほんご}をおぼえるいいほうほうを{教|おし}えてください。","Apprends-moi une bonne méthode pour retenir le japonais."),
 W("もくてき","もくてき","but","{旅行|りょこう}のもくてきは{何|なん}ですか。— かんこうです。","Quel est le but de votre voyage ? — Le tourisme."),
 W("けっか","けっか","résultat","{試験|しけん}のけっかは{来週|らいしゅう}{分|わ}かります。","On connaîtra les résultats de l'examen la semaine prochaine."),
 W("かんけい","かんけい","rapport, lien","{私|わたし}はそのじけんとかんけいがありません。","Je n'ai aucun lien avec cette affaire."),
 W("{場合|ばあい}","ばあい","cas","{雨|あめ}の{場合|ばあい}は、{試合|しあい}はありません。","En cas de pluie, le match n'a pas lieu."),
 W("{心|こころ}","こころ","cœur (esprit)","{心|こころ}のやさしい{人|ひと}です。","C'est quelqu'un de bon cœur."),
 W("わけ","わけ","raison, explication","どうしておくれたのか、わけを{話|はな}してください。","Explique-moi pourquoi tu es en retard."),
 W("ため","ため","pour, dans le but de","{家族|かぞく}のために、いっしょうけんめい{働|はたら}きます。","Je travaille dur pour ma famille."),
 W("ようす","ようす","air, état, situation","{田中|たなか}さんのようすがへんです。","M. Tanaka a l'air bizarre."),
 W("かたち","かたち","forme","このくもは{魚|さかな}のかたちをしています。","Ce nuage a la forme d'un poisson."),
 W("{部分|ぶぶん}","ぶぶん","partie","この{部分|ぶぶん}がよく{分|わ}かりません。","Je ne comprends pas bien cette partie."),
 W("かわり","かわり","à la place, remplacement","{父|ちち}のかわりに、{私|わたし}が{会議|かいぎ}に{出|で}ました。","J'ai assisté à la réunion à la place de mon père."),
 W("まちがい","まちがい","erreur, faute","{作文|さくぶん}にまちがいがたくさんあります。","Il y a beaucoup de fautes dans la rédaction."),
 W("まちがえる","まちがえる","se tromper (de)","{電車|でんしゃ}をまちがえて、ちがう{駅|えき}に{着|つ}きました。","Je me suis trompé de train et je suis arrivé à une autre gare."),
 W("くらべる","くらべる","comparer","{東京|とうきょう}と{大阪|おおさか}をくらべると、{東京|とうきょう}のほうが{大|おお}きいです。","Si on compare Tokyo et Osaka, Tokyo est plus grand."),
], "sections": [
 {"h": "Tournures utiles",
  "p": ["Ces noms servent surtout dans des tournures toutes faites."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["pour (but, personne)", "〜==のために=="],
   ["à la place de", "〜==のかわりに=="],
   ["en cas de", "〜==の{場合|ばあい}は=="],
   ["n'avoir aucun lien avec", "〜==と==かんけいがない"],
   ["se tromper de", "〜==を==まちがえる"],
   ["comparer A et B", "A==と==B==を==くらべる"]]}}
], "pieges": [
 "〜のために = pour (un but, une personne) : {家族|かぞく}のために.",
 "〜のかわりに = à la place de : {父|ちち}のかわりに.",
 "わけ = la raison, l'explication (≈ りゆう, plus oral).",
 "まちがい (nom : une faute) / まちがえる (verbe : se tromper de) : {電車|でんしゃ}**を**まちがえる.",
 "ようす = l'air, l'état : ようすがへん = il a l'air bizarre.",
 "{場合|ばあい} se lit ばあい (lecture spéciale)."
], "exercises": [
 C(L,1,["ほうほう","けっか","かんけい","{部分|ぶぶん}"],jp="{日本語|にほんご}のことばをおぼえるいい＿を{教|おし}えてください。",fr="Apprends-moi une bonne méthode pour retenir les mots japonais.",uses=["v5-28"]),
 C(L,2,["もくてき","けっか","かたち","まちがい"],jp="{旅行|りょこう}の＿は{何|なん}ですか。— かんこうです。",fr="Quel est le but de votre voyage ? — Le tourisme.",uses=["v4-62"]),
 C(L,3,["けっか","もくてき","ほうほう","かたち"],jp="{試験|しけん}の＿は{来週|らいしゅう}{分|わ}かります。",fr="On connaîtra les résultats de l'examen la semaine prochaine.",uses=["v5-29"]),
 C(L,4,["かんけい","けっか","ようす","かわり"],jp="{私|わたし}はそのじけんと＿がありません。",fr="Je n'ai aucun lien avec cette affaire.",uses=["v4-67"]),
 C(L,5,["{場合|ばあい}","ため","わけ","かたち"],jp="{雨|あめ}の＿は、{試合|しあい}は{来週|らいしゅう}です。",fr="En cas de pluie, le match aura lieu la semaine prochaine.",uses=["v4-61"]),
 C(L,6,["{心|こころ}","{部分|ぶぶん}","けっか","かたち"],jp="{田中|たなか}さんは＿のやさしい{人|ひと}です。",fr="M. Tanaka a bon cœur.",uses=["v5-18"]),
 C(L,7,["わけ","かたち","ほうほう","けっか"],jp="どうしておくれたのか、＿を{話|はな}してください。",fr="Explique-moi pourquoi tu es en retard.",uses=["v4-50"]),
 C(L,8,["ため","わけ","{場合|ばあい}","ようす"],jp="{家族|かぞく}の＿に、いっしょうけんめい{働|はたら}きます。",fr="Je travaille dur pour ma famille.",uses=["v4-55"]),
 C(L,9,["ようす","{部分|ぶぶん}","ほうほう","もくてき"],jp="{田中|たなか}さんの＿がへんです。ぜんぜん{元気|げんき}がありません。",fr="M. Tanaka a l'air bizarre. Il n'a aucune énergie.",uses=["v5-19"]),
 C(L,10,["かたち","{心|こころ}","ようす","かわり"],jp="あのくもは{魚|さかな}の＿をしていますね。",fr="Ce nuage a la forme d'un poisson.",uses=["v4-63"]),
 C(L,11,["{部分|ぶぶん}","{心|こころ}","かわり","ため"],jp="この＿がよく{分|わ}かりません。もう{一度|いちど}{説明|せつめい}してください。",fr="Je ne comprends pas bien cette partie. Expliquez-la encore une fois.",uses=["v4-53"]),
 C(L,12,["かわり","けっか","{場合|ばあい}","もくてき"],jp="{父|ちち}が{病気|びょうき}でしたから、{父|ちち}の＿に{私|わたし}が{会議|かいぎ}に{出|で}ました。",fr="Mon père était malade, alors j'ai assisté à la réunion à sa place.",uses=["v4-51"]),
 C(L,13,["まちがい","まちがえる","かんけい","けっか"],jp="{作文|さくぶん}に＿がたくさんありました。{先生|せんせい}がなおしてくれました。",fr="Il y avait beaucoup de fautes dans ma rédaction. Le professeur les a corrigées.",uses=["v4-56","v5-29"]),
 C(L,14,["まちがえて","まちがい","くらべて","かわって"],jp="{電車|でんしゃ}を＿、ちがう{駅|えき}に{着|つ}いてしまいました。",fr="Je me suis trompé de train et je suis arrivé à une autre gare.",uses=["v5-15"]),
 C(L,15,["くらべる","まちがえる","かわる","ならべる"],jp="{東京|とうきょう}と{大阪|おおさか}を＿と、{東京|とうきょう}のほうが{人口|じんこう}が{多|おお}いです。",fr="Si on compare Tokyo et Osaka, Tokyo est plus peuplé.",uses=["v4-68"]),
 C(L,16,["ばあい","じょうごう","ばごう","ばあう"],q=LECT+"**場合** ?"),
 C(L,17,["{父|ちち}のかわりに","{父|ちち}のために","{父|ちち}の{場合|ばあい}","{父|ちち}とかんけいに"],q="« À la place de mon père » se dit…"),
 O(L,18,"Je me suis trompé de train et je suis arrivé à une autre gare.",["{電車|でんしゃ}を","まちがえて、","ちがう{駅|えき}に","{着|つ}きました"],uses=["v5-15"]),
]}

TC, TO, XC, XO = make_block("v4-b15")
test = [
 TC(1,["おっしゃいました","もうしました","いたしました","まいりました"],jp="{先生|せんせい}は{明日|あした}{来|こ}ないと＿。",fr="Le professeur a dit qu'il ne viendrait pas demain.",uses=["v4-71","v4-72"]),
 TC(2,["もうします","おっしゃいます","いたします","ございます"],jp="はじめまして。{山田|やまだ}と＿。",fr="Enchanté. Je m'appelle Yamada.",uses=["v4-72"]),
 TC(3,["いらっしゃいませ","おじゃまします","いってきます","ただいま"],jp="＿。こちらのせきへどうぞ。",fr="Bienvenue. Par ici, je vous prie.",uses=["v4-50","v4-71"]),
 TC(4,["もうしわけありません","おかげさまで","おめでとうございます","ようこそ"],jp="おそくなって、＿。",fr="Je suis vraiment désolé d'être en retard.",uses=["v4-73"]),
 TC(5,["けいけん","さんせい","きそく","じゆう"],jp="{外国|がいこく}に{住|す}んだ＿がありますか。",fr="Avez-vous déjà vécu à l'étranger ?",uses=["v4-74"]),
 TC(6,["まちがえて","くらべて","かわって","しらべて"],jp="{電話|でんわ}ばんごうを＿、ちがう{人|ひと}にかけてしまいました。",fr="Je me suis trompé de numéro et j'ai appelé quelqu'un d'autre.",uses=["v4-75"]),
 TC(7,["めしあがって","まいって","もうして","いたして"],jp="どうぞ、たくさん＿ください。",fr="Je vous en prie, servez-vous bien.",uses=["v4-71","v4-72"]),
 TC(8,["はいけんしました","ごらんになりました","めしあがりました","おっしゃいました"],jp="{先生|せんせい}のお{手紙|てがみ}を＿。",fr="J'ai lu votre lettre, professeur.",uses=["v4-72"]),
 TC(9,["おまたせしました","おかげさまで","おじゃまします","おかえりなさい"],q="Tu as fait attendre un client. En revenant, tu lui dis :",uses=["v4-73"]),
 TC(10,["はんたい","さんせい","{特別|とくべつ}","ふつう"],jp="その{計画|けいかく}には＿です。お{金|かね}がかかりすぎますから。",fr="Je suis contre ce projet : il coûte beaucoup trop cher.",uses=["v4-54","v4-74"]),
 TC(11,["かんがえ","こうえ","かんえ","かんがい"],q=LECT+"**考え** ?",uses=["v4-74"]),
 TC(12,["おります","いらっしゃいます","ございます","なさいます"],q="Au téléphone, tu parles de **ton** chef à un client.",jp="{部長|ぶちょう}の{田中|たなか}は{今|いま}、{会議|かいぎ}に{出|で}て＿。",fr="Notre chef, M. Tanaka, est en réunion en ce moment.",uses=["v4-71","v4-72"],explain="Devant quelqu'un d'extérieur, on parle de son propre chef avec la modestie : おります."),
 TC(13,["ため","かわり","{場合|ばあい}","けっか"],jp="{子|こ}どもの＿に、{毎朝|まいあさ}おべんとうを{作|つく}ります。",fr="Tous les matins, je prépare un bentō pour mon enfant.",uses=["v4-75"]),
 TO(14,"Je viendrai demain à dix heures.",["{明日|あした}","{十時|じゅうじ}に","まいります"],uses=["v4-72"]),
 TC(15,["Il a l'intention d'aller au Japon l'an prochain.","Il est allé au Japon l'an dernier.","Il est obligé d'aller au Japon l'an prochain.","Il ne veut pas aller au Japon."],q="Ton ami dit : {来年|らいねん}、{日本|にほん}に{行|い}くつもりです. Que veut-il dire ?",uses=["v4-74"]),
 TC(16,["けっか","もくてき","かたち","{心|こころ}"],jp="{試験|しけん}の＿はどうでしたか。— ごうかくしました！",fr="Comment se sont passés les résultats de l'examen ? — J'ai réussi !",uses=["v4-52","v4-75"]),
]
bloc = {"id": "v4-b15", "level": "N4", "title": "Politesse : keigo, formules, mots abstraits",
        "lessons": [l71, l72, l73, l74, l75], "test": test}
save_n4(bloc, sys.argv[1])
