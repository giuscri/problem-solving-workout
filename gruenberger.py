import functools

mv_north = lambda tple: (tple[0]  , tple[1]+1, 'n')
mv_south = lambda tple: (tple[0]  , tple[1]-1, 's')
mv_east  = lambda tple: (tple[0]+1, tple[1]  , 'e')
mv_west  = lambda tple: (tple[0]-1, tple[1]  , 'w')

def nxt_pos(cur_pos, mv=None):
    if cur_pos[2] == 'n':
        if mv is None:
            return mv_north(cur_pos)
        elif mv == 'l':
            return mv_west(cur_pos)
        elif mv == 'r':
            return mv_east(cur_pos)

    if cur_pos[2] == 's':
        if mv is None:
            return mv_south(cur_pos)
        elif mv == 'l':
            return mv_east(cur_pos)
        elif mv == 'r':
            return mv_west(cur_pos)

    if cur_pos[2] == 'w':
        if mv is None:
            return mv_west(cur_pos)
        elif mv == 'l':
            return mv_south(cur_pos)
        elif mv == 'r':
            return mv_north(cur_pos)

    if cur_pos[2] == 'e':
        if mv is None:
            return mv_east(cur_pos)
        elif mv == 'l':
            return mv_north(cur_pos)
        elif mv == 'r':
            return mv_south(cur_pos)

    raise ValueError('You should not be here.')

def deep_recursion_allowed(f):
    def _f(*args, **kwargs):
        import sys
        deflt = sys.getrecursionlimit()
        sys.setrecursionlimit(deflt * 100)
        r = f(*args, **kwargs)
        sys.setrecursionlimit(deflt)
        return r
    return _f

@deep_recursion_allowed
def sieve(n):
    def f(itbl, ps):
        if len(itbl) == 0: return ps
        r = functools.reduce(lambda x,y: x or y, \
                                map(lambda p: itbl[0]%p == 0, ps))
        if r is False: return f(itbl[1:], ps+[itbl[0]])
        return f(itbl[1:], ps)
    return f(range(3,n +1), [2])

@deep_recursion_allowed
def crossing(n=10001):
    ps = sieve(n)

    def f(cur_pos, i, d):
        if i >= n: return d

        coords = cur_pos[:-1]
        if coords in d:
            d[coords] += [i]
        else:
            d[coords] = [i]

        if i not in ps:
            cur_pos = nxt_pos(cur_pos)
        elif (i-1)%6 == 0:
            cur_pos = nxt_pos(cur_pos, 'l')
        elif (i+1)%6 == 0:
            cur_pos = nxt_pos(cur_pos, 'r')
        else:
            raise ValueError('You should not be here.')

        return f(cur_pos, i+2, d)
    r = f((1,0,'e'), 5, { (0, 0): [3], })
    r = map(lambda p: p[1], r.items())
    r = filter(lambda l: len(l) > 1, r)
    r = list(map(lambda lst: sorted(lst), r))
    r.sort(key=lambda lst: lst[0])
    return r

if __name__ == '__main__':
    for i in crossing():
        print("### :- ", i)
