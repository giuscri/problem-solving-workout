import sys
import binascii
from util import fxd_xor

def rpting_xor(s, k):
    while len(k) < len(s): k += k
    k = k[:len(s)]
    return fxd_xor(s, k)

if __name__ == '__main__':
    s = sys.stdin.read()
    k = sys.argv[1] if len(sys.argv) > 1 else 'ICE'

    ec = 'utf8'

    c = rpting_xor(bytes(s, ec), bytes(k, ec))
    print(binascii.hexlify(c).decode(ec))
