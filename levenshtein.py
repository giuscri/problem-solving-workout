def timed(f):
    import time
    def _f(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        stop = time.time()
        print('Took {}'.format(stop-start))
        return res
    return _f

def memoized(f):
    cached_arguments = []
    cached_results = []
    def _f(*args, **kwargs):
        if (args,kwargs) in cached_arguments:
            #print('Fetching cached result for {}, {} ...'\
            #         .format(args, kwargs))
            return cached_results[cached_arguments.index((args,kwargs))]
        res = f(*args, **kwargs)
        cached_arguments.append((args,kwargs))
        cached_results.append(res)
        return res
    return _f

@memoized
def edit_distance(A, B):
    @memoized
    def _edit_distance(A, B):
        def replace_cost(x, y):
            if x == y: return 0
            return 1

        if len(A) == 0: return len(B)
        if len(B) == 0: return len(A)

        cs = []
        cs.append(replace_cost(A[0], B[0]) + _edit_distance(A[1:], B[1:]))
        cs.append(1 + _edit_distance(A[1:], B))
        cs.append(1 + _edit_distance(A, B[1:]))

        return min(cs)

    for i in range(1, len(A)):
        _edit_distance(A[:i], B[:i])

    return _edit_distance(A, B)
