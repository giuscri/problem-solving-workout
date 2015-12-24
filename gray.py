def cached_generator(f):
    cached_in, cached_out = [], []
    def _f(*args, **kwargs):
        if (f,args,kwargs) in cached_in:
            ix = cached_in.index((f,args,kwargs))
            res = cached_out[ix]
            print(' --> '.join([
                '### cached value for {}'.format(args),
                '{}'.format(res)
            ]))
            return res
        res = [x for x in f(*args, **kwargs)]
        cached_in.append((f,args,kwargs))
        cached_out.append(res)
        return res
    return _f

@cached_generator
def GC(n):
    if n==1: yield '0'; yield '1'
    else:
        lst = [c for c in GC(n-1)]
        for c in lst:
            yield '0' + c
        for c in reversed(lst):
            yield '1' + c
