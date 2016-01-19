as_key = lambda s: ''.join(sorted(s.lower()))

def build_dictionary(fname='wordlist-anagram.txt'):
    d = dict()
    with open(fname, 'r') as f:
        ws = f.read().strip().split('\n')
    ws = list(map(lambda x: [x, False], ws))
    for p in ws:
        if p[1] is True:
            # p[0] is somehow already
            # in the dictionary
            continue
        key = as_key(p[0])
        if key == p[0].lower():
            # p[0].lower() will be used
            # as a key
            pass
        elif key not in d:
            d[key] = [p[0]]
        else: d[key].append(p[0])
        p[1] = True
    return d

d = dict(filter(lambda p: len(p[1]) >= 2, \
                   build_dictionary().items()))

def anagrams(fname='wordlist-anagram.txt', d=d):
    lines = []
    already_found = {}
    with open(fname, 'r') as f:
        ws = f.read().strip().split()
    for w in ws: already_found[w] = False
    for w in ws:
        if already_found[w] is True:
            continue
        if as_key(w) not in d: continue
        line = '{} :- '.format(w) + anagram(w)
        for x in d[as_key(w)]:
            already_found[x] = True
        lines.append(line )
    return '\n'.join(lines)

def anagram(w, d=d):
    if as_key(w) not in d: return ''
    return ', '.join(filter(lambda x: x != w, d[as_key(w)]))
