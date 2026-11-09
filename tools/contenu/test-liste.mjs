// Test « Ma liste » au format téléphone : ☆ dans le tableau de mots et en correction,
// page 📌, révision de la liste, export Anki.
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
const [,, out, scheme = 'light'] = process.argv;
const items = {};
for (const f of JSON.parse(readFileSync('data/manifest.json', 'utf8')).blocks) {
  const b = JSON.parse(readFileSync(f, 'utf8'));
  for (const l of b.lessons) for (const e of l.exercises) items[e.id] = e;
}
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: scheme, acceptDownloads: true });
await ctx.addInitScript(() => {
  if (!localStorage.getItem('nv-memo-v1')) localStorage.setItem('nv-memo-v1', '{"freq":"jamais"}');
  if (!localStorage.getItem('nv-state-v1')) {
    const lessons = {}; for (let i = 1; i <= 40; i++) lessons[`v5-${String(i).padStart(2, '0')}`] = { done: true, best: 1, t: 1 };
    localStorage.setItem('nv-state-v1', JSON.stringify({ v: 1, resetAt: 0, lessons, tests: {}, items: {}, settings: { furigana: true, t: 0 } }));
  }
});
const p = await ctx.newPage();
const errors = [];
p.on('pageerror', e => errors.push(e.message));
p.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
p.on('dialog', d => d.accept());
const overflow = async name => {
  const o = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, w: document.documentElement.clientWidth,
    bad: [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1).map(e => e.tagName + '.' + e.className).slice(0, 4) }));
  console.log(`${name} : largeur ${o.sw}/${o.w}`, o.bad.length ? 'DÉBORDE ' + o.bad.join(' ') : 'sans débordement');
};
const liste = () => p.evaluate(() => {
  const d = JSON.parse(localStorage.getItem('nihongo-ma-liste-v1') || '{}');
  const mots = Array.isArray(d.mots) ? d.mots : Object.values(d.mots || d.items || d.words || {});
  return mots.map(x => `${x.id} [${(x.app || []).join(',')} · ${x.src}]`);
});
for (const id of ['v5-18', 'v5-16', 'v5-33']) {
  await p.goto(`http://localhost:8765/#/lecon/${id}`); await p.waitForSelector('.words');
  await overflow(`leçon ${id.slice(3)} (tableau des mots)`);
}
await p.goto('http://localhost:8765/#/lecon/v5-18'); await p.waitForSelector('.words');
const stars = await p.$$('.words [data-act="star"]');
await stars[0].click(); await stars[3].click(); await p.waitForTimeout(300);
await (await p.$('.words')).screenshot({ path: `${out}/${scheme}-words18.png` });
console.log('après ☆ dans le tableau :', await liste(), '| étoiles allumées :', await p.$$eval('.words .star.on', x => x.length));
await p.click('[data-act="lesson-ex"]'); await p.waitForSelector('.exercise');
for (let k = 0; k < 3; k++) {
  const it = items[await p.getAttribute('.exercise', 'data-id')];
  if (it?.type === 'order') { for (const i of it.tokens.map((_, i) => i)) await p.click(`.bank [data-act="place"][data-i="${i}"]`); await p.click('[data-act="check"]'); }
  else await p.click(`[data-act="pick"][data-i="${it ? it.a : 0}"]`);
  await p.waitForTimeout(150);
  const s = await p.$('main [data-act="star"]:not(.on)'); console.log('  ☆ en correction trouvée :', !!s, s ? await s.getAttribute('data-w') : '');
  if (k === 0) { await overflow('correction avec ☆'); await p.screenshot({ path: `${out}/${scheme}-fb.png` }); }
  if (s) await s.click();
  await p.waitForTimeout(200);
  await p.click('[data-act="next"]');
}
console.log('après ☆ en correction :', await liste());
await p.goto('http://localhost:8765/#/liste'); await p.waitForSelector('[data-act="liste-go"]');
await overflow('page 📌'); await p.screenshot({ path: `${out}/${scheme}-liste.png`, fullPage: true });
const [dl] = await Promise.all([p.waitForEvent('download'), p.click('[data-act="liste-anki"]')]);
await dl.saveAs(`${out}/anki.csv`); console.log('export Anki :', dl.suggestedFilename());
await p.click('[data-act="liste-go"]'); await p.waitForSelector('.exercise');
let n = 0;
while (await p.$('.exercise')) {
  if (n === 0) { await overflow('révision de ma liste'); await p.screenshot({ path: `${out}/${scheme}-revision.png` }); }
  await p.click('[data-act="pick"][data-i="0"]'); await p.click('[data-act="next"]'); n++;
}
console.log('révision de ma liste :', n, 'questions,', await p.textContent('.big-score').catch(() => '?'));
await p.goto('http://localhost:8765/#/'); await p.waitForSelector('.hero');
console.log('bouton 📌 :', !!(await p.$('.top .pin')), '| ma bulle :', await p.isVisible('#memo-bubble'), '| bouton 漢 :', !!(await p.$('.top .furi-toggle')));
await p.screenshot({ path: `${out}/${scheme}-accueil.png` });
console.log('Erreurs JS :', errors.length ? errors.join('\n') : 'aucune');
await b.close();
