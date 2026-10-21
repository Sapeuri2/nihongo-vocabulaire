# 語彙 Vocabulaire japonais

Appli web perso pour apprendre le vocabulaire japonais (JLPT N5 → N4, puis N3), en français.
Même moteur que l'appli de grammaire (`nihongo-grammaire`), mais l'accent est mis sur **le mot utilisé dans une phrase**, pas sur des flashcards.

- Leçon (≈ 15 mots d'un même thème, une phrase d'exemple par mot, pièges) → exercices → leçon suivante.
- Exercices : mot dans une phrase à trous, sens ↔ mot, lecture des kanji, mots proches, contraires, remise en ordre.
- Toutes les 5 leçons : un test du bloc (80 % pour continuer). Toutes les 20 leçons : un grand examen.
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
| Caches hors ligne | `ng-…` | `nv-…` (seuls ceux-là sont nettoyés) |

La même clé GitHub (droit « gist ») peut servir aux deux applis : chacune crée son propre Gist.

## Lancer en local

```sh
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

## Ajouter du contenu

1. Créer `data/n5/blocXX.json` sur le modèle de `data/n5/bloc01.json`.
2. L'ajouter à la fin de la liste `blocks` dans `data/manifest.json`.
3. Vérifier : `node tools/verifier.mjs`.

Les identifiants (leçons, exercices) ne doivent jamais changer une fois publiés : la progression y est rattachée.

### Format d'une leçon

```jsonc
{ "id": "v5-01", "title": "Les gens",
  "intro": ["paragraphe (facultatif)"],
  "words": [
    { "jp": "{大人|おとな}", "kana": "おとな", "fr": "adulte",
      "ex": { "jp": "{大人|おとな}は{五百円|ごひゃくえん}です。", "fr": "500 yens pour les adultes." } }
  ],
  "sections": [ /* facultatif : comme dans la grammaire (h, p, ex, vocab) */ ],
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
- Phrase à trous : la traduction est cachée (« Voir la traduction ») jusqu'à la réponse, pour que le contexte japonais fasse le travail.
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

Le vérificateur contrôle aussi : lecture (`kana`) = furigana du mot, phrase d'exemple qui contient le mot, mot déjà enseigné dans une autre leçon, kanji hors liste.
