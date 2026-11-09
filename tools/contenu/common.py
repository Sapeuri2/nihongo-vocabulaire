# Aides communes aux générateurs de blocs (tools/contenu/blocNN.py) : W = mot, C = QCM / phrase à trous, O = remise en ordre.
# Usage : python3 tools/contenu/bloc05.py data/n5/bloc05.json && python3 tools/contenu/fmt.py data/n5/bloc05.json
def W(jp, kana, fr, ex, exFr): return dict(jp=jp, kana=kana, fr=fr, ex=ex, exFr=exFr)
def C(lid, n, choices, a=0, q=None, jp=None, fr=None, explain=None, uses=None):
    e = {"id": f"{lid}-e{n:02d}", "type": "choice"}
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
