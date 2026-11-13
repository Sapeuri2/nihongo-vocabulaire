# Aides communes aux générateurs de blocs (tools/contenu/blocNN.py) : W = mot, C = QCM / phrase à trous, O = remise en ordre.
# Usage : python3 tools/contenu/bloc05.py data/n5/bloc05.json && python3 tools/contenu/fmt.py data/n5/bloc05.json
def W(jp, kana, fr, ex, exFr): return dict(jp=jp, kana=kana, fr=fr, ex=ex, exFr=exFr)
_NO = object()
def C(lid, n, choices, a=0, q=None, jp=None, fr=None, explain=None, uses=None, star=_NO):
    e = {"id": f"{lid}-e{n:02d}", "type": "choice"}
    if star is not _NO: e["star"] = star
    if uses: e["uses"] = uses
    if q: e["q"] = q
    if jp: e["jp"] = jp
    if fr: e["fr"] = fr
    e["choices"] = choices; e["a"] = a
    if explain: e["explain"] = explain
    return e
def O(lid, n, fr, tokens, alt=None, uses=None, explain=None):
    e = {"id": f"{lid}-e{n:02d}", "type": "order"}
    if uses: e["uses"] = uses
    e["fr"] = fr; e["tokens"] = tokens
    if alt: e["alt"] = alt
    if explain: e["explain"] = explain
    return e
LECT = "Comment se lit "

def make_block(T, X=None):
    """Fabriques d'IDs pour le test (T-tNN) et l'examen (X-NN)."""
    def TC(n, *a, **k):
        e = C("x", n, *a, **k); e["id"] = f"{T}-t{n:02d}"; return e
    def TO(n, *a, **k):
        e = O("x", n, *a, **k); e["id"] = f"{T}-t{n:02d}"; return e
    def XC(n, *a, **k):
        e = C("x", n, *a, **k); e["id"] = f"{X}-{n:02d}"; return e
    def XO(n, *a, **k):
        e = O("x", n, *a, **k); e["id"] = f"{X}-{n:02d}"; return e
    return TC, TO, XC, XO

def save(bloc, out):
    import json
    json.dump(bloc, open(out, "w"), ensure_ascii=False)
    print("ok", sum(len(l["exercises"]) for l in bloc["lessons"]), "exercices de leçon,", len(bloc["test"]), "de test,", len(bloc.get("examTest", [])), "d'examen")

# ---------- N4 et suivants : mot à épingler (📌) et enregistrement mis en forme ----------
import json as _json, re as _re, os as _os

def plain(s): return _re.sub(r'\{([^|{}]+)\|[^{}]+\}', r'\1', s or '').replace('**', '')

def stem(jp):
    """Radical, comme tools/verifier-appli.mjs : 勉強する → 勉強, 書く → 書, うれしい → うれし."""
    p = plain(jp).lstrip('〜')
    if p.endswith('する') and len(p) > 2: return p[:-2]
    if p[-1:] in 'うくぐすつぬぶむるい' and len(p) > 1: return p[:-1]
    return p

def known_words(extra_lessons=()):
    """Tous les mots des blocs déjà publiés (manifest) + ceux des leçons données."""
    root = _os.path.join(_os.path.dirname(__file__), '..', '..')
    words = []
    for f in _json.load(open(_os.path.join(root, 'data', 'manifest.json')))['blocks']:
        p = _os.path.join(root, f)
        if _os.path.exists(p):
            for l in _json.load(open(p))['lessons']: words += l.get('words', [])
    for l in extra_lessons: words += l.get('words', [])
    return words

def auto_star(bloc):
    """Phrase à trous dont la réponse est une forme conjuguée (心配して, うれしかった…) :
    le moteur ne retrouverait pas le mot dans les tableaux, on lui dit lequel épingler."""
    words = known_words(bloc['lessons'])
    exact = {plain(w['jp']) for w in words}
    jp_ok = lambda s: _re.search(r'[぀-ヿ㐀-鿿]', s or '')
    for e in [x for l in bloc['lessons'] for x in l['exercises']] + bloc['test'] + bloc.get('examTest', []):
        if e['type'] != 'choice' or 'star' in e or '＿' not in e.get('jp', ''): continue
        pa = plain(e['choices'][e['a']])
        if not jp_ok(pa) or pa in exact or '。' in pa or len(pa) > 12: continue
        best = None
        for w in words:
            s = stem(w['jp'])
            if (len(s) >= 2 or _re.search(r'[\u3400-\u9fff]', s)) and pa.startswith(s) and (best is None or len(s) > len(stem(best['jp']))): best = w
        if best: e['star'] = {"jp": best['jp'], "kana": best['kana'], "fr": best['fr']}

def save_n4(bloc, out):
    auto_star(bloc)
    _json.dump(bloc, open(out, 'w'), ensure_ascii=False)
    import subprocess, sys
    subprocess.run([sys.executable, _os.path.join(_os.path.dirname(__file__), 'fmt.py'), out], check=True)
    n = sum(len(l['exercises']) for l in bloc['lessons'])
    s = sum(1 for l in bloc['lessons'] for e in l['exercises'] if 'star' in e) + sum(1 for e in bloc['test'] + bloc.get('examTest', []) if 'star' in e)
    print('ok', n, 'exercices de leçon,', len(bloc['test']), 'de test,', len(bloc.get('examTest', [])), "d'examen,", s, 'mots épinglés ajoutés')
