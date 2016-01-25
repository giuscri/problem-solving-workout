def fxd_xor(a, b):
    assert len(a) == len(b)
    return bytes(map(lambda p: p[0]^p[1], zip(a, b)))

def hmming_dist(s, t):
    assert len(s) == len(t)
    s = s.encode('utf8')
    t = t.encode('utf8')
    bp = int(fxd_xor(s, t).hex(), 16)

    def f(bp, cnt=0):
        if bp == 0: return cnt
        if bp & 1 != 0: return f(bp >> 1, cnt +1)
        return f(bp >> 1, cnt)
    return f(bp)
