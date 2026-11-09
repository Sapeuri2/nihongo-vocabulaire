import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save

# ---------- L31 Loisirs et sport ----------
L = "v5-31"
l31 = {"id": L, "title": "Loisirs et sport", "words": [
 W("{映画|えいが}","えいが","film, cinéma","{週末|しゅうまつ}は{映画|えいが}を{見|み}に{行|い}きます。","Ce week-end, je vais voir un film."),
 W("{音楽|おんがく}","おんがく","musique","{毎晩|まいばん}{音楽|おんがく}を{聞|き}きます。","J'écoute de la musique tous les soirs."),
 W("{歌|うた}","うた","chanson","この{歌|うた}を{知|し}っていますか。","Tu connais cette chanson ?"),
 W("{歌|うた}う","うたう","chanter","カラオケで{歌|うた}を{歌|うた}いました。","J'ai chanté au karaoké."),
 W("スポーツ","スポーツ","sport","どんなスポーツが{好|す}きですか。","Quel sport aimes-tu ?"),
 W("{泳|およ}ぐ","およぐ","nager","{夏|なつ}は{海|うみ}で{泳|およ}ぎます。","En été, je nage à la mer."),
 W("{遊|あそ}ぶ","あそぶ","jouer, s'amuser","{子|こ}どもたちは{公園|こうえん}で{遊|あそ}んでいます。","Les enfants jouent au parc."),
 W("ひく","ひく","jouer (d'un instrument)","{妹|いもうと}はピアノをひきます。","Ma petite sœur joue du piano."),
 W("テニス","テニス","tennis","{日曜日|にちようび}に{友|とも}だちとテニスをします。","Dimanche, je joue au tennis avec un ami."),
 W("サッカー","サッカー","football","{弟|おとうと}はサッカーが{上手|じょうず}です。","Mon petit frère joue bien au foot."),
 W("ゲーム","ゲーム","jeu (vidéo)","{子|こ}どもはゲームが{大好|だいす}きです。","Les enfants adorent les jeux vidéo."),
 W("パーティー","パーティー","fête, soirée","{金曜日|きんようび}にパーティーがあります。","Il y a une fête vendredi."),
 W("コンサート","コンサート","concert","{昨日|きのう}のコンサートはとても{楽|たの}しかったです。","Le concert d'hier était très agréable."),
 W("ピアノ","ピアノ","piano","ピアノを{習|なら}っています。","Je prends des cours de piano."),
 W("ギター","ギター","guitare","{兄|あに}はギターが{上手|じょうず}です。","Mon grand frère joue bien de la guitare."),
], "sections": [
 {"h": "« Jouer » : quel verbe ?",
  "p": ["Le français dit « jouer » pour tout. Le japonais choisit selon l'activité."],
  "grid": {"head": ["", "verbe"], "rows": [
   ["スポーツ, テニス, サッカー, ゲーム", "==する=="],
   ["ピアノ, ギター", "==ひく=="],
   ["{子|こ}どもが… ; s'amuser", "=={遊|あそ}ぶ=="],
   ["{歌|うた}", "=={歌|うた}う=="],
   ["{映画|えいが} · {音楽|おんがく}", "=={見|み}る== · =={聞|き}く=="]]}}
], "pieges": [
 "テニスを**する**, ピアノを**ひく**, {子|こ}どもが**{遊|あそ}ぶ** : trois façons de dire « jouer ».",
 "{遊|あそ}ぶ = s'amuser, jouer (enfants), sortir avec des amis. Jamais pour un sport ou un instrument.",
 "ひく (un instrument) ≠ {引|ひ}く (tirer) ≠ かぜをひく (attraper un rhume) : même son !",
 "Formes て : {泳|およ}ぐ → {泳|およ}**いで** ; {遊|あそ}ぶ → {遊|あそ}**んで** ; {歌|うた}う → {歌|うた}**って**.",
 "Pour dire le but d'un déplacement : radical + に{行|い}く → {映画|えいが}を{見|み}**に**{行|い}く.",
 "{大好|だいす}き = adorer."
], "exercises": [
 C(L,1,["ひきます","{遊|あそ}びます","{歌|うた}います","{泳|およ}ぎます"],jp="{妹|いもうと}は{毎日|まいにち}ピアノを＿。",fr="Ma petite sœur joue du piano tous les jours.",uses=["v5-21"]),
 C(L,2,["します","ひきます","{遊|あそ}びます","{歌|うた}います"],jp="{日曜日|にちようび}に{友|とも}だちとテニスを＿。",fr="Dimanche, je joue au tennis avec un ami.",uses=["v5-17"]),
 C(L,3,["{遊|あそ}んで","ひいて","{泳|およ}いで","しめて"],jp="{子|こ}どもたちは{公園|こうえん}で＿います。",fr="Les enfants jouent au parc.",uses=["v5-04"]),
 C(L,4,["{泳|およ}ぎます","ひきます","{引|ひ}きます","{借|か}ります"],jp="{夏|なつ}は{海|うみ}で＿。",fr="En été, je nage à la mer.",uses=["v5-25"]),
 C(L,5,["{歌|うた}いました","ひきました","しました","{泳|およ}ぎました"],jp="カラオケで{歌|うた}を＿。",fr="J'ai chanté au karaoké."),
 C(L,6,["{聞|き}きます","{見|み}ます","{歌|うた}います","ひきます"],jp="{毎晩|まいばん}{音楽|おんがく}を＿。",fr="J'écoute de la musique tous les soirs.",uses=["v5-02","v5-16"]),
 C(L,7,["{行|い}きます","{見|み}ます","します","{遊|あそ}びます"],jp="{週末|しゅうまつ}は{映画|えいが}を{見|み}に＿。",fr="Ce week-end, je vais voir un film.",uses=["v5-02","v5-17"],explain="Radical + に{行|い}く : aller faire quelque chose."),
 C(L,8,["{泳|およ}いで","{泳|およ}いて","{泳|およ}んで","{泳|およ}って"],q="Forme て de **{泳|およ}ぐ** ?",uses=["v5-02"],explain="ぐ → いで."),
 C(L,9,["{遊|あそ}んで","{遊|あそ}って","{遊|あそ}いで","{遊|あそ}びて"],q="Forme て de **{遊|あそ}ぶ** ?",uses=["v5-02"],explain="ぶ → んで."),
 C(L,10,["おんがく","おとがく","おんらく","いんがく"],q=LECT+"**音楽** ?"),
 C(L,11,["えいが","えいかく","はいが","えが"],q=LECT+"**映画** ?"),
 C(L,12,["スポーツ","{音楽|おんがく}","{映画|えいが}","{歌|うた}"],jp="どんな＿が{好|す}きですか。— サッカーです。",fr="Quel sport aimes-tu ? — Le foot.",uses=["v5-09","v5-19"]),
 C(L,13,["パーティー","サッカー","ピアノ","{音楽|おんがく}"],jp="{金曜日|きんようび}に{友|とも}だちのうちで＿があります。{二十人|にじゅうにん}ぐらい{来|き}ます。",fr="Vendredi, il y a une fête chez un ami. Une vingtaine de personnes viennent.",uses=["v5-17","v5-22"]),
 C(L,14,["jouer, s'amuser","chanter","nager","danser"],q="Que veut dire **{遊|あそ}ぶ** ?"),
 C(L,15,["{好|す}きです","{好|す}きいです","{好|す}くです","{好|す}きなです"],jp="{弟|おとうと}はサッカーが＿。",fr="Mon petit frère aime le foot.",uses=["v5-19"]),
 C(L,16,["jouer (d'un instrument)","tirer","attraper","acheter"],q="Dans « ギターをひきます », ひく veut dire…"),
 C(L,17,["コンサート","テニス","ゲーム","サッカー"],jp="{昨日|きのう}の＿はとても{楽|たの}しかったです。{有名|ゆうめい}な{歌手|かしゅ}が{歌|うた}いました。",fr="Le concert d'hier était très agréable. Un chanteur célèbre a chanté.",uses=["v5-18","v5-30"]),
 O(L,18,"Je vais voir un film avec un ami.",["{友|とも}だちと","{映画|えいが}を","{見|み}に","{行|い}きます"],alt=[["{映画|えいが}を","{見|み}に","{友|とも}だちと","{行|い}きます"]],uses=["v5-01","v5-02"]),
 O(L,19,"Mon grand frère joue bien de la guitare.",["{兄|あに}は","ギターが","{上手|じょうず}です"],uses=["v5-19","v5-21"]),
]}

# ---------- L32 En ville (2) ----------
L = "v5-32"
l32 = {"id": L, "title": "En ville : boutiques et chemin", "words": [
 W("{本屋|ほんや}","ほんや","librairie","{駅|えき}の{前|まえ}の{本屋|ほんや}でじしょを{買|か}いました。","J'ai acheté un dictionnaire à la librairie devant la gare."),
 W("きっさてん","きっさてん","café (l'établissement)","きっさてんでコーヒーを{飲|の}みましょう。","Allons boire un café dans un café."),
 W("{映画館|えいがかん}","えいがかん","cinéma (la salle)","{日曜日|にちようび}の{映画館|えいがかん}は{人|ひと}が{多|おお}いです。","Le dimanche, il y a beaucoup de monde au cinéma."),
 W("デパート","デパート","grand magasin","デパートでくつを{買|か}いました。","J'ai acheté des chaussures au grand magasin."),
 W("スーパー","スーパー","supermarché","スーパーで{野菜|やさい}を{買|か}います。","J'achète des légumes au supermarché."),
 W("{入口|いりぐち}","いりぐち","entrée","{入口|いりぐち}はあちらです。","L'entrée est par là."),
 W("{出口|でぐち}","でぐち","sortie","すみません、{出口|でぐち}はどこですか。","Excusez-moi, où est la sortie ?"),
 W("かど","かど","coin (de rue)","つぎのかどを{右|みぎ}にまがってください。","Tournez à droite au prochain coin."),
 W("はし","はし","pont","はしをわたって、まっすぐ{行|い}ってください。","Traversez le pont et allez tout droit."),
 W("こうばん","こうばん","poste de police (de quartier)","{駅|えき}の{前|まえ}にこうばんがあります。","Il y a un poste de police devant la gare."),
 W("ゆうびんきょく","ゆうびんきょく","bureau de poste","ゆうびんきょくで{手紙|てがみ}を{出|だ}しました。","J'ai posté une lettre au bureau de poste."),
 W("{花屋|はなや}","はなや","fleuriste","{花屋|はなや}で{母|はは}に{花|はな}を{買|か}いました。","J'ai acheté des fleurs pour ma mère chez le fleuriste."),
 W("まがる","まがる","tourner","あのかどを{左|ひだり}にまがってください。","Tournez à gauche à ce coin-là."),
 W("わたる","わたる","traverser","{道|みち}をわたるときは、{車|くるま}に{気|き}をつけてください。","Quand vous traversez la rue, faites attention aux voitures."),
 W("まっすぐ","まっすぐ","tout droit","この{道|みち}をまっすぐ{行|い}ってください。","Allez tout droit dans cette rue."),
], "sections": [
 {"h": "Indiquer le chemin",
  "p": ["Le lieu qu'on traverse ou au coin duquel on tourne prend **を** ; la direction prend **に**."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["tout droit", "まっすぐ{行|い}く"],
   ["tourner au coin", "かど==を=={右|みぎ}==に==まがる"],
   ["traverser", "はし==を==わたる · {道|みち}==を==わたる"],
   ["boutique de…", "〜{屋|や} : {本屋|ほんや}, {花屋|はなや}, パン{屋|や}"]]}}
], "pieges": [
 "かど**を**まがる, はし**を**わたる : le lieu parcouru prend を. La direction : {右|みぎ}**に**まがる.",
 "〜{屋|や} = boutique de… : {本屋|ほんや} (librairie), {花屋|はなや} (fleuriste), パン{屋|や} (boulangerie).",
 "はし (pont) a le même son que おはし (baguettes) : c'est le contexte qui décide.",
 "{入口|いりぐち}, {出口|でぐち} : くち (bouche, ouverture) devient **ぐ**ち.",
 "こうばん = petit poste de police de quartier, avec ses おまわりさん. Parfait pour demander son chemin.",
 "デパート = grand magasin ; スーパー = supermarché ; きっさてん = café à l'ancienne."
], "exercises": [
 C(L,1,["{本屋|ほんや}","{花屋|はなや}","きっさてん","こうばん"],jp="じしょを{買|か}いたいですから、＿へ{行|い}きます。",fr="Je veux acheter un dictionnaire, alors je vais à la librairie.",uses=["v5-12"]),
 C(L,2,["きっさてん","こうばん","ゆうびんきょく","{花屋|はなや}"],jp="ちょっとつかれましたね。＿でコーヒーを{飲|の}みましょう。",fr="On est un peu fatigués. Allons boire un café dans un café."),
 C(L,3,["ゆうびんきょく","{映画館|えいがかん}","{花屋|はなや}","きっさてん"],jp="{国|くに}に{手紙|てがみ}を{送|おく}りますから、＿へ{行|い}きます。",fr="J'envoie une lettre dans mon pays, alors je vais à la poste.",uses=["v5-12","v5-26"]),
 C(L,4,["を","が","へ","と"],jp="つぎのかど＿{右|みぎ}にまがってください。",fr="Tournez à droite au prochain coin.",explain="Le coin qu'on « passe » en tournant : を."),
 C(L,5,["に","を","が","で"],jp="あのかどを{左|ひだり}＿まがってください。",fr="Tournez à gauche à ce coin-là.",uses=["v5-20"],explain="La direction : に."),
 C(L,6,["を","に","が","で"],jp="はし＿わたって、まっすぐ{行|い}ってください。",fr="Traversez le pont et allez tout droit."),
 C(L,7,["まっすぐ","となり","{近|ちか}く","{間|あいだ}"],jp="この{道|みち}を＿{行|い}ってください。{三分|さんぷん}ぐらいで{駅|えき}です。",fr="Allez tout droit dans cette rue. La gare est à trois minutes environ.",uses=["v5-16","v5-20"]),
 C(L,8,["des agents de police","des livres","des fleurs","des timbres"],q="Qui ou que trouve-t-on dans une **こうばん** ?",uses=["v5-30"]),
 C(L,9,["{花屋|はなや}","{本屋|ほんや}","こうばん","{映画館|えいがかん}"],jp="{母|はは}のたんじょうびですから、＿で{花|はな}を{買|か}います。",fr="C'est l'anniversaire de ma mère, alors j'achète des fleurs chez le fleuriste.",uses=["v5-17","v5-21"]),
 C(L,10,["えいがかん","えいかかん","えがかん","えいがやかた"],q=LECT+"**映画館** ?"),
 C(L,11,["いりぐち","はいりぐち","いりくち","にゅうこう"],q=LECT+"**入口** ?"),
 C(L,12,["{出口|でぐち}","{外|そと}","{後|うし}ろ","かど"],q="Contraire de **{入口|いりぐち}** ?"),
 C(L,13,["スーパー","こうばん","{映画館|えいがかん}","はし"],jp="＿で{野菜|やさい}や{肉|にく}を{買|か}います。",fr="J'achète des légumes et de la viande au supermarché.",uses=["v5-06"]),
 C(L,14,["grand magasin","supermarché","marché","appartement"],q="Que veut dire **デパート** ?"),
 C(L,15,["わたる","{泳|およ}ぐ","{借|か}りる","{売|う}る"],jp="{道|みち}を＿ときは、{車|くるま}に{気|き}をつけてください。",fr="Quand vous traversez la rue, faites attention aux voitures.",uses=["v5-15","v5-23"]),
 C(L,16,["boutique (qui vend…)","maison","usine","école"],q="Que veut dire le suffixe **〜{屋|や}** dans {本屋|ほんや}, {花屋|はなや} ?"),
 C(L,17,["un pont","des baguettes","un coin de rue","une rue"],q="Dans « はしをわたります », はし veut dire…"),
 O(L,18,"Tournez à droite au prochain coin.",["つぎの","かどを","{右|みぎ}に","まがってください"],uses=["v5-20"]),
 O(L,19,"Traversez le pont et allez tout droit.",["はしを","わたって","まっすぐ","{行|い}ってください"],uses=["v5-02"]),
]}

# ---------- L33 Voyages, pays, langues ----------
L = "v5-33"
l33 = {"id": L, "title": "Voyages, pays, langues", "words": [
 W("{旅行|りょこう}","りょこう","voyage","{来月|らいげつ}、{京都|きょうと}へ{旅行|りょこう}に{行|い}きます。","Le mois prochain, je pars en voyage à Kyoto."),
 W("{外国|がいこく}","がいこく","étranger (pays)","{外国|がいこく}で{働|はたら}きたいです。","Je veux travailler à l'étranger."),
 W("〜{語|ご}","〜ご","langue …","{田中|たなか}さんはフランス{語|ご}が{上手|じょうず}です。","M. Tanaka parle bien français."),
 W("〜{人|じん}","〜じん","(nationalité) …","マリーさんはフランス{人|じん}です。","Marie est française."),
 W("ホテル","ホテル","hôtel","{駅|えき}の{近|ちか}くのホテルにとまります。","Je loge dans un hôtel près de la gare."),
 W("パスポート","パスポート","passeport","パスポートを{持|も}っていますか。","Tu as ton passeport ?"),
 W("{英語|えいご}","えいご","anglais","{英語|えいご}で{話|はな}してもいいですか。","Je peux parler en anglais ?"),
 W("にもつ","にもつ","bagages","にもつが{重|おも}いですから、タクシーで{行|い}きます。","Mes bagages sont lourds, alors j'y vais en taxi."),
 W("{住所|じゅうしょ}","じゅうしょ","adresse","ここに{住所|じゅうしょ}と{名前|なまえ}を{書|か}いてください。","Écrivez ici votre adresse et votre nom."),
 W("ばんごう","ばんごう","numéro","{電話|でんわ}ばんごうを{教|おし}えてください。","Donnez-moi votre numéro de téléphone."),
 W("{大使館|たいしかん}","たいしかん","ambassade","フランス{大使館|たいしかん}はどこですか。","Où est l'ambassade de France ?"),
 W("{何語|なにご}","なにご","quelle langue","メキシコでは{何語|なにご}を{話|はな}しますか。","Quelle langue parle-t-on au Mexique ?"),
 W("はじめて","はじめて","pour la première fois","はじめて{日本|にほん}へ{来|き}ました。","C'est la première fois que je viens au Japon."),
], "sections": [
 {"h": "Pays, langue, nationalité",
  "p": ["Pays + {語|ご} = la langue ; pays + {人|じん} = la nationalité."],
  "grid": {"head": ["", "exemples"], "rows": [
   ["pays", "フランス, {日本|にほん}, {中国|ちゅうごく}"],
   ["+ {語|ご} (langue)", "フランス=={語|ご}==, {日本|にほん}=={語|ご}==, {中国|ちゅうごく}=={語|ご}=="],
   ["+ {人|じん} (nationalité)", "フランス=={人|じん}==, {日本|にほん}=={人|じん}==, {中国|ちゅうごく}=={人|じん}=="],
   ["exception", "anglais = =={英語|えいご}== (pas イギリス{語|ご})"]]}}
], "pieges": [
 "〜{人|じん} (nationalité) ≠ 〜{人|にん} (compteur) : フランス{人|じん}が{三人|さんにん}います.",
 "L'anglais se dit {英語|えいご}, jamais イギリス{語|ご}.",
 "{旅行|りょこう}**に**{行|い}く = partir en voyage (ou {旅行|りょこう}する).",
 "{何語|なにご} = quelle langue ; {何人|なにじん} = quelle nationalité ; {何人|なんにん} = combien de personnes.",
 "はじめて = pour la première fois. はじめまして (enchanté) vient du même mot.",
 "ホテルに**とまる** = loger à l'hôtel."
], "exercises": [
 C(L,1,["{人|じん}","{語|ご}","{国|くに}","{円|えん}"],jp="マリーさんはフランス＿です。",fr="Marie est française.",uses=["v5-01"]),
 C(L,2,["{語|ご}","{人|じん}","{国|くに}","{円|えん}"],jp="{田中|たなか}さんはフランス＿が{上手|じょうず}です。{毎日|まいにち}フランスのニュースを{聞|き}いています。",fr="M. Tanaka parle bien français. Il écoute les informations françaises tous les jours.",uses=["v5-19","v5-28"]),
 C(L,3,["{英語|えいご}","イギリス{語|ご}","アメリカ{語|ご}","{英人|えいじん}"],q="Comment dit-on « anglais » (la langue) ?"),
 C(L,4,["{旅行|りょこう}","{外国|がいこく}","ホテル","パスポート"],jp="{来月|らいげつ}、{家族|かぞく}と{京都|きょうと}へ＿に{行|い}きます。",fr="Le mois prochain, je pars en voyage à Kyoto avec ma famille.",uses=["v5-17","v5-21"]),
 C(L,5,["パスポート","{住所|じゅうしょ}","ばんごう","{大使館|たいしかん}"],jp="{外国|がいこく}へ{行|い}きますから、＿を{持|も}って{行|い}きます。",fr="Je pars à l'étranger, alors j'emporte mon passeport.",uses=["v5-26"]),
 C(L,6,["にもつ","パスポート","{住所|じゅうしょ}","{英語|えいご}"],jp="＿が{重|おも}いですから、タクシーで{行|い}きます。",fr="Mes bagages sont lourds, alors j'y vais en taxi.",uses=["v5-15","v5-24"]),
 C(L,7,["{住所|じゅうしょ}","にもつ","ホテル","パスポート"],jp="ここに{名前|なまえ}と＿を{書|か}いてください。{手紙|てがみ}を{送|おく}りますから。",fr="Écrivez ici votre nom et votre adresse : nous vous enverrons une lettre.",uses=["v5-26"]),
 C(L,8,["{何語|なにご}","{何人|なんにん}","どこ","いつ"],jp="メキシコでは＿を{話|はな}しますか。— スペイン{語|ご}です。",fr="Quelle langue parle-t-on au Mexique ? — L'espagnol.",uses=["v5-09"]),
 C(L,9,["はじめて","はじめまして","いつも","まだ"],jp="＿{日本|にほん}へ{来|き}ました。{日本|にほん}はとてもきれいですね。",fr="C'est la première fois que je viens au Japon. Le Japon est très beau, hein.",uses=["v5-19"]),
 C(L,10,["ホテル","パスポート","にもつ","{英語|えいご}"],jp="{駅|えき}の{近|ちか}くの＿にとまります。",fr="Je loge dans un hôtel près de la gare.",uses=["v5-20"]),
 C(L,11,["りょこう","たびこう","りょぎょう","りょうこう"],q=LECT+"**旅行** ?"),
 C(L,12,["じゅうしょ","すみしょ","じゅうどころ","じゅしょ"],q=LECT+"**住所** ?"),
 C(L,13,["ばんごう","{住所|じゅうしょ}","にもつ","{旅行|りょこう}"],jp="{電話|でんわ}＿を{教|おし}えてください。",fr="Donnez-moi votre numéro de téléphone, s'il vous plaît.",uses=["v5-12","v5-28"]),
 C(L,14,["ambassade","office de tourisme","mairie","aéroport"],q="Que veut dire **{大使館|たいしかん}** ?"),
 C(L,15,["イタリアへ{旅行|りょこう}に{行|い}きました。","イタリアへ{旅行|りょこう}を{行|い}きました。","イタリアへ{旅行|りょこう}が{行|い}きました。","イタリアへ{旅行|りょこう}に{行|い}きます。"],q="« Je suis parti en voyage en Italie » se dit…"),
 C(L,16,["じん、にん","にん、じん","じん、じん","ひと、にん"],q="Dans « 日本人が三人います », comment se lisent les deux 人, dans l'ordre ?",uses=["v5-08"]),
 C(L,17,["l'étranger, un pays étranger","un pays voisin","la campagne","une région"],q="Que veut dire **{外国|がいこく}** ?"),
 O(L,18,"C'est la première fois que je viens au Japon.",["はじめて","{日本|にほん}へ","{来|き}ました"],alt=[["{日本|にほん}へ","はじめて","{来|き}ました"]],uses=["v5-02"]),
 O(L,19,"Je peux parler en anglais ?",["{英語|えいご}で","{話|はな}しても","いいですか"],uses=["v5-02"]),
]}

# ---------- L34 Cuisine et table ----------
L = "v5-34"
l34 = {"id": L, "title": "À table", "words": [
 W("おさら","おさら","assiette","おさらを{洗|あら}ってください。","Lave les assiettes, s'il te plaît."),
 W("コップ","コップ","verre","コップに{水|みず}を{入|い}れます。","Je verse de l'eau dans un verre."),
 W("おはし","おはし","baguettes","{日本|にほん}ではおはしでご{飯|はん}を{食|た}べます。","Au Japon, on mange le riz avec des baguettes."),
 W("スプーン","スプーン","cuillère","スプーンでカレーを{食|た}べます。","Je mange le curry avec une cuillère."),
 W("ナイフ","ナイフ","couteau","ナイフとフォークをください。","Un couteau et une fourchette, s'il vous plaît."),
 W("フォーク","フォーク","fourchette","すみません、フォークがありますか。","Excusez-moi, vous avez une fourchette ?"),
 W("しお","しお","sel","すみません、しおをとってください。","Excusez-moi, passez-moi le sel."),
 W("さとう","さとう","sucre","このケーキはさとうが{多|おお}いです。","Ce gâteau contient beaucoup de sucre."),
 W("しょうゆ","しょうゆ","sauce soja","すしにしょうゆをつけて{食|た}べます。","Je trempe les sushis dans la sauce soja."),
 W("ちゃわん","ちゃわん","bol (à riz)","ちゃわんにご{飯|はん}を{入|い}れます。","Je mets le riz dans le bol."),
 W("おべんとう","おべんとう","bentō (repas à emporter)","{毎朝|まいあさ}おべんとうを{作|つく}ります。","Je prépare un bentō tous les matins."),
 W("メニュー","メニュー","menu, carte","メニューを{見|み}せてください。","Montrez-moi la carte, s'il vous plaît."),
 W("〜はい","〜はい","… verre(s), … tasse(s)","コーヒーを{二|に}はい{飲|の}みました。","J'ai bu deux tasses de café."),
 W("{食堂|しょくどう}","しょくどう","cantine, petit restaurant","{昼|ひる}ご{飯|はん}は{会社|かいしゃ}の{食堂|しょくどう}で{食|た}べます。","Je déjeune à la cantine de l'entreprise."),
 W("いっぱい","いっぱい","plein ; un verre","たくさん{食|た}べましたから、おなかがいっぱいです。","J'ai beaucoup mangé, je n'ai plus faim."),
], "sections": [
 {"h": "Compter les verres et les tasses : 〜はい",
  "p": ["Même rythme que 〜{本|ほん} : ぱ ou ば aux mêmes endroits."],
  "grid": {"head": ["", "lecture"], "rows": [
   ["à retenir", "1 ==いっぱい== · 3 さん==ばい== · 6 ==ろっぱい== · 8 ==はっぱい== · 10 ==じゅっぱい== · ? なん==ばい=="],
   ["les autres", "2 にはい · 4 よんはい · 5 ごはい · 7 ななはい · 9 きゅうはい"]]}}
], "pieges": [
 "いっぱい = un verre (〜はい) **et** « plein » : おなかがいっぱい = je n'ai plus faim.",
 "しょうゆを**つける** = tremper dans la sauce soja. (つける veut aussi dire allumer !)",
 "On dit おはし pour les baguettes, ce qui évite la confusion avec はし (pont).",
 "ちゃわん = bol à riz ; コップ = verre ; おさら = assiette.",
 "{食堂|しょくどう} = cantine ou petit restaurant simple ; le « restaurant » chic : レストラン."
], "exercises": [
 C(L,1,["おはし","ナイフ","コップ","しお"],jp="{日本|にほん}では＿でご{飯|はん}を{食|た}べます。",fr="Au Japon, on mange le riz avec des baguettes.",uses=["v5-06"]),
 C(L,2,["スプーン","おはし","ナイフ","フォーク"],jp="スープは＿で{飲|の}みます。",fr="La soupe se mange avec une cuillère."),
 C(L,3,["しょうゆ","さとう","ぎゅうにゅう","コップ"],jp="すしに＿をつけて{食|た}べます。",fr="Je trempe les sushis dans la sauce soja.",uses=["v5-06"]),
 C(L,4,["はい","{人|にん}","まい","{台|だい}"],jp="コーヒーを{二|に}＿{飲|の}みました。",fr="J'ai bu deux tasses de café.",uses=["v5-08"]),
 C(L,5,["いっぱい","すき","{少|すく}ない","{多|おお}い"],jp="たくさん{食|た}べましたから、おなかが＿です。",fr="J'ai beaucoup mangé, je n'ai plus faim.",uses=["v5-23"]),
 C(L,6,["いっぱい","いちはい","ひとはい","いっはい"],q="Comment dit-on « un verre » (〜はい) ?"),
 C(L,7,["さんばい","さんはい","さんぱい","みはい"],q="Comment dit-on « trois verres » (〜はい) ?"),
 C(L,8,["{食堂|しょくどう}","メニュー","しょうゆ","コップ"],jp="{昼|ひる}ご{飯|はん}は{会社|かいしゃ}の＿で{食|た}べます。",fr="Je déjeune à la cantine de l'entreprise.",uses=["v5-04","v5-06"]),
 C(L,9,["メニュー","おさら","しお","スプーン"],jp="すみません、＿をください。{何|なに}がありますか。",fr="Excusez-moi, la carte, s'il vous plaît. Qu'est-ce que vous avez ?",uses=["v5-09"]),
 C(L,10,["ちゃわん","コップ","フォーク","しょうゆ"],jp="＿にご{飯|はん}を{入|い}れます。",fr="Je mets le riz dans le bol.",uses=["v5-27"]),
 C(L,11,["さとう","しお","しょうゆ","{水|みず}"],jp="このケーキは＿がたくさん{入|はい}っていますから、とてもあまいです。",fr="Il y a beaucoup de sucre dans ce gâteau, alors il est très sucré.",uses=["v5-18"]),
 C(L,12,["おべんとう","{食堂|しょくどう}","メニュー","コップ"],jp="{毎朝|まいあさ}{子|こ}どもの＿を{作|つく}ります。{子|こ}どもは{学校|がっこう}で{食|た}べます。",fr="Tous les matins, je prépare le bentō de mon enfant. Il le mange à l'école.",uses=["v5-27"]),
 C(L,13,["plein (j'ai bien mangé)","vide (j'ai faim)","malade","un verre"],q="Dans « おなかがいっぱいです », que veut dire いっぱい ?"),
 C(L,14,["tremper (dans la sauce)","allumer","manger","acheter"],q="Dans « すしにしょうゆをつけます », que veut dire つける ?"),
 C(L,15,["フォーク","おはし","ちゃわん","コップ"],jp="ナイフと＿で{肉|にく}を{食|た}べます。",fr="Je mange la viande avec un couteau et une fourchette.",uses=["v5-06"]),
 C(L,16,["ならべます","{切|き}ります","おします","{消|け}します"],jp="{食|た}べるまえに、テーブルにおさらとおはしを＿。",fr="Avant de manger, je dispose les assiettes et les baguettes sur la table.",uses=["v5-27"]),
 C(L,17,["とって","{入|い}って","{切|き}って","{開|あ}いて"],jp="すみません、しおを＿ください。",fr="Excusez-moi, passez-moi le sel, s'il vous plaît.",uses=["v5-26"]),
 O(L,18,"Je bois deux verres d'eau.",["{水|みず}を","{二|に}はい","{飲|の}みます"],uses=["v5-06"]),
 O(L,19,"Je trempe les sushis dans la sauce soja et je les mange.",["すしに","しょうゆを","つけて","{食|た}べます"],alt=[["しょうゆを","すしに","つけて","{食|た}べます"]]),
]}

# ---------- L35 Nature et animaux ----------
L = "v5-35"
l35 = {"id": L, "title": "Nature et animaux", "words": [
 W("{山|やま}","やま","montagne","{日本|にほん}でいちばん{高|たか}い{山|やま}はふじさんです。","La plus haute montagne du Japon, c'est le mont Fuji."),
 W("{川|かわ}","かわ","rivière, fleuve","{家|いえ}の{近|ちか}くに{大|おお}きい{川|かわ}があります。","Il y a une grande rivière près de chez moi."),
 W("{海|うみ}","うみ","mer","{夏|なつ}は{海|うみ}で{泳|およ}ぎます。","En été, je nage à la mer."),
 W("{空|そら}","そら","ciel","{今日|きょう}は{空|そら}がとても{青|あお}いです。","Aujourd'hui, le ciel est très bleu."),
 W("{花|はな}","はな","fleur","にわにきれいな{花|はな}がたくさんあります。","Il y a beaucoup de jolies fleurs dans le jardin."),
 W("{木|き}","き","arbre","{公園|こうえん}に{大|おお}きい{木|き}があります。","Il y a un grand arbre dans le parc."),
 W("{犬|いぬ}","いぬ","chien","{毎朝|まいあさ}{犬|いぬ}とさんぽします。","Je promène le chien tous les matins."),
 W("ねこ","ねこ","chat","ねこがいすの{上|うえ}でねています。","Le chat dort sur la chaise."),
 W("{鳥|とり}","とり","oiseau","{木|き}の{上|うえ}に{鳥|とり}がいます。","Il y a un oiseau dans l'arbre."),
 W("{池|いけ}","いけ","étang","{公園|こうえん}の{池|いけ}に{魚|さかな}がたくさんいます。","Il y a beaucoup de poissons dans l'étang du parc."),
 W("{森|もり}","もり","forêt","{森|もり}の{中|なか}は{静|しず}かです。","Dans la forêt, c'est calme."),
 W("{動物|どうぶつ}","どうぶつ","animal","どんな{動物|どうぶつ}が{好|す}きですか。","Quel animal aimes-tu ?"),
 W("{牛|うし}","うし","vache, bœuf","{牛|うし}が{三頭|さんとう}います。","Il y a trois vaches."),
 W("ペット","ペット","animal de compagnie","ペットがいますか。","Tu as un animal de compagnie ?"),
 W("〜ひき","〜ひき","(petits animaux) …","ねこが{二|に}ひきいます。","J'ai deux chats."),
], "sections": [
 {"h": "Compter les animaux : 〜ひき",
  "p": ["Chiens, chats, poissons… : 〜ひき. Encore le même rythme que 〜{本|ほん} et 〜はい."],
  "grid": {"head": ["", "lecture"], "rows": [
   ["à retenir", "1 ==いっぴき== · 3 さん==びき== · 6 ==ろっぴき== · 8 ==はっぴき== · 10 ==じゅっぴき== · ? なん==びき=="],
   ["les autres", "2 にひき · 4 よんひき · 5 ごひき · 7 ななひき · 9 きゅうひき"]]}}
], "pieges": [
 "Animaux : **います** ; arbres et fleurs : **あります**.",
 "〜ひき : petits animaux (et souvent les oiseaux). Les gros animaux (vaches…) ont leur propre compteur.",
 "{木|き} (arbre) et {気|き} ({元気|げんき}) : même son, rien à voir.",
 "{牛|うし} (vache) se lit ぎゅう dans les composés : ぎゅうにゅう (lait), ぎゅうにく (bœuf).",
 "{森|もり} (forêt) : trois {木|き} dans le kanji !",
 "ふじさん : le さん de ふじさん est le kanji {山|やま} (montagne), pas le さん de politesse."
], "exercises": [
 C(L,1,["あります","います","です","します"],jp="{公園|こうえん}に{大|おお}きい{木|き}が＿。",fr="Il y a un grand arbre dans le parc.",uses=["v5-04","v5-20"],explain="Un arbre (une plante) : あります."),
 C(L,2,["います","あります","です","します"],jp="{池|いけ}に{魚|さかな}がたくさん＿。",fr="Il y a beaucoup de poissons dans l'étang.",uses=["v5-06","v5-10"],explain="Des poissons vivants : います."),
 C(L,3,["びき","ひき","ぴき","にん"],jp="{犬|いぬ}が{三|さん}＿います。",fr="Il y a trois chiens.",explain="さんびき (comme さんぼん, さんばい)."),
 C(L,4,["いっぴき","いちひき","ひとひき","いっひき"],q="Comment dit-on « un » (petit animal) avec 〜ひき ?"),
 C(L,5,["ろっぴき","ろくひき","ろくびき","むっぴき"],q="Comment dit-on « six » (petits animaux) avec 〜ひき ?"),
 C(L,6,["{海|うみ}","{山|やま}","{空|そら}","{森|もり}"],jp="{夏|なつ}は＿で{泳|およ}ぎます。",fr="En été, je nage à la mer.",uses=["v5-25","v5-31"]),
 C(L,7,["{山|やま}","{川|かわ}","{海|うみ}","{池|いけ}"],jp="{日本|にほん}でいちばん{高|たか}い＿はふじさんです。",fr="La plus haute montagne du Japon, c'est le mont Fuji.",uses=["v5-05"]),
 C(L,8,["{鳥|とり}","{花|はな}","{牛|うし}","{池|いけ}"],jp="{木|き}の{上|うえ}に＿がいます。",fr="Il y a un oiseau dans l'arbre.",uses=["v5-20"]),
 C(L,9,["{空|そら}","{木|き}","{森|もり}","{犬|いぬ}"],jp="{今日|きょう}は＿がとても{青|あお}いです。",fr="Aujourd'hui, le ciel est très bleu.",uses=["v5-24"]),
 C(L,10,["どうぶつ","どうもの","うごきもの","どうぶし"],q=LECT+"**動物** ?"),
 C(L,11,["とり","どり","とお","しま"],q=LECT+"**鳥** (oiseau) ?"),
 C(L,12,["forêt","montagne","rivière","étang"],q="Que veut dire **{森|もり}** ?"),
 C(L,13,["{動物|どうぶつ}","{花|はな}","{空|そら}","{山|やま}"],jp="どんな＿が{好|す}きですか。— {犬|いぬ}とねこです。",fr="Quels animaux aimes-tu ? — Les chiens et les chats.",uses=["v5-09","v5-19"]),
 C(L,14,["ペット","{花|はな}","{木|き}","{森|もり}"],jp="＿がいますか。— はい、ねこが{一|いっ}ぴきいます。",fr="Tu as un animal de compagnie ? — Oui, un chat."),
 C(L,15,["vache, bœuf","cochon","cheval","mouton"],q="Que veut dire **{牛|うし}** ?"),
 C(L,16,["{花|はな}","{犬|いぬ}","{山|やま}","{空|そら}"],jp="{花屋|はなや}で＿を{買|か}いました。",fr="J'ai acheté des fleurs chez le fleuriste.",uses=["v5-32"]),
 C(L,17,["{川|かわ}","{空|そら}","{木|き}","{鳥|とり}"],jp="この＿には{大|おお}きいはしがあります。",fr="Il y a un grand pont sur cette rivière.",uses=["v5-32"]),
 O(L,18,"Il y a deux chats dans le jardin.",["にわに","ねこが","{二|に}ひき","います"],alt=[["ねこが","にわに","{二|に}ひき","います"]],uses=["v5-22"]),
 O(L,19,"Je promène le chien tous les matins.",["{毎朝|まいあさ}","{犬|いぬ}と","さんぽします"],uses=["v5-14","v5-16"]),
]}

TC, TO, XC, XO = make_block("v5-b07")
test = [
 TC(1,["{遊|あそ}んで","ひいて","ならべて","わたって"],jp="{子|こ}どもたちは{公園|こうえん}で＿います。",fr="Les enfants jouent au parc.",uses=["v5-31"]),
 TC(2,["まがって","わたって","{泳|およ}いで","{遊|あそ}んで"],jp="つぎのかどを{右|みぎ}に＿ください。",fr="Tournez à droite au prochain coin.",uses=["v5-20","v5-32"]),
 TC(3,["マリーさんはフランス{人|じん}で、{英語|えいご}も{話|はな}します。","マリーさんはフランス{語|ご}で、{英語|えいご}も{話|はな}します。","マリーさんはフランス{人|じん}で、イギリス{語|ご}も{話|はな}します。","マリーさんはフランス{人|じん}で、{英人|えいじん}も{話|はな}します。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v5-33"]),
 TC(4,["しお","おはし","コップ","メニュー"],jp="このスープは＿が{少|すく}ないですから、あまりおいしくないです。",fr="Il n'y a pas assez de sel dans cette soupe, alors elle n'est pas très bonne.",uses=["v5-05","v5-18","v5-34"]),
 TC(5,["きっさてん","こうばん","{花屋|はなや}","ゆうびんきょく"],jp="＿でコーヒーを{一|いっ}ぱい{飲|の}みました。",fr="J'ai bu un café dans un café.",uses=["v5-32","v5-34"]),
 TC(6,["にひき","にびき","にぴき","ふたひき"],q="Comment dit-on « deux » (petits animaux) avec 〜ひき ?",uses=["v5-35"]),
 TC(7,["{泳|およ}ぐ","ひく","わたる","まがる"],jp="{夏|なつ}は{海|うみ}で＿のが{好|す}きです。",fr="En été, j'aime nager à la mer.",uses=["v5-25","v5-31","v5-35"]),
 TC(8,["ひいています","{遊|あそ}んでいます","{歌|うた}っています","{泳|およ}いでいます"],jp="{妹|いもうと}は{毎日|まいにち}ピアノを＿。",fr="Ma petite sœur joue du piano tous les jours.",uses=["v5-31"]),
 TC(9,["はじめて","はじめまして","いつも","{毎日|まいにち}"],jp="＿{外国|がいこく}へ{行|い}きますから、パスポートを{作|つく}りました。",fr="Je pars à l'étranger pour la première fois, alors j'ai fait faire un passeport.",uses=["v5-27","v5-33"]),
 TC(10,["います","あります","です","ます"],jp="{公園|こうえん}の{池|いけ}にきれいな{魚|さかな}が＿。",fr="Il y a de jolis poissons dans l'étang du parc.",uses=["v5-35"]),
 TC(11,["Traversez le pont et allez tout droit.","Prenez vos baguettes et mangez.","Tournez au coin et allez tout droit.","Passez devant le pont, puis tournez."],q="Que veut dire : はしをわたって、まっすぐ{行|い}ってください。",uses=["v5-32"]),
 TC(12,["{本屋|ほんや}","{花屋|はなや}","{食堂|しょくどう}","こうばん"],jp="＿で{本|ほん}を{三|さん}さつ{買|か}いました。",fr="J'ai acheté trois livres à la librairie.",uses=["v5-08","v5-32"]),
 TC(13,["{旅行|りょこう}","{外国|がいこく}","ホテル","にもつ"],jp="{京都|きょうと}へ＿に{行|い}きました。",fr="Je suis parti en voyage à Kyoto.",uses=["v5-33"]),
 TO(14,"Je regarde un film au cinéma.",["{映画館|えいがかん}で","{映画|えいが}を","{見|み}ます"],alt=[["{映画|えいが}を","{映画館|えいがかん}で","{見|み}ます"]],uses=["v5-31","v5-32"]),
 TC(15,["スプーン","フォーク","ナイフ","おさら"],jp="＿でスープを{飲|の}みます。",fr="Je mange la soupe avec une cuillère.",uses=["v5-34"]),
 TC(16,["{花|はな}","{犬|いぬ}","{鳥|とり}","{牛|うし}"],q="Lequel n'est **pas** un animal ?",uses=["v5-35"]),
]
bloc = {"id": "v5-b07", "level": "N5", "title": "Sortir : loisirs, ville, voyages, table, nature",
        "lessons": [l31, l32, l33, l34, l35], "test": test}
save(bloc, sys.argv[1])
