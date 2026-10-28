# 語彙 Vocabulaire japonais

Appli web perso pour apprendre le vocabulaire japonais (JLPT N5 → N4, puis N3), en français.
Même moteur que l'appli de grammaire (`nihongo-grammaire`, voir [MOTEUR.md](MOTEUR.md)), mais l'accent est mis sur **le mot utilisé dans une phrase**, pas sur des flashcards.

- Leçon (≈ 15 mots d'un même thème, une phrase d'exemple par mot, pièges) → exercices → leçon suivante.
- Exercices : mot dans une phrase à trous, sens ↔ mot, lecture des kanji, mots proches, contraires, remise en ordre.
- Toutes les 5 leçons : un test du bloc (80 % pour continuer, 30 questions).
- Toutes les 10 leçons : un examen intermédiaire (40 questions) ; toutes les 20 : un grand examen (60).
- Tests et examens mélangent environ 25 % de rappels des leçons précédentes, et des questions de réflexion propres à chaque examen (`examTest`).
- Les erreurs reviennent en fin de série, puis en révision (répétition espacée).
- Progression synchronisée entre appareils via un Gist GitHub privé (optionnel).
- Fonctionne hors ligne une fois chargée ; installable sur l'écran d'accueil du téléphone.

Le plan complet des leçons est dans [PROGRAMME.md](PROGRAMME.md).

## Cohabitation avec l'appli de grammaire

Les deux applis sont sur le même domaine (`sapeuri2.github.io`) et ne doivent pas se marcher dessus :

| | Grammaire | Vocabulaire |
|---|---|---|
| Progression (localStorage) | `ng-state-v1` | `nv-state-v1` |
| Réglages de synchro | `ng-sync` | `nv-sync` |
| Fichier dans le Gist | `nihongo-grammaire-progression.json` | `nihongo-vocabulaire-progression.json` |
| Caches hors ligne | `cache:/nihongo-grammaire/:…` | `cache:/nihongo-vocabulaire/:…` (seuls ceux-là sont nettoyés) |

Les clés et le nom du Gist sont dans `js/config.js` : **ne jamais les changer** une fois l'appli en ligne.
La même clé GitHub (droit « gist ») peut servir aux deux applis : chacune crée son propre Gist.

## Moteur partagé

`js/app.js`, `js/state.js`, `js/sync.js`, `js/text.js`, `css/style.css`, `sw.js`, `tools/verifier.mjs` viennent du dépôt grammaire :
**ne pas les modifier ici**. Mise à jour : `bash tools/maj-moteur.sh` (voir [MOTEUR.md](MOTEUR.md)).
Propres à cette appli : `js/config.js`, `css/theme.css` (bleu), `index.html`, `manifest.webmanifest`, `icons/`, `data/`,
`tools/verifier-appli.mjs`, `tools/kanji.mjs`, et la bulle « い ou な ? » (`js/memo.js`, `css/memo.css`, `data/rappels.json`).

## Bulle « い / な / て » : adjectifs, passé poli, forme て

Une bulle **い/な** en bas à droite, sur toutes les pages, ouvre une antisèche illustrée (conjugaison des adjectifs en い et en な, faux い, passé poli でした / ました / ありました / かったです, forme て des verbes, erreurs interdites) et un quiz éclair de 10 questions.
Les thèmes (い / な, passé poli, forme て) se cochent dans la bulle : on peut ne travailler que la forme て.
Dans chaque fenêtre de la bulle, un bouton **漢** affiche ou masque les furigana (même réglage que le bouton 漢 du haut).
Des **rappels surprise** surgissent pendant l'utilisation (souvent / normal / rarement / jamais, réglable dans la bulle) et ne se ferment qu'après une bonne réponse.
Les questions sont générées depuis `data/rappels.json` (adjectifs, noms et verbes pour le passé, 63 verbes pour la forme て, phrases fixes) : les mauvais choix sont les erreurs typiques (高いじゃありません, きれくない, 寒いでした, 降りでした, 高かったでした, いくない…), et ce qui est raté revient plus souvent.
Statistiques et réglage restent sur l'appareil (`nv-memo-v1`), sans synchro.
Pour ajouter un adjectif, un nom, un verbe ou une phrase : `data/rappels.json` (lire la note en tête du fichier : ne jamais proposer comme erreur une forme qui existe, comme 大きな ou 上手い).

## Lancer en local

```sh
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

## Ajouter du contenu

1. Créer `data/n5/blocXX.json` sur le modèle de `data/n5/bloc01.json`.
2. L'ajouter à la fin de la liste `blocks` dans `data/manifest.json`.
3. Vérifier : `node tools/verifier.mjs` (lance aussi `tools/verifier-appli.mjs`).
4. Le bloc qui précède un examen (blocs 2, 4, 6…) reçoit aussi ses questions de réflexion dans `examTest`.

Les identifiants (leçons, exercices) ne doivent jamais changer une fois publiés : la progression y est rattachée.

### Format d'une leçon

```jsonc
{ "id": "v5-01", "title": "Les gens",
  "words": [
    { "jp": "{大人|おとな}", "kana": "おとな", "fr": "adulte",
      "ex": "{大人|おとな}は{五百円|ごひゃくえん}です。", "exFr": "500 yens pour les adultes." }
  ],
  "sections": [ /* facultatif, après le tableau : comme dans la grammaire (h, p, ex, vocab) */ ],
  "pieges": ["mots proches, faux amis, lectures irrégulières…"],
  "exercises": [ /* voir ci-dessous */ ] }
```

### Format d'un exercice

```jsonc
// Choix (phrase à trous ＿, ou question dans "q")
{ "id": "v5-02-e02", "type": "choice", "uses": ["v5-01"],
  "q": "consigne (facultatif)", "jp": "{駅|えき}で{友|とも}だちに＿。", "fr": "traduction",
  "choices": ["{会|あ}います", "{見|み}ます", "{起|お}きます", "{飲|の}みます"], "a": 0, "explain": "explication" }

// Remise en ordre
{ "id": "v5-02-e17", "type": "order", "fr": "traduction",
  "tokens": ["コンビニ", "で", "{水|みず}", "を", "{買|か}います"],
  "alt": [["{水|みず}", "を", "コンビニ", "で", "{買|か}います"]] }
```

- `{漢字|かんじ}` affiche des furigana, `**texte**` met en gras.
- `words` s'affiche en tableau Mot / Lecture / Sens, avec la phrase d'exemple sous chaque mot. La colonne Lecture suit le réglage des furigana.
- Phrase à trous : la traduction reste cachée (« Voir la traduction ») jusqu'à la réponse (`hideBlankTranslation` dans `js/config.js`).
- Lecture d'un kanji : écrire le mot **sans** furigana dans `q` (`Comment se lit **大人** ?`), sinon la réponse est affichée.
- `uses` : les leçons **précédentes** que l'exercice mobilise en plus de la sienne.

### Règles de qualité (à respecter pour chaque exercice)

1. **Une seule bonne réponse en japonais.** Chaque mauvais choix doit rendre la phrase japonaise fausse ou absurde (ou incohérente avec le contexte japonais), sans compter sur la traduction. Si un autre mot marche aussi (たくさん / みんな, {行|い}く / {帰|かえ}る…), on change le distracteur ou on ajoute du contexte japonais (une deuxième phrase, から, un temps du verbe…).
2. **Du japonais naturel.** Pas de {私|わたし}は inutile, pas de répétitions maladroites, pas deux fois la même particule (で…で).
3. **Remise en ordre : tous les ordres naturels sont acceptés** (`alt`). Éviter les éléments qui peuvent se placer n'importe où.
4. **Nuances** : décrire la situation dans la consigne plutôt que de laisser la traduction trancher.
5. **Pas deux choix qui s'affichent pareil sans furigana** (écrire alors en kana).
6. **Kanji N5/N4 seulement** (liste dans `tools/kanji.mjs`, quelques N3 tolérés) ; sinon le mot s'écrit en kana.
7. **Grammaire de niveau N5** dans les phrases d'exemple et les exercices.

`tools/verifier-appli.mjs` contrôle en plus : lecture (`kana`) = furigana du mot, phrase d'exemple qui contient le mot, mot déjà enseigné dans une autre leçon, kanji hors liste.
