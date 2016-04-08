#!/usr/bin/python3

'''
Tried a bruteforce approach first, like

    for a in range(999, 100, -1):
        for b in range(999, 100, -1):   
            ...

performing good enough to solve the problem: ~1.5sec

Then, after a quick glance to the writeup, I realised
I needed to test only half the (a,b) pairs. Indeed,
as Gauss as a kid teached us, we can see the products as

    999 998 997 ... 100
     *   *   *       *
    100 101 102 ... 999

so, we can half the number of pairs to test,
stopping (or starting) at (999 + 100) // 2

After that improvement, execution time
improved by ~75%.

Also, given the hint that 143 * 177 == 111111,
we can state that any palindrome obtained from
two 3digits numbers must be AT LEAST of 6digits
(since we're searching something >= 111111).

Given that, it's easy to show that our candidate
must be a multiple of 11. Since 11 is prime then
a, b or both must be multiple of 11.

If a % 11 != 0 then b MUST be a multiple of 11:
that means that we can iterate over the set of b's
by 11 -- reducing the number of cases to test.

After this last two elegant improvements, execution time
improved by ~90% (~0.17sec) from the bruteforce approach.
'''

from functools import reduce

def fn(n):
    s = str(n)
    return s == ''.join(reversed(s))

a_start = 999
a_stop = (999 + 100) // 2 -1
a_step = -1

if a_start % 11 != 0:
    b_start = 110
    b_step = 11
    b_stop = (999 + 100) // 2 +11

else:
    b_start = 100
    b_step = 1
    b_stop = (999 + 100) // 2 +1

lst = []
for a in range(a_start, a_stop, a_step):
    for b in range(b_start, 1000, b_step):
        n = a * b
        if fn(n):
            lst.append(n)

res = reduce(lambda x, y: x if x > y else y, lst[1:], lst[0])
print('*** Computed {}'.format(res))
