import binascii

from fxd_xor import fxd_xor

def hmming_dist(s, t):
    assert len(s) == len(t)
    bp = int(binascii.hexlify(fxd_xor(s, t)), 16)

    def f(bp, cnt=0):
        if bp == 0: return cnt
        if bp & 1 != 0: return f(bp >> 1, cnt +1)
        return f(bp >> 1, cnt)
    return f(bp)

if __name__ == '__main__':
    s = b'this is a test'
    t = b'wokka wokka!!!'
    r = hmming_dist(s, t)
    assert r == 37
