def reverse(s):
    ret = []
    def f(s, ret):
        if len(s) == 0: return
        f(s[1:], ret)
        ret += s[0]
    f(s, ret)
    return ''.join(ret)

def strip(s, chars):
    ret = []
    def f(s, ret):
        if len(s) == 0: return
        if s[0] not in chars: ret.append(s[0])
        f(s[1:], ret)
    f(s, ret)
    return ''.join(ret)

def split(s, seps):
    ret = []
    def f(s, tk, ret):
        if len(s) == 0:
            tk = ''.join(tk)
            tk is not '' and ret.append(tk)
        elif s[0] in seps:
            tk = ''.join(tk)
            tk is not '' and ret.append(tk)
            f(s[1:], [], ret)
        else:
            f(s[1:], tk + [s[0]], ret)
    f(s, [], ret)
    return ret

def _cycle(f):
    cache = dict()
    def _f(s, ch):
        nonlocal cache
        if (s,ch) in cache:
            r = f(s[cache[(s,ch)]:], ch)
            if r < 0:
                cache[(s,ch)] = 0
            else:
                chd = cache[(s,ch)]
                rtnd = r
                cache[(s,ch)] += rtnd +1
                r = chd + rtnd
            return r
        r = f(s, ch)
        cache[(s,ch)] = r +1
        return r
    return _f

@_cycle
def find(s, ch):
    def f(s, ch, pos):
        if len(s) == 0: return -1
        if s[0] == ch: return pos
        return f(s[1:], ch, pos + 1)
    return f(s, ch, 0)

if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    s3 = "The topic ais appealing nevertheless the speaker was too monotonous."
    print(strip(s0, 'aeiou'))
    print(reverse(s0))
    print(strip(reverse(s0), 'aeiou'))
    print(split(s1, ' ;,.'))
    print(reverse(s2))
    print("tests on find:")
    print(find(s2, 'a'))
    print(find(s2, 'a'))
    print(find(s2, 'a'))
    print(find(s3, 'a'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
