def limited_resources(f):
    ncalls = 0
    depth = 0
    def _f(*args, **kwargs):
        global resource
        nonlocal ncalls
        nonlocal depth
        ncalls += 1
        depth += 1
        if ncalls-1 >= resource:
            print('resources run out')
            ncalls = 0
            raise SystemExit()
        ret = f(*args, **kwargs)
        depth -= 1
        if depth == 0: ncalls = 0
        return ret
    return _f

@limited_resources
def fact(n):
    if n < 2: return 1
    return n * fact(n - 1)

@limited_resources
def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

if __name__ == "__main__":
    resource = 10
    print("{0}! :- {1}".format(10,fact(10)))
    resource = 9
    try:
        print("{0}! :- {1}".format(10,fact(10)))
    except SystemExit: pass
    resource = 160
    try:
        print("fibo({0}) :- {1}".format(10,fibo(10)))
    except SystemExit: pass
    resource = 180
    print("fibo({0}) :- {1}".format(10,fibo(10)))
