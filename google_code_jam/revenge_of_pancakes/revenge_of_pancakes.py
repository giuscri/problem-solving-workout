from functools import reduce
import math

'''
After struggling with running a bruteforce
solution for `fn` I came out with the guess
that the minimum number of move can be
achieved by moving only entire groups
of pancakes -- whenever they have different
sides up. That is, I'll never flip `--`.

Given that, memory/time consumption can
be reduced via a shrink function such
that `--+-+--` becomes `-+-+-`.

Then, I came out with a O(n) solution
via knowing minimum number of moves
for all the possibile configurations:

    '+-' => 2
    '-+' => 1
    '-'  => 1

After reading the writeup, I realised
that it's possible to have a O(1)
solution via

def fn(s):
    s = shrink(s)
    H = len(s)
    if s[-1] == '-': return H
    return H - 1
'''

def flip_first(s, k):
    lst = []
    for i in range(0, k):
        if i >= len(s): break
        lst.append('+' if s[i] == '-' else '-')
    return ''.join(reversed(lst)) + s[k:]

def shrink(s):
    ret = s[0]
    for c in s:
        if c != ret[-1]:
            ret += c
    return ret

'''
# Bruteforcing: not feasible even for the small case
def fn(s, c, costs, ancestors, blacklist, cache):
    s = shrink(s)

    if '-' not in s:
        for i, a in enumerate(ancestors):
            if a in cache and c - i < cache[a]:
                cache[a] = c - i
            elif a not in cache:
                cache[a] = c - i
            
        return costs.append(c)

    if s in ancestors:
        blacklist.append(s)
        return None # loop detected!

    for i in range(1, len(s) + 1):
        flipped = flip_first(s, i)

        if flipped in blacklist:
            continue

        elif flipped in cache:
            costs.append(c + cache[flipped] + 1)
            continue

        else:
            fn(flipped, c + 1, costs, ancestors + [s], blacklist, cache)
'''

def fn(s):
    s = shrink(s)
    c = 0
    cache = {'-+': 1, '+-': 2, '-': 1}
    while '-' in s:
        c += cache[s[:2]]
        s = '+' + s[2:]
        s = shrink(s)
    return c

if __name__ == '__main__':
    import sys, re

    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        ncases = int(f.readline().strip())

        for i in range(1, ncases + 1):
            s = f.readline().strip()

            costs = []
            print('Case #{}: {}'.format(i, fn(s)))
