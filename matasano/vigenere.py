import sys
import functools
import itertools
import re
import binascii
import math

from unb64 import unb64
from hmming_dist import hmming_dist
from crk_1bxor import crk_1bxor

def bet_kln(c):
    r = []
    for kln in range(2, 50):
        mn = 0 
        for cmb in itertools.combinations(range(0,4), r=2):
            frst_tk = c[cmb[0]*kln:(cmb[0]+1)*kln]
            scnd_tk = c[cmb[1]*kln:(cmb[1]+1)*kln]
            mn += hmming_dist(frst_tk, scnd_tk)/kln/6
        r.append((mn, kln))
    r.sort(key=lambda p: p[0])
    return r[0][-1]

def unvgnr(c, tl=0.9):
    kln = bet_kln(c)
    while len(c) % kln != 0: c += b'\x00'
    rws = [c[i:i+kln] for i in range(0, len(c), kln)]
    cls = [bytes([r[i] for r in rws]) for i in range(kln)]
    cls = list(map(lambda c: crk_1bxor(c, tl=tl)[0][1], cls))
    h = len(cls[0])
    rws = [c[i] for i in range(h) for c in cls]
    return bytes(rws)

if __name__ == '__main__':
    '''
    Expected output,
        λ> python3 vigenere.py 6.txt
        I'm back and I'm ringin''the bell
        In ecstasy in the back of me'he fly girls yell
        Well that's my DJ Deshay custin' all them Z's
        ...
    '''
    if len(sys.argv) < 2: sys.exit(-1)
    fname = sys.argv[1].strip()
    with open(fname) as f:
        c = unb64(''.join(f.read().strip().split()))
    r = unvgnr(c)
    print(r.decode())
