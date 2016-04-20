'''
CodeChef returns a NZEC error -- though
for the input sample the output is the
same. Don't know why my solution is rejected.
Maybe the input format used is not the same 
described in the problem description?
'''

def fn(n, lst):
    js = [i for i in range(1, n+1) if i not in lst]
    res0 = [x for i,x in enumerate(js) if i%2 == 0]
    res1 = [x for i,x in enumerate(js) if i%2 == 1]
    return (res0, res1)

if __name__ == '__main__':
    import sys, re

    T = int(sys.stdin.readline().strip())

    for i in range(0, T):
        n, _ = map(int, re.split(' ', sys.stdin.readline().strip()))
        lst = list(map(int, re.split(' ', sys.stdin.readline().strip())))
        res0, res1 = fn(n, lst)
        res0 = ' '.join(map(str, res0))
        res1 = ' '.join(map(str, res1))
        print('{}\n{}'.format(res0, res1))
