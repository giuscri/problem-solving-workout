#!/usr/bin/python3

'''
You can show that every third fibonacci
number is even. More specifically,
if fib(3n-2) is odd, fib(3n-1) is odd
and fib(3n) is even, then fib(3n+3) is even:

fib(3n + 1) = fib(3n - 1) + fib(3n) = {odd} + {even} = {odd}
fib(3n + 2) = fib(3n) + fib(3n + 1) = {even} + {odd} = {odd}
fib(3n + 3) = fib(3n + 1) + fib(3n + 2) = {odd} + {odd} = {even}

Then, whenever you have O-O-E, you'll have O-O-E again.

Since you start with O-O-D (1, 1, 2), you'll have this
pattern over and over again -- just proved by induction.

We can simply add the third fibonacci number then.
'''

def g(n):
    a, b = 1, 1
    c = a + b
    while c < n:
        yield c
        a = c + b
        b = a + c
        c = a + b
    raise StopIteration()

res = sum([x for x in g(4 * 10**6)])
print('*** Computed {}'.format(res))
