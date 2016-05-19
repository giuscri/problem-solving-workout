def fn(n, cache):
    if n in cache: return cache[n]

    r = fn(n - 1, cache)**2 + fn(n - 2, cache)
    cache[n] = r
    return r

if __name__ == '__main__':
    import sys, re

    A, B, N = map(int, sys.stdin.readline().strip().split(' '))

    cache = { 0: A, 1: B }
    print(fn(N - 1, cache))
