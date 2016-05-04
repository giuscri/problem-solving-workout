def from_base10_to_baseb(n, b):
    if n == 0: return 0

    lst = []
    while n != 0:
        lst.append(n % b)
        n //= b

    return int(''.join(map(str, reversed(lst))))

def from_baseb_to_base10(n, b):
    ret = 0
    for i, n in enumerate(reversed(str(n))):
        ret += int(n) * (b ** i)
    return ret

if __name__ == '__main__':
    assert from_baseb_to_base10(from_base10_to_baseb(42, 7), 7) == 42
