import re
import string

t9_map = dict()
cs = string.printable[10:10+26]
v = 1
for i in range(0, 15):
    if i%3 == 0:
        v += 1
    t9_map[cs[i]] = v
for i in range(15, 19):
    t9_map[cs[i]] = 7
for i in range(19, 22):
    t9_map[cs[i]] = 8
for i in range(22, 26):
    t9_map[cs[i]] = 9
for k in t9_map:
    t9_map[k] = str(t9_map[k])

def to_t9_code(w, t9_map=t9_map):
    return ''.join(map(lambda x: t9_map[x], w)) 

def build_dictionary(fname='dictionary.txt'):
    d = dict()
    with open(fname, 'r') as f:
        ws = f.read().strip().split()
    for w in ws:
        if to_t9_code(w) in d:
            d[to_t9_code(w)].append(w)
        else:
            d[to_t9_code(w)] = [w]
    for c in ('a', 'e', 'i', 'o', 'u'):
        d[to_t9_code(c)] = [c]
    return d

d = build_dictionary()

def find_translations(lst, d=d):
    def _f(lst, translation, translations):
        if len(lst) == 0:
            translations.append(translation.strip())
        else:
            for x in d[lst[0]]:
                _f(lst[1:], '{} {}'.format(translation, x), translations)
        return translations
    return _f(lst, '', [])

if __name__ == '__main__':
    with open('texts.t9.txt', 'r') as f:
        lines = f.read().strip().split('\n')
    for line in lines:
        lst = re.split('\D+', line)
        ts = find_translations(lst)
        for t in ts: print(ts)
