import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import W, C, O, LECT, make_block, save_n4

# ---------- L56 Ménage et objets ----------
L = "v4-56"
l56 = {"id": L, "title": "Ranger, jeter, réparer", "words": [
 W("かたづける","かたづける","ranger, mettre de l'ordre","{部屋|へや}をかたづけてから、{出|で}かけます。","Je range ma chambre, puis je sors."),
 W("ごみ","ごみ","déchets, poubelle","ごみは{火曜日|かようび}と{金曜日|きんようび}に{出|だ}します。","On sort les poubelles le mardi et le vendredi."),
 W("すてる","すてる","jeter","{古|ふる}い{服|ふく}をすてました。","J'ai jeté mes vieux vêtements."),
 W("よごれる","よごれる","se salir","{雨|あめ}の{中|なか}を{歩|ある}いて、くつがよごれました。","J'ai marché sous la pluie, mes chaussures sont sales."),
 W("きたない","きたない","sale","{弟|おとうと}の{部屋|へや}はいつもきたないです。","La chambre de mon petit frère est toujours sale."),
 W("なおす","なおす","réparer ; corriger","{父|ちち}がこわれたいすをなおしました。","Mon père a réparé la chaise cassée."),
 W("ふく","ふく","essuyer","テーブルをふいてください。","Essuie la table, s'il te plaît."),
 W("しまう","しまう","ranger (à sa place)","{使|つか}ったどうぐを{引|ひ}き{出|だ}しにしまってください。","Range les outils dans le tiroir après usage."),
 W("{引|ひ}き{出|だ}し","ひきだし","tiroir","はさみは{引|ひ}き{出|だ}しの{中|なか}にあります。","Les ciseaux sont dans le tiroir."),
 W("たな","たな","étagère","たなの{上|うえ}にかばんをおきました。","J'ai posé le sac sur l'étagère."),
 W("どうぐ","どうぐ","outil, ustensile","{料理|りょうり}のどうぐを{洗|あら}います。","Je lave les ustensiles de cuisine."),
 W("しゅうりする","しゅうりする","réparer (un spécialiste)","こわれたパソコンをしゅうりしてもらいました。","J'ai fait réparer l'ordinateur en panne."),
 W("もえる","もえる","brûler","このごみはもえますか。","Ces déchets, ils se brûlent ?"),
 W("{水道|すいどう}","すいどう","eau du robinet, conduite d'eau","{水道|すいどう}の{水|みず}を{飲|の}んでもいいですか。","On peut boire l'eau du robinet ?"),
 W("そうじき","そうじき","aspirateur","{毎週|まいしゅう}{土曜日|どようび}にそうじきをかけます。","Je passe l'aspirateur tous les samedis."),
], "sections": [
 {"h": "Ranger, jeter, réparer",
  "p": ["Au Japon, on trie ses déchets et on les sort certains jours seulement."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["mettre de l'ordre", "{部屋|へや}==を==かたづける"],
   ["ranger à sa place", "〜==に==しまう"],
   ["jeter / sortir les poubelles", "すてる / ごみ==を=={出|だ}す"],
   ["essuyer", "テーブル==を==ふく"],
   ["réparer", "なおす · しゅうりする"],
   ["passer l'aspirateur", "そうじき==を==かける"]]}}
], "pieges": [
 "かたづける = mettre de l'ordre (une pièce, une table) ; しまう = ranger un objet **à sa place** (〜にしまう).",
 "ごみを**{出|だ}す** = sortir les poubelles (le jour prévu) ; すてる = jeter.",
 "もえるごみ / もえないごみ : déchets qui se brûlent / qui ne se brûlent pas.",
 "なおす = réparer **et** corriger. なおる (leçon 44) = guérir (ou « être réparé »).",
 "ふく (essuyer) a le même son que {服|ふく} (vêtements).",
 "そうじきを**かける** = passer l'aspirateur (encore un sens de かける !)."
], "exercises": [
 C(L,1,["かたづけます","よごれます","すてます","もえます"],jp="{友|とも}だちが{来|き}ますから、{部屋|へや}を＿。",fr="Un ami vient, alors je range ma chambre.",uses=["v5-04"]),
 C(L,2,["すて","よごれ","なおし","もえ"],jp="もう{着|き}ない{古|ふる}い{服|ふく}を＿ました。",fr="J'ai jeté les vieux vêtements que je ne mets plus.",uses=["v5-13"]),
 C(L,3,["よごれました","よごしました","きたないでした","すてました"],jp="{雨|あめ}の{中|なか}を{歩|ある}いて、くつが＿。",fr="J'ai marché sous la pluie, mes chaussures se sont salies.",uses=["v5-13","v5-15"]),
 C(L,4,["きたない","きれい","よごれる","もえる"],jp="{弟|おとうと}の{部屋|へや}はいつも＿です。ぜんぜんそうじをしません。",fr="La chambre de mon petit frère est toujours sale. Il ne fait jamais le ménage.",uses=["v5-14"]),
 C(L,5,["なおしました","なおりました","かわきました","もえました"],jp="{父|ちち}がこわれたいすを＿。",fr="Mon père a réparé la chaise cassée.",uses=["v4-48"]),
 C(L,6,["ふいて","すてて","もえて","よごれて"],jp="{食|た}べたあとで、テーブルを＿ください。",fr="Après le repas, essuie la table, s'il te plaît."),
 C(L,7,["しまって","すてて","ふいて","なおして"],jp="{使|つか}ったはさみは{引|ひ}き{出|だ}しに＿ください。",fr="Range les ciseaux dans le tiroir après t'en être servi.",uses=["v5-27"]),
 C(L,8,["{引|ひ}き{出|だ}し","{水道|すいどう}","そうじき","しゅうり"],jp="はさみはつくえの＿の{中|なか}にあります。",fr="Les ciseaux sont dans le tiroir du bureau.",uses=["v5-12"]),
 C(L,9,["たな","ごみ","{水道|すいどう}","しゅうり"],jp="＿の{上|うえ}に{本|ほん}をならべました。",fr="J'ai aligné des livres sur l'étagère.",uses=["v5-27"]),
 C(L,10,["どうぐ","ごみ","しゅうり","{水道|すいどう}"],jp="{料理|りょうり}の＿をきれいに{洗|あら}います。",fr="Je lave bien les ustensiles de cuisine.",uses=["v5-14"]),
 C(L,11,["しゅうり","かたづけ","そうじき","ごみ"],jp="こわれたパソコンを{店|みせ}で＿してもらいました。",fr="J'ai fait réparer l'ordinateur en panne au magasin.",uses=["v4-48"]),
 C(L,12,["もえる","もえて","しまう","ふく"],jp="これは＿ごみですから、{火曜日|かようび}に{出|だ}してください。",fr="Ce sont des déchets qui se brûlent : sortez-les le mardi.",uses=["v5-17"]),
 C(L,13,["{水道|すいどう}","たな","どうぐ","そうじき"],jp="＿の{水|みず}は{飲|の}めますか。",fr="On peut boire l'eau du robinet ?"),
 C(L,14,["そうじき","ごみ","たな","{水道|すいどう}"],jp="{毎週|まいしゅう}{土曜日|どようび}に＿をかけます。",fr="Je passe l'aspirateur tous les samedis.",uses=["v5-38"]),
 C(L,15,["essuyer","vêtements","ranger","laver"],q="Dans « テーブルをふく », que veut dire ふく ?"),
 C(L,16,["sale","propre","cassé","vieux"],q="Que veut dire **きたない** ?"),
 O(L,17,"J'ai jeté mes vieux vêtements.",["{古|ふる}い","{服|ふく}を","すてました"],uses=["v5-13"]),
 O(L,18,"Range ta chambre avant de sortir.",["{出|で}かける{前|まえ}に","{部屋|へや}を","かたづけて","ください"],alt=[["{部屋|へや}を","{出|で}かける{前|まえ}に","かたづけて","ください"]],uses=["v5-14"]),
]}

# ---------- L57 Argent et magasins ----------
L = "v4-57"
l57 = {"id": L, "title": "Argent et magasins", "words": [
 W("ねだん","ねだん","prix","このかばんはねだんが{高|たか}いです。","Ce sac est cher."),
 W("はらう","はらう","payer","カードではらってもいいですか。","Je peux payer par carte ?"),
 W("おつり","おつり","monnaie (rendue)","{千円|せんえん}{出|だ}して、おつりを{二百円|にひゃくえん}もらいました。","J'ai donné mille yens et on m'a rendu deux cents yens."),
 W("{品物|しなもの}","しなもの","article, marchandise","この{店|みせ}の{品物|しなもの}はいいです。","Les articles de ce magasin sont de bonne qualité."),
 W("{売|う}り{場|ば}","うりば","rayon (d'un magasin)","くつの{売|う}り{場|ば}は{何|なん}がいですか。","À quel étage est le rayon chaussures ?"),
 W("〜{代|だい}","〜だい","frais de …","{電気|でんき}{代|だい}が{高|たか}くなりました。","La facture d'électricité a augmenté."),
 W("{料金|りょうきん}","りょうきん","tarif","バスの{料金|りょうきん}はいくらですか。","Combien coûte le bus ?"),
 W("レジ","レジ","caisse","レジでお{金|かね}をはらいます。","On paie à la caisse."),
 W("げんきん","げんきん","espèces, liquide","この{店|みせ}はげんきんだけです。","Ce magasin n'accepte que les espèces."),
 W("ちょきんする","ちょきんする","économiser, épargner","{毎月|まいつき}{一万円|いちまんえん}ちょきんしています。","J'économise dix mille yens par mois."),
 W("{注文|ちゅうもん}する","ちゅうもんする","commander","{店|みせ}の{人|ひと}にコーヒーを{注文|ちゅうもん}しました。","J'ai commandé un café au serveur."),
 W("{売|う}り{切|き}れ","うりきれ","épuisé (plus en stock)","すみません、そのパンは{売|う}り{切|き}れです。","Désolé, ce pain est épuisé."),
 W("つつむ","つつむ","emballer","プレゼントですから、きれいにつつんでください。","C'est un cadeau, emballez-le joliment s'il vous plaît."),
 W("ふくろ","ふくろ","sac (en plastique, en papier)","ふくろはいりますか。","Vous voulez un sac ?"),
 W("おきゃくさん","おきゃくさん","client ; invité","この{店|みせ}はいつもおきゃくさんが{多|おお}いです。","Il y a toujours beaucoup de clients dans ce magasin."),
], "sections": [
 {"h": "À la caisse",
  "p": ["Les phrases qu'on entend (et qu'on dit) dans tous les magasins."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["payer avec", "カード==で==はらう · げんきん==で==はらう"],
   ["c'est cher", "ねだん==が=={高|たか}い"],
   ["frais de…", "{電気|でんき}{代|だい} · バスの{料金|りょうきん}"],
   ["la monnaie", "おつり"],
   ["plus en stock", "{売|う}り{切|き}れ"],
   ["un sac ?", "ふくろはいりますか"]]}}
], "pieges": [
 "Cher = ねだん**が{高|たか}い** (jamais ねだんが{大|おお}きい).",
 "〜{代|だい} = frais de… ({電気|でんき}{代|だい}, タクシー{代|だい}) ; ≠ 〜{台|だい} (compteur des machines).",
 "{料金|りょうきん} = le tarif d'un service (bus, électricité, entrée).",
 "おつり = la monnaie rendue.",
 "{注文|ちゅうもん}する = commander (plus formel que たのむ, leçon 53).",
 "ふくろはいりますか : いる = avoir besoin (leçon 36).",
 "おきゃくさん = un client ; dans un magasin, le personnel dit おきゃくさま (plus poli)."
], "exercises": [
 C(L,1,["ねだん","おつり","ふくろ","レジ"],jp="このかばんはいいですが、＿が{高|たか}いです。",fr="Ce sac est bien, mais il est cher.",uses=["v5-12"]),
 C(L,2,["はらって","つつんで","ちょきんして","よごれて"],jp="カードで＿もいいですか。",fr="Je peux payer par carte ?"),
 C(L,3,["おつり","{料金|りょうきん}","ねだん","ふくろ"],jp="{千円|せんえん}{出|だ}して、＿を{二百円|にひゃくえん}もらいました。",fr="J'ai donné mille yens et on m'a rendu deux cents yens.",uses=["v5-07"]),
 C(L,4,["{売|う}り{場|ば}","おつり","ちょきん","{料金|りょうきん}"],jp="くつの＿は{三|さん}がいです。",fr="Le rayon chaussures est au deuxième étage (3がい).",uses=["v5-22"]),
 C(L,5,["{代|だい}","{台|だい}","{円|えん}","ふくろ"],jp="{今月|こんげつ}は{電気|でんき}＿が{高|たか}かったです。",fr="Ce mois-ci, la facture d'électricité était élevée.",uses=["v5-38"]),
 C(L,6,["{料金|りょうきん}","おつり","{売|う}り{場|ば}","ふくろ"],jp="タクシーの＿は{夜|よる}{高|たか}くなります。",fr="Le tarif des taxis augmente la nuit.",uses=["v5-15"]),
 C(L,7,["レジ","ふくろ","おつり","ねだん"],jp="お{金|かね}はあちらの＿ではらってください。",fr="Payez à la caisse là-bas, s'il vous plaît."),
 C(L,8,["げんきん","おつり","ねだん","{料金|りょうきん}"],jp="この{店|みせ}はカードが{使|つか}えません。＿だけです。",fr="Ce magasin n'accepte pas les cartes. Seulement les espèces.",uses=["v5-27"]),
 C(L,9,["ちょきん","はらう","{注文|ちゅうもん}","つつむ"],jp="{車|くるま}を{買|か}いたいですから、{毎月|まいつき}＿しています。",fr="Je veux acheter une voiture, alors j'économise tous les mois.",uses=["v5-38"]),
 C(L,10,["{注文|ちゅうもん}","ちょきん","つつむ","はらい"],jp="レストランで、{店|みせ}の{人|ひと}に{料理|りょうり}を＿しました。",fr="Au restaurant, j'ai commandé les plats au serveur."),
 C(L,11,["{売|う}り{切|き}れ","{売|う}り{場|ば}","おつり","げんきん"],jp="すみません、そのケーキはもう＿です。",fr="Désolé, ce gâteau est déjà épuisé."),
 C(L,12,["つつんで","はらって","ちょきんして","すてて"],jp="プレゼントですから、きれいに＿ください。",fr="C'est un cadeau, emballez-le joliment s'il vous plaît.",uses=["v5-26"]),
 C(L,13,["ふくろ","おつり","レジ","{料金|りょうきん}"],jp="＿はいりますか。— いいえ、だいじょうぶです。かばんがありますから。",fr="Vous voulez un sac ? — Non merci, j'ai un sac à dos.",uses=["v5-36"]),
 C(L,14,["おきゃくさん","おつり","{料金|りょうきん}","{売|う}り{切|き}れ"],jp="{安|やす}くておいしいですから、この{店|みせ}はいつも＿が{多|おお}いです。",fr="C'est bon marché et bon, alors ce restaurant a toujours beaucoup de clients."),
 C(L,15,["しなもの","ひんもの","しなぶつ","ひんぶつ"],q=LECT+"**品物** ?"),
 C(L,16,["カードではらってもいいですか。","カードをはらってもいいですか。","カードにはらってもいいですか。","カードではらいてもいいですか。"],q="« Je peux payer par carte ? » se dit…"),
 O(L,17,"J'économise dix mille yens par mois.",["{毎月|まいつき}","{一万円|いちまんえん}","ちょきん","しています"],uses=["v5-07","v5-38"]),
 O(L,18,"Ce sac est cher.",["この","かばんは","ねだんが","{高|たか}いです"],uses=["v5-12"]),
]}

# ---------- L58 Cuisine et goûts ----------
L = "v4-58"
l58 = {"id": L, "title": "Cuisiner et goûter", "words": [
 W("{味|あじ}","あじ","goût, saveur","このスープはいい{味|あじ}がします。","Cette soupe a bon goût."),
 W("におい","におい","odeur","{台所|だいどころ}からいいにおいがします。","Ça sent bon dans la cuisine."),
 W("やく","やく","griller, cuire","{魚|さかな}をやいて{食|た}べます。","Je fais griller le poisson pour le manger."),
 W("ゆでる","ゆでる","faire bouillir (un aliment)","たまごを{十分|じゅっぷん}ゆでます。","Je fais cuire les œufs dix minutes."),
 W("いためる","いためる","faire sauter (à la poêle)","{野菜|やさい}を{肉|にく}といためました。","J'ai fait sauter les légumes avec la viande."),
 W("にがい","にがい","amer","この{薬|くすり}はとてもにがいです。","Ce médicament est très amer."),
 W("すっぱい","すっぱい","acide","このりんごはすっぱいです。","Cette pomme est acide."),
 W("ざいりょう","ざいりょう","ingrédients","カレーのざいりょうを{買|か}いに{行|い}きます。","Je vais acheter les ingrédients du curry."),
 W("{作|つく}り{方|かた}","つくりかた","manière de faire, recette","このケーキの{作|つく}り{方|かた}を{教|おし}えてください。","Donne-moi la recette de ce gâteau."),
 W("{食事|しょくじ}する","しょくじする","prendre un repas","{家族|かぞく}とレストランで{食事|しょくじ}しました。","J'ai mangé au restaurant avec ma famille."),
 W("こめ","こめ","riz (cru)","{日本|にほん}の{人|ひと}はよくこめを{食|た}べます。","Les Japonais mangent beaucoup de riz."),
 W("おゆ","おゆ","eau chaude","おゆをわかして、おちゃを{入|い}れます。","Je fais bouillir de l'eau et je prépare le thé."),
 W("{生|なま}","なま","cru","この{魚|さかな}は{生|なま}で{食|た}べられます。","Ce poisson se mange cru."),
 W("こしょう","こしょう","poivre","スープにしおとこしょうを{入|い}れます。","Je mets du sel et du poivre dans la soupe."),
 W("{牛肉|ぎゅうにく}","ぎゅうにく","bœuf","{牛肉|ぎゅうにく}は{高|たか}いですから、あまり{買|か}いません。","Le bœuf est cher, alors j'en achète peu."),
], "sections": [
 {"h": "Cuisiner, goûter",
  "p": ["« Ça sent… », « ça a le goût de… » : 〜の**においがする**, 〜の**{味|あじ}がする**."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["griller", "やく (poisson, viande, pain)"],
   ["cuire à l'eau", "ゆでる (œufs, pâtes)"],
   ["faire sauter", "いためる (légumes)"],
   ["cru", "{生|なま}で{食|た}べる"],
   ["les goûts", "あまい · からい · すっぱい · にがい"]]}}
], "pieges": [
 "いいにおい**がする** = ça sent bon ; いい{味|あじ}**がする** = ça a bon goût.",
 "こめ = le riz **cru** (le grain) ; ご{飯|はん} = le riz cuit, le repas.",
 "おゆ = eau chaude ; on dit quand même おゆをわかす (faire bouillir de l'eau).",
 "ゆでる = cuire **dans** l'eau bouillante ; わかす (leçon 48) = faire bouillir l'eau elle-même.",
 "{生|なま} = cru. Même kanji que {生|い}きる, {生|う}まれる, {学生|がくせい}…",
 "{作|つく}り{方|かた} = la manière de faire, la recette (〜{方|かた}, leçon 39)."
], "exercises": [
 C(L,1,["{味|あじ}","こめ","ざいりょう","おゆ"],jp="このスープはいい＿がします。だれが{作|つく}りましたか。",fr="Cette soupe a bon goût. Qui l'a faite ?",uses=["v5-27"]),
 C(L,2,["におい","{味|あじ}","こしょう","{生|なま}"],jp="{台所|だいどころ}からいい＿がします。カレーですね。",fr="Ça sent bon dans la cuisine. C'est du curry !",uses=["v5-22"]),
 C(L,3,["やいて","わいて","にがくて","すっぱくて"],jp="{魚|さかな}を＿、しょうゆをつけて{食|た}べます。",fr="Je fais griller le poisson et je le mange avec de la sauce soja.",uses=["v5-34"]),
 C(L,4,["ゆでます","わきます","すてます","にがいです"],jp="たまごを{十分|じゅっぷん}＿。",fr="Je fais cuire les œufs dix minutes.",uses=["v5-06","v5-16"]),
 C(L,5,["いためました","わかしました","すっぱいでした","{食事|しょくじ}しました"],jp="{野菜|やさい}と{肉|にく}をフライパンで＿。",fr="J'ai fait sauter les légumes et la viande à la poêle.",uses=["v5-06"]),
 C(L,6,["にがい","あまい","{生|なま}","おゆ"],jp="この{薬|くすり}はとても＿です。でも、{飲|の}まなければなりません。",fr="Ce médicament est très amer. Mais je dois le prendre.",uses=["v5-23"]),
 C(L,7,["すっぱい","あまい","{生|なま}","からい"],jp="このりんごはまだ＿です。あまくないです。",fr="Cette pomme est encore acide. Elle n'est pas sucrée.",uses=["v5-18"]),
 C(L,8,["ざいりょう","{作|つく}り{方|かた}","におい","おゆ"],jp="カレーの＿を{買|か}いに、スーパーへ{行|い}きます。",fr="Je vais au supermarché acheter les ingrédients du curry.",uses=["v5-32"]),
 C(L,9,["{作|つく}り{方|かた}","におい","こめ","おゆ"],jp="このケーキはとてもおいしいですね。＿を{教|おし}えてください。",fr="Ce gâteau est délicieux. Donne-moi la recette !",uses=["v5-28"]),
 C(L,10,["{食事|しょくじ}","{作|つく}り{方|かた}","ざいりょう","こしょう"],jp="{週末|しゅうまつ}は{家族|かぞく}とレストランで＿しました。",fr="Ce week-end, j'ai mangé au restaurant avec ma famille.",uses=["v5-21"]),
 C(L,11,["こめ","{牛肉|ぎゅうにく}","こしょう","におい"],jp="ご{飯|はん}は＿から{作|つく}ります。",fr="Le riz cuit se prépare à partir du riz cru.",uses=["v5-06"]),
 C(L,12,["おゆ","こめ","におい","{生|なま}"],jp="おちゃを{入|い}れますから、＿をわかしてください。",fr="Je vais faire du thé, fais bouillir de l'eau s'il te plaît.",uses=["v4-48"]),
 C(L,13,["{生|なま}","におい","ざいりょう","{作|つく}り{方|かた}"],jp="この{魚|さかな}は＿で{食|た}べられます。さしみです。",fr="Ce poisson se mange cru. C'est du sashimi."),
 C(L,14,["こしょう","におい","{作|つく}り{方|かた}","{味|あじ}"],jp="スープにしおと＿を{入|い}れます。",fr="Je mets du sel et du poivre dans la soupe.",uses=["v5-34"]),
 C(L,15,["ぎゅうにく","うしにく","ぎゅにく","ぎゅうじく"],q=LECT+"**牛肉** ?"),
 C(L,16,["amer","acide","sucré","salé"],q="Que veut dire **にがい** ?"),
 C(L,17,["なま","せい","いき","うま"],q="Dans « 生の魚 » (poisson cru), comment se lit 生 ?"),
 O(L,18,"Ça sent bon dans la cuisine.",["{台所|だいどころ}から","いいにおいが","します"],uses=["v5-22"]),
]}

# ---------- L59 Services et démarches ----------
L = "v4-59"
l59 = {"id": L, "title": "Poste, mairie, police", "words": [
 W("ゆうびん","ゆうびん","courrier, poste","ゆうびんで{本|ほん}を{送|おく}りました。","J'ai envoyé un livre par la poste."),
 W("けいさつ","けいさつ","police","さいふをとられて、けいさつに{行|い}きました。","On m'a volé mon portefeuille, je suis allé à la police."),
 W("もうしこむ","もうしこむ","s'inscrire, faire une demande","{日本語|にほんご}の{試験|しけん}にもうしこみました。","Je me suis inscrit à l'examen de japonais."),
 W("とどける","とどける","livrer, rapporter","{道|みち}でひろったさいふをこうばんにとどけました。","J'ai rapporté au poste de police le portefeuille trouvé dans la rue."),
 W("とどく","とどく","arriver (courrier, colis)","{国|くに}の{母|はは}から{手紙|てがみ}がとどきました。","J'ai reçu une lettre de ma mère, restée au pays."),
 W("{切手|きって}","きって","timbre","{手紙|てがみ}に{切手|きって}をはります。","Je colle un timbre sur la lettre."),
 W("はがき","はがき","carte postale","{旅行|りょこう}のとき、{友|とも}だちにはがきを{出|だ}しました。","Pendant le voyage, j'ai envoyé une carte postale à un ami."),
 W("ふうとう","ふうとう","enveloppe","{手紙|てがみ}をふうとうに{入|い}れます。","Je mets la lettre dans l'enveloppe."),
 W("こづつみ","こづつみ","colis","{国|くに}にこづつみを{送|おく}りたいです。","Je voudrais envoyer un colis dans mon pays."),
 W("しやくしょ","しやくしょ","mairie","{住所|じゅうしょ}がかわったら、しやくしょに{行|い}きます。","Quand on change d'adresse, on va à la mairie."),
 W("{窓口|まどぐち}","まどぐち","guichet","あちらの{窓口|まどぐち}で{聞|き}いてください。","Renseignez-vous au guichet là-bas."),
 W("サイン","サイン","signature","ここにサインをおねがいします。","Signez ici, s'il vous plaît."),
 W("{送料|そうりょう}","そうりょう","frais d'envoi","{送料|そうりょう}はいくらですか。","Combien coûtent les frais d'envoi ?"),
 W("{用紙|ようし}","ようし","formulaire","この{用紙|ようし}に{名前|なまえ}と{住所|じゅうしょ}を{書|か}いてください。","Écrivez votre nom et votre adresse sur ce formulaire."),
 W("そくたつ","そくたつ","courrier express","{急|いそ}ぎますから、そくたつで{送|おく}ってください。","C'est urgent, envoyez-le en express."),
], "sections": [
 {"h": "À la poste, à la mairie",
  "p": ["La lettre **arrive** (とどく, が) ; quelqu'un la **livre** (とどける, を)."],
  "grid": {"head": ["", "japonais"], "rows": [
   ["envoyer par la poste", "ゆうびん==で=={送|おく}る"],
   ["coller un timbre", "{切手|きって}==を==はる"],
   ["ça arrive", "{手紙|てがみ}==が==とどく"],
   ["rapporter à", "〜==に==とどける"],
   ["s'inscrire à", "〜==に==もうしこむ"],
   ["en express", "そくたつ==で=={送|おく}る"]]}}
], "pieges": [
 "とどく : la chose arrive (が) ; とどける : on la livre, on la rapporte (を, 〜に).",
 "〜**に**もうしこむ = s'inscrire **à** (un examen, un cours).",
 "はがき = carte postale ; ふうとう = enveloppe ; こづつみ = colis.",
 "けいさつ = la police ; こうばん = le petit poste de quartier ; おまわりさん = l'agent.",
 "しやくしょ = la mairie (adresse, démarches) ; {窓口|まどぐち} = le guichet.",
 "{切手|きって}を**はる** = coller un timbre."
], "exercises": [
 C(L,1,["とどきました","とどけました","もうしこみました","はりました"],jp="{国|くに}の{母|はは}から{手紙|てがみ}が＿。",fr="J'ai reçu une lettre de ma mère, restée au pays.",uses=["v5-12","v5-21"]),
 C(L,2,["とどけました","とどきました","もうしこみました","サインしました"],jp="{道|みち}でひろったさいふを、こうばんに＿。",fr="J'ai rapporté au poste de police le portefeuille trouvé dans la rue.",uses=["v4-45","v5-32"]),
 C(L,3,["もうしこみました","とどきました","とどけました","ごうかくしました"],jp="{日本語|にほんご}の{試験|しけん}に＿。{試験|しけん}は{十二月|じゅうにがつ}です。",fr="Je me suis inscrit à l'examen de japonais. L'examen est en décembre.",uses=["v4-52"]),
 C(L,4,["{切手|きって}","ふうとう","サイン","{送料|そうりょう}"],jp="{手紙|てがみ}に＿をはって、{出|だ}します。",fr="Je colle un timbre sur la lettre et je la poste.",uses=["v5-26"]),
 C(L,5,["はがき","{切手|きって}","{用紙|ようし}","そくたつ"],jp="{旅行|りょこう}のとき、{友|とも}だちにきれいな{写真|しゃしん}の＿を{出|だ}しました。",fr="Pendant le voyage, j'ai envoyé à un ami une carte postale avec une jolie photo.",uses=["v5-12","v5-33"]),
 C(L,6,["ふうとう","サイン","はがき","{窓口|まどぐち}"],jp="{手紙|てがみ}を＿に{入|い}れて、{切手|きって}をはります。",fr="Je mets la lettre dans l'enveloppe et je colle un timbre.",uses=["v5-27"]),
 C(L,7,["こづつみ","はがき","{切手|きって}","サイン"],jp="{国|くに}の{家族|かぞく}に、{服|ふく}や{本|ほん}を＿で{送|おく}ります。",fr="J'envoie des vêtements et des livres à ma famille par colis.",uses=["v5-26"]),
 C(L,8,["しやくしょ","けいさつ","サイン","{送料|そうりょう}"],jp="{住所|じゅうしょ}がかわりましたから、＿に{行|い}って{用紙|ようし}を{出|だ}します。",fr="J'ai changé d'adresse, alors je vais à la mairie déposer le formulaire.",uses=["v4-47","v5-33"]),
 C(L,9,["けいさつ","しやくしょ","ゆうびん","はがき"],jp="さいふをとられましたから、＿に{電話|でんわ}しました。",fr="On m'a volé mon portefeuille, alors j'ai appelé la police.",uses=["v5-12"]),
 C(L,10,["サイン","{切手|きって}","こづつみ","{送料|そうりょう}"],jp="ここに＿をおねがいします。ペンをどうぞ。",fr="Signez ici, s'il vous plaît. Voici un stylo.",uses=["v5-29"]),
 C(L,11,["{窓口|まどぐち}","ふうとう","そくたつ","サイン"],jp="この{用紙|ようし}に{名前|なまえ}を{書|か}いて、あちらの＿に{出|だ}してください。",fr="Écrivez votre nom sur ce formulaire et déposez-le au guichet là-bas."),
 C(L,12,["そくたつ","はがき","{用紙|ようし}","サイン"],jp="{急|いそ}ぎますから、＿で{送|おく}ってください。",fr="C'est urgent, envoyez-le en express s'il vous plaît.",uses=["v5-36"]),
 C(L,13,["{送料|そうりょう}","サイン","{窓口|まどぐち}","{用紙|ようし}"],jp="フランスまでの＿はいくらですか。",fr="Combien coûtent les frais d'envoi jusqu'en France ?",uses=["v5-07"]),
 C(L,14,["{用紙|ようし}","{切手|きって}","そくたつ","サイン"],jp="この＿に{名前|なまえ}と{住所|じゅうしょ}を{書|か}いてください。",fr="Écrivez votre nom et votre adresse sur ce formulaire.",uses=["v5-33"]),
 C(L,15,["un colis","une carte postale","une enveloppe","un timbre"],q="Que veut dire **こづつみ** ?"),
 C(L,16,["{手紙|てがみ}がとどきました。","{手紙|てがみ}をとどきました。","{手紙|てがみ}がとどけました。","{手紙|てがみ}にとどきました。"],q="« La lettre est arrivée » se dit…"),
 O(L,17,"J'ai envoyé un colis dans mon pays.",["{国|くに}に","こづつみを","{送|おく}りました"],alt=[["こづつみを","{国|くに}に","{送|おく}りました"]],uses=["v5-26"]),
 O(L,18,"Je me suis inscrit à l'examen de japonais.",["{日本語|にほんご}の","{試験|しけん}に","もうしこみました"],uses=["v5-29"]),
]}

# ---------- L60 Adverbes et connecteurs N4 (2) ----------
L = "v4-60"
l60 = {"id": L, "title": "Connecteurs et adverbes N4 (2)", "words": [
 W("しかし","しかし","cependant, mais","{日本語|にほんご}はむずかしいです。しかし、おもしろいです。","Le japonais est difficile. Cependant, c'est intéressant."),
 W("それで","それで","et donc, c'est pour ça que","バスがおくれました。それで、{会社|かいしゃ}におくれました。","Le bus avait du retard. C'est pour ça que je suis arrivé en retard."),
 W("ところで","ところで","au fait (changer de sujet)","ところで、{明日|あした}はひまですか。","Au fait, tu es libre demain ?"),
 W("たとえば","たとえば","par exemple","{日本|にほん}の{料理|りょうり}、たとえばすしやてんぷらが{好|す}きです。","J'aime la cuisine japonaise, par exemple les sushis et les tempuras."),
 W("はっきり","はっきり","clairement","もっとはっきり{話|はな}してください。","Parlez plus clairement, s'il vous plaît."),
 W("それに","それに","en plus","この{部屋|へや}は{広|ひろ}いです。それに、{安|やす}いです。","Cette chambre est grande. En plus, elle n'est pas chère."),
 W("それなら","それなら","dans ce cas","{雨|あめ}ですか。それなら、{家|いえ}で{映画|えいが}を{見|み}ましょう。","Il pleut ? Dans ce cas, regardons un film à la maison."),
 W("けれど","けれど","mais (fin de proposition)","{高|たか}いけれど、このかばんを{買|か}います。","C'est cher, mais j'achète ce sac."),
 W("かなり","かなり","assez, plutôt","{今日|きょう}はかなり{寒|さむ}いですね。","Il fait plutôt froid aujourd'hui."),
 W("ちっとも","ちっとも","(ne…) pas du tout","この{本|ほん}はちっともおもしろくないです。","Ce livre n'est pas intéressant du tout."),
 W("なるべく","なるべく","autant que possible","なるべく{早|はや}く{来|き}てください。","Venez le plus tôt possible."),
 W("なるほど","なるほど","je vois, en effet","なるほど、よく{分|わ}かりました。","Je vois, j'ai bien compris."),
 W("ひさしぶり","ひさしぶり","ça faisait longtemps","ひさしぶりですね。お{元気|げんき}ですか。","Ça faisait longtemps ! Tu vas bien ?"),
 W("すっかり","すっかり","complètement","やくそくをすっかりわすれていました。","J'avais complètement oublié le rendez-vous."),
 W("もちろん","もちろん","bien sûr","パーティーに{来|き}ますか。— もちろん{行|い}きます。","Tu viens à la fête ? — Bien sûr !"),
], "sections": [
 {"h": "Relier, ajouter, changer de sujet",
  "p": ["Ces mots ouvrent la phrase suivante (sauf けれど, qui termine la première)."],
  "grid": {"head": ["", "sens"], "rows": [
   ["しかし · 〜けれど", "mais (しかし : soutenu ; けれど : en fin de proposition)"],
   ["それで", "et donc (conséquence)"],
   ["それに", "en plus"],
   ["それなら", "dans ce cas (réaction à ce que dit l'autre)"],
   ["ところで", "au fait (nouveau sujet)"],
   ["たとえば", "par exemple"]]}}
], "pieges": [
 "しかし = でも, mais en plus soutenu (surtout à l'écrit), en début de phrase. 〜けれど (ou 〜けど) se colle à la fin de la proposition : {高|たか}いけれど、{買|か}います.",
 "それで = et donc (on raconte une conséquence) ; だから (leçon 37) insiste plus.",
 "それなら = dans ce cas : on réagit à ce que l'autre vient de dire.",
 "ちっとも + négatif = pas du tout (comme ぜんぜん).",
 "なるべく = autant que possible ; なるほど = je vois (on vient de comprendre).",
 "すっかり = complètement (oublié, changé, guéri)."
], "exercises": [
 C(L,1,["それで","ところで","たとえば","なるほど"],jp="バスが{三十分|さんじゅっぷん}おくれました。＿、{会社|かいしゃ}におくれました。",fr="Le bus avait trente minutes de retard. C'est pour ça que je suis arrivé en retard au bureau.",uses=["v4-50"]),
 C(L,2,["それに","それで","しかし","それなら"],jp="この{部屋|へや}は{広|ひろ}くて{明|あか}るいです。＿、{駅|えき}にも{近|ちか}いです。",fr="Cet appartement est grand et lumineux. En plus, il est près de la gare.",uses=["v5-24"]),
 C(L,3,["それなら","それに","たとえば","かなり"],jp="{明日|あした}は{雨|あめ}だそうですよ。— ＿、{家|いえ}で{映画|えいが}を{見|み}ましょう。",fr="Il paraît qu'il pleuvra demain. — Dans ce cas, regardons un film à la maison.",uses=["v5-31"]),
 C(L,4,["ところで","けれど","それに","なるべく"],jp="{仕事|しごと}の{話|はなし}はもう{終|お}わりましたね。＿、{週末|しゅうまつ}は{何|なに}をしますか。",fr="On a fini de parler du travail. Au fait, que fais-tu ce week-end ?",uses=["v5-17"]),
 C(L,5,["たとえば","ちっとも","なるほど","すっかり"],jp="{日本|にほん}の{料理|りょうり}、＿すしやてんぷらが{大好|だいす}きです。",fr="J'adore la cuisine japonaise, par exemple les sushis et les tempuras."),
 C(L,6,["はっきり","ちっとも","すっかり","なるほど"],jp="{声|こえ}が{小|ちい}さくて{分|わ}かりません。もっと＿{話|はな}してください。",fr="Je n'entends pas, vous parlez trop bas. Parlez plus clairement, s'il vous plaît.",uses=["v5-23"]),
 C(L,7,["けれど","それで","それに","たとえば"],jp="{高|たか}い＿、このかばんはとても{便利|べんり}ですから{買|か}います。",fr="Il est cher, mais ce sac est très pratique, alors je l'achète.",uses=["v5-19"]),
 C(L,8,["かなり","ちっとも","なるべく","ひさしぶり"],jp="{今日|きょう}は＿{寒|さむ}いですね。コートを{着|き}てきてよかったです。",fr="Il fait plutôt froid aujourd'hui. J'ai bien fait de mettre mon manteau.",uses=["v5-25"]),
 C(L,9,["ちっとも","なるべく","それに","たとえば"],jp="この{映画|えいが}は＿おもしろくなかったです。ねてしまいました。",fr="Ce film n'était pas intéressant du tout. Je me suis endormi.",uses=["v5-31"]),
 C(L,10,["なるべく","ちっとも","すっかり","なるほど"],jp="＿{早|はや}く{来|き}てください。{会議|かいぎ}は{九時|くじ}からです。",fr="Venez le plus tôt possible. La réunion commence à neuf heures.",uses=["v4-51"]),
 C(L,11,["なるほど","なるべく","ちっとも","たとえば"],jp="「この{漢字|かんじ}は{木|き}が{三|みっ}つで『{森|もり}』です。」「＿、おもしろいですね。」",fr="« Ce kanji, c'est trois arbres : la forêt. » « Je vois, c'est amusant ! »",uses=["v5-35"]),
 C(L,12,["ひさしぶり","はじめまして","なるほど","もちろん"],jp="＿ですね。{三年|さんねん}ぶりですね。お{元気|げんき}でしたか。",fr="Ça faisait longtemps ! Trois ans, hein. Tu allais bien ?",uses=["v5-19"]),
 C(L,13,["すっかり","ちっとも","なるべく","たとえば"],jp="{友|とも}だちとのやくそくを＿わすれていました。ごめんなさい。",fr="J'avais complètement oublié le rendez-vous avec mon ami. Pardon.",uses=["v4-54"]),
 C(L,14,["もちろん","ちっとも","たとえば","ところで"],jp="{明日|あした}のパーティーに{来|き}ますか。— ＿{行|い}きます！",fr="Tu viens à la fête demain ? — Bien sûr que je viens !",uses=["v5-31"]),
 C(L,15,["でも","それに","それで","たとえば"],q="Quel mot a le même sens que **しかし** ?",uses=["v5-37"]),
 C(L,16,["pas du tout","pas encore","pas souvent","pas assez"],q="Que veut dire **ちっとも 〜ない** ?"),
 O(L,17,"Venez le plus tôt possible.",["なるべく","{早|はや}く","{来|き}て","ください"],uses=["v4-55"]),
 O(L,18,"Ça faisait longtemps ! Tu vas bien ?",["ひさしぶりですね。","お{元気|げんき}","ですか"],uses=["v5-19"]),
]}

TC, TO, XC, XO = make_block("v4-b12", "v4-x06")
test = [
 TC(1,["きたない","きれい","しまう","もえる"],jp="{部屋|へや}が＿ですから、そうじします。",fr="La chambre est sale, alors je fais le ménage.",uses=["v4-56"]),
 TC(2,["ねだん","おつり","げんきん","サイン"],jp="このシャツはいいですが、＿がちょっと{高|たか}いです。",fr="Cette chemise est bien, mais elle est un peu chère.",uses=["v4-57"]),
 TC(3,["ゆでて","わかして","いって","とどけて"],jp="たまごを＿{食|た}べます。",fr="Je fais cuire les œufs dans l'eau et je les mange.",uses=["v4-58"]),
 TC(4,["とどきました","とどけました","もうしこみました","はらいました"],jp="{国|くに}の{母|はは}からこづつみが＿。",fr="J'ai reçu un colis de ma mère, restée au pays.",uses=["v4-59"]),
 TC(5,["ところで","なるべく","それに","たとえば"],jp="{旅行|りょこう}の{話|はなし}、{楽|たの}しかったです。＿、{明日|あした}の{会議|かいぎ}は{何時|なんじ}からですか。",fr="Le récit du voyage était sympa. Au fait, la réunion de demain commence à quelle heure ?",uses=["v4-60"]),
 TC(6,["なおしました","すてました","なおりました","よごれました"],jp="こわれたかさを＿。まだ{使|つか}えます。",fr="J'ai réparé le parapluie cassé. Il est encore utilisable.",uses=["v4-56"]),
 TC(7,["はらって","つつんで","ちょきんして","とどけて"],jp="カードで＿もいいですか。— すみません、げんきんだけです。",fr="Je peux payer par carte ? — Désolé, seulement en espèces.",uses=["v4-57"]),
 TC(8,["にがい","{生|なま}","おゆ","ざいりょう"],jp="この{薬|くすり}は＿ですが、よくききます。",fr="Ce médicament est amer, mais il est efficace.",uses=["v4-58"]),
 TC(9,["きって","きりて","せって","きっしゅ"],q=LECT+"**切手** ?",uses=["v4-59"]),
 TC(10,["それなら","ところで","たとえば","ちっとも"],jp="{雨|あめ}ですか。＿、タクシーで{行|い}きましょう。",fr="Il pleut ? Dans ce cas, prenons un taxi.",uses=["v4-60"]),
 TC(11,["もえる","ふく","よごれ","しまう"],jp="いらない{紙|かみ}は＿ごみです。",fr="Le papier dont on n'a plus besoin, ce sont des déchets qui se brûlent.",uses=["v4-56"]),
 TC(12,["レジ","おつり","ねだん","{品物|しなもの}"],jp="＿でお{金|かね}をはらってから、ふくろをもらいました。",fr="J'ai payé à la caisse, puis on m'a donné un sac.",uses=["v4-57"]),
 TC(13,["におい","{味|あじ}","こめ","こしょう"],jp="{台所|だいどころ}から{魚|さかな}をやく＿がします。",fr="Ça sent le poisson grillé dans la cuisine.",uses=["v4-58"]),
 TO(14,"La lettre de ma mère est arrivée.",["{母|はは}からの","{手紙|てがみ}が","とどきました"],uses=["v4-59"]),
 TC(15,["はっきり","すっかり","ちっとも","なるべく"],jp="もっと＿{言|い}ってください。よく{聞|き}こえません。",fr="Dites-le plus clairement. Je n'entends pas bien.",uses=["v4-60","v5-40"]),
 TC(16,["すっかり","ちっとも","なるべく","もちろん"],jp="{十年|じゅうねん}ぶりに{町|まち}に{帰|かえ}りましたが、＿かわっていました。",fr="Je suis revenu en ville après dix ans : elle avait complètement changé.",uses=["v4-47","v4-60"]),
]
exam = [
 XC(1,["{部長|ぶちょう}に{仕事|しごと}のことをそうだんしました。","{部長|ぶちょう}を{仕事|しごと}のことをそうだんしました。","{部長|ぶちょう}に{仕事|しごと}のことがそうだんしました。","{部長|ぶちょう}に{仕事|しごと}のことをそうだんいました。"],q="Une seule de ces phrases est correcte. Laquelle ?",uses=["v4-51","v4-53"]),
 XC(2,["れんらく","あいさつ","しゅっちょう","ちょきん"],jp="{急|きゅう}にねつが{上|あ}がって、{会社|かいしゃ}を{休|やす}みました。{朝|あさ}、{部長|ぶちょう}に＿しました。",fr="J'ai eu de la fièvre d'un coup et je ne suis pas allé travailler. Le matin, j'ai prévenu mon chef.",uses=["v4-47","v4-51","v4-53"]),
 XC(3,["ごうかくする","おちる","そつぎょうする","{入学|にゅうがく}する"],jp="{試験|しけん}に＿ために、{毎日|まいにち}いっしょうけんめい{勉強|べんきょう}しています。",fr="J'étudie de toutes mes forces tous les jours pour réussir l'examen.",uses=["v4-52","v4-55"]),
 XC(4,["しゅうりして","すてて","よごして","かたづけて"],jp="こわれたパソコンを{店|みせ}で＿もらいました。{今|いま}はよく{動|うご}きます。",fr="J'ai fait réparer l'ordinateur en panne au magasin. Maintenant il marche bien.",uses=["v4-45","v4-48","v4-56"]),
 XC(5,["すわる","すく","とまる","まがる"],jp="{電車|でんしゃ}がこんでいて、＿せきがありませんでした。",fr="Le train était bondé, il n'y avait pas de place pour s'asseoir.",uses=["v4-50","v5-36"]),
 XC(6,["{下|さ}がります","{下|さ}げます","へります","なくなります"],jp="このスーパーは{夜|よる}{八時|はちじ}になると、{魚|さかな}のねだんが＿。",fr="Dans ce supermarché, le prix du poisson baisse à partir de vingt heures.",uses=["v4-47","v4-57"]),
 XC(7,["{聞|き}きました","ことわりました","あやまりました","しょうかいしました"],jp="カレーの{作|つく}り{方|かた}が{分|わ}からなかったので、{母|はは}に{電話|でんわ}で＿。",fr="Je ne savais pas comment faire le curry, alors j'ai demandé à ma mère au téléphone.",uses=["v4-53","v4-58"]),
 XO(8,"Faites attention aux voitures quand vous traversez.",["{道|みち}をわたるときは、","{車|くるま}に","{注意|ちゅうい}して","ください"],uses=["v4-44","v5-32"]),
 XC(9,["Ça faisait longtemps !","Enchanté !","À bientôt !","Quel sale temps !"],q="Ton voisin te dit : ひさしぶりですね. Que veut-il dire ?",uses=["v4-60"]),
 XC(10,["おとして","かたづけて","つつんで","ちょきんして"],jp="{電車|でんしゃ}でさいふを＿、けいさつに{行|い}きました。",fr="J'ai perdu mon portefeuille dans le train, alors je suis allé à la police.",uses=["v4-48","v4-59"]),
 XC(11,["ちょきんして","{注文|ちゅうもん}して","つつんで","とどけて"],jp="{車|くるま}を{買|か}うために、きゅうりょうから{毎月|まいつき}{二万円|にまんえん}＿います。",fr="Pour acheter une voiture, je mets de côté vingt mille yens de mon salaire chaque mois.",uses=["v4-51","v4-57"]),
 XC(12,["よやく","キャンセル","しゅうり","ちょきん"],jp="このレストランはいつもこんでいますから、{前|まえ}の{日|ひ}に＿しておいたほうがいいです。",fr="Ce restaurant est toujours bondé, alors il vaut mieux réserver la veille.",uses=["v4-50","v4-54"]),
 XC(13,["Il refuse poliment.","Il accepte avec plaisir.","Il s'excuse d'être en retard.","Il demande l'heure."],q="A : {明日|あした}、いっしょに{映画|えいが}に{行|い}きませんか。 B : すみません、{明日|あした}はちょっと…  Que fait B ?",uses=["v4-53"]),
 XC(14,["Je suis allé à l'aéroport accompagner un ami qui rentrait chez lui.","Je suis allé chercher un ami qui arrivait.","Je suis rentré dans mon pays avec un ami.","Mon ami est venu me chercher à l'aéroport."],q="Que veut dire : {国|くに}に{帰|かえ}る{友|とも}だちを{見送|みおく}りに、くうこうへ{行|い}きました。",uses=["v4-46"]),
 XC(15,["{足|た}り","のこら","へら","なくなら"],jp="スープにしおが＿なかったので、もう{少|すこ}し{入|い}れました。",fr="Il n'y avait pas assez de sel dans la soupe, alors j'en ai rajouté un peu.",uses=["v4-49","v4-58"]),
]
bloc = {"id": "v4-b12", "level": "N4", "title": "Vie pratique : ménage, argent, cuisine, démarches, connecteurs",
        "lessons": [l56, l57, l58, l59, l60], "test": test, "examTest": exam}
save_n4(bloc, sys.argv[1])
