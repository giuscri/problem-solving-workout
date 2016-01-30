import binascii
import string

mp = dict(zip(range(0, 64), string.printable[10+26:10+2*26] + \
                               string.printable[10:10+26] + \
                                  string.printable[:10] + '+/'))

def b64(bs):
    r = []

    for i in range(0, len(bs), 3):
        try:
            r.append(bs[i] >> 2 & 0x3f)
            r.append((bs[i] << 4 | bs[i+1] >> 4) & 0x3f)
            r.append((bs[i+1] << 2 | bs[i+2] >> 6) & 0x3f)
            r.append(bs[i+2] & 0x3f)
        except IndexError:
            if len(bs) % 3 == 1: r.append(bs[-1] << 4 & 0x3f)
            elif len(bs) % 3 == 2: r.append(bs[-1] << 2 & 0x3f)
            break

    r = list(map(lambda x: mp[x], r))
    while len(r)%4 != 0: r.append('=')
    
    return ''.join(r)

if __name__ == '__main__':
    assert 'Rm9vYmFyaXNtIGlzIHRoZSB3YXk=' == b64(b'Foobarism is the way')
