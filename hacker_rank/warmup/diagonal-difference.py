def fn(m):
    res = 0
    for i in range(N):
        res += m[i][i]

    for i in range(N):
        res -= m[i][N-1 -i]
    return abs(res)

if __name__ == '__main__':
    import sys, re

    N = int(sys.stdin.readline().strip())
    m = []
    for i in range(N):
        m.append(list(map(int, re.split(' ', sys.stdin.readline().strip()))))
    print(fn(m))
