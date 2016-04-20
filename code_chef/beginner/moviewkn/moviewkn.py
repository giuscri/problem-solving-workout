def fn(L, R):
    lst = list(enumerate(map(lambda p: (p[0]*p[1], p[1]), zip(L, R))))
    lst.sort(key=lambda p: p[1][0], reverse=True)
    max_v = lst[0][1][0]

    lst = list(filter(lambda p: p[1][0] == max_v, lst))

    if len(lst) > 1:
        lst.sort(key=lambda p: p[0])
        lst.sort(key=lambda p: p[1][1], reverse=True)
        return lst[0][0] +1

    return lst[0][0] +1

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())

    for i in range(0, T):
        _ = sys.stdin.readline()
        L = list(map(int, re.split(' ', sys.stdin.readline().strip())))
        R = list(map(int, re.split(' ', sys.stdin.readline().strip())))

        print(fn(L, R))
