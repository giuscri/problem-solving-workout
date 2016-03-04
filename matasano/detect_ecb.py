import itertools

def detect_ecb(bs):
    cnks = [bs[i:i+8] for i in range(0, len(bs), 8)]
    for a,b in itertools.combinations(cnks, r=2):
        if a==b: return True
    return False

if __name__ == '__main__':
    import requests, binascii
    res = requests.get('http://cryptopals.com/static/challenge-data/8.txt')
    res = res.text.strip().split('\n')
    res = map(lambda x: binascii.unhexlify(x), res)
    for x in res:
        yeah = detect_ecb(x)
        if yeah:
            print('*** Found!!')
            print('*** {}'.format(binascii.hexlify(x).decode()))
