def fn(A, B):
    lst = list(str(A - B))
    if lst[-1] == '9':
        lst[-1] = '8'
    else:
        lst[-1] = str((int(lst[-1]) + 1) % 10)
    return ''.join(lst)

if __name__ == '__main__':
    import sys, re

    A, B = map(int, re.split(' ', sys.stdin.readline().strip()))
    res = fn(A, B)
    print(res)
