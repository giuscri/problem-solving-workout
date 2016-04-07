# Pretty convoluted code to test the matrix(, hard to debug!) 

import re
import sys

def upside_down(m):
    return list(reversed(m))

def transpose(m):
    ret = []
    for i in range(len(m)):
        c = []
        for r in m:
            c.append(r[i])
        ret.append(''.join(c))
    return ret

def left_pad(s, n):
    while len(s) < n:
        s = '.' + s
    return s

def rotate(m):
    ret = []
    for r in m:
        _r = left_pad(''.join(re.split('\.', r)), len(r))
        ret.append(_r)
    
    ret = upside_down(ret)
    ret = transpose(ret)

    return ret

def winner(m, k):
    def check_orizontally(m, k):
        ws = set()

        for r in m:
            rs, bs = 0, 0
            for e in r:
                if e == 'R':
                    rs += 1
                    if rs >= k:
                        ws.add('Red')
                    bs = 0
                elif e == 'B':
                    bs += 1
                    if bs >= k:
                        ws.add('Blue')
                    rs = 0
                else:
                    rs, bs = 0, 0

        return ws

    def check_vertically(m, k):
        ws = set()

        for i in range(len(m)):
            rs, bs = 0, 0
            for r in m:
                if r[i] == 'R':
                    rs += 1
                    if rs >= k:
                        ws.add('Red')
                    bs = 0
                elif r[i] == 'B':
                    bs += 1
                    if bs >= k:
                        ws.add('Blue')
                    rs = 0
                else:
                    rs, bs = 0, 0

        return ws

    def check_diagonals_left_to_right(m, k):
        ws = set()

        n = len(m)
        for i in range(0, n):
            rs, bs = 0, 0

            for h in range(0, i + 1):
                if m[i - h][h] == 'R':
                    rs += 1
                    if rs >= k:
                        ws.add('Red')
                    bs = 0
                elif m[i - h][h] == 'B':
                    bs += 1
                    if bs >= k:
                        ws.add('Blue')
                    rs = 0
                else:
                    rs, bs = 0, 0

            rs, bs = 0, 0
            for h in range(0, n - i):
                if m[i + h][n - 1 - h] == 'R':
                    rs += 1
                    if rs >= k:
                        ws.add('Red')
                    bs = 0
                elif m[i + h][n - 1 - h] == 'B':
                    bs += 1
                    if bs >= k:
                        ws.add('Blue')
                    rs = 0
                else:
                    rs, bs = 0, 0

        return ws

    def check_diagonals_right_to_left(m, k):
        ws = set()

        for i in range(0, n):   
            rs, bs = 0, 0

            for h in range(0, n - i):
                if m[i + h][h] == 'R':
                    rs += 1
                    if rs >= k:
                        ws.add('Red')
                    bs = 0
                elif m[i + h][h] == 'B':
                    bs += 1
                    if bs >= k:
                        ws.add('Blue')
                    rs = 0
                else:
                    rs, bs = 0, 0

            rs, bs = 0, 0

            for h in range(0, i + 1):
                if m[i - h][n - 1 - h] == 'R':
                    rs += 1
                    if rs >= k:
                        ws.add('Red')
                    bs = 0
                elif m[i - h][n - 1 - h] == 'B':
                    bs += 1
                    if bs >= k:
                        ws.add('Blue')
                    rs = 0
                else:
                    rs, bs = 0, 0

        return ws

    ws = set()

    ws.update(check_orizontally(m, k))
    ws.update(check_vertically(m, k))
    ws.update(check_diagonals_left_to_right(m, k))
    ws.update(check_diagonals_right_to_left(m, k))

    if 'Red' in ws and 'Blue' in ws:
        return 'Both'
    elif 'Red' in ws:
        return 'Red'
    elif 'Blue' in ws:
        return 'Blue'
    else:
        return 'Neither'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        lines = f.read().strip().split('\n')

    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(1, ncases + 1):
        n, k = map(int, re.split(' ', lines[0]))
        lines = lines[1:]

        m = []

        for r_ix in range(n):
            m.append(lines[0])
            lines = lines[1:]

        m = rotate(m)
        w = winner(m, k)

        print('Case #{}: {}'.format(i, w))
