import itertools

def fn(lst, amount):
    for i in range(len(lst) + 1):
        for c in itertools.combinations(lst, r=i):
            if sum(c) == amount:
                return 'Yes'
    return 'No'

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())
    for i in range(T):
        n, amount = map(int, re.split(' ', sys.stdin.readline().strip()))

        lst = []
        for j in range(n):
            lst.append(int(sys.stdin.readline().strip()))

        print(fn(lst, amount))
