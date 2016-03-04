def pkcs7_padding(bs, n):
    """Pad the bytestring in bs
    such to obtain a n bytes string"""
    assert len(bs) <= n, 'bytestring is longer than {} bytes'.format(n)
    if len(bs) == n: return bs
    r = bs[:]
    k = n-len(r)
    while len(r) < n: r.append(k)
    return r

if __name__ == '__main__':
    bs = bytearray(b'YELLOW SUBMARINE')
    print(pkcs7_padding(bs, 20))
