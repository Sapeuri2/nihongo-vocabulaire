# Passation — appli Vocabulaire (nihongo-vocabulaire)

Rapport écrit par l'instance Claude Code du vocabulaire, pour l'**agent central** qui reprend tout le code
(moteur commun et code des trois applis). À lire avec `README.md`, `MOTEUR.md` et `PROGRAMME.md`.

## 1. Identité

- Dépôt : https://github.com/Sapeuri2/nihongo-vocabulaire, branche `main`, publiée par GitHub Pages à la racine.
  J'ai aussi poussé chaque commit sur la branche `ccr-e2a604b3-9okw8y` (ma branche de travail, copie de `main`).
- Site : https://sapeuri2.github.io/nihongo-vocabulaire/ . Je n'ai pas pu l'ouvrir depuis mon conteneur
  (réseau fermé vers github.io) : l'adresse suit la règle de GitHub Pages, et l'utilisateur m'a dit avoir testé
  l'appli en ligne, mais je ne l'ai pas vérifié moi-même.
- Dernier commit avant ce rapport : `fe4f244` (2026-11-05), « Moteur 720473c : Ma liste commune aux applis et
  suite automatique ». Le commit de ce rapport ajoute seulement `PASSATION.md` et `tools/contenu/`.
- **Version du moteur : `720473c` appliquée** (autoNext et Ma liste), avec `appId: 'vocabulaire'`,
  `listeEnabled: true`, `autoNext: 0` dans `js/config.js`.
- **Fichiers du moteur modifiés : aucun.** Vérifié le 2026-11-09 octet par octet : `js/app.js`, `js/state.js`,
  `js/sync.js`, `js/text.js`, `js/liste.js`, `css/style.css`, `sw.js`, `tools/verifier.mjs`, `tools/maj-moteur.sh`
  et `MOTEUR.md` sont identiques à ceux de `nihongo-grammaire@720473c`.
- **Code propre à l'appli : oui**, la bulle « い/な/て » (`js/memo.js`, `css/memo.css`, données dans
  `data/rappels.json`). Elle est expliquée en détail au § 3 et au § 4.

## 2. L'utilisateur et sa méthode (ce que je sais pour le vocabulaire)

- Francophone, prépare le JLPT : N5 → N4, puis N3. Il me parle en français et veut des réponses **simples**.
- Appli perso, gratuite, statique (GitHub Pages + Gist privé pour la synchro), hors ligne, en français.
- Le vocabulaire doit être appris **dans des phrases**, pas en cartes : il utilise déjà Anki pour les kanji.
- ~15 mots par leçon, regroupés par thème, les plus utiles d'abord. Page de leçon = tableau des mots
  (mot, lecture, sens) + une phrase d'exemple par mot + pièges. Thème bleu, icône 語彙, titre « Vocabulaire japonais ».
- Types d'exercices voulus : phrase à trous (**le plus important**), sens ↔ mot, lecture des kanji, mots proches,
  contraires et paires, remise en ordre ; les exercices réutilisent les leçons précédentes (`uses`).
- Exigences fortes sur la qualité (voir § 6) : il veut que je relise **chaque exercice un par un** avant de livrer.
- Isolation obligatoire avec la grammaire (même domaine) : clés `nv-…`, Gist à part. « Ne change JAMAIS ces clés
  une fois l'appli en ligne. »
- Moteur commun : « ne modifie pas les fichiers du moteur ici ; si une amélioration est nécessaire, décris-la-moi ».
  Je l'ai toujours respecté (mes propositions passaient par lui vers l'instance grammaire).
- Il voulait **ma propre bulle** pour marteler les adjectifs い/な, le passé poli (でした / ました / ありました /
  かったです) et la conjugaison des verbes (groupes, dictionnaire ↔ ます, forme て) avec **beaucoup de verbes**.
  « Garde ta bulle », mais **une bulle par appli** : pas de champ `focus` dans `data/manifest.json`
  (le point clé du moteur reste pour la grammaire ; il alterne entre les deux applis).
- Les rappels surprise ne se ferment **qu'après une bonne réponse** ; il voulait un bouton 漢 dans la fenêtre surprise.
- Leçon 5 : ses 35 exercices sont voulus (spécial い/な), ne pas les réduire. Leçon 2 : 38 exercices (formes des verbes).
- Il écrit parfois plusieurs idées dans un même message, ou se trompe d'appli (« j'étais dans vocabulaire mdr ») :
  il faut séparer les demandes et vérifier de quelle appli il parle.
- Sa progression réelle (où il en est) : **je ne sais pas**. Elle est dans son navigateur et son Gist.

## 3. Ce que fait l'appli

- Parcours du moteur : leçon (tableau des mots + sections + pièges) → exercices (70 %) → toutes les 5 leçons un
  **test de bloc** (30 q., 80 %) → après les blocs 2, 6, 10, 14… un **examen intermédiaire** (40 q.)
  (`miniExamEvery: 2`) → après les blocs 4, 8… un **grand examen** (60 q.) (`examEvery: 4`).
  Tests et examens : ~25 % de rappels + questions de réflexion (`examTest`, dans les blocs 2, 4, 6, 8).
- Exercices : `choice` (QCM, phrase à trous avec ＿, sens ↔ mot, lecture, contraires, « une seule phrase correcte »)
  et `order` (remise en ordre, variantes `alt`).
- Phrases à trous : traduction cachée jusqu'à la réponse (`hideBlankTranslation: true`).
- Contenu actuel : **N5 complet**, 8 blocs, 40 leçons (`v5-01` à `v5-40`), 591 mots, 792 exercices de leçons
  (710 `choice`, 82 `order`), 128 questions de tests, 60 `examTest`. Plan N4 (leçons 41 à 80) dans `PROGRAMME.md`, pas commencé.
- Moteur : répétition espacée, reprise de série, bouton 漢, 🔥, synchro Gist, **Ma liste** (📌, commune aux 3 applis).
- **Bulle « い/な/て »** (propre à l'appli, en bas à droite sur toutes les pages) :
  - antisèche illustrée : adjectifs い / な, faux い (きれい, きらい…), passé poli, verbes (groupe d'abord,
    ます, dictionnaire, て, erreurs interdites) ;
  - quiz éclair de 10 questions ; thèmes à cocher (い/な, passé poli, verbes) ;
  - rappels surprise pendant l'utilisation (souvent / normal / rarement / jamais), qui ne se ferment qu'après une bonne réponse ;
  - bouton 漢 dans chaque fenêtre (il clique le bouton 漢 du moteur) ;
  - données : `data/rappels.json` = 42 adjectifs, passé (5 noms, 11 verbes), 8 phrases, **65 verbes** (5 questions
    par verbe : dict → ます, ます → dict, dict → て, ます → て, groupe) et 20 phrases de verbes ;
    les mauvais choix sont des erreurs typiques, jamais une forme qui existe ;
  - statistiques et réglages sur l'appareil seulement (`nv-memo-v1`), **pas synchronisés**.
- Réglages de `js/config.js` : `storageKey 'nv-state-v1'`, `syncKey 'nv-sync'`,
  `gistFile 'nihongo-vocabulaire-progression.json'`, `tokenName 'nihongo-vocabulaire'`, `appId 'vocabulaire'`,
  `listeEnabled true`, `autoNext 0`, `lessonPass 0.7`, `testPass 0.8`, `lessonRecall 5`, `testSize 30`,
  `miniExamSize 40`, `examSize 60`, `recallShare 0.25`, `reviewSize 20`, `drillSize 15`, `maxRetries 2`,
  `hideBlankTranslation true`, `focusEvery 4`, `focusInTests 3`, `focusChallengeSize 10` (ces trois derniers inutilisés : pas de `focus`).

## 4. Architecture (fichiers qui ne sont pas du moteur)

| Fichier | Rôle |
| --- | --- |
| `js/config.js` | Clés de stockage et réglages pédagogiques (ci-dessus). |
| `css/theme.css` | Couleurs bleues (`--accent #2a5fa8`, sombre `#6ea6f0`). |
| `index.html` | Charge en plus `css/memo.css` et `js/memo.js` (après `js/app.js`). |
| `manifest.webmanifest`, `icons/` | Nom « Vocabulaire japonais », 語彙, bleu. |
| `js/memo.js` (~540 lignes) | La bulle い/な/て : antisèche, quiz, rappels surprise, statistiques (`nv-memo-v1`). |
| `css/memo.css` | Style de la bulle (pastille en bas à droite, fiches colorées, tableaux de conjugaison). |
| `data/manifest.json` | `examEvery 4`, `miniExamEvery 2`, liste des 8 blocs. **Pas de `focus`.** |
| `data/n5/bloc01.json` … `bloc08.json` | Le contenu (leçons avec `words`, `sections`, `pieges`, `exercises` ; `test` ; `examTest`). |
| `data/rappels.json` | Données de la bulle (lire la note `_` en tête du fichier). |
| `tools/verifier-appli.mjs` | Contrôles propres au vocabulaire, lancés par `tools/verifier.mjs` (voir § 7). |
| `tools/kanji.mjs` | Liste des kanji N5 + N4 + tolérés (`TOLERES`). |
| `tools/contenu/` | Mes générateurs et tests (voir § 7). Ajouté pour la passation : avant, ils étaient dans mon dossier temporaire. |
| `README.md`, `PROGRAMME.md`, `PASSATION.md` | Doc, plan des 80 leçons, ce rapport. |

**Écarts avec le moteur commun :**
- `js/memo.js` dépend du moteur : il importe `esc` et `rich` de `js/text.js`, clique `.top .furi-toggle`,
  lit et bascule la classe `body.nofuri`, réutilise les classes `.btn`, `.btn.primary`, `.choice`, `.fb`.
  Si l'agent central renomme ces éléments, la bulle casse.
- `js/memo.js` écoute `keydown` sur `window` en phase de capture et bloque la propagation quand sa fenêtre est
  ouverte (1–4 = choix, Entrée = suivant), pour ne pas déclencher les raccourcis du moteur en dessous.
- `css/memo.css` met `main { padding-bottom: 96px; }` (au lieu de 88 px) pour laisser la place à la pastille.
- `sw.js` ne précharge pas `js/memo.js`, `css/memo.css`, `data/rappels.json` ni `data/n5/*` : ils entrent dans le
  cache à la première visite en ligne (stratégie « réseau d'abord » qui met tout en cache).
- Format de leçon : le vocabulaire utilise le champ `words` du moteur (`{ jp, kana, fr, ex, exFr }`),
  ajouté au moteur à ma demande le 2026-10-21.

## 5. Données à ne jamais casser

- localStorage (domaine `sapeuri2.github.io`, partagé avec grammaire et kanji) :
  `nv-state-v1` (progression), `nv-state-v1:seance` (série en cours), `nv-sync` (clé GitHub + id du Gist),
  `nv-memo-v1` (bulle), et les clés **communes** `nihongo-ma-liste-v1`, `nihongo-ma-liste-gist`.
- Gist : `nihongo-vocabulaire-progression.json` (progression) ; `nihongo-ma-liste.json` (commun aux 3 applis).
- Caches hors ligne : `cache:/nihongo-vocabulaire/:…`. Les anciens `nv-v1` / `ng-v1` sont supprimés par `sw.js`.
- Identifiants (la progression y est rattachée, **ne jamais les changer ni les réutiliser**) :
  leçons `v5-NN` (N5 : 01 à 40), exercices `v5-NN-eNN`, tests `v5-b0N-tNN`, questions d'examen `v5-x0N-NN`
  (x01 = examen intermédiaire 1, x02 = grand examen 1, x03 = examen intermédiaire 2, x04 = grand examen 2).
  Pour le N4, j'avais prévu `v4-41`… (même logique) : **pas encore décidé**, à confirmer avec l'utilisateur.

## 6. Règles de qualité du contenu

- **Une seule bonne réponse en japonais** : chaque mauvais choix rend la phrase fausse ou absurde **sans la traduction**
  (elle est cachée). Une consigne indispensable va dans `q`, jamais dans `fr`.
- Attention aux pièges qui sont de vraies formes ou de vrais mots : 上手い, 大きな, もらして, うちにつきます (着く),
  テレビを切る, 来月に… Ces cas m'ont déjà piégé ; je les ai tous retirés.
- Pas deux choix identiques une fois les furigana masqués (ex. {四人|よにん} / {四人|よんにん}, {降|ふ}りました / {降|お}りました).
- Japonais naturel : pas de 私は inutile, pas de répétitions maladroites.
- Remise en ordre : tous les ordres naturels sont dans `alt`.
- Kanji N5/N4 seulement (`tools/kanji.mjs`), N3 seulement si indispensable (`TOLERES`). Sinon le mot est en kana :
  にわ, かいだん, 〜かい (étage), ゆき, ねつ, かえす, しめる, おぼえる, わすれる, ことば, こうばん, ゆうびんきょく,
  おさら, しお, ほんとうに, たんじょうび, おそい…
- Chaque mot : `jp` avec furigana `{漢字|かんじ}`, `kana` = lecture exacte, `fr` court (le tableau est étroit sur téléphone),
  une phrase d'exemple `ex` qui contient le mot, avec sa traduction `exFr`.
- Un mot n'apparaît qu'une fois dans tout le cours (même `jp` + même `kana`).
- Avant de livrer : relire chaque exercice **sans traduction**, un par un (`tools/contenu/revue.py`).

## 7. Outils et façon de travailler

- `node tools/verifier.mjs` : moteur + `tools/verifier-appli.mjs`, qui vérifie les mots (champs remplis, lecture en kana
  = furigana, pas de doublon, la phrase d'exemple contient le mot) et les kanji hors liste (leçons, tests, examens, `rappels.json`).
- `tools/contenu/` (Python 3 et Node, sans dépendance à installer) :
  - `bloc04.py` … `bloc08.py` + `common.py` : générateurs des blocs 4 à 8 (`W` mot, `C` QCM / trou, `O` remise en ordre).
    Usage : `python3 tools/contenu/bloc05.py data/n5/bloc05.json && python3 tools/contenu/fmt.py data/n5/bloc05.json`.
    Ils redonnent **exactement** les JSON publiés (vérifié le 2026-11-09).
  - Les blocs 1 à 3 n'ont pas de générateur à jour : leur JSON a été corrigé à la main, **c'est le JSON qui fait foi**.
  - `fmt.py` : mise en forme compacte des JSON (une ligne par objet court).
  - `revue.py data/n5/blocNN.json` : liste chaque exercice sans furigana, bonne réponse et pièges, pour la relecture.
  - `parcours.mjs` : tout le parcours dans Chromium au format téléphone (toutes les étapes, débordements, erreurs JS).
    Usage : `python3 -m http.server 8765` puis `node tools/contenu/parcours.mjs http://localhost:8765/ . <dossier-captures> [light|dark]`.
  - `test-liste.mjs` : test de « Ma liste » à 390 px (☆ tableau et correction, page 📌, révision, export Anki).
    Usage : depuis la racine, serveur sur 8765, `node tools/contenu/test-liste.mjs <dossier> [light|dark]`.
  - Les deux tests `.mjs` utilisent les chemins du conteneur Claude Code (`/opt/node22/lib/node_modules/`,
    `/opt/pw-browsers/chromium`).
  - J'avais aussi des tests de la bulle (rappels surprise avec `page.clock`, bouton 漢, verbes) : ils sont restés dans
    mon dossier temporaire et ne sont pas dans le dépôt.
- Méthode : plan du bloc → générateur → `verifier.mjs` → relecture sans traduction → corrections → parcours complet
  en clair et en sombre → mise à jour de `PROGRAMME.md` (blocs cochés, mots déjà vus retirés du plan) → commit en
  français → push sur `main` (et sur ma branche de travail).

## 8. Limites, bugs connus, demandes en attente

- **Moteur, tableau `words` sur téléphone** (signalé 3 fois, pas fait) : les mots en kana se coupent en morceaux
  (おい / しい, むず / かし / い), encore plus depuis la colonne ☆. Proposition : `.words td.jp { white-space: nowrap; }`
  et ne pas répéter la lecture quand le mot est déjà en kana. Pas de défilement horizontal, c'est de la lisibilité.
- **Moteur, Ma liste depuis une phrase à trous** (signalé le 2026-11-05) : le ☆ enregistre la bonne réponse avec,
  comme sens, la traduction de toute la phrase ou l'explication (ex. 帰る → « Faux groupe 2 : … »). La révision et la
  carte Anki deviennent fausses. Proposition : prendre lecture et sens dans les tableaux `words` / `vocab` quand le mot y est.
- Les tableaux `grid` s'affichent en fiches empilées sur téléphone : accepté, j'ai gardé mes tableaux courts.
- La pastille de la bulle (en bas à droite) recouvre un peu le bord droit des gros boutons du bas (« Continuer ») et les toasts.
- `nv-memo-v1` n'est pas synchronisé entre appareils (choix initial ; idée possible).
- Synchro Gist de la progression et de Ma liste : **je ne l'ai pas testée avec son vrai compte**.
- Idées que j'avais : commencer le N4 (bloc 9, plan dans `PROGRAMME.md`) ; ajouter des verbes N4 à la bulle
  (`data/rappels.json`) ; écrire un générateur pour les blocs 1 à 3 à partir des JSON, si on veut tout regénérer.
- Demandes abandonnées : réduire la leçon 5 (il a dit de garder ses 35 exercices) ; points clés du moteur dans le
  vocabulaire (non, une seule bulle par appli).

## 9. Après la passation

Je ne gère plus que le **contenu** : `data/` (blocs, `manifest.json`, `rappels.json`), `PROGRAMME.md`,
la partie « contenu » du `README.md`, et mes outils de contenu (`tools/contenu/`, `tools/verifier-appli.mjs`
et `tools/kanji.mjs` pour les règles du contenu). Je ne touche plus à `js/`, `css/`, `sw.js`, `index.html` ni aux
outils du moteur : toute évolution du code (y compris la bulle `js/memo.js`) passe par l'agent central.
