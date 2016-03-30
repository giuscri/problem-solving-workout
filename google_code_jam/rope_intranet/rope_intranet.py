import sys

def intersect(w0, w1):
    ret = False
    ret |= w1[0] < w0[0] and w1[1] > w0[1]
    ret |= w1[0] > w0[0] and w1[1] < w0[1]
    return ret

if len(sys.argv) < 2:
    sys.exit(-1)

with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().split('\n')

ncases = int(lines[0])
lines = lines[1:]

for c in range(1, ncases +1):
    nwires = int(lines[0])
    lines = lines[1:]
    wires = []
    for i in range(nwires):
        wires.append(tuple(map(int, lines[0].split(' '))))
        lines = lines[1:]

    counter = 0
    for w0 in wires:
        for w1 in wires:
            if intersect(w0, w1):
                counter += 1

    print('Case #{}: {}'.format(c, counter // 2))
