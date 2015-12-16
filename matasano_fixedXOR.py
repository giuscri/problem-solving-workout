import binascii

def fixedXOR(a, b):
    return bytes([x^y for x, y in zip(a, b)])

if __name__ == '__main__':
    a = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
    b = binascii.unhexlify('686974207468652062756c6c277320657965')
    assert binascii.hexlify(fixedXOR(a, b)).decode() == '746865206b696420646f6e277420706c6179'
