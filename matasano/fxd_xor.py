def fxd_xor(a, b):
    assert len(a) == len(b)
    return bytes(map(lambda p: p[0]^p[1], zip(a, b)))
