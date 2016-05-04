def fn(lst):
    n_pos = 0
    n_neg = 0
    n_zeroes = 0

    for i in range(len(lst)):
        if lst[i] > 0:
            n_pos += 1
        elif lst[i] < 0:
            n_neg += 1
        else:
            n_zeroes += 1

    N = len(lst)
    return n_pos/N, n_neg/N, n_zeroes/N

if __name__ == '__main__':
    import sys, re

    _ = sys.stdin.readline()
    lst = list(map(int, re.split(' ', sys.stdin.readline().strip())))
    print('\n'.join(map(lambda x: '{0:.6}'.format(x), fn(lst))))
