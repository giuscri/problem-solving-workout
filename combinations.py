def zero_one_combinations(n):
    # Dirty, bro...
    if n==1: return [0,1]
    if n==2: return [[0,0], [0,1], [1,0], [1,1]]

    res = zero_one_combinations(n-1)
    lst = []
    for x in res:
        lst.append([0] + x)
    for x in res:
        lst.append([1] + x)
    return lst

def combinations(S, r):
    res = []
    def f(r, lst):
        if r == 0:
            return res.append(lst)
        for x in S:
            if x not in lst:
                f(r - 1, lst + [x])
    f(r, [])
    return res
