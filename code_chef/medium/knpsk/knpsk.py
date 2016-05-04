def fn(els, M):
    dp = [(0, set()) for i in range(M +1)]

    for i in range(1, len(dp)):
        for j in range(len(els)):
            w, c = els[j]
            if i - w < 0:
                continue
            if j in dp[i - w][1]:
                continue

            if dp[i - w][0] + c > dp[i][0]:
                dp[i] = (dp[i - w][0] + c, dp[i - w][1].union({j}))

    return list(map(lambda p: p[0], dp))[1:]

if __name__ == '__main__':
    import sys, re

    M = 0
    els = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        w, c = map(int, sys.stdin.readline().strip().split(' '))
        M += w
        els.append((w, c))

    r = fn(els, M)
    print(' '.join(map(str, r)))
