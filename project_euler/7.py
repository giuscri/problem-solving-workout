import math

n = 1
counter = 2

while counter <= 10001:
    n += 2
    prime = True
    for i in range(2, int(math.sqrt(n)) +1):
        if n%i == 0:
            prime = False
            break
    if prime:
        counter += 1

print('*** Computed {}'.format(n))
