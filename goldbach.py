import itertools

def sieve(n):
    lst = [[x,0] for x in range(2,n)]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j][0]%lst[i][0]==0:
                lst[j][1] = 1
    return [p[0] for p in lst if p[1]==0]

def goldbach(n):
    if n%2 != 0:
        raise ValueError("Can't accept odd numbers")
    ps = sieve(n)
    ixs = [x for x in range(len(ps))]
    for p in itertools.combinations_with_replacement(ixs,2):
        if ps[p[0]]+ps[p[1]]==n:
            return ps[p[0]],ps[p[1]]

def goldbach_list(n,m):
    ret = {}
    lst = [x for x in range(n,m) if x%2==0]
    for even in lst:
        ret[even] = goldbach(even)
    return ret
