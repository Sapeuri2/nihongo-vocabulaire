// Parcours complet : toutes les étapes disponibles (leçons, tests, examens), au format téléphone.
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');
const [,, base, root, shots, scheme = 'light'] = process.argv;
const manifest = JSON.parse(readFileSync(`${root}/data/manifest.json`, 'utf8'));
const items = {};
for (const f of manifest.blocks) {
  const b = JSON.parse(readFileSync(`${root}/${f}`, 'utf8'));
  for (const l of b.lessons) for (const e of l.exercises) items[e.id] = e;
  for (const e of [...(b.test || []), ...(b.examTest || [])]) items[e.id] = e;
}
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const ctx = await browser.newContext({ viewport: { width: 375, height: 740 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, colorScheme: scheme });
await ctx.addInitScript(() => { if (!localStorage.getItem('nv-memo-v1')) localStorage.setItem('nv-memo-v1', '{"freq":"jamais"}'); });
const page = await ctx.newPage();
const errors = [];
page.on('pageerror', e => errors.push(`pageerror: ${e.message}`));
page.on('console', m => { if (m.type() === 'error') errors.push(`console: ${m.text()}`); });
const overflow = [];
async function check(name, shot) {
  const o = await page.evaluate(() => {
    const w = document.documentElement.clientWidth;
    const bad = [...document.querySelectorAll('body *')].filter(el => el.getBoundingClientRect().right > w + 1).map(el => el.tagName + '.' + el.className).slice(0, 5);
    return { sw: document.documentElement.scrollWidth, w, bad };
  });
  if (o.sw > o.w || o.bad.length) overflow.push(`${name}: ${o.sw}>${o.w} ${o.bad.join(' ')}`);
  if (shot) await page.screenshot({ path: `${shots}/${scheme}-${name}.png`, fullPage: true });
}
const unknown = new Set();
async function runSession(label) {
  let n = 0;
  while (await page.$('.exercise')) {
    const id = await page.getAttribute('.exercise', 'data-id');
    const it = items[id];
    if (!it) { unknown.add(id); }
    if (it?.type === 'order') {
      for (const i of it.tokens.map((_, i) => i)) await page.click(`.bank [data-act="place"][data-i="${i}"]`);
      await page.click('[data-act="check"]');
    } else await page.click(`[data-act="pick"][data-i="${it ? it.a : 0}"]`);
    await check(`${label}-${n}`, false);
    await page.click('[data-act="next"]');
    n++;
  }
  const score = await page.textContent('.big-score');
  await check(`${label}-resultat`, false);
  return `${label} : ${n} questions, ${score}`;
}
const report = [];
await page.goto(base);
for (let step = 0; step < 80; step++) {
  await page.goto(base + '#/');
  await page.waitForSelector('.hero');
  const btn = await page.$('.hero [data-act="step"]');
  if (!btn) break;
  const label = (await btn.textContent()).replace('Continuer', '').trim();
  await btn.click();
  await page.waitForSelector('.lesson, .exercise');
  if (await page.$('.lesson')) {
    const num = label.match(/Leçon (\d+)/)?.[1];
    await check(`lecon${num}`, +num >= 99);
    await page.click('[data-act="lesson-ex"]');
    await page.waitForSelector('.exercise');
    report.push(await runSession(`L${num}`));
  } else report.push(await runSession(label.replace(/\W+/g, '_').slice(0, 40)));
}
await page.goto(base + '#/');
await check('accueil-fin', true);
console.log(report.join('\n'));
console.log('Exercices inconnus (attendus : rappels et points clés) :', [...unknown].join(' ') || 'aucun');
console.log('Débordements :', overflow.length ? overflow.join('\n') : 'aucun');
console.log('Erreurs JS :', errors.length ? errors.join('\n') : 'aucune');
await browser.close();
