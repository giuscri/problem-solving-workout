#!/usr/bin/python3

n = 4 * 10**6

a, b = 1, 2

res = b

c = a + b
while c < n:
    if c%2 == 0: res += c
    a = b
    b = c
    c = a + b

print('*** Computed {}'.format(res))
