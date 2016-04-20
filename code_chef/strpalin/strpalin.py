def fn(A, B):
    if len(set(A).intersection(set(B))) > 0:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())

    for i in range(0, T):
        A = sys.stdin.readline().strip()
        B = sys.stdin.readline().strip()

        print(fn(A, B))
