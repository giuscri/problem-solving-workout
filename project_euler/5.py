'''
The simplest approach is iterating over the
positive integers. This takes too much when
testing for divisors in [2..20]

    n = 20
    while sum([n%i for i in range(2, 20 +1)]) != 0:
        n += 1
    print('*** Computed {}'.format(n))

Another approach was needed.

I precomputed (...on paper) a list containing
the factorization of each number in [2..20],
then fetched only the factors I really needed,
discarding redudant values (e.g. choosing
4 discarding 2, such that the resulting number
is both divisible by 4 and 2 _for free_).
'''

lst = [
    {2: 1},
    {3: 1},
    {2: 2},
    {5: 1},
    {2: 1, 3: 1},
    {7: 1},
    {2: 3},
    {3: 2},
    {2: 1, 5: 1},
    {11: 1},
    {2: 2, 3: 1},
    {13: 1},
    {2: 1, 7: 1},
    {3: 1, 5: 1},
    {2: 4},
    {17: 1},
    {2: 1, 3: 2},
    {19: 1},
    {2: 2, 5: 1},
]

d = {}
for x in lst:
    for k, v in x.items():
        if k not in d or d[k] < v:
            d[k] = v

r = 1
for k, v in d.items():
    r *= k ** v

print('*** Computed {}'.format(r))
