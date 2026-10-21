// Antisèche « い ou な ? » et rappels surprise. Propre à l'appli de vocabulaire (pas au moteur) :
// une bulle sur toutes les pages, et un mini-quiz qui surgit de temps en temps
// et ne se ferme qu'après une bonne réponse. Questions générées depuis data/adjectifs.json.
import { esc, rich } from './text.js';

const KEY = 'nv-memo-v1';
const FREQ = { souvent: 3, normal: 7, rarement: 15, jamais: 0 }; // minutes d'utilisation entre deux rappels
const FORMS = {
  type: 'en い ou en な ?',
  neg: 'présent négatif (poli)',
  past: 'passé (poli)',
  pastneg: 'passé négatif (poli)',
  noun: 'devant un nom',
};
const ECLAIR = 10;

let ADJ = [];
let mem = load();
let box = null; // la fenêtre (overlay)
let quiz = null; // { mode, q, picked, n, okCount }
let usedSec = 0;
let nextAt = 0;

function load() {
  const base = { freq: 'souvent', stats: {}, streak: 0, best: 0 };
  try { return { ...base, ...JSON.parse(localStorage.getItem(KEY) || '{}') }; } catch { return base; }
}
function save() {
  try { localStorage.setItem(KEY, JSON.stringify(mem)); } catch { /* stockage indisponible */ }
}

const shuffle = a => a.map(x => [Math.random(), x]).sort((p, q) => p[0] - q[0]).map(p => p[1]);
const pick = a => a[Math.floor(Math.random() * a.length)];

// ---------- Questions ----------

// Les bonnes formes, et les erreurs typiques comme mauvais choix.
function forms(a, form) {
  const w = a.jp;
  const n = a.n;
  if (a.t === 'i') {
    const s = w.slice(0, -1); // sans le い final
    const c = w === 'いい' ? 'よ' : s; // いい se conjugue sur よい
    const ii = w === 'いい';
    return {
      neg: [`${c}くないです`, [`${w}じゃありません`, `${w}くないです`, `${s}じゃないです`, ...(ii ? [`${s}くないです`] : [])]],
      past: [`${c}かったです`, [`${w}でした`, `${c}かったでした`, `${w}かったです`, ...(ii ? [`${s}かったです`] : [])]],
      pastneg: [`${c}くなかったです`, [`${w}じゃありませんでした`, `${c}くないでした`, `${w}くなかったです`, ...(ii ? [`${s}くなかったです`] : [])]],
      // 大きな / 小さな existent : ne pas les proposer comme erreur.
      noun: [`${w}${n}`, [`${w}な${n}`, `${w}の${n}`, a.naOk ? `${w}だ${n}` : `${s}な${n}`]],
    }[form];
  }
  const endsI = w.endsWith('い');
  const s = endsI ? w.slice(0, -1) : w; // l'erreur typique : faire tomber le い de きれい
  return {
    neg: [`${w}じゃありません`, [`${w}くないです`, `${w}なじゃありません`, endsI ? `${s}くないです` : `${w}じゃないでした`]],
    past: [`${w}でした`, [`${w}かったです`, `${w}なでした`, endsI ? `${s}かったです` : `${w}だったでした`]],
    pastneg: [`${w}じゃありませんでした`, [`${w}くなかったです`, `${w}じゃありませんかった`, endsI ? `${s}くなかったです` : `${w}なじゃありませんでした`]],
    // 上手い existe (うまい) : ne pas le proposer comme erreur.
    noun: [`${w}な${n}`, [`${w}${n}`, `${w}だ${n}`, a.pasI ? `${w}の${n}` : `${w}い${n}`]],
  }[form];
}

function weight(a) {
  const st = mem.stats[a.jp] || { ok: 0, ko: 0 };
  return (a.piege ? 2 : 1) * (1 + (3 * st.ko) / (1 + st.ok / 2));
}

function newQuestion() {
  const total = ADJ.reduce((s, a) => s + weight(a), 0);
  let x = Math.random() * total;
  const a = ADJ.find(adj => (x -= weight(adj)) <= 0) || ADJ[0];
  const form = pick(a.piege ? ['type', 'type', 'neg', 'past', 'pastneg', 'noun'] : ['type', 'neg', 'past', 'pastneg', 'noun']);
  if (form === 'type') return { a, form, choices: ['en い', 'en な'], good: a.t === 'i' ? 'en い' : 'en な' };
  const [good, bad] = forms(a, form);
  const wrong = shuffle([...new Set(bad)].filter(b => b !== good)).slice(0, 3);
  return { a, form, choices: shuffle([good, ...wrong]), good };
}

function explain(a) {
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

function record(a, ok) {
  const st = mem.stats[a.jp] || { ok: 0, ko: 0 };
  if (ok) st.ok++; else st.ko++;
  mem.stats[a.jp] = st;
  mem.streak = ok ? mem.streak + 1 : 0;
  mem.best = Math.max(mem.best, mem.streak);
  save();
}

// ---------- Affichage ----------

const tile = (stem, end, cls = 'm-end') => `${rich(stem)}<span class="${cls}">${rich(end)}</span>`;

function viewSheet() {
  const conj = rows => `<table class="m-conj">${rows.map(([l, v]) => `<tr><td>${l}</td><td class="jp">${v}</td></tr>`).join('')}</table>`;
  const weak = Object.entries(mem.stats).filter(([, s]) => s.ko).sort((x, y) => y[1].ko - x[1].ko).slice(0, 4);
  let h = `<div class="m-head"><h2>い ou な ? L'antisèche</h2><button class="m-x" data-m="close" aria-label="Fermer">✕</button></div>
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
  <section class="m-card m-ban"><h3>⛔ Les 4 erreurs interdites</h3>
    <ul class="m-list jp">
      <li><s>${rich('{高|たか}いじゃありません')}</s> → ${rich('{高|たか}くないです')}</li>
      <li><s>${rich('{静|しず}かくないです')}</s> → ${rich('{静|しず}かじゃありません')}</li>
      <li><s>${rich('{高|たか}かったでした')}</s> → ${rich('{高|たか}かったです')}</li>
      <li><s>いくないです</s> → よくないです</li>
    </ul></section>
  <p class="small muted">Entre amis (forme neutre) : enlève です pour い (${rich('{高|たか}くない')}, ${rich('{高|たか}かった')}).
    Pour な : ${rich('{静|しず}かじゃない')}, ${rich('{静|しず}かだった')}, ${rich('{静|しず}かじゃなかった')}.</p>
  <div class="m-actions"><button class="btn primary" data-m="eclair">Quiz éclair (${ECLAIR} questions)</button></div>
  <section class="m-card"><h3>Rappels surprise</h3>
    <p class="small muted">Un quiz surgit pendant que tu utilises l'appli. Il ne se ferme qu'après une bonne réponse.</p>
    <div class="m-seg">${Object.keys(FREQ).map(f => `<button data-m="freq" data-f="${f}" class="${mem.freq === f ? 'on' : ''}">${f}</button>`).join('')}</div>
    <p class="small">Série : <strong>${mem.streak}</strong> bonne${mem.streak > 1 ? 's' : ''} réponse${mem.streak > 1 ? 's' : ''} d'affilée · record : <strong>${mem.best}</strong></p>
    ${weak.length ? `<p class="small">Tes pièges : <span class="jp">${weak.map(([w, s]) => `${rich(w)} (${s.ko}✗)`).join(' · ')}</span></p>` : ''}
  </section>`;
  return h;
}

function viewQuiz() {
  const { q, picked, mode } = quiz;
  const answered = picked != null;
  const ok = answered && q.choices[picked] === q.good;
  const title = mode === 'surprise' ? '⚡ Rappel surprise : い ou な ?' : `Quiz éclair · ${quiz.n + 1}/${ECLAIR}`;
  let h = `<div class="m-head"><h2>${title}</h2>${mode === 'eclair' ? '<button class="m-x" data-m="close" aria-label="Fermer">✕</button>' : ''}</div>`;
  h += `<p class="m-q"><span class="jp m-word">${rich(q.a.jp)}</span> <span class="muted">(${esc(q.a.fr)})</span></p>`;
  h += `<p class="m-form">${q.form === 'noun' ? `devant ${rich(q.a.n)}` : FORMS[q.form]}</p>`;
  h += `<div class="choices m-choices">${q.choices.map((c, i) => {
    let cls = 'choice';
    if (answered) cls += c === q.good ? ' good' : i === picked ? ' bad' : ' dim';
    return `<button class="${cls}" data-m="pick" data-i="${i}" ${answered ? 'disabled' : ''}><span class="key">${i + 1}</span><span class="jp">${rich(c)}</span></button>`;
  }).join('')}</div>`;
  if (answered) {
    h += `<div class="fb ${ok ? 'ok' : 'ko'}"><strong>${ok ? '✓ Correct' : '✗ Raté'}</strong>${explain(q.a)}`;
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
  } else if (act === 'sheet') { quiz = null; show(viewSheet()); }
  else if (act === 'eclair') startQuiz('eclair');
  else if (act === 'freq') { mem.freq = el.dataset.f; save(); schedule(); show(viewSheet()); }
  else if (act === 'pick' && quiz && quiz.picked == null) {
    quiz.picked = +el.dataset.i;
    const ok = quiz.q.choices[quiz.picked] === quiz.q.good;
    if (ok) quiz.okCount++;
    record(quiz.q.a, ok);
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
    const r = await fetch('data/adjectifs.json', { cache: 'no-cache' });
    ADJ = (await r.json()).adjectifs;
  } catch { return; } // hors ligne sans cache : pas de bulle
  const bubble = document.createElement('button');
  bubble.id = 'memo-bubble';
  bubble.setAttribute('aria-label', 'Antisèche い / な');
  bubble.innerHTML = 'い<small>/</small>な';
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
