import aes_ecb, pkcs7_padding, fxd_xor

def decrypt(ct, k):
    # pad the ciphertext using PKCS#7 if needed
    if len(ct) % len(k) > 0:
        ct = pkcs7_padding(ct, len(ct)+(len(k)-len(ct)%len(k)))
    assert len(ct) % len(k) == 0

    pt = [0 for i in range(len(ct))]

    for i in range(len(ct), len(k), -len(k)):
        x = aes_ecb.decrypt(ct[i-len(k):i], k)
        pt[i-len(k):i] = fxd_xor.fxd_xor(x, ct[i-2*len(k):i-len(k)])

    x = aes_ecb.decrypt(ct[0:len(k)], k)
    pt[0:len(k)] = fxd_xor.fxd_xor(x, [0 for x in range(len(k))]) # using the IV
    return pt

if __name__ == '__main__':
    import requests
    import base64
    r = requests.get('http://cryptopals.com/static/challenge-data/10.txt')
    ct = base64.b64decode(''.join(r.text.strip().split('\n')))
    pt = decrypt(ct, b'YELLOW SUBMARINE')
    print(bytes(pt).decode('UTF-8'))
