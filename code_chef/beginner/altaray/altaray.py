def fn(A):
    v = [1 for i in range(len(A))]

    for i in range(len(A)-2, -1, -1):
        if A[i]*A[i+1] < 0:
            v[i] = 1 + v[i+1]

    return v

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())

    for i in range(0, T):
        _ = sys.stdin.readline()

        lst = list(map(int, re.split(' ', sys.stdin.readline().strip())))
        r = fn(lst)
        print(' '.join(map(str, r)))
