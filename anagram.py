with open('wordlist-anagram.txt') as f:
    ws = sorted(f.read().strip().split('\n'))

as_key = lambda s: ''.join(sorted(s.lower()))

def build_dict(ws=ws):
    r = dict()
    for w in ws:
        k = as_key(w)
        if k in r: r[k].append(w)
        else: r[k] = [w]
    return dict(filter(lambda p: len(p[1]) > 2, r.items()))

d = build_dict()
assert len(d.items()) == 6238 # A hint provided

def anagrams(d=d, ws=ws):
    fmt = '{:14} :- {}'
    lns = []
    vstd = dict(map(lambda w: (w,False), ws))
    for w in ws:
        if vstd[w] is True: continue

        k = as_key(w)
        if k not in d: continue

        vstd[w] = True
        lst = list(filter(lambda x,w=w: x != w, d[k]))
        for x in lst: vstd[x] = True

        lst.sort(key=lambda s: s.lower())
        lns.append(fmt.format(w, ', '.join(lst)))
    return '\n'.join(lns) + '\n'

def anagram(w, d=d):
    k = as_key(w)
    r = list(filter(lambda x, w=w: x!= w, d[k]))
    r.sort(key=lambda s: s.lower())
    return ', '.join(r)
