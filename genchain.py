import string

ws_by_init = dict()
for c in string.printable[10:10+26]:
    ws_by_init[c] = []

with open('animals.txt') as f:
    ws = f.read().strip().split('\n')

for w in ws:
    ws_by_init[w[0]].append(w)

def genchain(src, cb=max):
    with open('animals.txt') as f: ws = f.read().strip().split('\n')
    def f(src, c, cs=[]):
        def anything_left():
            for x in ws_by_init[src[-1]]:
                if x not in c:
                    return True
            return False

        if not anything_left():
            cs.append(c)
            return cs

        for nxt in ws_by_init[src[-1]]:
            if nxt not in c:
                f(nxt, c+[nxt], cs)
        return cs
    cs = f(src, [src])
    srchd_val = cb(map(lambda x: len(x), cs))
    filtrd_cs = list(filter(lambda x: len(x)==srchd_val, cs))
    if len(filtrd_cs) == 1:
        return filtrd_cs[0]
    _lst = list(map(lambda p: (p[0],''.join(p[1])), enumerate(filtrd_cs)))
    _lst.sort(key=lambda p: p[1])
    return filtrd_cs[_lst[0][0]]
