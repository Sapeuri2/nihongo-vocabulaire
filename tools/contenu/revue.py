import json,re,sys
d=json.load(open(sys.argv[1]))
P=lambda s: re.sub(r'\{([^|}]+)\|[^}]+\}',r'\1',s or '').replace('**','')
def show(e):
    if e['type']=='order':
        print(e['id'],'ORDRE',' / '.join(P(t) for t in e['tokens']), '| alt:', [' '.join(P(t) for t in a) for a in e.get('alt',[])]); return
    print(e['id'], P(e.get('q','')), '|', P(e.get('jp','')))
    cs=[P(c) for c in e['choices']]
    print('    ✓', cs[e['a']], ' ✗', ' · '.join(c for i,c in enumerate(cs) if i!=e['a']))
    if len(set(cs))<len(cs): print('   !!! doublon sans furigana')
for l in d['lessons']:
    for e in l['exercises']: show(e)
for e in d['test']+d.get('examTest',[]): show(e)
