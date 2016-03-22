# Very bad code. I was rusty!!

import re

def to_regex(in_str):

    def fn(x):
        if not re.match('\(.*?\)$', x): return x
        i = 1
        ret = ''
        while x[i] != ')':
            ret += x[i] + '|'
            i += 1
        return '({})'.format(ret[:-1])

    i = j = 0
    chunks = []
    delim = '('
    while j < len(in_str):
        if in_str[j] == '(':
            chunks.append(in_str[i:j])
            i = j
            delim = ')'
        elif in_str[j] == ')':
            chunks.append(in_str[i:j + 1])
            i = j + 1
            delim = '('
        j += 1
    chunks.append(in_str[i:])

    ret = []
    for c in chunks:
        ret.append(fn(c))

    return ''.join(ret)

if __name__ == '__main__':
    with open('A-large-practice.in') as f:
        lines = f.read().strip().split('\n')

    L, D, N = map(int, re.split(' ', lines[0]))

    words = lines[1:D+1]
    assert len(words) == D

    gath_regexes = list(map(to_regex, lines[D+1:]))
    assert len(gath_regexes) == N

    res = dict(map(lambda x: (x, 0), range(N)))

    for i, r in enumerate(gath_regexes):
        for w in words:
            if re.match(r, w):
                res[i] += 1

    for k,v in res.items():
        fmt = 'Case #{}: {}'
        print(fmt.format(k+1, v))
