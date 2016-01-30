def fxd_xor(a, b):
    assert len(a) == len(b)
    return list(map(lambda p: p[0]^p[1], zip(a, b)))

if __name__ == '__main__':
    assert fxd_xor(b'Hello', b'Hello') == [0]*len(b'Hello')
