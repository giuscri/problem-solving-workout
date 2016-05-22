def rot13_decode(s):
    r = []

    for c in s:
        if c.isupper():
            r.append(chr(((ord(c) - 65) - 13) % 26 + 65))

        elif c.islower():
            r.append(chr(((ord(c) - 97) - 13) % 26 + 97))

        else:
            r.append(c)

    return ''.join(r)

if __name__ == '__main__':
    print(rot13_decode('Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'))
