def fn(N):
    if N == 0: return 'INSOMNIA'

    s = set(str(N))
    i = 2
    res = N
    while len(s) < 10:
        s.update(set(str(i * N)))
        res = i * N
        i += 1
    return res

if __name__ == '__main__':
    import re, sys

    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        lines = f.read().strip().split('\n')

    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(1, ncases + 1):
        N = int(lines[0])
        lines = lines[1:]

        print('Case #{}: {}'.format(i, fn(N)))
