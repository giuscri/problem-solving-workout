import functools

def sieve(n):
    def f(itbl, ps):
        if len(itbl) == 0: return ps
        r = functools.reduce(lambda x,y: x or y, \
                                map(lambda p: itbl[0]%p == 0, ps))
        if r is False: return f(itbl[1:], ps+[itbl[0]])
        return f(itbl[1:], ps)
    return f(range(3,n +1), [2])
