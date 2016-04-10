#!/usr/bin/python3

'''
The tricky part was to be sure the
code doesn't block: are we sure
that 0 is the only value that leads to
"insomnia"?

Since we know that 0 < N <= 10**6,
we could preventively see if

    for N in range(0, 10**6):
        _ = counting_sheep.fn(N)

results in an infinite loop.

If not, we're sure that when 
downloading even the large dataset
we will compute all the needed values
in finite time.

What if we didn't have the range for N?

Could we be sure that fn() is right the
way we wrote it?, that

    if N == 0: return 'INSOMNIA'
    else: <find_digits>

Yes.

For any number N > 0, we're
assured we'll find 0 as the rightmost
digit at worst at 10*N.

For digits in [1-9] instead, let's
find P, the smallest power of 10
larger than N. If x, y are some
two multiples of N such that x < k * P
and y > (k+1) * P, we know they cannot
be "consecutive" multiples, otherwise

    y - x > P, y - x == N, then N > P

Then after x, some other multiples of N
smaller than (k+1) * P must exist.

Thus, as we start from N < 0*P, we'll
end up in [1*P, 2*P] meaning we'll
have 1 as the leftmost digit, and so on.

After going over 9*P, we're sure we've
collected all the digits in [0-9].

So, 0 is the only case where 'INSOMNIA'
must be returned.
'''

def fn(N):
    if N == 0: return 'INSOMNIA'

    s = set(str(N))
    i = 2
    res = N
    while len(s) < 10:
        s.update(set(str(i * N)))
        res = i * N
        i += 1
    return res

if __name__ == '__main__':
    import re, sys

    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        ncases = int(f.readline().strip())

        for i in range(1, ncases + 1):
            N = int(f.readline().strip())
            print('Case #{}: {}'.format(i, fn(N)))
