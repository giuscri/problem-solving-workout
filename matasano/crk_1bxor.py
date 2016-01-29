import binascii
import re
import math
import string
import json
import functools

from fxd_xor import fxd_xor

with open('letter_freq.json') as f:
    en = dict(map(lambda p: (ord(p[0]),p[1]), \
                 json.loads(f.read()).items()))

def chi_sqrd(o, e):
    assert sorted(o.keys()) == sorted(e.keys())
    r = 0
    for k in e: r += (e[k] - o[k])**2 / e[k]
    return r

def crk_1bxor(c, tl=0.98):
    lst = []
    for b in range(0, 256):
        k = bytes([b]) * len(c)
        _p = fxd_xor(c, k)
        p = bytes(map(lambda x: x+32 if x in range(65,91) else x, _p))
        o = dict(zip(range(97,123), [0]*26))
        ln = 0
        for x in p:
            if x in o:
                o[x] += 1
                ln += 1
            elif x in b' \n\r\t\'':
                ln += 1
        if ln/len(p) < tl: continue
        e = dict(map(lambda x: (x[0], x[1]/100*ln), en.items()))
        lst.append((chi_sqrd(o, e), _p, k))
    return lst

if __name__ == '__main__':
    # Challenge 1.3
    c = '1b37373331363f78151b7f2b783431333' + \
               'd78397828372d363c78373e783a393b3736'
    lst = crk_1bxor(binascii.unhexlify(c))
    lst.sort(key=lambda x: x[0])
    for x in lst[:3]: print('{}, ~{}'.format(repr(x[1].decode()), x[0]))

    # Challenge 1.4
    with open('4.txt') as f: cs = f.read().strip().split('\n')
    cs = map(lambda c: binascii.unhexlify(c), cs)
    lst = []
    for c in cs: lst += crk_1bxor(c)
    lst.sort(key=lambda x: x[0])
    for x in lst[:3]: print('{}, ~{}'.format(repr(x[1].decode()), x[0]))

    '''
    Expected output:

        λ> python3 crk_1bxor.py
        "Cooking MC's like a pound of bacon", ~32.283483614814095
        'Now that the party is jumping\n', ~33.43710784445039
    '''
