// Vérifie le contenu du cours : node tools/verifier.mjs
import { readFileSync } from 'node:fs';
import { KANJI } from './kanji.mjs';

const root = new URL('../', import.meta.url);
const read = p => JSON.parse(readFileSync(new URL(p, root), 'utf8'));

const errors = [];
const err = (where, msg) => errors.push(`${where} : ${msg}`);

const manifest = read('data/manifest.json');
const lessonOrder = new Map(); // id → numéro
const ids = new Set();
let n = 0;
let count = 0;

const plain = s => s.replace(/\{([^|{}]+)\|[^{}]+\}/g, '$1');
const reading = s => s.replace(/\{[^|{}]+\|([^{}]+)\}/g, '$1');
const seenWords = new Map(); // mot → leçon

// Kanji hors N5/N4 (voir tools/kanji.mjs).
function checkKanji(where, obj) {
  const bad = [...new Set(JSON.stringify(obj).match(/\p{Script=Han}/gu) || [])].filter(k => !KANJI.has(k));
  if (bad.length) err(where, `kanji hors N5/N4 : ${bad.join(' ')} (écrire en kana ou l'ajouter à tools/kanji.mjs)`);
}

// Tableau de mots d'une leçon de vocabulaire.
function checkWords(where, words) {
  if (!Array.isArray(words) || words.length < 5) return err(where, 'il faut au moins 5 mots (words)');
  for (const w of words) {
    const at = `${where} ${w.jp}`;
    if (!w.jp || !w.kana || !w.fr) { err(at, 'mot incomplet (jp, kana, fr)'); continue; }
    checkText(at, w.jp);
    checkText(at, w.fr);
    if (!/^[\p{Script=Hiragana}\p{Script=Katakana}ー〜・ ]+$/u.test(w.kana)) err(at, `lecture pas en kana : ${w.kana}`);
    // Les furigana du mot doivent redonner exactement sa lecture.
    if (reading(w.jp) !== w.kana) err(at, `lecture « ${w.kana} » ≠ furigana « ${reading(w.jp)} »`);
    const key = `${plain(w.jp)}|${w.kana}`;
    if (seenWords.has(key)) err(at, `mot déjà vu en ${seenWords.get(key)}`);
    seenWords.set(key, where);
    if (!w.ex?.jp || !w.ex?.fr) { err(at, 'phrase d’exemple manquante (ex.jp, ex.fr)'); continue; }
    checkText(at, w.ex.jp);
    checkText(at, w.ex.fr);
    // La phrase doit contenir le mot (verbes et adjectifs en い : le radical suffit).
    const p = plain(w.jp).replace(/^〜/, '');
    const stem = /[うくぐすつぬぶむるい]$/.test(p) && p.length > 1 ? p.slice(0, -1) : p;
    if (!plain(w.ex.jp).includes(stem)) err(at, `l'exemple ne contient pas le mot : ${w.ex.jp}`);
  }
}

function checkText(where, s) {
  if (typeof s !== 'string') return;
  const stripped = s.replace(/\{[^|{}]+\|[^{}]+\}/g, '');
  if (/[{}|]/.test(stripped)) err(where, `balisage furigana mal formé : ${s}`);
}

function checkExercise(where, ex, maxLesson) {
  if (!ex.id) return err(where, 'exercice sans id');
  where = `${where} ${ex.id}`;
  if (ids.has(ex.id)) err(where, 'id en double');
  ids.add(ex.id);
  count++;
  for (const k of ['q', 'jp', 'fr', 'explain']) checkText(where, ex[k]);
  for (const u of ex.uses || []) {
    if (!lessonOrder.has(u)) err(where, `uses : leçon inconnue ou pas encore vue ${u}`);
    else if (lessonOrder.get(u) > maxLesson) err(where, `uses : ${u} vient après cet exercice`);
  }
  if (ex.type === 'choice') {
    if (!Array.isArray(ex.choices) || ex.choices.length < 2) err(where, 'il faut au moins 2 choix');
    else {
      if (!(ex.a >= 0 && ex.a < ex.choices.length)) err(where, `réponse a=${ex.a} hors limites`);
      if (new Set(ex.choices).size !== ex.choices.length) err(where, 'choix en double');
      // Furigana masqués : deux choix ne doivent pas s'afficher pareil (ex. {来|き}て / {来|く}て).
      if (new Set(ex.choices.map(plain)).size !== ex.choices.length) err(where, 'choix identiques sans furigana : écrire en kana');
      ex.choices.forEach(c => checkText(where, c));
    }
    const blanks = (ex.jp || '').split('＿').length - 1;
    if (blanks > 1) err(where, 'un seul trou ＿ par phrase');
    if (!ex.jp && !ex.q) err(where, 'ni jp ni q');
  } else if (ex.type === 'order') {
    if (!Array.isArray(ex.tokens) || ex.tokens.length < 2) err(where, 'il faut au moins 2 mots');
    else {
      ex.tokens.forEach(t => checkText(where, t));
      const key = a => [...a].sort().join('\u0000');
      for (const alt of ex.alt || []) if (key(alt) !== key(ex.tokens)) err(where, 'une variante (alt) n’a pas les mêmes mots');
    }
    if (!ex.fr) err(where, 'traduction fr manquante');
  } else err(where, `type inconnu ${ex.type}`);
}

for (const file of manifest.blocks) {
  const b = read(file);
  for (const l of b.lessons) {
    if (lessonOrder.has(l.id)) err(file, `leçon en double ${l.id}`);
    lessonOrder.set(l.id, ++n);
    checkText(l.id, l.title);
    checkKanji(l.id, l);
    (l.intro || []).forEach(p => checkText(l.id, p));
    checkWords(l.id, l.words);
    for (const s of l.sections || []) {
      checkText(l.id, s.h);
      (s.p || []).forEach(p => checkText(l.id, p));
      (s.ex || []).forEach(e => { checkText(l.id, e.jp); checkText(l.id, e.fr); });
      (s.vocab || []).forEach(v => checkText(l.id, v.jp));
    }
    (l.pieges || []).forEach(p => checkText(l.id, p));
    for (const ex of l.exercises || []) checkExercise(l.id, ex, n);
    if ((l.exercises || []).length < 5) err(l.id, 'moins de 5 exercices');
  }
  // Un test peut aussi réutiliser des leçons des blocs précédents.
  for (const ex of b.test || []) checkExercise(`${b.id} test`, ex, n);
  checkKanji(`${b.id} test`, b.test || []);
}

if (errors.length) {
  console.error(errors.join('\n'));
  console.error(`\n${errors.length} problème(s).`);
  process.exit(1);
}
console.log(`OK : ${n} leçons, ${seenWords.size} mots, ${count} exercices.`);
