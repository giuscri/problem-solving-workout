import math

n = 600851475143

lst = [[i, False] for i in range(2, int(math.sqrt(n)))]

for i, f in enumerate(lst):
    if f[1]: continue

    for x in lst[i+1:]:
        if x[0]%f[0] == 0:
            x[1] = True
        if n%x[0] != 0:
            x[1] = True

for x in reversed(lst):
    if not x[1]:
        print('*** Computed {}'.format(x[0]))
        break
