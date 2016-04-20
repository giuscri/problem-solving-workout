def fn(s):
    lst = list(map(lambda c: (c, s.count(c)), set(s)))
    lst.sort(key=lambda p: p[1], reverse=True)
    lst = list(''.join(re.split(lst[0][0], s)))
    return len(lst)

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())

    for i in range(T):
        _ = sys.stdin.readline()
        res = fn(sys.stdin.readline().strip())
        print(res)
