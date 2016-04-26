'''
Using python's comprehension was too easy. Indeed,
you can easily compute the result via

    lst = [n for n in range(1, 100 +1)]
    res = sum(lst)**2 - sum(map(lambda x: x**2, lst))

in ~0.06sec.

In case some C-like language was used, one
could easily use a for-loop such as

    s0 = 0
    for n in range(1, 100 +1):
        s0 += n
    s0 **= 2

    s1 = 0
    for n in range(1, 100 +1):
        s1 += n**2

    r = s0 - s1

`time` reports the exact same performance.
'''

r = 0
for i in range(1, 1000 +1):
    for j in range(1, 1000 +1):
        if i == j: continue
        r += i * j
print('*** Computed {}'.format(r))
