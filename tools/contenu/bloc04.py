import json, sys
out = sys.argv[1]
def W(jp, kana, fr, ex, exFr): return dict(jp=jp, kana=kana, fr=fr, ex=ex, exFr=exFr)
def C(lid, n, choices, a=0, q=None, jp=None, fr=None, explain=None, uses=None):
    e = {"id": f"{lid}-e{n:02d}", "type": "choice"}
    if uses: e["uses"] = uses
    if q: e["q"] = q
    if jp: e["jp"] = jp
    if fr: e["fr"] = fr
    e["choices"] = choices; e["a"] = a
    if explain: e["explain"] = explain
    return e
def O(lid, n, fr, tokens, alt=None, uses=None, explain=None):
    e = {"id": f"{lid}-e{n:02d}", "type": "order"}
    if uses: e["uses"] = uses
    e["fr"] = fr; e["tokens"] = tokens
    if alt: e["alt"] = alt
    if explain: e["explain"] = explain
    return e
LECT = "Comment se lit "

# ---------- L16 L'heure et la journée ----------
L = "v5-16"
l16 = {"id": L, "title": "L'heure et la journée", "words": [
 W("〜{時|じ}","〜じ","… heure(s)","{毎朝|まいあさ}{七時|しちじ}に{起|お}きます。","Je me lève à sept heures tous les matins."),
 W("〜{分|ふん}","〜ふん","… minute(s)","{駅|えき}まで{歩|ある}いて{五分|ごふん}です。","La gare est à cinq minutes à pied."),
 W("{半|はん}","はん","et demie","{授業|じゅぎょう}は{九時半|くじはん}に{始|はじ}まります。","Le cours commence à neuf heures et demie."),
 W("{午前|ごぜん}","ごぜん","le matin (avant midi)","{銀行|ぎんこう}は{午前|ごぜん}{九時|くじ}からです。","La banque ouvre à neuf heures du matin."),
 W("{午後|ごご}","ごご","l'après-midi (après midi)","{午後|ごご}は{図書館|としょかん}で{勉強|べんきょう}します。","L'après-midi, j'étudie à la bibliothèque."),
 W("{今朝|けさ}","けさ","ce matin","{今朝|けさ}、{六時|ろくじ}に{起|お}きました。","Ce matin, je me suis levé à six heures."),
 W("{今晩|こんばん}","こんばん","ce soir","{今晩|こんばん}、{友|とも}だちと{晩|ばん}ご{飯|はん}を{食|た}べます。","Ce soir, je dîne avec un ami."),
 W("{毎朝|まいあさ}","まいあさ","tous les matins","{毎朝|まいあさ}コーヒーを{飲|の}みます。","Je bois un café tous les matins."),
 W("{毎晩|まいばん}","まいばん","tous les soirs","{毎晩|まいばん}{十一時|じゅういちじ}ごろねます。","Je me couche vers onze heures tous les soirs."),
 W("{夕方|ゆうがた}","ゆうがた","fin d'après-midi","{夕方|ゆうがた}、{公園|こうえん}をさんぽします。","En fin d'après-midi, je me promène dans le parc."),
 W("{早|はや}い","はやい","tôt ; rapide","{明日|あした}は{早|はや}く{起|お}きます。","Demain, je me lève tôt."),
 W("おそい","おそい","tard ; lent","バスはおそいですから、{電車|でんしゃ}で{行|い}きます。","Le bus est lent, alors j'y vais en train."),
 W("〜ごろ","〜ごろ","vers (… heures)","{十時|じゅうじ}ごろ{家|いえ}に{帰|かえ}ります。","Je rentre à la maison vers dix heures."),
 W("{何分|なんぷん}","なんぷん","combien de minutes ; quelle minute","{今|いま}、{何時|なんじ}{何分|なんぷん}ですか。","Quelle heure est-il, là ?"),
 W("〜{前|まえ}","〜まえ","moins (… minutes) ; il y a","{今|いま}、{九時|くじ}{五分|ごふん}{前|まえ}です。","Il est neuf heures moins cinq."),
], "sections": [
 {"h": "Lire l'heure : les lectures pièges",
  "p": ["Heures : nombre + じ. Minutes : nombre + ふん, qui devient **ぷん** après 1, 3, 4, 6, 8 et 10. Le surligné est à apprendre par cœur."],
  "grid": {"head": ["", "lecture"], "rows": [
   ["heures : 3 pièges", "4 h ==よ==じ · 7 h ==しち==じ · 9 h ==く==じ"],
   ["minutes en ぷん", "1 ==いっ==ぷん · 3 さんぷん · 4 よんぷん · 6 ==ろっ==ぷん · 8 ==はっ==ぷん · 10 ==じゅっ==ぷん · ? なんぷん"],
   ["minutes en ふん", "2 にふん · 5 ごふん · 7 ななふん · 9 きゅうふん"],
   ["et demie", "{三時半|さんじはん} = 3 h 30"]]}}
], "pieges": [
 "{四時|よじ} (pas よんじ), {七時|しちじ}, {九時|くじ} (pas きゅうじ).",
 "{分|ふん} devient **ぷん** : いっぷん, さんぷん, よんぷん, ろっぷん, はっぷん, じゅっぷん, なんぷん. 20 min = にじゅっぷん.",
 "{午前|ごぜん} / {午後|ごご} se mettent **avant** l'heure : {午後|ごご}{三時|さんじ} = 15 h.",
 "Heure précise + **に** : {七時|しちじ}に{起|お}きます. Mais pas de に après {今朝|けさ}, {今晩|こんばん}, {毎朝|まいあさ}, {毎晩|まいばん}.",
 "{十時|じゅうじ}ごろ = vers dix heures (approximatif). {十時|じゅうじ}**から** = à partir de dix heures, {十時|じゅうじ}**まで** = jusqu'à dix heures.",
 "{九時|くじ}{五分|ごふん}{前|まえ} = 9 h moins 5 (8 h 55). {前|まえ} après une durée = il y a : {三年前|さんねんまえ} = il y a trois ans.",
 "{早|はや}い = tôt **et** rapide ; おそい = tard **et** lent. Devant un verbe : {早|はや}**く**{起|お}きる, おそ**く**{帰|かえ}る.",
 "{今朝|けさ} se lit けさ (lecture spéciale) ; {今晩|こんばん} comme dans こんばんは."
], "exercises": [
 C(L,1,["よじ","よんじ","しじ","よっじ"],q=LECT+"**4時** (4 h) ?"),
 C(L,2,["くじ","きゅうじ","くうじ","ここのじ"],q=LECT+"**9時** (9 h) ?"),
 C(L,3,["ろっぷん","ろくふん","ろくぷん","むっぷん"],q=LECT+"**6分** (6 minutes) ?"),
 C(L,4,["じゅっぷん","じゅうふん","とおふん","じゅうぷん"],q=LECT+"**10分** (10 minutes) ?"),
 C(L,5,["さんぷん","さんふん","みっぷん","さっぷん"],q=LECT+"**3分** (3 minutes) ?"),
 C(L,6,["けさ","いまあさ","きょうあさ","いまさ"],q=LECT+"**今朝** (ce matin) ?"),
 C(L,7,["よじにじゅっぷん","よんじにじゅっぷん","よじにじゅうふん","しじにじゅっぷん"],q="Comment dit-on « 4 h 20 » ?"),
 C(L,8,["{午前|ごぜん}","{午後|ごご}","{今晩|こんばん}","{毎晩|まいばん}"],jp="{銀行|ぎんこう}は＿{九時|くじ}から{午後|ごご}{三時|さんじ}までです。",fr="La banque est ouverte de 9 h à 15 h.",uses=["v5-04"],explain="De 9 h **du matin** à 3 h de l'après-midi. {午後|ごご}{九時|くじ} (21 h) serait après {午後|ごご}{三時|さんじ}."),
 C(L,9,["{午後|ごご}","{今朝|けさ}","{昨日|きのう}","{毎朝|まいあさ}"],jp="{朝|あさ}は{家|いえ}で{勉強|べんきょう}して、＿は{図書館|としょかん}へ{行|い}きます。",fr="Le matin, j'étudie à la maison, et l'après-midi je vais à la bibliothèque.",uses=["v5-03","v5-04"],explain="Le matin ({朝|あさ}) est déjà pris : l'autre moment de la journée, c'est {午後|ごご}. {昨日|きのう} ne va pas avec {行|い}きます (non-passé)."),
 C(L,10,["{早|はや}く","おそく","{早|はや}い","おそい"],jp="{明日|あした}は{六時|ろくじ}の{電車|でんしゃ}に{乗|の}りますから、＿{起|お}きます。",fr="Demain je prends le train de six heures, alors je me lève tôt.",uses=["v5-15"],explain="Devant un verbe, l'adjectif en い prend く : {早|はや}く{起|お}きます."),
 C(L,11,["おそく","{早|はや}く","おそい","{早|はや}い"],jp="{今朝|けさ}は＿{起|お}きましたから、{朝|あさ}ご{飯|はん}を{食|た}べませんでした。",fr="Ce matin, je me suis levé tard, alors je n'ai pas pris de petit-déjeuner.",uses=["v5-06"]),
 C(L,12,["vers dix heures","à dix heures pile","après dix heures","jusqu'à dix heures"],q="Que veut dire {十時|じゅうじ}**ごろ** ?"),
 C(L,13,["3 h 30","3 h 50","2 h 30","3 h 05"],q="Que veut dire **{三時半|さんじはん}** ?"),
 C(L,14,["{午後|ごご}{三時|さんじ}","{午前|ごぜん}{三時|さんじ}","{三時|さんじ}{午後|ごご}","{午後|ごご}{十五時|じゅうごじ}"],q="Comment dit-on « 15 h » avec {午前|ごぜん} / {午後|ごご} ?",explain="{午後|ごご} se met avant l'heure, et on compte de 1 à 12."),
 C(L,15,["{今晩|こんばん}","{今朝|けさ}","{昨日|きのう}","{毎朝|まいあさ}"],jp="＿、{友|とも}だちと{晩|ばん}ご{飯|はん}を{食|た}べます。",fr="Ce soir, je dîne avec un ami.",uses=["v5-03","v5-06"]),
 C(L,16,["{毎晩|まいばん}","{毎朝|まいあさ}","{今朝|けさ}","{昨日|きのう}"],jp="{朝|あさ}は{六時|ろくじ}に{起|お}きて、＿は{十一時|じゅういちじ}ごろねます。",fr="Le matin je me lève à six heures, et le soir je me couche vers onze heures.",uses=["v5-02"]),
 C(L,17,["la fin de l'après-midi (vers 17-18 h)","le petit matin","midi","minuit"],q="**{夕方|ゆうがた}**, c'est…"),
 C(L,18,["{何分|なんぷん}","{何時|なんじ}","{何人|なんにん}","いくら"],jp="{駅|えき}から{学校|がっこう}まで{歩|ある}いて＿ですか。— {十五分|じゅうごふん}です。",fr="De la gare à l'école, c'est combien de minutes à pied ? — Quinze minutes.",uses=["v5-09","v5-15"]),
 C(L,19,["8 h 55","9 h 05","9 h 50","8 h 05"],q="Que veut dire {九時|くじ}{五分|ごふん}**{前|まえ}** ?"),
 O(L,20,"Je me lève à sept heures tous les matins.",["{毎朝|まいあさ}","{七時|しちじ}に","{起|お}きます"],uses=["v5-02"]),
 O(L,21,"Le cours commence à neuf heures et demie.",["{授業|じゅぎょう}は","{九時半|くじはん}に","{始|はじ}まります"],alt=[["{九時半|くじはん}に","{授業|じゅぎょう}は","{始|はじ}まります"]],uses=["v5-14"]),
 O(L,22,"Ce soir, je rentre à la maison vers dix heures.",["{今晩|こんばん}","{十時|じゅうじ}ごろ","{家|いえ}に","{帰|かえ}ります"],alt=[["{今晩|こんばん}","{家|いえ}に","{十時|じゅうじ}ごろ","{帰|かえ}ります"]],uses=["v5-02","v5-04"]),
]}

# ---------- L17 Semaine, mois, dates ----------
L = "v5-17"
l17 = {"id": L, "title": "Semaine, mois, dates", "words": [
 W("{月曜日|げつようび}","げつようび","lundi","{月曜日|げつようび}から{金曜日|きんようび}まで{働|はたら}きます。","Je travaille du lundi au vendredi."),
 W("{火曜日|かようび}","かようび","mardi","{火曜日|かようび}は{日本語|にほんご}の{授業|じゅぎょう}があります。","Le mardi, j'ai cours de japonais."),
 W("{水曜日|すいようび}","すいようび","mercredi","{水曜日|すいようび}の{午後|ごご}はひまです。","Le mercredi après-midi, je suis libre."),
 W("{木曜日|もくようび}","もくようび","jeudi","{木曜日|もくようび}に{図書館|としょかん}へ{行|い}きます。","Jeudi, je vais à la bibliothèque."),
 W("{金曜日|きんようび}","きんようび","vendredi","{金曜日|きんようび}の{夜|よる}、{友|とも}だちとお{酒|さけ}を{飲|の}みます。","Vendredi soir, je bois un verre avec des amis."),
 W("{土曜日|どようび}","どようび","samedi","{土曜日|どようび}は{家|いえ}でそうじします。","Le samedi, je fais le ménage à la maison."),
 W("{日曜日|にちようび}","にちようび","dimanche","{日曜日|にちようび}は{仕事|しごと}が{休|やす}みです。","Le dimanche, je ne travaille pas."),
 W("{何曜日|なんようび}","なんようび","quel jour (de la semaine)","{今日|きょう}は{何曜日|なんようび}ですか。— {水曜日|すいようび}です。","On est quel jour aujourd'hui ? — Mercredi."),
 W("〜{月|がつ}","〜がつ","(mois de) …","{日本|にほん}の{学校|がっこう}は{四月|しがつ}に{始|はじ}まります。","Au Japon, l'école commence en avril."),
 W("{一日|ついたち}","ついたち","le 1er (du mois)","{四月|しがつ}{一日|ついたち}から{新|あたら}しい{会社|かいしゃ}で{働|はたら}きます。","À partir du 1er avril, je travaille dans une nouvelle entreprise."),
 W("{二日|ふつか}","ふつか","le 2 (du mois) ; deux jours","{五月|ごがつ}{二日|ふつか}に{国|くに}へ{帰|かえ}ります。","Je rentre dans mon pays le 2 mai."),
 W("{二十日|はつか}","はつか","le 20 (du mois)","{今月|こんげつ}の{二十日|はつか}は{日曜日|にちようび}です。","Le 20 de ce mois tombe un dimanche."),
 W("たんじょうび","たんじょうび","anniversaire","{明日|あした}は{母|はは}のたんじょうびです。","Demain, c'est l'anniversaire de ma mère."),
 W("{週末|しゅうまつ}","しゅうまつ","week-end","{週末|しゅうまつ}は{何|なに}をしますか。","Que fais-tu ce week-end ?"),
 W("{来月|らいげつ}","らいげつ","le mois prochain","{来月|らいげつ}、{日本|にほん}へ{行|い}きます。","Le mois prochain, je vais au Japon."),
 W("{先月|せんげつ}","せんげつ","le mois dernier","{先月|せんげつ}、{新|あたら}しいカメラを{買|か}いました。","Le mois dernier, j'ai acheté un nouvel appareil photo."),
], "sections": [
 {"h": "Les jours de la semaine viennent des astres",
  "p": ["Chaque jour = un élément + {曜日|ようび}. Les kanji sont ceux que tu connais déjà :",
        "=={月|げつ}== lune → lundi · =={火|か}== feu → mardi · =={水|すい}== eau → mercredi · =={木|もく}== bois → jeudi",
        "=={金|きん}== or → vendredi · =={土|ど}== terre → samedi · =={日|にち}== soleil → dimanche"]},
 {"h": "Les dates : les jours du mois",
  "p": ["Du 1 au 10, puis le 14, le 20 et le 24 : lectures spéciales (à apprendre). Les autres : nombre + にち ({十一日|じゅういちにち}, {十五日|じゅうごにち}…)."],
  "grid": {"head": ["", "lecture"], "rows": [
   ["1 → 5", "==ついたち== · ふつか · みっか · よっか · いつか"],
   ["6 → 10", "むいか · なのか · ようか · ここのか · とおか"],
   ["14 · 20 · 24", "じゅうよっか · ==はつか== · にじゅうよっか"],
   ["les autres", "nombre + にち : じゅういちにち, じゅうごにち…"]]}},
 {"h": "Les mois : nombre + がつ",
  "p": ["Facile, sauf trois mois à retenir."],
  "grid": {"head": ["mois", "lecture"], "rows": [
   ["4 (avril)", "==し==がつ"],
   ["7 (juillet)", "==しち==がつ"],
   ["9 (septembre)", "==く==がつ"],
   ["les autres", "いちがつ, にがつ, さんがつ… じゅうにがつ"]]}}
], "pieges": [
 "{四月|しがつ}, {七月|しちがつ}, {九月|くがつ} : jamais よんがつ, きゅうがつ.",
 "{一日|ついたち} = le 1er du mois ; {一日|いちにち} = une journée. Même écriture, sens différent !",
 "Ordre japonais : mois → jour → jour de la semaine : {五月|ごがつ}{二日|ふつか}（{土曜日|どようび}）.",
 "Jour de la semaine ou date + **に** : {日曜日|にちようび}に{会|あ}います. Mais pas de に après {来月|らいげつ}, {先月|せんげつ}, {今日|きょう}, {毎日|まいにち}… (moments vus depuis aujourd'hui).",
 "〜{月|がつ} = le mois de l'année ({三月|さんがつ} = mars). Pour une durée (trois mois), on dit autre chose : {三|さん}か{月|げつ}.",
 "{来月|らいげつ} / {先月|せんげつ} (げつ) suivent le modèle de {来週|らいしゅう} / {先週|せんしゅう}. Ce mois-ci : {今月|こんげつ}.",
 "{週末|しゅうまつ} = la fin (末) de la semaine (週) : le week-end."
], "exercises": [
 C(L,1,["しがつ","よんがつ","よがつ","よつき"],q=LECT+"**4月** (avril) ?"),
 C(L,2,["くがつ","きゅうがつ","ここのがつ","くつき"],q=LECT+"**9月** (septembre) ?"),
 C(L,3,["しちがつ","しちつき","なのがつ","しつがつ"],q=LECT+"**7月** (juillet) ?"),
 C(L,4,["ついたち","いちにち","ひとひ","いちび"],q="Dans « 四月一日 » (le 1er avril), comment se lit **一日** ?",explain="Dans une date, le 1er se dit ついたち. いちにち veut dire « une journée »."),
 C(L,5,["ふつか","ににち","ふたか","ふつび"],q=LECT+"**二日** (le 2) ?"),
 C(L,6,["はつか","にじゅうにち","にじゅうか","はたか"],q=LECT+"**二十日** (le 20) ?"),
 C(L,7,["ようか","はちにち","やっか","よっか"],q=LECT+"**八日** (le 8) ?",explain="ようか = le 8 ; よっか = le 4. On les confond facilement !"),
 C(L,8,["じゅうよっか","じゅうよんにち","じゅうよにち","じゅうしにち"],q="Comment dit-on « le 14 » (du mois) ?"),
 C(L,9,["jeudi","mercredi","vendredi","mardi"],q="Que veut dire **{木曜日|もくようび}** ?"),
 C(L,10,["mardi","samedi","lundi","mercredi"],q="Que veut dire **{火曜日|かようび}** ?"),
 C(L,11,["きんようび","かねようび","きんよび","こんようび"],q=LECT+"**金曜日** ?"),
 C(L,12,["にちようび","ひようび","にちよび","じつようび"],q=LECT+"**日曜日** ?"),
 C(L,13,["{水曜日|すいようび}","{金曜日|きんようび}","{土曜日|どようび}","{日曜日|にちようび}"],jp="{月曜日|げつようび}、{火曜日|かようび}、＿、{木曜日|もくようび}、{金曜日|きんようび}",fr="Lundi, mardi, mercredi, jeudi, vendredi."),
 C(L,14,["{何曜日|なんようび}","{何時|なんじ}","{何月|なんがつ}","いくら"],jp="{今日|きょう}は＿ですか。— {金曜日|きんようび}です。",fr="On est quel jour aujourd'hui ? — Vendredi.",uses=["v5-03","v5-09"]),
 C(L,15,["{来月|らいげつ}","{先月|せんげつ}","{去年|きょねん}","{昨日|きのう}"],jp="＿、{日本|にほん}へ{行|い}きます。",fr="Le mois prochain, je vais au Japon.",uses=["v5-02","v5-03"],explain="{行|い}きます est au non-passé : il faut un moment futur."),
 C(L,16,["{先月|せんげつ}","{来月|らいげつ}","{来週|らいしゅう}","{明日|あした}"],jp="＿、{新|あたら}しいカメラを{買|か}いました。",fr="Le mois dernier, j'ai acheté un nouvel appareil photo.",uses=["v5-03","v5-12"]),
 C(L,17,["le week-end","la fin du mois","la semaine prochaine","tous les jours"],q="Que veut dire **{週末|しゅうまつ}** ?"),
 C(L,18,["たんじょうび","{週末|しゅうまつ}","{日曜日|にちようび}","{来月|らいげつ}"],jp="{明日|あした}は{父|ちち}の＿ですから、プレゼントを{買|か}います。",fr="Demain, c'est l'anniversaire de mon père, alors j'achète un cadeau."),
 C(L,19,["に","を","が","へ"],jp="{日曜日|にちようび}＿{友|とも}だちに{会|あ}います。",fr="Dimanche, je vois un ami.",uses=["v5-02"],explain="Jour de la semaine + に."),
 C(L,20,["{明日|あした}、{友|とも}だちに{会|あ}います。","{明日|あした}に{友|とも}だちに{会|あ}います。","{明日|あした}、{友|とも}だちを{会|あ}います。","{昨日|きのう}、{友|とも}だちに{会|あ}います。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-02","v5-03"],explain="Pas de に après {明日|あした} ; on « rencontre » quelqu'un avec に ; {昨日|きのう} demande le passé."),
 O(L,21,"L'anniversaire de ma mère, c'est le 20 juin.",["{母|はは}の","たんじょうびは","{六月|ろくがつ}","{二十日|はつか}","です"]),
 O(L,22,"Je travaille du lundi au vendredi.",["{月曜日|げつようび}から","{金曜日|きんようび}まで","{働|はたら}きます"],uses=["v5-14"]),
]}

# ---------- L18 Adjectifs en い ----------
L = "v5-18"
l18 = {"id": L, "title": "Adjectifs en い : goûts et impressions", "words": [
 W("おいしい","おいしい","bon (au goût), délicieux","この{店|みせ}のラーメンはとてもおいしいです。","Les ramens de ce restaurant sont délicieux."),
 W("まずい","まずい","mauvais (au goût)","この{店|みせ}のコーヒーはまずいです。","Le café de ce restaurant est mauvais."),
 W("あまい","あまい","sucré","{子|こ}どもはあまい{物|もの}が{好|す}きです。","Les enfants aiment les choses sucrées."),
 W("からい","からい","épicé, piquant","このカレーはからいですね。","Ce curry est épicé, hein."),
 W("{楽|たの}しい","たのしい","agréable, amusant (à vivre)","{旅行|りょこう}はとても{楽|たの}しかったです。","Le voyage était très agréable."),
 W("おもしろい","おもしろい","intéressant ; drôle","この{本|ほん}はおもしろいです。","Ce livre est intéressant."),
 W("つまらない","つまらない","ennuyeux","{昨日|きのう}の{映画|えいが}はつまらなかったです。","Le film d'hier était ennuyeux."),
 W("むずかしい","むずかしい","difficile","{漢字|かんじ}はむずかしいですが、おもしろいです。","Les kanji sont difficiles, mais intéressants."),
 W("やさしい","やさしい","facile ; gentil","{田中|たなか}{先生|せんせい}はやさしいです。","M. Tanaka (le professeur) est gentil."),
 W("いそがしい","いそがしい","occupé","{今週|こんしゅう}は{仕事|しごと}がいそがしいです。","Cette semaine, je suis très pris au travail."),
 W("かわいい","かわいい","mignon","かわいいねこですね。","Quel chat mignon !"),
 W("いたい","いたい","qui fait mal","{頭|あたま}がいたいです。","J'ai mal à la tête."),
 W("{若|わか}い","わかい","jeune","{先生|せんせい}はまだ{若|わか}いです。","Le professeur est encore jeune."),
 W("{強|つよ}い","つよい","fort","{今日|きょう}は{風|かぜ}が{強|つよ}いです。","Aujourd'hui, le vent est fort."),
 W("{弱|よわ}い","よわい","faible","{兄|あに}はお{酒|さけ}に{弱|よわ}いです。","Mon grand frère ne tient pas l'alcool."),
], "sections": [
 {"h": "Conjuguer un adjectif en い",
  "p": ["On change le い final. Le です reste toujours tel quel à la fin. いい est irrégulier : il passe par よ."],
  "grid": {"head": ["", "+", "−", "passé +", "passé −"], "rows": [
   ["おいしい", "おいし==い==です", "おいし==くない==です", "おいし==かった==です", "おいし==くなかった==です"],
   ["{楽|たの}しい", "{楽|たの}し==い==です", "{楽|たの}し==くない==です", "{楽|たの}し==かった==です", "{楽|たの}し==くなかった==です"],
   ["いい", "==いい==です", "==よくない==です", "==よかった==です", "==よくなかった==です"]]}}
], "pieges": [
 "Passé : おいし**かった**です. Jamais おいしいでした !",
 "やさしい = facile **et** gentil : やさしい{問題|もんだい} (un problème facile), やさしい{人|ひと} (une personne gentille).",
 "いたい : la partie du corps prend **が** : {頭|あたま}**が**いたいです = j'ai mal à la tête.",
 "{楽|たの}しい = agréable à vivre (une fête, un voyage) ; おもしろい = intéressant ou drôle (un livre, un film, une personne).",
 "お{酒|さけ}**に**{強|つよ}い = bien tenir l'alcool ; お{酒|さけ}**に**{弱|よわ}い = mal le tenir.",
 "まずい est assez direct. Plus poli : あまりおいしくないです.",
 "Devant un nom, l'adjectif en い reste tel quel : からいカレー, かわいいねこ (pas de な !)."
], "exercises": [
 C(L,1,["からい","かわいい","{若|わか}い","いそがしい"],jp="このカレーはとても＿ですから、{水|みず}をたくさん{飲|の}みました。",fr="Ce curry est très épicé, alors j'ai bu beaucoup d'eau.",uses=["v5-06"]),
 C(L,2,["あまい","からい","{若|わか}い","いたい"],jp="チョコレートはとても＿です。",fr="Le chocolat, c'est très sucré."),
 C(L,3,["{楽|たの}しかったです","{楽|たの}しいでした","{楽|たの}しかったでした","{楽|たの}しくでした"],jp="{週末|しゅうまつ}、{友|とも}だちと{海|うみ}へ{行|い}きました。とても＿。",fr="Ce week-end, je suis allé à la mer avec des amis. C'était très agréable.",uses=["v5-17"],explain="Adjectif en い au passé : い → かった, puis です."),
 C(L,4,["つまらない","むずかしい","まずい","{弱|よわ}い"],q="Contraire de **おもしろい** ?"),
 C(L,5,["{弱|よわ}い","{若|わか}い","{低|ひく}い","{短|みじか}い"],q="Contraire de **{強|つよ}い** ?",uses=["v5-05"]),
 C(L,6,["やさしい","おもしろい","いそがしい","{若|わか}い"],q="Contraire de **むずかしい** ?"),
 C(L,7,["まずい","おいしい","{安|やす}い","おもしろい"],jp="この{店|みせ}のラーメンは＿ですから、もう{行|い}きません。",fr="Les ramens de ce restaurant sont mauvais, alors je n'y retourne plus.",uses=["v5-05","v5-10"]),
 C(L,8,["いたい","いそがしい","{若|わか}い","つまらない"],jp="{頭|あたま}が＿ですから、{今日|きょう}は{会社|かいしゃ}を{休|やす}みます。",fr="J'ai mal à la tête, alors aujourd'hui je ne vais pas au travail.",uses=["v5-14"]),
 C(L,9,["いそがしい","やさしい","かわいい","あまい"],jp="{今週|こんしゅう}は{仕事|しごと}が＿ですから、{友|とも}だちに{会|あ}う{時間|じかん}がありません。",fr="Cette semaine, je suis très pris au travail, alors je n'ai pas le temps de voir mes amis.",uses=["v5-03"]),
 C(L,10,["{若|わか}い","{古|ふる}い","{強|つよ}い","{新|あたら}しい"],jp="{田中|たなか}さんは{二十二|にじゅうに}さいです。まだ＿です。",fr="M. Tanaka a vingt-deux ans. Il est encore jeune.",uses=["v5-05","v5-08"],explain="Pour l'âge d'une personne : {若|わか}い. {古|ふる}い et {新|あたら}しい sont pour les choses."),
 C(L,11,["mignon","effrayant","rapide","bruyant"],q="Que veut dire **かわいい** ?"),
 C(L,12,["{弱|よわ}い","{強|つよ}い","{若|わか}い","からい"],jp="{兄|あに}はお{酒|さけ}に＿ですから、ビールを{少|すこ}し{飲|の}んで、すぐねました。",fr="Mon grand frère ne tient pas l'alcool : il a bu un peu de bière et s'est endormi tout de suite.",uses=["v5-02","v5-10"],explain="お{酒|さけ}に{弱|よわ}い = ne pas tenir l'alcool ; お{酒|さけ}に{強|つよ}い = bien le tenir."),
 C(L,13,["おいしくないです","おいしいじゃないです","おいしないです","おいしくじゃないです"],q="Négatif poli de **おいしい** ?"),
 C(L,14,["おもしろくなかったです","おもしろいじゃなかったです","おもしろくないでした","おもしろかったじゃないです"],q="« Ce n'était pas intéressant » ?",explain="い → くなかった, puis です."),
 C(L,15,["gentil","facile","jeune","occupé"],q="Dans « {田中|たなか}{先生|せんせい}はやさしいです », やさしい veut dire…"),
 C(L,16,["やさしい","むずかしい","いたい","{若|わか}い"],jp="この{問題|もんだい}は＿です。{子|こ}どもも{分|わ}かります。",fr="Ce problème est facile. Même les enfants comprennent."),
 C(L,17,["おなかがいたいです","おなかをいたいです","おなかがいたいます","おなかにいたいです"],q="Comment dit-on « j'ai mal au ventre » ?"),
 O(L,18,"Ce curry est très épicé.",["この","カレーは","とても","からい","です"]),
 O(L,19,"Le voyage était très agréable.",["{旅行|りょこう}は","とても","{楽|たの}しかった","です"]),
 O(L,20,"Les kanji sont difficiles, mais intéressants.",["{漢字|かんじ}は","むずかしいですが、","おもしろい","です"]),
]}

# ---------- L19 Adjectifs en な ----------
L = "v5-19"
l19 = {"id": L, "title": "Adjectifs en な", "words": [
 W("{好|す}き","すき","aimer (bien)","{父|ちち}は{魚|さかな}が{好|す}きです。","Mon père aime le poisson."),
 W("きらい","きらい","ne pas aimer, détester","{子|こ}どもは{野菜|やさい}がきらいです。","Les enfants n'aiment pas les légumes."),
 W("{上手|じょうず}","じょうず","doué, habile","{田中|たなか}さんは{料理|りょうり}が{上手|じょうず}です。","Mme Tanaka cuisine très bien."),
 W("{下手|へた}","へた","maladroit, pas doué","まだ{運転|うんてん}が{下手|へた}です。","Je conduis encore mal."),
 W("{元気|げんき}","げんき","en forme","お{元気|げんき}ですか。— はい、{元気|げんき}です。","Vous allez bien ? — Oui, très bien."),
 W("{静|しず}か","しずか","calme, silencieux","{図書館|としょかん}は{静|しず}かです。","La bibliothèque est calme."),
 W("にぎやか","にぎやか","animé, vivant","{駅|えき}の{近|ちか}くはにぎやかです。","Le quartier de la gare est animé."),
 W("{有名|ゆうめい}","ゆうめい","célèbre","ここは{有名|ゆうめい}なレストランです。","C'est un restaurant célèbre."),
 W("{便利|べんり}","べんり","pratique","{駅|えき}が{近|ちか}いですから、この{家|いえ}は{便利|べんり}です。","La gare est proche, alors cette maison est pratique."),
 W("きれい","きれい","beau ; propre","きれいな{公園|こうえん}ですね。","Quel joli parc !"),
 W("{親切|しんせつ}","しんせつ","gentil, serviable","{駅|えき}の{人|ひと}はとても{親切|しんせつ}でした。","L'employé de la gare a été très serviable."),
 W("ひま","ひま","libre, pas occupé","{明日|あした}はひまですか。","Tu es libre demain ?"),
 W("{大切|たいせつ}","たいせつ","important, précieux","これは{母|はは}の{大切|たいせつ}な{写真|しゃしん}です。","C'est une photo précieuse pour ma mère."),
 W("かんたん","かんたん","simple, facile","このテストはかんたんでした。","Ce test était facile."),
 W("だいじょうぶ","だいじょうぶ","ça va, pas de problème","だいじょうぶですか。— はい、だいじょうぶです。","Ça va ? — Oui, ça va."),
], "sections": [
 {"h": "Conjuguer un adjectif en な",
  "p": ["L'adjectif en な ne bouge pas : c'est です qui se conjugue, comme après un nom. Le な n'apparaît que devant un nom."],
  "grid": {"head": ["", "devant un nom", "−", "passé +", "passé −"], "rows": [
   ["{静|しず}か", "{静|しず}か==な=={町|まち}", "{静|しず}か==じゃないです==", "{静|しず}か==でした==", "{静|しず}か==じゃなかったです=="],
   ["きれい", "きれい==な=={部屋|へや}", "きれい==じゃないです==", "きれい==でした==", "きれい==じゃなかったです=="],
   ["{好|す}き", "{好|す}き==な=={食|た}べ{物|もの}", "{好|す}き==じゃないです==", "{好|す}き==でした==", "{好|す}き==じゃなかったです=="]]}},
 {"h": "Aimer, être doué : avec が",
  "p": ["Avec {好|す}き, きらい, {上手|じょうず} et {下手|へた}, la chose aimée (ou l'activité) prend **が**, pas を : {魚|さかな}**が**{好|す}きです, {料理|りょうり}**が**{上手|じょうず}です."]}
], "pieges": [
 "すし**が**{好|す}きです. Jamais すし**を**{好|す}きです !",
 "きれい et きらい finissent par い, mais ce sont des adjectifs **な** : きれい**じゃない**, きらい**でした**.",
 "{上手|じょうず} est un compliment qu'on fait aux autres. Pour soi-même, on reste modeste : いいえ、まだまだです.",
 "{下手|へた} se lit へた (lecture spéciale).",
 "ひま = libre, pas occupé : le contraire de いそがしい.",
 "だいじょうぶです sert aussi à refuser poliment : « non merci, ça va ».",
 "Pour relier deux adjectifs en な : で. {静|しず}か**で**きれいです = c'est calme et joli."
], "exercises": [
 C(L,1,["が","を","に","で"],jp="{父|ちち}は{魚|さかな}＿{好|す}きです。",fr="Mon père aime le poisson.",uses=["v5-06"]),
 C(L,2,["すしが{好|す}きです。","すしを{好|す}きです。","すしが{好|す}きいです。","すしが{好|す}きます。"],q="Une seule de ces phrases est correcte. Laquelle ?",explain="{好|す}き est un adjectif en な, et la chose aimée prend が."),
 C(L,3,["{上手|じょうず}","{下手|へた}","きらい","ひま"],jp="{田中|たなか}さんの{料理|りょうり}はいつもおいしいです。{料理|りょうり}が＿ですね。",fr="La cuisine de Mme Tanaka est toujours délicieuse. Elle cuisine bien, hein.",uses=["v5-10","v5-14","v5-18"]),
 C(L,4,["{下手|へた}","{上手|じょうず}","{好|す}き","{有名|ゆうめい}"],jp="まだ{日本語|にほんご}が＿ですから、ゆっくり{話|はな}してください。",fr="Je parle encore mal japonais, alors parlez lentement, s'il vous plaît.",uses=["v5-02"]),
 C(L,5,["{静|しず}か","にぎやか","{便利|べんり}","{有名|ゆうめい}"],jp="{図書館|としょかん}では＿にしてください。",fr="Dans la bibliothèque, restez silencieux, s'il vous plaît.",uses=["v5-04"]),
 C(L,6,["{静|しず}か","きれい","ひま","{親切|しんせつ}"],q="Contraire de **にぎやか** ?"),
 C(L,7,["ひま","{下手|へた}","かんたん","{有名|ゆうめい}"],jp="{明日|あした}は＿ですか。いっしょに{映画|えいが}を{見|み}ませんか。",fr="Tu es libre demain ? On va voir un film ensemble ?",uses=["v5-10"]),
 C(L,8,["いそがしい","かんたん","{元気|げんき}","{静|しず}か"],q="Contraire de **ひま** ?",uses=["v5-18"]),
 C(L,9,["{有名|ゆうめい}","{静|しず}か","ひま","{下手|へた}"],jp="ここは＿な{店|みせ}ですから、いつも{人|ひと}が{多|おお}いです。",fr="C'est un restaurant célèbre, alors il y a toujours beaucoup de monde.",uses=["v5-04","v5-05"]),
 C(L,10,["{便利|べんり}","{親切|しんせつ}","{元気|げんき}","{上手|じょうず}"],jp="{駅|えき}が{近|ちか}いですから、この{家|いえ}はとても＿です。",fr="La gare est proche, alors cette maison est très pratique.",uses=["v5-04","v5-05"]),
 C(L,11,["gentil, serviable","propre","célèbre","pratique"],q="Que veut dire **{親切|しんせつ}** ?"),
 C(L,12,["{大切|たいせつ}","ひま","だいじょうぶ","いそがしい"],jp="これは{母|はは}の＿な{写真|しゃしん}です。",fr="C'est une photo précieuse pour ma mère.",uses=["v5-12"]),
 C(L,13,["きれいじゃないです","きれくないです","きれいくないです","きれいないです"],q="Négatif poli de **きれい** ?",explain="きれい est un adjectif en な (malgré son い) : じゃないです."),
 C(L,14,["きらいでした","きらかったです","きらいかったです","きらいました"],q="« Je n'aimais pas ça » : きらい au passé poli ?",explain="きらい est un adjectif en な : でした."),
 C(L,15,["きれいな","きれい","きれいの","きれいい"],jp="{駅|えき}の{近|ちか}くに＿{公園|こうえん}があります。",fr="Il y a un joli parc près de la gare.",uses=["v5-04"]),
 C(L,16,["だいじょうぶですか","お{元気|げんき}ですか","ひまですか","{好|す}きですか"],q="Quelqu'un tombe dans la rue devant toi. Que lui demandes-tu ?"),
 C(L,17,["お{元気|げんき}ですか","{有名|ゆうめい}ですか","かんたんですか","{上手|じょうず}ですか"],q="Tu revois un ami après un an. Tu lui demandes comment il va :"),
 C(L,18,["かんたん","にぎやか","{親切|しんせつ}","{元気|げんき}"],jp="この{問題|もんだい}は＿ですから、すぐ{分|わ}かりました。",fr="Ce problème est simple, alors j'ai tout de suite compris.",uses=["v5-10"]),
 C(L,19,["へた","したで","したじ","かしゅ"],q=LECT+"**下手** (pas doué) ?"),
 C(L,20,["じょうず","うえて","じょうしゅう","かみず"],q=LECT+"**上手** (doué) ?"),
 O(L,21,"Mon père aime beaucoup le poisson.",["{父|ちち}は","{魚|さかな}が","とても","{好|す}きです"],alt=[["{父|ちち}は","とても","{魚|さかな}が","{好|す}きです"]],uses=["v5-06","v5-10"]),
 O(L,22,"Ce parc est calme et joli.",["この","{公園|こうえん}は","{静|しず}かで","きれいです"],uses=["v5-04"],explain="Pour relier deux adjectifs en な : {静|しず}か**で**."),
]}

# ---------- L20 Position ----------
L = "v5-20"
l20 = {"id": L, "title": "Position et direction", "words": [
 W("{上|うえ}","うえ","sur, au-dessus","つくえの{上|うえ}に{本|ほん}があります。","Il y a un livre sur le bureau."),
 W("{下|した}","した","sous, en dessous","いすの{下|した}にねこがいます。","Il y a un chat sous la chaise."),
 W("{前|まえ}","まえ","devant ; avant","{駅|えき}の{前|まえ}で{友|とも}だちに{会|あ}います。","Je retrouve un ami devant la gare."),
 W("{後|うし}ろ","うしろ","derrière","{田中|たなか}さんは{私|わたし}の{後|うし}ろにいます。","M. Tanaka est derrière moi."),
 W("{中|なか}","なか","dedans, à l'intérieur","かばんの{中|なか}にさいふがあります。","Il y a un portefeuille dans le sac."),
 W("{外|そと}","そと","dehors, à l'extérieur","{外|そと}は{寒|さむ}いです。","Dehors, il fait froid."),
 W("{右|みぎ}","みぎ","droite","{銀行|ぎんこう}は{駅|えき}を{出|で}て{右|みぎ}です。","La banque est à droite en sortant de la gare."),
 W("{左|ひだり}","ひだり","gauche","{写真|しゃしん}の{左|ひだり}の{人|ひと}は{父|ちち}です。","La personne à gauche sur la photo, c'est mon père."),
 W("となり","となり","juste à côté","{病院|びょういん}のとなりに{銀行|ぎんこう}があります。","Il y a une banque à côté de l'hôpital."),
 W("{近|ちか}く","ちかく","les environs, près de","{家|いえ}の{近|ちか}くに{公園|こうえん}があります。","Il y a un parc près de chez moi."),
 W("{間|あいだ}","あいだ","entre","{銀行|ぎんこう}と{病院|びょういん}の{間|あいだ}に{店|みせ}があります。","Il y a un magasin entre la banque et l'hôpital."),
 W("{東|ひがし}","ひがし","est","{駅|えき}の{東|ひがし}に{大|おお}きい{公園|こうえん}があります。","À l'est de la gare, il y a un grand parc."),
 W("{西|にし}","にし","ouest","{大阪|おおさか}は{東京|とうきょう}の{西|にし}にあります。","Osaka se trouve à l'ouest de Tokyo."),
 W("{南|みなみ}","みなみ","sud","{駅|えき}の{南口|みなみぐち}で{待|ま}っています。","Je t'attends à la sortie sud de la gare."),
 W("{北|きた}","きた","nord","{北海道|ほっかいどう}は{日本|にほん}の{北|きた}にあります。","Hokkaidō se trouve au nord du Japon."),
], "sections": [
 {"h": "Dire où se trouve quelque chose",
  "p": ["On part du repère : repère **の** position **に** あります / います. つくえ**の**{上|うえ}**に** = « le dessus du bureau » = sur le bureau.",
        "あります pour les objets et les plantes, います pour les personnes et les animaux."],
  "grid": {"head": ["", "sens"], "rows": [
   ["{上|うえ} ↔ {下|した}", "sur ↔ sous"],
   ["{前|まえ} ↔ {後|うし}ろ", "devant ↔ derrière"],
   ["{中|なか} ↔ {外|そと}", "dedans ↔ dehors"],
   ["{右|みぎ} ↔ {左|ひだり}", "droite ↔ gauche"],
   ["{東|ひがし} ↔ {西|にし}", "est ↔ ouest"],
   ["{南|みなみ} ↔ {北|きた}", "sud ↔ nord"],
   ["となり · {近|ちか}く · {間|あいだ}", "juste à côté · près · entre"]]}}
], "pieges": [
 "L'ordre est inversé par rapport au français : « sur le bureau » = つくえ**の**{上|うえ} (le bureau, son dessus).",
 "あります (objets, plantes) ↔ います (personnes, animaux) : いすの{下|した}にねこが**います**.",
 "となり = juste à côté, collé ; {近|ちか}く = dans les environs, pas loin.",
 "{前|まえ} = devant (lieu) **et** avant / il y a (temps) : {駅|えき}の{前|まえ}, {三年前|さんねんまえ}.",
 "{後|うし}ろ (derrière, dans l'espace) ≠ {後|あと} (après, dans le temps) : même kanji, lectures différentes.",
 "Entre A et B : A **と** B **の**{間|あいだ}.",
 "{東京|とうきょう} = la capitale de l'**est** : dans les mots composés, {東|ひがし} se lit とう."
], "exercises": [
 C(L,1,["{下|した}","{中|なか}","{外|そと}","{後|うし}ろ"],q="Contraire de **{上|うえ}** ?"),
 C(L,2,["{後|うし}ろ","{上|うえ}","{右|みぎ}","{中|なか}"],q="Contraire de **{前|まえ}** ?"),
 C(L,3,["{左|ひだり}","{北|きた}","{外|そと}","{下|した}"],q="Contraire de **{右|みぎ}** ?"),
 C(L,4,["{外|そと}","{下|した}","{前|まえ}","となり"],q="Contraire de **{中|なか}** ?"),
 C(L,5,["{西|にし}","{南|みなみ}","{北|きた}","{左|ひだり}"],q="Contraire de **{東|ひがし}** ?"),
 C(L,6,["{南|みなみ}","{西|にし}","{東|ひがし}","{下|した}"],q="Contraire de **{北|きた}** ?"),
 C(L,7,["に","で","を","へ"],jp="つくえの{上|うえ}＿{本|ほん}があります。",fr="Il y a un livre sur le bureau.",uses=["v5-12"],explain="Lieu où une chose se trouve (あります / います) : に."),
 C(L,8,["います","あります","です","します"],jp="いすの{下|した}にねこが＿。",fr="Il y a un chat sous la chaise.",explain="Un animal : います."),
 C(L,9,["あります","います","です","{行|い}きます"],jp="{病院|びょういん}のとなりに{銀行|ぎんこう}が＿。",fr="Il y a une banque à côté de l'hôpital.",uses=["v5-04"],explain="Un bâtiment : あります."),
 C(L,10,["{外|そと}","{中|なか}","{上|うえ}","{間|あいだ}"],jp="{雨|あめ}ですから、{子|こ}どもたちは＿で{遊|あそ}びません。",fr="Il pleut, alors les enfants ne jouent pas dehors."),
 C(L,11,["{間|あいだ}","{上|うえ}","{中|なか}","{外|そと}"],jp="{銀行|ぎんこう}と{病院|びょういん}の＿に{店|みせ}があります。",fr="Il y a un magasin entre la banque et l'hôpital.",uses=["v5-04"],explain="A と B の{間|あいだ} = entre A et B."),
 C(L,12,["juste à côté","en face","derrière","loin"],q="Que veut dire **となり** ?"),
 C(L,13,["{近|ちか}く","{中|なか}","{上|うえ}","{下|した}"],jp="{家|いえ}の＿に{公園|こうえん}がありますから、{毎朝|まいあさ}さんぽします。",fr="Il y a un parc près de chez moi, alors je me promène tous les matins.",uses=["v5-04","v5-14","v5-16"]),
 C(L,14,["うしろ","あとろ","ごろ","のちろ"],q=LECT+"**後ろ** (derrière) ?"),
 C(L,15,["nord","sud","est","ouest"],q="Que veut dire **{北|きた}** ?"),
 C(L,16,["{東|ひがし}","{西|にし}","{南|みなみ}","{北|きた}"],q="Le soleil se lève à l'est. Comment dit-on « est » ?"),
 C(L,17,["il y a (trois ans)","devant","après","dans (trois ans)"],q="Dans « {三年前|さんねんまえ} », que veut dire {前|まえ} ?",uses=["v5-16"]),
 C(L,18,["{前|まえ}","{後|うし}ろ","{中|なか}","{間|あいだ}"],jp="{田中|たなか}さんはいつも{教室|きょうしつ}のいちばん＿にすわります。{先生|せんせい}の{話|はなし}がよく{聞|き}こえますから。",fr="M. Tanaka s'assoit toujours tout devant dans la classe, parce qu'il entend bien le professeur.",uses=["v5-01","v5-10"]),
 O(L,19,"Il y a un livre sur le bureau.",["つくえの","{上|うえ}に","{本|ほん}が","あります"],alt=[["{本|ほん}が","つくえの","{上|うえ}に","あります"]],uses=["v5-12"]),
 O(L,20,"Il y a une banque entre la gare et l'hôpital.",["{駅|えき}と","{病院|びょういん}の","{間|あいだ}に","{銀行|ぎんこう}が","あります"],alt=[["{銀行|ぎんこう}が","{駅|えき}と","{病院|びょういん}の","{間|あいだ}に","あります"]],uses=["v5-04"]),
 O(L,21,"M. Tanaka est derrière moi.",["{田中|たなか}さんは","{私|わたし}の","{後|うし}ろに","います"],uses=["v5-01"]),
]}

T = "v5-b04"
def TC(n, *a, **k):
    e = C("x", n, *a, **k); e["id"] = f"{T}-t{n:02d}"; return e
def TO(n, *a, **k):
    e = O("x", n, *a, **k); e["id"] = f"{T}-t{n:02d}"; return e
test = [
 TC(1,["{四月|しがつ}","{去年|きょねん}","{毎朝|まいあさ}","{先月|せんげつ}"],jp="{日本|にほん}の{学校|がっこう}は＿に{始|はじ}まります。",fr="Au Japon, l'école commence en avril.",uses=["v5-14","v5-16","v5-17"],explain="Un mois précis + に. Pas de に après {去年|きょねん}, {毎朝|まいあさ}, {先月|せんげつ} (et {去年|きょねん}, {先月|せんげつ} demanderaient le passé)."),
 TC(2,["くがつ","きゅうがつ","ここのつき","くげつ"],q=LECT+"**九月** (septembre) ?",uses=["v5-17"]),
 TC(3,["ひまでした","ひまかったです","ひまだったでした","ひまくなかったです"],jp="{昨日|きのう}は{仕事|しごと}がありませんでした。とても＿。",fr="Hier, je n'avais pas de travail. J'étais vraiment libre.",uses=["v5-03","v5-19"]),
 TC(4,["{母|はは}はすしが{好|す}きです。","{母|はは}はすしを{好|す}きです。","{母|はは}はすしが{好|す}きいです。","{母|はは}はすしが{好|す}くです。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-19"]),
 TC(5,["よじはん","よんじはん","しじはん","よじなかば"],q="Comment dit-on « 4 h 30 » ?",uses=["v5-16"]),
 TC(6,["います","あります","です","ます"],jp="{木|き}の{下|した}に{犬|いぬ}が＿。",fr="Il y a un chien sous l'arbre.",uses=["v5-20"]),
 TC(7,["{早|はや}く","おそく","{早|はや}い","おそい"],jp="{明日|あした}は{朝|あさ}{六時|ろくじ}の{飛行機|ひこうき}に{乗|の}りますから、{今晩|こんばん}は＿ねます。",fr="Demain je prends l'avion de six heures du matin, alors ce soir je me couche tôt.",uses=["v5-15","v5-16"]),
 TC(8,["からい","かわいい","{静|しず}か","ひま"],jp="このカレーはとても＿ですから、{水|みず}をたくさん{飲|の}みます。",fr="Ce curry est très épicé, alors je bois beaucoup d'eau.",uses=["v5-06","v5-18"]),
 TC(9,["{上手|じょうず}","{下手|へた}","きらい","ひま"],jp="{兄|あに}は{毎週|まいしゅう}テニスをしますから、テニスが＿です。",fr="Mon grand frère joue au tennis toutes les semaines, alors il est doué.",uses=["v5-19"]),
 TC(10,["いつか","ごにち","ごか","いっか"],q="Dans « 五月五日 » (le 5 mai), comment se lit **五日** ?",uses=["v5-17"]),
 TC(11,["Sortez de la gare et allez à droite.","Entrez dans la gare et allez à droite.","Sortez de la gare et allez à gauche.","Allez à droite de la gare, puis entrez."],q="Que veut dire : {駅|えき}を{出|で}て、{右|みぎ}に{行|い}ってください。",uses=["v5-14","v5-20"]),
 TC(12,["{何曜日|なんようび}","{何時|なんじ}","{何分|なんぷん}","{何人|なんにん}"],jp="{明日|あした}は＿ですか。— {土曜日|どようび}です。",fr="Demain, c'est quel jour ? — Samedi.",uses=["v5-09","v5-17"]),
 TC(13,["この{部屋|へや}はきれいじゃないです。","この{部屋|へや}はきれくないです。","この{部屋|へや}はきれいくないです。","この{部屋|へや}はきれいないです。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-04","v5-19"]),
 TO(14,"Je me lève à six heures et demie tous les matins.",["{毎朝|まいあさ}","{六時半|ろくじはん}に","{起|お}きます"],uses=["v5-02","v5-16"]),
 TC(15,["{今朝|けさ}","{明日|あした}","{来週|らいしゅう}","{今晩|こんばん}"],jp="＿、{七時|しちじ}に{起|お}きました。",fr="Ce matin, je me suis levé à sept heures.",uses=["v5-02","v5-03","v5-16"]),
 TC(16,["きらい","{下手|へた}","ひま","いたい"],q="Contraire de **{好|す}き** ?",uses=["v5-19"]),
]

X = "v5-x02"
def XC(n, *a, **k):
    e = C("x", n, *a, **k); e["id"] = f"{X}-{n:02d}"; return e
def XO(n, *a, **k):
    e = O("x", n, *a, **k); e["id"] = f"{X}-{n:02d}"; return e
exam = [
 XC(1,["{駅|えき}の{前|まえ}に{銀行|ぎんこう}があります。","{駅|えき}の{前|まえ}に{銀行|ぎんこう}がいます。","{駅|えき}の{前|まえ}で{銀行|ぎんこう}があります。","{駅|えき}の{前|まえ}を{銀行|ぎんこう}があります。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-04","v5-20"],explain="Un bâtiment : あります ; le lieu où il se trouve : に."),
 XC(2,["いたかった","いたいでした","いたかったでした","いたくて"],jp="{昨日|きのう}は{頭|あたま}が＿から、{会社|かいしゃ}を{休|やす}みました。",fr="Hier, j'avais mal à la tête, alors je ne suis pas allé au travail.",uses=["v5-03","v5-14","v5-18"]),
 XC(3,["にちようびのしちじじゅっぷん","ひようびのしちじじゅっぷん","にちようびのしちじじゅうふん","にちようびのしつじじゅっぷん"],q="Comment se lit **日曜日の七時十分** ?",uses=["v5-16","v5-17"]),
 XC(4,["{静|しず}か","にぎやか","{有名|ゆうめい}","ひま"],jp="{図書館|としょかん}は＿ですから、よく{勉強|べんきょう}できます。",fr="La bibliothèque est calme, alors on peut bien y étudier.",uses=["v5-04","v5-14","v5-19"]),
 XC(5,["Tous les soirs, j'étudie à la bibliothèque jusque vers 22 h.","Tous les matins, j'étudie à la bibliothèque jusque vers 10 h.","Ce soir, j'étudie à la bibliothèque à partir de 22 h.","Tous les soirs, je vais à la bibliothèque vers 22 h."],q="Que veut dire : {毎晩|まいばん}{十時|じゅうじ}ごろまで{図書館|としょかん}で{勉強|べんきょう}します。",uses=["v5-04","v5-14","v5-16"]),
 XC(6,["{静|しず}か","にぎやか","{静|しず}かい","{静|しず}かった"],jp="この{町|まち}は{前|まえ}は＿でしたが、{今|いま}はにぎやかです。",fr="Avant, cette ville était calme, mais maintenant elle est animée.",uses=["v5-03","v5-04","v5-19","v5-20"]),
 XC(7,["よかったです","いかったです","いいでした","よいでした"],jp="{週末|しゅうまつ}は{天気|てんき}が＿。",fr="Ce week-end, il a fait beau.",uses=["v5-05","v5-17"],explain="いい passe par よ : よかったです."),
 XO(8,"Il y a un chat sous la chaise de la chambre.",["{部屋|へや}の","いすの","{下|した}に","ねこが","います"],alt=[["ねこが","{部屋|へや}の","いすの","{下|した}に","います"]],uses=["v5-04","v5-20"]),
 XC(9,["いいえ、まだまだです。","はい、{上手|じょうず}です。","はい、{有名|ゆうめい}です。","いいえ、{下手|へた}じゃないです。"],q="Un Japonais te dit : « {日本語|にほんご}が{上手|じょうず}ですね ». Que réponds-tu, en restant modeste ?",uses=["v5-19"]),
 XC(10,["1 h 30","1 h","2 h 30","30 minutes"],q="{授業|じゅぎょう}は{九時|くじ}に{始|はじ}まって、{十時半|じゅうじはん}に{終|お}わります。Combien de temps dure le cours ?",uses=["v5-14","v5-16"]),
 XC(11,["{先月|せんげつ}、{京都|きょうと}へ{行|い}きました。","{来月|らいげつ}、{京都|きょうと}へ{行|い}きました。","{先月|せんげつ}、{京都|きょうと}を{行|い}きました。","{先月|せんげつ}、{京都|きょうと}へ{行|い}きます。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-02","v5-17"]),
 XC(12,["{西|にし}","{東|ひがし}","{南|みなみ}","{北|きた}"],jp="{公園|こうえん}は{学校|がっこう}の{東|ひがし}にあります。では、{学校|がっこう}は{公園|こうえん}の＿にあります。",fr="Le parc est à l'est de l'école. Donc l'école est à l'ouest du parc.",uses=["v5-04","v5-20"]),
 XC(13,["{下|した}","{上|うえ}","{中|なか}","{外|そと}"],jp="{本|ほん}はかばんの{上|うえ}にあります。では、かばんは{本|ほん}の＿にあります。",fr="Le livre est sur le sac. Donc le sac est sous le livre.",uses=["v5-12","v5-20"]),
 XC(14,["{四月|しがつ}{一日|ついたち}","{三月|さんがつ}{一日|ついたち}","{四月|しがつ}{二日|ふつか}","{三月|さんがつ}{三十日|さんじゅうにち}"],jp="{今日|きょう}は{三月|さんがつ}{三十一日|さんじゅういちにち}です。{明日|あした}は＿です。",fr="Aujourd'hui, nous sommes le 31 mars. Demain, c'est le 1er avril.",uses=["v5-03","v5-17"]),
 XC(15,["10 minutes","50 minutes","1 h 10","5 minutes"],q="{今|いま}、{八時|はちじ}{五十分|ごじゅっぷん}です。{九時|くじ}の{電車|でんしゃ}に{乗|の}ります。Il reste combien de temps avant le train ?",uses=["v5-15","v5-16"]),
]
bloc = {"id": T, "level": "N5", "title": "Le temps et la description : heure, dates, adjectifs, positions",
        "lessons": [l16, l17, l18, l19, l20], "test": test, "examTest": exam}
json.dump(bloc, open(out, "w"), ensure_ascii=False)
print("ok", sum(len(l["exercises"]) for l in bloc["lessons"]), "exercices de leçon,", len(test), "de test,", len(exam), "d'examen")
