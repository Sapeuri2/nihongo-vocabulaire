// Antisèche « い ou な ? » + passé poli + verbes (groupe, ます, dictionnaire, て), et rappels surprise. Propre à l'appli de vocabulaire (pas au moteur) :
// une bulle sur toutes les pages, et un mini-quiz qui surgit de temps en temps
// et ne se ferme qu'après une bonne réponse. Questions générées depuis data/rappels.json.
import { esc, rich } from './text.js';

const KEY = 'nv-memo-v1';
const FREQ = { souvent: 3, normal: 7, rarement: 15, jamais: 0 }; // minutes d'utilisation entre deux rappels
const FORMS = {
  type: 'en い ou en な ?',
  neg: 'présent négatif (poli)',
  past: 'passé (poli)',
  pastneg: 'passé négatif (poli)',
};
const ECLAIR = 10;

// Le passé poli selon le type de mot (carte de l'antisèche et explications).
const PAST_RULES = [
  { id: 'nom', label: 'Nom', fin: 'でした', ex: '{雨|あめ}でした', fr: 'c\'était (un jour de) pluie' },
  { id: 'na', label: 'Adjectif en な', fin: 'でした', ex: '{静|しず}かでした', fr: 'c\'était calme' },
  { id: 'verbe', label: 'Verbe', fin: 'ます → ました', ex: '{雨|あめ}が{降|ふ}りました', fr: 'il a plu' },
  { id: 'exist', label: 'ある / いる', fin: 'ありました / いました', ex: '{銀行|ぎんこう}がありました', fr: 'il y avait une banque' },
  { id: 'i', label: 'Adjectif en い', fin: 'い → かったです', ex: '{寒|さむ}かったです', fr: 'il faisait froid' },
];

// La forme て selon la fin du verbe (carte de l'antisèche et explications).
const TE_RULES = [
  { id: 'utr', label: 'う・つ・る', fin: 'って', ex: '{買|か}う → {買|か}って' },
  { id: 'mbn', label: 'む・ぶ・ぬ', fin: 'んで', ex: '{飲|の}む → {飲|の}んで' },
  { id: 'ku', label: 'く', fin: 'いて', ex: '{書|か}く → {書|か}いて' },
  { id: 'gu', label: 'ぐ', fin: 'いで', ex: '{泳|およ}ぐ → {泳|およ}いで' },
  { id: 'su', label: 'す', fin: 'して', ex: '{話|はな}す → {話|はな}して' },
  { id: 'iku', label: '{行|い}く (exception)', fin: '{行|い}って', ex: 'jamais {行|い}いて' },
  { id: 'g2', label: 'Groupe 2 (〜いる・〜える)', fin: 'る → て', ex: '{食|た}べる → {食|た}べて' },
  { id: 'irr', label: 'Irréguliers', fin: 'して・{来|き}て', ex: 'する → して, {来|く}る → {来|き}て' },
];
// ます et dictionnaire selon le groupe (carte de l'antisèche et explications).
const MASU_RULES = [
  { id: 'm1', label: 'Groupe 1', fin: 'う → い + ます', ex: '{書|か}く ⇄ {書|か}きます' },
  { id: 'm2', label: 'Groupe 2', fin: 'る ⇄ ます', ex: '{食|た}べる ⇄ {食|た}べます' },
  { id: 'mirr', label: 'Irréguliers', fin: 'する ⇄ します', ex: '{来|く}る ⇄ {来|き}ます' },
];
const THEMES = { ina: 'い / な', passe: 'passé poli', verbes: 'verbes (ます・る・て)' };

let DATA = { adjectifs: [], passe: { noms: [], verbes: [] }, phrases: [], verbes: { liste: [], phrases: [] } };
let mem = load();
let box = null; // la fenêtre (overlay)
let quiz = null; // { mode, q, picked, n, okCount }
let usedSec = 0;
let nextAt = 0;

function load() {
  const base = { freq: 'souvent', stats: {}, streak: 0, best: 0, themes: { ina: true, passe: true, verbes: true } };
  try {
    const m = { ...base, ...JSON.parse(localStorage.getItem(KEY) || '{}') };
    m.themes = Object.fromEntries(Object.keys(base.themes).map(t => [t, m.themes?.[t] !== false]));
    return m;
  } catch { return base; }
}
function save() {
  try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch { /* stockage indisponible */ }
}

const shuffle = a => a.map(x => [Math.random(), x]).sort((p, q) => p[0] - q[0]).map(p => p[1]);
const pick = a => a[Math.floor(Math.random() * a.length)];

// Tirage pondéré : ce qui a été raté revient plus souvent.
function weighted(pool) {
  const w = c => {
    const st = mem.stats[c.key] || { ok: 0, ko: 0 };
    return (c.boost || 1) * (1 + (3 * st.ko) / (1 + st.ok / 2));
  };
  let x = Math.random() * pool.reduce((s, c) => s + w(c), 0);
  return pool.find(c => (x -= w(c)) <= 0) || pool[0];
}

// Une question : bonne réponse + erreurs typiques comme mauvais choix.
function question(key, word, fr, label, good, bad, explain) {
  const wrong = shuffle([...new Set(bad)].filter(b => b !== good)).slice(0, 3);
  return { key, word, fr, label, good, choices: shuffle([good, ...wrong]), explain };
}

// ---------- Adjectifs en い / な ----------

function adjForms(a, form) {
  const w = a.jp;
  const n = a.n;
  if (a.t === 'i') {
    const s = w.slice(0, -1); // sans le い final
    const c = w === 'いい' ? 'よ' : s; // いい se conjugue sur よい
    const ii = w === 'いい';
    return {
      neg: [`${c}くないです`, [`${w}じゃありません`, `${w}くないです`, `${s}じゃないです`, ...(ii ? [`${s}くないです`] : [])]],
      past: [`${c}かったです`, [`${w}でした`, `${c}かったでした`, `${w}かったです`, `${w}ました`, ...(ii ? [`${s}かったです`] : [])]],
      pastneg: [`${c}くなかったです`, [`${w}じゃありませんでした`, `${c}くないでした`, `${w}くなかったです`, ...(ii ? [`${s}くなかったです`] : [])]],
      // 大きな / 小さな existent : ne pas les proposer comme erreur.
      noun: [`${w}${n}`, [`${w}な${n}`, `${w}の${n}`, a.naOk ? `${w}だ${n}` : `${s}な${n}`]],
    }[form];
  }
  const endsI = w.endsWith('い');
  const s = endsI ? w.slice(0, -1) : w; // l'erreur typique : faire tomber le い de きれい
  return {
    neg: [`${w}じゃありません`, [`${w}くないです`, `${w}なじゃありません`, endsI ? `${s}くないです` : `${w}じゃないでした`]],
    past: [`${w}でした`, [`${w}かったです`, `${w}なでした`, `${w}ました`, endsI ? `${s}かったです` : `${w}だったでした`]],
    pastneg: [`${w}じゃありませんでした`, [`${w}くなかったです`, `${w}じゃありませんかった`, endsI ? `${s}くなかったです` : `${w}なじゃありませんでした`]],
    // 上手い existe (うまい) : ne pas le proposer comme erreur.
    noun: [`${w}な${n}`, [`${w}${n}`, `${w}だ${n}`, a.pasI ? `${w}の${n}` : `${w}い${n}`]],
  }[form];
}

function adjExplain(a) {
  const w = a.jp;
  if (a.t === 'i') {
    const c = w === 'いい' ? 'よ' : w.slice(0, -1);
    return `<p><strong>${rich(w)}</strong> est un adjectif en <strong>い</strong> : le い final se transforme.</p>
      <p class="jp">${rich(`${c}くないです`)} · ${rich(`${c}かったです`)} · ${rich(`${c}くなかったです`)} · ${rich(`${w}${a.n}`)}</p>
      ${w === 'いい' ? '<p>いい se conjugue sur <strong>よい</strong> : よくない, よかった (jamais いくない).</p>' : ''}`;
  }
  return `<p><strong>${rich(w)}</strong> est un adjectif en <strong>な</strong> : il se conjugue comme un <strong>nom</strong> (NA = NOM).</p>
    <p class="jp">${rich(`${w}じゃありません`)} · ${rich(`${w}でした`)} · ${rich(`${w}じゃありませんでした`)} · ${rich(`${w}な${a.n}`)}</p>
    ${a.piege ? `<p>🪤 Piège : ${rich(w)} finit par い, mais ce い fait partie du mot : il ne tombe <strong>jamais</strong>.</p>` : ''}`;
}

function adjQuestion() {
  const a = weighted(DATA.adjectifs.map(x => ({ ...x, key: x.jp, boost: x.piege ? 2 : 1 })));
  const form = pick(a.piege ? ['type', 'type', 'neg', 'past', 'pastneg', 'noun'] : ['type', 'neg', 'past', 'pastneg', 'noun']);
  const label = form === 'noun' ? `devant ${rich(a.n)}` : FORMS[form];
  if (form === 'type') {
    const good = a.t === 'i' ? 'en い' : 'en な';
    return { key: a.key, word: a.jp, fr: a.fr, label, good, choices: ['en い', 'en な'], explain: adjExplain(a) };
  }
  const [good, bad] = adjForms(a, form);
  return question(a.key, a.jp, a.fr, label, good, bad, adjExplain(a));
}

// ---------- Passé poli : でした / ました / ありました / かったです ----------

function pastRule(id) {
  return `<ul class="m-rules">${PAST_RULES.map(r => `<li class="${r.id === id ? 'on' : ''}"><span>${r.label}</span> <span class="jp">${rich(r.fin)}</span></li>`).join('')}</ul>`;
}

function pastQuestion() {
  const { noms, verbes } = DATA.passe;
  const pool = [
    ...noms.map(x => ({ ...x, cat: 'nom', key: `p:${x.jp}` })),
    ...verbes.map(x => ({ ...x, cat: x.exist ? 'exist' : 'verbe', key: `p:${x.jp}` })),
    ...DATA.adjectifs.map(x => ({ ...x, cat: x.t === 'i' ? 'i' : 'na', key: `p:${x.jp}`, boost: 0.3 })),
  ];
  const c = weighted(pool);
  const w = c.jp;
  let good;
  let bad;
  if (c.cat === 'nom') {
    good = `${w}でした`;
    bad = [`${w}ました`, `${w}かったです`, `${w}ありました`];
  } else if (c.cat === 'verbe' || c.cat === 'exist') {
    const stem = w.slice(0, -2); // sans ます
    good = `${stem}ました`;
    bad = [`${w}でした`, `${stem}でした`, `${stem}かったです`];
  } else [good, bad] = adjForms(c, 'past');
  const what = { nom: 'un nom', na: 'un adjectif en な', i: 'un adjectif en い', verbe: 'un verbe', exist: 'le verbe d\'existence' }[c.cat];
  const explain = `<p>${rich(w)} est ${what} → <strong class="jp">${rich(good)}</strong></p>${pastRule(c.cat)}`;
  return question(c.key, w, c.fr, 'passé poli : quelle fin ?', good, bad, explain);
}

function phraseQuestion() {
  const p = weighted(DATA.phrases.map(x => ({ ...x, key: `f:${x.key}` })));
  const explain = `<p>${rich(p.explain)}</p>${pastRule(p.rule)}`;
  return { ...question(p.key, null, p.fr, 'Comment le dit-on ?', p.choices[0], p.choices.slice(1), explain), phrase: true };
}

// ---------- Verbes : groupe, ます, dictionnaire, て ----------

const U2I = { う: 'い', つ: 'ち', る: 'り', む: 'み', ぶ: 'び', ぬ: 'に', く: 'き', ぐ: 'ぎ', す: 'し' };
const U2A = { う: 'わ', つ: 'た', る: 'ら', む: 'ま', ぶ: 'ば', ぬ: 'な', く: 'か', ぐ: 'が', す: 'さ' };
const I2U = Object.fromEntries(Object.entries(U2I).map(([u, i]) => [i, u]));
const TE_FIN = { う: 'って', つ: 'って', る: 'って', む: 'んで', ぶ: 'んで', ぬ: 'んで', く: 'いて', ぐ: 'いで', す: 'して' };
const DIRS = {
  d2m: 'forme ます ?',
  m2d: 'forme du dictionnaire ?',
  d2t: 'forme て ?',
  m2t: 'forme て ?',
  grp: 'quel groupe ?',
};
const GROUP_NAME = { 1: 'groupe 1', 2: 'groupe 2', iku: 'groupe 1', irr: 'irrégulier' };

// Les trois formes d'un verbe.
function verbForms(v) {
  const d = v.jp;
  if (v.g === 'irr') return { dict: d, masu: v.masu, te: v.te };
  const s = d.slice(0, -1);
  if (v.g === '2') return { dict: d, masu: `${s}ます`, te: `${s}て`, s };
  const last = d.slice(-1);
  return { dict: d, masu: `${s}${U2I[last]}ます`, te: v.g === 'iku' ? `${s}って` : `${s}${TE_FIN[last]}`, s, last };
}

// Groupe 2 dont le radical finit par un son en i (起き, 借り) : on le prendrait pour un groupe 1 (起く, 借る).
function falseG1(f) {
  const k = f.s?.slice(-1);
  return k && I2U[k] ? `${f.s.slice(0, -1)}${I2U[k]}` : null;
}

// Erreurs typiques pour chaque sens de transformation.
function verbBad(v, f, dir) {
  if (v.bad?.[dir]) return v.bad[dir];
  const { s, last, dict } = f;
  const stem = f.masu.slice(0, -2);
  if (v.g === '2') {
    const g1 = falseG1(f);
    return {
      d2m: [`${s}ります`, `${dict}ます`, `${s}います`],
      m2d: [...(g1 ? [g1] : []), `${s}う`, `${s}つ`, `${s}く`],
      d2t: [`${s}って`, `${dict}て`, `${s}んで`],
      // 借ります → 借って : la règle du groupe 1 appliquée à 借る, qui n'existe pas.
      m2t: [...(g1 ? [`${g1.slice(0, -1)}${TE_FIN[g1.slice(-1)]}`] : []), `${s}って`, `${s}ますて`, `${s}んで`],
    }[dir];
  }
  if (v.g === 'iku') {
    return { d2m: [`${s}ます`, `${dict}ます`, `${s}かます`], m2d: [`${stem}る`, `${s}る`, `${s}つ`], d2t: [`${s}いて`, `${s}きて`, `${s}いで`], m2t: [`${s}いて`, `${stem}て`, `${s}いで`] }[dir];
  }
  const i = U2I[last];
  const te = {
    う: [`${s}んで`, `${s}いて`, `${s}して`],
    つ: [`${s}んで`, `${s}いて`, `${s}${i}て`],
    る: [`${s}て`, `${s}んで`, `${s}${i}て`], // ${s}て : la règle du groupe 2 (帰て)
    む: [`${s}って`, `${s}${i}て`, `${s}んて`],
    ぶ: [`${s}って`, `${s}${i}て`, `${s}んて`],
    ぬ: [`${s}って`, `${s}${i}て`, `${s}んて`],
    く: [`${s}って`, `${s}いで`, `${s}${i}て`],
    ぐ: [`${s}いて`, `${s}って`, `${s}${i}て`],
    す: [`${s}いて`, `${s}んで`, `${dict}て`],
  }[last];
  return {
    d2m: [`${s}ます`, `${dict}ます`, `${s}${U2A[last]}ます`], // ${s}ます : la règle du groupe 2 (帰ます)
    m2d: [`${stem}る`, ...(last === 'る' ? [] : [`${s}る`]), `${s}${last === 'う' ? 'つ' : 'う'}`, `${s}${last === 'つ' ? 'く' : 'つ'}`], // ${stem}る : 帰りる
    d2t: te,
    m2t: te,
  }[dir];
}

function verbCat(v) {
  if (v.g !== '1') return { 2: 'g2', iku: 'iku', irr: 'irr' }[v.g];
  return { う: 'utr', つ: 'utr', る: 'utr', む: 'mbn', ぶ: 'mbn', ぬ: 'mbn', く: 'ku', ぐ: 'gu', す: 'su' }[v.jp.slice(-1)];
}

function teRule(id) {
  return `<ul class="m-rules m-te-rules">${TE_RULES.map(r => `<li class="${r.id === id ? 'on' : ''}"><span>${rich(r.label)}</span> <span class="jp">${rich(r.fin)}</span></li>`).join('')}</ul>`;
}

function masuRule(id) {
  return `<ul class="m-rules m-te-rules">${MASU_RULES.map(r => `<li class="${r.id === id ? 'on' : ''}"><span>${rich(r.label)}</span> <span class="jp">${rich(r.fin)}</span></li>`).join('')}</ul>`;
}

function verbExplain(v, f, dir) {
  const g = GROUP_NAME[v.g];
  let h = `<p class="jp m-forms">${rich(f.dict)} · ${rich(f.masu)} · ${rich(f.te)}</p>`;
  h += `<p>${rich(v.jp)} est un verbe du <strong>${g}</strong>${v.g === 'iku' ? ` (exception pour て : ${rich('{行|い}って')})` : ''}.</p>`;
  if (v.piege && v.g === '1') h += `<p>🪤 Piège : il finit par いる / える mais c'est un <strong>groupe 1</strong> → ${rich(f.masu)}, ${rich(f.te)}.</p>`;
  const g1 = v.g === '2' && falseG1(f);
  if (g1) h += `<p>🪤 Piège : ${rich(f.masu)} vient de ${rich(f.dict)} (groupe 2), pas de « ${rich(g1)} ».</p>`;
  if (v.note) h += `<p>✂️ Ne pas confondre : ${rich(v.note)}</p>`;
  const mId = { 1: 'm1', iku: 'm1', 2: 'm2', irr: 'mirr' }[v.g];
  return h + (dir === 'd2t' || dir === 'm2t' ? teRule(verbCat(v)) : masuRule(mId));
}

function verbQuestion() {
  const v = weighted(DATA.verbes.liste.map(x => ({ ...x, key: `vb:${x.jp}`, boost: x.piege || x.note || x.g === 'iku' ? 2.5 : 1 })));
  const f = verbForms(v);
  const dir = pick(['d2m', 'm2d', 'd2t', 'm2t', 'm2t', 'grp']);
  const explain = verbExplain(v, f, dir);
  if (dir === 'grp') {
    const shown = pick([f.dict, f.masu]);
    const good = GROUP_NAME[v.g];
    return { key: v.key, word: shown, fr: v.fr, label: DIRS.grp, good, choices: ['groupe 1', 'groupe 2', 'irrégulier'], explain };
  }
  const word = { d2m: f.dict, m2d: f.masu, d2t: f.dict, m2t: f.masu }[dir];
  const good = { d2m: f.masu, m2d: f.dict, d2t: f.te, m2t: f.te }[dir];
  return question(v.key, word, v.fr, DIRS[dir], good, verbBad(v, f, dir), explain);
}

function verbPhraseQuestion() {
  const p = weighted(DATA.verbes.phrases.map(x => ({ ...x, key: `vp:${x.key}` })));
  const rule = p.rule === 'dict' ? '<p class="small">Devant まえに, つもり, こと… : toujours la forme du dictionnaire.</p>'
    : p.rule.startsWith('m') ? masuRule(p.rule) : teRule(p.rule);
  return { ...question(p.key, null, p.fr, 'Comment le dit-on ?', p.choices[0], p.choices.slice(1), `<p>${rich(p.explain)}</p>${rule}`), phrase: true };
}

function newQuestion() {
  // Thèmes cochés dans la bulle, chacun avec son poids.
  const gens = [];
  if (mem.themes.ina) gens.push([0.35, adjQuestion]);
  if (mem.themes.passe) gens.push([0.2, pastQuestion], [0.1, phraseQuestion]);
  if (mem.themes.verbes) gens.push([0.3, verbQuestion], [0.1, verbPhraseQuestion]);
  let x = Math.random() * gens.reduce((t, g) => t + g[0], 0);
  return (gens.find(g => (x -= g[0]) <= 0) || gens[0])[1]();
}

function record(q, ok) {
  const st = mem.stats[q.key] || { ok: 0, ko: 0 };
  if (ok) st.ok++; else st.ko++;
  st.w = q.word || q.fr;
  mem.stats[q.key] = st;
  mem.streak = ok ? mem.streak + 1 : 0;
  mem.best = Math.max(mem.best, mem.streak);
  save();
}

// ---------- Affichage ----------

const tile = (stem, end, cls = 'm-end') => `${rich(stem)}<span class="${cls}">${rich(end)}</span>`;
// ==texte== : partie qui change, surlignée.
const hl = x => x.split('==').map((part, i) => (i % 2 ? `<span class="m-new">${rich(part)}</span>` : rich(part))).join('');

function viewSheet() {
  const conj = rows => `<table class="m-conj">${rows.map(([l, v]) => `<tr><td>${l}</td><td class="jp">${v}</td></tr>`).join('')}</table>`;
  const weak = Object.entries(mem.stats).filter(([, s]) => s.ko).sort((x, y) => y[1].ko - x[1].ko).slice(0, 4);
  return `<div class="m-head"><h2>い / な, passé poli, forme て</h2>${furiButton()}<button class="m-x" data-m="close" aria-label="Fermer">✕</button></div>
  <section class="m-card m-i"><h3>🦎 Adjectif en い : la queue change</h3>
    <p>Le い reste au présent. Pour le reste, il tombe et on colle une nouvelle fin.</p>
    ${conj([
      ['présent', tile('{高|たか}', 'い') + 'です'],
      ['négatif', tile('{高|たか}', 'くない', 'm-new') + 'です'],
      ['passé', tile('{高|たか}', 'かった', 'm-new') + 'です'],
      ['passé nég.', tile('{高|たか}', 'くなかった', 'm-new') + 'です'],
      ['+ nom', tile('{高|たか}', 'い') + rich('{本|ほん}')],
    ])}
    <p class="m-warn">⚠ いい → <span class="jp">よくない · よかった · よくなかった</span> (jamais いくない)</p></section>
  <section class="m-card m-na"><h3>🧱 Adjectif en な = comme un NOM</h3>
    <p>Le mot ne bouge pas : on ajoute ce qu'on mettrait après ${rich('{学生|がくせい}')}. Le な n'apparaît que devant un nom.</p>
    ${conj([
      ['présent', rich('{静|しず}か') + '<span class="m-new">です</span>'],
      ['négatif', rich('{静|しず}か') + '<span class="m-new">じゃありません</span>'],
      ['passé', rich('{静|しず}か') + '<span class="m-new">でした</span>'],
      ['passé nég.', rich('{静|しず}か') + '<span class="m-new">じゃありませんでした</span>'],
      ['+ nom', tile('{静|しず}か', 'な') + rich('{部屋|へや}')],
    ])}</section>
  <section class="m-card m-trap"><h3>🪤 Les faux い</h3>
    <p class="jp m-big">きれい · きらい · ${rich('{有名|ゆうめい}')} · ていねい · しつれい</p>
    <p>Ce sont des adjectifs en <strong>な</strong> : leur い fait partie du mot et ne tombe jamais.
      <span class="jp">きれいじゃありません</span>, jamais <span class="jp">きれくない</span>.</p>
    <p><strong>Astuce kanji :</strong> い écrit en hiragana <em>après</em> le kanji (${rich('{高|たか}い')}, ${rich('{新|あたら}しい')}) → い.
      い caché <em>dans</em> la lecture du kanji (${rich('{有名|ゆうめい}')} = ゆう・めい) → な. Seule exception courante : きらい (${rich('{嫌|きら}い')}).</p></section>
  <section class="m-card m-past"><h3>🕰️ Le passé poli : quelle fin ?</h3>
    <p>Ça dépend du <strong>type de mot</strong>. Regarde le mot avant de choisir la fin.</p>
    <table class="m-conj m-past-table">${PAST_RULES.map(r => `<tr><td>${r.label}</td><td><span class="jp m-fin">${rich(r.fin)}</span>
      <span class="jp">${rich(r.ex)}</span> <span class="small muted">${esc(r.fr)}</span></td></tr>`).join('')}</table>
    <p class="m-warn">☔ « Il a plu » = ${rich('{雨|あめ}が{降|ふ}りました')} (la pluie tombe). ${rich('{雨|あめ}でした')} = c'était un jour de pluie.
      ${rich('{雨|あめ}がありました')} ne se dit pas pour « il a plu ».</p>
    <p class="small">Au négatif : でした → じゃありませんでした · ました → ませんでした · ありました → ありませんでした · かったです → くなかったです.</p></section>
  <section class="m-card m-te"><h3>🔁 Les verbes : d'abord le groupe</h3>
    <p><strong>Groupe 2</strong> : finit par <strong>る</strong> avec un son <strong>i</strong> ou <strong>e</strong> juste avant
      (${rich('{食|た}べる')}, ${rich('{起|お}きる')}, ${rich('{見|み}る')}). <strong>Irréguliers</strong> : する, ${rich('{来|く}る')}.
      <strong>Groupe 1</strong> : tout le reste.</p>
    <p class="m-warn">🪤 <strong>Faux groupe 2</strong> (groupe 1 !) : ${rich('{帰|かえ}る')}, ${rich('{入|はい}る')}, ${rich('{走|はし}る')}, ${rich('{知|し}る')}, ${rich('{切|き}る')}.</p>
    <table class="m-conj m-verbs"><tr><th></th><th>dictionnaire</th><th>ます</th><th>て</th></tr>
      ${[
        ['う', '{買|か}う', '{買|か}==い==ます', '{買|か}==って=='],
        ['つ', '{待|ま}つ', '{待|ま}==ち==ます', '{待|ま}==って=='],
        ['る (1)', '{帰|かえ}る', '{帰|かえ}==り==ます', '{帰|かえ}==って=='],
        ['む', '{飲|の}む', '{飲|の}==み==ます', '{飲|の}==んで=='],
        ['ぶ', '{遊|あそ}ぶ', '{遊|あそ}==び==ます', '{遊|あそ}==んで=='],
        ['ぬ', '{死|し}ぬ', '{死|し}==に==ます', '{死|し}==んで=='],
        ['く', '{書|か}く', '{書|か}==き==ます', '{書|か}==いて=='],
        ['★', '{行|い}く', '{行|い}==き==ます', '{行|い}==って=='],
        ['ぐ', '{泳|およ}ぐ', '{泳|およ}==ぎ==ます', '{泳|およ}==いで=='],
        ['す', '{話|はな}す', '{話|はな}==し==ます', '{話|はな}==して=='],
        ['2', '{食|た}べる', '{食|た}べ==ます==', '{食|た}べ==て=='],
        ['2', '{起|お}きる', '{起|お}き==ます==', '{起|お}き==て=='],
        ['irr.', 'する', '==します==', '==して=='],
        ['irr.', '{来|く}る', '=={来|き}ます==', '=={来|き}て=='],
      ].map(([l, ...c]) => `<tr><td>${l}</td>${c.map(x => `<td class="jp">${hl(x)}</td>`).join('')}</tr>`).join('')}</table>
    <p class="small">${rich("**ます → dictionnaire** : groupe 1, son i → son u ({書|か}きます → {書|か}く) ; groupe 2, ます → る ({起|お}きます → {起|お}きる, jamais {起|お}く). **ます → て** : d'abord le groupe ! Groupe 1 : on applique le tableau à la syllabe avant ます (き → いて, い・ち・り → って, み・び・に → んで, ぎ → いで, し → して ; exception {行|い}きます → {行|い}って). Groupe 2 : ます → て, même si la syllabe est り ou き ({借|か}ります → {借|か}りて, {起|お}きます → {起|お}きて).")}</p>
    <p class="m-warn">✂️ Paires à ne pas confondre : ${rich('{着|き}る')} → ${rich('{着|き}て')} / ${rich('{切|き}る')} → ${rich('{切|き}って')} ·
      ${rich('{入|い}れる')} → ${rich('{入|い}れて')} / ${rich('{入|はい}る')} → ${rich('{入|はい}って')} ·
      ${rich('{始|はじ}める')} → ${rich('{始|はじ}めて')} / ${rich('{始|はじ}まる')} → ${rich('{始|はじ}まって')}.</p>
    <p class="small">Astuce : <strong>んで</strong> et <strong>いで</strong> gardent le petit « ゛ » de む・ぶ・ぬ・ぐ ; tout le reste finit par て.</p></section>
  <section class="m-card m-ban"><h3>⛔ Les erreurs interdites</h3>
    <ul class="m-list jp">
      <li><s>${rich('{高|たか}いじゃありません')}</s> → ${rich('{高|たか}くないです')}</li>
      <li><s>${rich('{静|しず}かくないです')}</s> → ${rich('{静|しず}かじゃありません')}</li>
      <li><s>${rich('{寒|さむ}いでした')}</s> → ${rich('{寒|さむ}かったです')}</li>
      <li><s>${rich('{高|たか}かったでした')}</s> → ${rich('{高|たか}かったです')}</li>
      <li><s>${rich('{降|ふ}りでした')}</s> → ${rich('{降|ふ}りました')}</li>
      <li><s>いくないです</s> → よくないです</li>
      <li><s>${rich('{行|い}いて')}</s> → ${rich('{行|い}って')}</li>
      <li><s>${rich('{帰|かえ}て')}</s> → ${rich('{帰|かえ}って')}</li>
      <li><s>${rich('{飲|の}みて')}</s> → ${rich('{飲|の}んで')}</li>
      <li><s>${rich('{食|た}べって')}</s> → ${rich('{食|た}べて')}</li>
      <li><s>${rich('{起|お}きます')} → ${rich('{起|お}く')}</s> → ${rich('{起|お}きる')}</li>
    </ul></section>
  <p class="small muted">Entre amis (forme neutre) : enlève です pour い (${rich('{高|たか}くない')}, ${rich('{高|たか}かった')}).
    Pour な : ${rich('{静|しず}かじゃない')}, ${rich('{静|しず}かだった')}, ${rich('{静|しず}かじゃなかった')}.</p>
  <div class="m-actions"><button class="btn primary" data-m="eclair">Quiz éclair (${ECLAIR} questions)</button></div>
  <section class="m-card"><h3>Rappels surprise</h3>
    <p class="small muted">Un quiz surgit pendant que tu utilises l'appli. Il ne se ferme qu'après une bonne réponse.</p>
    <div class="m-seg">${Object.keys(FREQ).map(f => `<button data-m="freq" data-f="${f}" class="${mem.freq === f ? 'on' : ''}">${f}</button>`).join('')}</div>
    <p class="small muted">Thèmes des questions (rappels et quiz éclair) :</p>
    <div class="m-seg">${Object.entries(THEMES).map(([t, l]) => `<button data-m="theme" data-t="${t}" class="${mem.themes[t] ? 'on' : ''}">${mem.themes[t] ? '✓ ' : ''}${l}</button>`).join('')}</div>
    <p class="small">Série い/な (propre à cette bulle) : <strong>${mem.streak}</strong> bonne${mem.streak > 1 ? 's' : ''} réponse${mem.streak > 1 ? 's' : ''} d'affilée · record : <strong>${mem.best}</strong></p>
    ${weak.length ? `<p class="small">Tes pièges : <span class="jp">${weak.map(([k, s]) => `${rich(s.w || k)} (${s.ko}✗)`).join(' · ')}</span></p>` : ''}
  </section>`;
}

// Bouton 漢 : même réglage que le bouton 漢 du moteur dans la barre du haut (cachée par la fenêtre).
function furiButton() {
  const off = document.body.classList.contains('nofuri');
  return `<button class="m-furi jp${off ? ' off' : ''}" data-m="furi" title="Afficher / masquer les furigana" aria-label="Furigana ${off ? 'masqués' : 'affichés'}"><ruby>漢<rt>かん</rt></ruby></button>`;
}

function toggleFurigana() {
  const btn = document.querySelector('.top .furi-toggle');
  if (btn) btn.click(); // le moteur enregistre le réglage et met à jour la page
  else document.body.classList.toggle('nofuri');
}

function viewQuiz() {
  const { q, picked, mode } = quiz;
  const answered = picked != null;
  const ok = answered && q.choices[picked] === q.good;
  const title = mode === 'surprise' ? '⚡ Rappel surprise' : `Quiz éclair · ${quiz.n + 1}/${ECLAIR}`;
  let h = `<div class="m-head"><h2>${title}</h2>${furiButton()}${mode === 'eclair' ? '<button class="m-x" data-m="close" aria-label="Fermer">✕</button>' : ''}</div>`;
  h += q.word
    ? `<p class="m-q"><span class="jp m-word">${rich(q.word)}</span> <span class="muted">(${esc(q.fr)})</span></p>`
    : `<p class="m-q m-fr">« ${esc(q.fr)} »</p>`;
  h += `<p class="m-form">${q.label}</p>`;
  h += `<div class="choices m-choices">${q.choices.map((c, i) => {
    let cls = 'choice';
    if (answered) cls += c === q.good ? ' good' : i === picked ? ' bad' : ' dim';
    return `<button class="${cls}" data-m="pick" data-i="${i}" ${answered ? 'disabled' : ''}><span class="key">${i + 1}</span><span class="jp">${rich(c)}</span></button>`;
  }).join('')}</div>`;
  if (answered) {
    h += `<div class="fb ${ok ? 'ok' : 'ko'}"><strong>${ok ? '✓ Correct' : '✗ Raté'}</strong>${q.explain}`;
    if (mode === 'surprise') {
      h += ok
        ? '<div class="m-actions"><button class="btn primary" data-m="close">Continuer</button><button class="btn" data-m="again">Encore une</button></div>'
        : '<p class="small">Une bonne réponse pour fermer.</p><div class="m-actions"><button class="btn primary" data-m="again">Encore une</button></div>';
    } else if (quiz.n + 1 < ECLAIR) h += '<div class="m-actions"><button class="btn primary" data-m="next">Suivante</button></div>';
    else h += `<p><strong>Score : ${quiz.okCount}/${ECLAIR}</strong></p><div class="m-actions"><button class="btn primary" data-m="eclair">Recommencer</button><button class="btn" data-m="sheet">Antisèche</button></div>`;
    h += '</div>';
  }
  return h;
}

function show(html) {
  box.querySelector('.memo-box').innerHTML = html;
  box.hidden = false;
  document.documentElement.classList.add('memo-open');
}

function close() {
  box.hidden = true;
  quiz = null;
  document.documentElement.classList.remove('memo-open');
  schedule();
}

function startQuiz(mode) {
  quiz = { mode, q: newQuestion(), picked: null, n: 0, okCount: 0 };
  show(viewQuiz());
  box.querySelector('.memo-box').scrollTop = 0;
}

function onAct(act, el) {
  if (act === 'close') {
    if (quiz?.mode === 'surprise' && !(quiz.picked != null && quiz.q.choices[quiz.picked] === quiz.q.good)) return;
    close();
  } else if (act === 'furi') { toggleFurigana(); show(quiz ? viewQuiz() : viewSheet()); }
  else if (act === 'sheet') { quiz = null; show(viewSheet()); }
  else if (act === 'eclair') startQuiz('eclair');
  else if (act === 'theme') {
    const t = el.dataset.t;
    // Au moins un thème reste coché.
    if (!mem.themes[t] || Object.values(mem.themes).filter(Boolean).length > 1) { mem.themes[t] = !mem.themes[t]; save(); }
    show(viewSheet());
  } else if (act === 'freq') { mem.freq = el.dataset.f; save(); schedule(); show(viewSheet()); }
  else if (act === 'pick' && quiz && quiz.picked == null) {
    quiz.picked = +el.dataset.i;
    const ok = quiz.q.choices[quiz.picked] === quiz.q.good;
    if (ok) quiz.okCount++;
    record(quiz.q, ok);
    show(viewQuiz());
  } else if (act === 'again') { quiz.q = newQuestion(); quiz.picked = null; show(viewQuiz()); }
  else if (act === 'next') { quiz.n++; quiz.q = newQuestion(); quiz.picked = null; show(viewQuiz()); }
}

// ---------- Rappels surprise ----------

function schedule() {
  const m = FREQ[mem.freq] || 0;
  nextAt = m ? usedSec + Math.round(m * 60 * (0.6 + 0.8 * Math.random())) : Infinity;
}

function tick() {
  if (document.visibilityState !== 'visible' || !box.hidden) return;
  usedSec++;
  if (usedSec < nextAt) return;
  // Pas pendant la saisie de la clé de synchro.
  if (location.hash === '#/reglages' || document.activeElement?.tagName === 'INPUT') { nextAt = usedSec + 30; return; }
  startQuiz('surprise');
}

// ---------- Démarrage ----------

async function init() {
  try {
    const r = await fetch('data/rappels.json', { cache: 'no-cache' });
    DATA = await r.json();
  } catch { return; } // hors ligne sans cache : pas de bulle
  const bubble = document.createElement('button');
  bubble.id = 'memo-bubble';
  bubble.setAttribute('aria-label', 'Antisèche : い / な, passé poli, forme て');
  bubble.innerHTML = 'い<small>/</small>な<small>/</small>て';
  bubble.addEventListener('click', () => show(viewSheet()));
  box = document.createElement('div');
  box.className = 'memo-overlay';
  box.hidden = true;
  box.innerHTML = '<div class="memo-box" role="dialog" aria-modal="true"></div>';
  box.addEventListener('click', e => {
    if (e.target === box) return onAct('close');
    const ruby = e.target.closest('ruby');
    if (ruby && document.body.classList.contains('nofuri') && !ruby.closest('button')) ruby.classList.toggle('reveal');
    const el = e.target.closest('[data-m]');
    if (el && !el.disabled) onAct(el.dataset.m, el);
  });
  // Fenêtre ouverte : les touches vont au quiz, pas à l'exercice en dessous.
  window.addEventListener('keydown', e => {
    if (box.hidden) return;
    e.stopImmediatePropagation();
    if (/^[1-4]$/.test(e.key)) box.querySelector(`[data-m="pick"][data-i="${+e.key - 1}"]`)?.click();
    else if (e.key === 'Enter') { e.preventDefault(); box.querySelector('.m-actions .btn.primary')?.click(); }
    else if (e.key === 'Escape') onAct('close');
  }, true);
  document.body.append(bubble, box);
  // Premier rappel assez vite, puis au rythme choisi.
  const m = FREQ[mem.freq] || 0;
  nextAt = m ? Math.round(m * 60 * (0.2 + 0.3 * Math.random())) : Infinity;
  setInterval(tick, 1000);
}

init();
