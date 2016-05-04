import itertools

def power_set(S):
    for r in range(len(S) +1):
        for cmb in itertools.combinations(range(len(S)), r=r):
            yield set(map(lambda p: p[1], \
                             filter(lambda p,cmb=cmb: p[0] in cmb, \
                                       enumerate(S))))
