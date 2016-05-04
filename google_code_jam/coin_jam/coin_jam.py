import itertools, math, decimal

'''
At first I simply tried every odd number
between 2**(N-1) +1 and 2**N -1, then
checked if I could find enough factors
and if n was among those factors.

Notice that in the case of `find_factor`
since we're only searching for *some*
factor -- the first one we get is valid --
we can stop at the sqrt(n).

Indeed, it's a known fact that if n has
a factor greater than sqrt(n), that's unique.

For us, that means that some "twin" factor
< sqrt(n) must exist (it's 1 for prime numbers).

Also, since we want to move very fast towards
generating J coins -- and one coin is as valid
as any another -- if we can't find
a divisor for n in range(3, 4200),
we simply try to mine another coin.

I didn't came up with this "agile" approach
during the competition; instead I insisted
on numbers that I'd better to discard.

Using this rebel approach was enough to
generate enough coins to earning 20pts!

My bad.

Yet, the writeup proposes another, more
elegant approach to that problem.
'''

def find_factor(n):
    if n % 2 == 0: return 2

    ceil = math.ceil(decimal.Decimal(n).sqrt())
    for d in range(3, 4200, 2):
        if n % d == 0: return d
    return n

def g(N):
    for x in range((1 << N-1) +1, (1 << N) -1, 2):
        yield x
    raise StopIteration

def generate(N, J):
    ret = {}

    #itrbl = filter(lambda x: x[0] == x[-1] == '1', map(lambda x: ''.join(x), itertools.product('01', repeat=N)))
    itrbl = g(N)

    counter = 0
    while counter < J:
        x = bin(next(itrbl))[2:]

        fs = []
        for base in range(2, 10 + 1):
            n = int(x, base)
            f = find_factor(n)
            if f != n:
                fs.append(f)
            else:
                break

        if len(fs) == 9:
            ret[x] = fs
            counter += 1

    return ret

if __name__ == '__main__':
    import sys, re

    if len(sys.argv) < 2:
        sys.exit(-1)

    fname = sys.argv[1]

    with open(fname) as f:
        lines = f.read().strip().split('\n')

    ncases = int(lines[0])
    lines = lines[1:]

    for i in range(1, ncases + 1):
        N, J = map(int, re.split(' ', lines[0]))
        lines = lines[1:]

        d = generate(N, J)
        print('Case #{}:'.format(i))
        for k, v in d.items():
            print('{} {}'.format(k, ' '.join(map(str, v))))
