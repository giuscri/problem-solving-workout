import binascii

def b64(hx_s):
    hx_s = binascii.unhexlify(hx_s)
    r = bytearray()

    for i in range(0, len(hx_s), 3):
        r.append(hx_s[i] >> 2)
        r.append((hx_s[i] << 4) & 0x3f | hx_s[i+1] >> 4)
        r.append((hx_s[i+1] << 2) & 0x3f| hx_s[i+2] >> 6)
        r.append(hx_s[i+2] & 0x3f)

    prntbl = [chr(x) for x in range(ord('A'), ord('Z') +1)]
    prntbl += [chr(x) for x in range(ord('a'), ord('z') +1)]
    prntbl += [chr(x) for x in range(ord('0'), ord('9') +1)]
    prntbl += ['+', '/']

    return ''.join(map(lambda x: prntbl[x], r))

def fxdXOR(a, b):
    return bytes(map(lambda p: p[0]^p[1], zip(a, b)))

if __name__ == '__main__':
    hx_s = '49276d206b696c6c696e6720796f757220627261696e20' + \
              '6c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64_s = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert b64(hx_s) == b64_s 

    a = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
    b = binascii.unhexlify('686974207468652062756c6c277320657965')
    assert binascii.hexlify(fxdXOR(a, b)).decode('utf8') == \
       '746865206b696420646f6e277420706c6179'
