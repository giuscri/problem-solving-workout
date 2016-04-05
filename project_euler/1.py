#!/usr/bin/python3

res = 0
for i in range(1000):
    if i%3 == 0:
        res += i
        continue

    if i%5 == 0:
        res += i
        continue

print('*** Computed {}'.format(res))

