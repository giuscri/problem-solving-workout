def convert_number(s, b1, b2):
    l = list(s)
    l.reverse()
    l = map(lambda x: int(x) if ord('0') <= ord(x) <= ord('9') else ord(x)-ord('A')+10, l)
    powers_of_b1 = [b1**i for i in range(len(s))]
    n = sum(map(lambda p: p[0]*p[1], zip(l, powers_of_b1)))
    digits = []
    while n != 0:
        d = n % b2
        if d < 10:
            digits.append(str(d))
        else:
            digits.append(chr(ord('A') + d-10))
        n //= b2
    return ''.join((lambda l: l.reverse() or l)(digits))
