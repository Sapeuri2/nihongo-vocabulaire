// Kanji autorisés dans le contenu : JLPT N5 + N4 (listes usuelles de l'ancien JLPT 4級/3級).
// Tout autre kanji fait échouer tools/verifier.mjs : écrire le mot en kana,
// ou l'ajouter à TOLERES s'il est vraiment nécessaire (N3).

const N5 = `
一二三四五六七八九十百千万円 日月火水木金土 年時分半今何午前後毎週先 生学校人男女子父母友名
上下中外右左東西南北 山川天気雨電車道駅社会国語本 見行来食飲聞読書話買休入出立言
大小高安新古長白間花空目耳口手足魚`;

const N4 = `
悪暗医意以引院員運映英屋音歌夏家画海界開楽館漢寒顔起帰究急牛去京強教業近銀区計兄軽犬研県建験
元工広考光好合黒菜作産紙思姉止市仕死使始試私字自事持室質写者借弱首主秋集習終住重春所暑場乗色
森心親真進図青正声世赤夕切説洗早走送族村体待貸台代題短知地池茶着昼注町鳥朝通低弟転田都度答冬
頭同動堂働特肉売発飯病品不風服物文別勉便歩方妹味民明門問夜野薬有曜用洋理旅料力林遠少多店太犬
映帰`;

// N3 tolérés : déjà utilisés dans l'appli de grammaire, donc familiers.
// Plus 昨 (昨日) : mot N5 de base, toujours écrit en kanji.
const TOLERES = `公園部晩降遊泳静宿紅酒窓授速歯若果飛機晴議座消配末阪昨利`;

export const KANJI = new Set([...(N5 + N4 + TOLERES)].filter(c => /\p{Script=Han}/u.test(c)));
