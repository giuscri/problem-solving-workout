as_key = lambda s: s[0]+s[-1]

def build_dictionary(fname='wordlist.txt'):
    d = dict()
    with open(fname, 'r') as f:
        ws = f.read().strip().split()
    for w in ws:
        key = as_key(w)
        if key not in d:
            d[key] = [w]
        else:
            d[key].append(w)
    return d

d = build_dictionary()

# A bit convoluted, but couldn't found
# anything better at the moment
def contains(s, t):
    j = 0
    for i in range(len(t)):
        if t[i] not in s[j:]:
            return False
        while j < len(s):
            j += 1
            if s[j-1] == t[i]: break
    return True

qwerty_map = dict()
rows = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]
for i in range(3):
    for c in rows[i]:
        qwerty_map[c] = i

def qwerty_row_traversals(w, qwerty_map=qwerty_map):
    lst = list(map(lambda c,qwerty_map=qwerty_map: \
                      qwerty_map[c], w))
    cnt = 0
    for i in range(1, len(lst)):
        if lst[i-1] != lst[i]: cnt += 1
    return cnt

def get_suggestions(swype, d=d):
    lst = d[as_key(swype)]
    lst = list(filter(lambda x,swype=swype: \
                         contains(swype, x), lst))
    lst = list(filter(lambda x,swype=swype: \
                         qwerty_traversals(x) in range(qwerty_traversals(swype) -4,qwerty_traversals(swype)), lst))
    return lst
