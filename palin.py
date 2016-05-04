import itertools

is_palin = lambda s: s == ''.join(reversed(s))

def palin(s):
    def f(s, i, j, c, cs):
        if is_palin(s): return cs.append(c) or cs
        if i >= j: return cs
        if s[i] == s[j]: return f(s, i+1, j-1, c, cs)
        f(s[:i] + s[j] + s[i:], i, j+1, c + [s[j]], cs)
        f(s[:j+1] + s[i] + s[j+1:], i+1, j, c + [s[i]], cs)
        return cs
    r = f(s, 0, len(s)-1, [], [])
    r.sort(key=lambda l: len(l))
    fmt = 'The word «{}» needs {} insertions to become palindrome'
    ret = fmt.format(s, len(r[0]))
    if len(r[0]) > 0: ret += ': {}'.format(r[0])
    return ret 

if __name__ == '__main__':
    print(palin('casa'))
    print(palin('otto'))
    print(palin('palindromo'))
    print(palin('posero'))
    print(palin('coccinella'))
