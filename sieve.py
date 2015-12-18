def primes_between(a, b):
    A = [[x,0] for x in range(a, b)]
    for p in A:
        if p[1]==1:
            continue
        for q in A:
            if q[0]!=p[0] and q[0]%p[0]==0:
                q[1] = 1
    return list(map(lambda p: p[0], \
                       filter(lambda x: x[1]==0, A)))
