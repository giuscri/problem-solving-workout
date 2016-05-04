import math, decimal

def find_factor(n):
    if n % 2 == 0: return 2

    ceil = math.ceil(decimal.Decimal(n).sqrt())
    for d in range(3, ceil + 1, 2):
        if n % d == 0: return d
    return n

