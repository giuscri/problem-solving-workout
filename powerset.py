import itertools

def powerset(s):
    ps = []
    combs = set()
    for x in map(lambda x: set(itertools.permutations(x)), \
       itertools.combinations_with_replacement((0,1),3)):
        combs.update({*x})
    for c in combs:
        psi = []
        for x,y in zip(s, c):
            if y==1:
                psi.append(x)
        ps.append(psi)
    return ps

if __name__ == '__main__':
    ps = powerset({0,2,4})
