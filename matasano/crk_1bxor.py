import binascii
import re
import math
import string
import json

import functools

from util import fxdXOR

with open('letter_freq.json') as f: en = json.loads(f.read())

def chi_sqrd_en(s, en=en):

    # Recursively fill the distribution dictionary
    def f(s, d=dict()):
        if len(s) == 0: return d
        if s[0] in d:
            d[s[0]] += 1
        return f(s[1:], d)
    orig = s
    s = ''.join(re.split('[^a-zA-Z]', orig)).strip().lower()
    obs = f(s, dict([(c, 0) for c in string.printable[10:10+26]]))

    en = dict(map(lambda p: (p[0],p[1]/100*len(orig)), en.items()))
    return sum(map(lambda k: (en[k]-obs[k])**2 / en[k], obs))

def crk_1bxor(c_txt):
    # Take an hex string, return some bets
    # for the plaintext's as
    #   [ ..., ( <chi_sqrd>, <ptext>, <byte used as key>), ... ]
    c_txt = binascii.unhexlify(c_txt)
    ps = []
    for c in range(0, 256):
        key = bytes([c]) * len(c_txt)
        p_txt = fxdXOR(c_txt, key)
        prntble = string.printable
        nt_prntble = functools.reduce(lambda x,y: x or y, \
                                         map(lambda b: \
                                                chr(b) not in prntble, p_txt))
        if nt_prntble: continue
        try:
            p_txt = p_txt.decode('utf8')
        except UnicodeDecodeError: continue
        ps.append((chi_sqrd_en(p_txt), p_txt, c))
    return ps

if __name__ == '__main__':
    # Challenge 1.3
    c_txt = '1b37373331363f78151b7f2b783431333' + \
               'd78397828372d363c78373e783a393b3736'
    crkd = crk_1bxor(c_txt)
    crkd.sort(key=lambda p: p[0])
    for x in range(5):
        print('[+] \"{}\", with key {}'.format(repr(crkd[x][-2]), crkd[x][-1]))

    print('-'*80)

    # Challenge 1.4
    with open('4.txt') as f: c_ts = f.read().strip().split('\n')
    crkd = []
    for c_txt in c_ts:
        tple = crk_1bxor(c_txt)
        crkd += tple
    crkd.sort(key=lambda p: p[0])
    for x in range(10):
        print('[+] {}, with key {}'.format(repr(crkd[x][-2]), crkd[x][-1]))

    print('-'*80)
