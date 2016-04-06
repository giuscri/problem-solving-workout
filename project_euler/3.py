import math

'''
We can stop at the sqrt(n), since
IF EXISTS (not always true![0]) a prime factor
larger than sqrt(n), that's unique.

Indeed, say that

    n = k * p * q

where k is some integer, and p,q are
two prime factors larger than sqrt(n),
then you'll have

    n = k * p * q > k * n

i.e.

    n > k * n

which can't be.

Thus, when searching for the prime factors of n,
we can stop at the first one after the sqrt(n), since
we've just shown that that's the last one.

---
[0], 10 = 2 * 5 and the sqrt(10) < 5; yet
30 = 2 * 3 * 5 and sqrt(30) > 5.
'''

# TODO
