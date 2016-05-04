def fn(lst, K):
    return len(list(filter(lambda x: x <= 0, lst))) < K

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())

    for i in range(T):
        _, K = map(int, re.split(' ', sys.stdin.readline().strip()))
        lst = list(map(int, re.split(' ', sys.stdin.readline().strip())))
        if fn(lst, K):
            print('YES')
        else:
            print('NO')
