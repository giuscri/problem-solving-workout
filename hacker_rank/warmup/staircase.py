def fn(N):
    lst = []
    for l in range(1, N +1):
        lst.append(' ' * (N-l) + '#' * l)
    return '\n'.join(lst)

if __name__ == '__main__':
    import sys, re

    N = int(sys.stdin.readline().strip())
    print(fn(N))
