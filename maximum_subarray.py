## You have < 5min to write down a bruteforce solution

def max_subarray(A):
    import itertools

    '''
    Very nerdy stuff: the # of pairs in

        0 1 2 3 4 5 6 ... len(A)

    is
        <the # of possible first value> * \
           <the # of possible second value, \
              i.e. when the possible first value is locked>

    thus, `(len(A) +1) * len(A)`

    `sum`ming an array of len == n, is something
    of order `n`, then we're running something
    of order `n` of a set of order `n**2`.

    That means the algorithm running time
    is order `n**3`, which will kick you out
    of the interview. (:
    '''

    max_p = (0,1)
    max_sum = A[0]

    for p in itertools.combinations(range(len(A) +1), 2):
        s = sum(A[p[0]:p[1]])
        if s > max_sum:
            max_p = p
            max_sum = s

    return max_p

A = [904, 40, 523, 12, -335, -385, -124, 481, -31]
assert max_subarray(A) == (0, 4)

## Ok, now let's come up with
## something less bruteforcing

#...
