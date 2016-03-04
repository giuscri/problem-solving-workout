import sys
import binascii

from fxd_xor import fxd_xor

def rpting_xor(s, k):
    while len(k) < len(s): k += k
    k = k[:len(s)]
    return fxd_xor(s, k)

if __name__ == '__main__':
    s = sys.stdin.buffer.read().strip()
    k = sys.argv[1].encode() if len(sys.argv) > 1 else b'ICE'
    c = rpting_xor(s, k)
    print(binascii.hexlify(bytes(c)).decode())
