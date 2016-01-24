import binascii
import re
import math
import string
import json

from util import fxdXOR

with open('letter_freq.json') as f: en = json.loads(f.read())

def chs_dist(s):
    # Compute a characters distribution out of a string
    def f(s, d):
        if len(s) == 0: return d
        hd = s[0]
        if hd in d: d[hd] += 1
        return f(s[1:], d)
    d = dict()
    for k in string.printable[10:10+26]: d[k] = 0
    d = f(s, d)
    s = ''.join(re.split('[^a-zA-Z]', s))
    for k,v in d.items():
        d[k] = int(v/len(s) * 100 * 100) / 100
    sm = sum(map(lambda p: math.ceil(p[1]), d.items()))
    assert sm >= 100
    return d

def dist_distance(obs, exp):
    if sorted(obs.keys()) != sorted(exp.keys()):
        raise ValueError('Not the same sample space')

    r = 0
    for k in obs: r += (exp[k]-obs[k])**2 / exp[k]
    return abs(1-r)

if __name__ == '__main__':
    c_txt = binascii.unhexlify('1b37373331363f78151b7f2b783431333' + \
                                  'd78397828372d363c78373e783a393b3736')
    ps = []
    for c in range(0, 256):
        p_txt = fxdXOR(c_txt, bytes([c])*len(c_txt))
        try:
            p_txt = p_txt.decode('utf8')
        except UnicodeDecodeError: continue
        strppd = ''.join(re.split('[^a-zA-Z]', p_txt)).lower()
        if len(strppd) == 0: continue
        ps.append((dist_distance(chs_dist(strppd), en), p_txt, c))

    ps.sort(key=lambda p: p[0])
    print('✓ Best bet is \"{}\", with key {}'.format(ps[0][-2], ps[0][-1]))
