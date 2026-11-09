# Mise en forme compacte : tout objet ou tableau court tient sur une ligne.
import json, sys
W = 150
def one(v): return json.dumps(v, ensure_ascii=False, separators=(', ', ': '))
def fmt(v, ind=0):
    pad = '  ' * ind
    s = one(v)
    if len(s) + len(pad) <= W or not isinstance(v, (dict, list)) or (isinstance(v, dict) and 'kana' in v): return s
    inner = '  ' * (ind + 1)
    if isinstance(v, list):
        return '[\n' + ',\n'.join(inner + fmt(x, ind + 1) for x in v) + '\n' + pad + ']'
    return '{\n' + ',\n'.join(inner + json.dumps(k, ensure_ascii=False) + ': ' + fmt(x, ind + 1) for k, x in v.items()) + '\n' + pad + '}'
for p in sys.argv[1:]:
    d = json.load(open(p))
    open(p, 'w').write(fmt(d) + '\n')
