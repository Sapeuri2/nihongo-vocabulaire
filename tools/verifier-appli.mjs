// Contrôles propres à l'appli de vocabulaire, lancés automatiquement par tools/verifier.mjs (moteur).
// Chaque leçon a un champ words = [{ jp, kana, fr, ex, exFr }].
import { readFileSync } from 'node:fs';
import { KANJI } from './kanji.mjs';

const root = new URL('../', import.meta.url);
const read = p => JSON.parse(readFileSync(new URL(p, root), 'utf8'));

const errors = [];
const err = (where, msg) => errors.push(`${where} : ${msg}`);
const plain = s => s.replace(/\{([^|{}]+)\|[^{}]+\}/g, '$1').replace(/\*\*/g, '');
const reading = s => s.replace(/\{[^|{}]+\|([^{}]+)\}/g, '$1');
const seenWords = new Map(); // mot → leçon

// Kanji hors N5/N4 (voir tools/kanji.mjs).
function checkKanji(where, obj) {
  const bad = [...new Set(JSON.stringify(obj).match(/\p{Script=Han}/gu) || [])].filter(k => !KANJI.has(k));
  if (bad.length) err(where, `kanji hors N5/N4 : ${bad.join(' ')} (écrire en kana ou l'ajouter à tools/kanji.mjs)`);
}

function checkLesson(l) {
  const words = l.words || [];
  if (words.length < 5) err(l.id, 'il faut au moins 5 mots (words)');
  words.forEach(w => {
    const at = `${l.id} ${w.jp}`;
    if (!w.jp || !w.kana || !w.fr) return err(at, 'mot incomplet (jp, kana, fr)');
    if (!/^[\p{Script=Hiragana}\p{Script=Katakana}ー〜・ ]+$/u.test(w.kana)) err(at, `lecture pas en kana : ${w.kana}`);
    // Les furigana du mot doivent redonner exactement sa lecture.
    if (reading(w.jp) !== w.kana) err(at, `lecture « ${w.kana} » ≠ furigana « ${reading(w.jp)} »`);
    const key = `${plain(w.jp)}|${w.kana}`;
    if (seenWords.has(key)) err(at, `mot déjà vu en ${seenWords.get(key)}`);
    seenWords.set(key, l.id);
    // La phrase doit contenir le mot (verbes et adjectifs en い : le radical suffit).
    if (!w.ex || !w.exFr) return err(at, 'phrase d’exemple manquante (ex, exFr)');
    const p = plain(w.jp).replace(/^〜/, '');
    const stem = /[うくぐすつぬぶむるい]$/.test(p) && p.length > 1 ? p.slice(0, -1) : p;
    if (!plain(w.ex).includes(stem)) err(at, `la phrase d'exemple ne contient pas le mot : ${w.ex}`);
  });
}

const manifest = read('data/manifest.json');
for (const file of manifest.blocks) {
  const b = read(file);
  for (const l of b.lessons) {
    checkLesson(l);
    checkKanji(l.id, l);
  }
  checkKanji(`${b.id} test`, b.test || []);
  checkKanji(`${b.id} examen`, b.examTest || []);
}

if (errors.length) {
  console.error(errors.join('\n'));
  console.error(`\n${errors.length} problème(s).`);
  process.exit(1);
}
console.log(`OK (vocabulaire) : ${seenWords.size} mots.`);
