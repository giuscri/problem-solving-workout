T = (
    ('I', 1),
    ('IV', 4),
    ('V', 5),
    ('IX', 9),
    ('X', 10),
    ('XL', 40),
    ('L', 50),
    ('XC', 90),
    ('C', 100),
    ('CD', 400),
    ('D', 500),
    ('CM', 900),
    ('M', 1000)
)

def roman2decimal(s):
    _T = dict(T)
    # Saving input in case raising
    # an exception is necessary
    in_s = s[:]
    n = 0
    while s != '':
        if s[:2] in _T:
            n += _T[s[:2]]
            s = s[2:]
        elif s[:1] in _T:
            n += _T[s[:1]]
            s = s[1:]
        else:
            raise Exception('{} is not a valid roman number'.format(in_s))
    return n

def decimal2roman(n):
    _T = tuple(map(lambda p: (p[1],p[0]), T))
    s = ''
    while n != 0:
        i = 0
        while i < len(_T) and _T[i][0] <= n:
            i += 1
        s += _T[i-1][1]
        n = n - _T[i-1][0]
    return s

if __name__ == '__main__':
    assert roman2decimal('XXX') == 30
    assert roman2decimal('XXXIV') == 34
    assert decimal2roman(6) == 'VI'
