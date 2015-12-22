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


