import re
import itertools

def solve(puzzle):
    ordinals = set(map(lambda x: ord(x), \
                      set(''.join(re.split('\W+', s)))))
    initials = set(map(lambda x: ord(x[0]), re.split('\W+', s)))
    finals = ordinals.difference(initials)
    ordinals = list(initials) + list(finals)

    permutations = itertools.permutations([x for x in range(10)])
    for p in permutations:

        if 0 in p[:len(initials)]:
            ## Discard permutation
            continue

        T = {}
        for o,t in zip(ordinals, p):
            T[o] = str(t)
        evald = eval(puzzle.translate(T))
        if evald == True:
            print('Found solutions via {}'.format(T))
            print('{}'.format(puzzle.translate(T)))
            break

if __name__ == '__main__':
    s = 'HAWAII + IDAHO + IOWA + OHIO == STATES'
    solve(s)
