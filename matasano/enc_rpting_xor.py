import sys
import rpting_xor

if __name__ == '__main__':
    if len(sys.argv) < 2: print('*** Need a passwd to derive the key') or sys.exit(-1)
    passwd = sys.argv[1].encode()
    c = rpting_xor.rpting_xor(sys.stdin.buffer.read(), passwd)
    sys.stdout.buffer.write(bytes(c))
