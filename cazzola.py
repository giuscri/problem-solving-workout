import time
import traceback
import types

class _memoization:
    def __init__(self):
        self.cached_keys = []
        self.cached_results = []
    def __call__(self, f):
        def _f(*args,**kwargs):
            if (f,args,kwargs) in self.cached_keys:
                print('Lucky you!, retrieving from cache.')
                print('Getting {}'.format((f,args,kwargs)))
                ix = self.cached_keys.index((f,args,kwargs))
                return self.cached_results[ix]
            result = f(*args,**kwargs)
            self.cached_keys.append((f,args,kwargs))
            self.cached_results.append(result)
            ## Simulating hard computation
            ## when caching was useless ...
            time.sleep(0.5)
            return result
        return _f

memoization = _memoization()

@memoization
def f(a, b):
    return a+b

@memoization
def g(a):
    return 100 + a


@memoization
def _sum(lst,cntr=0):
    if len(lst) < 1: return cntr
    return _sum(lst[1:], lst[0]+cntr)

class MyMathMeta(type):
    print('Creating cache...',end=' ')
    memoization = _memoization()
    print('Done!')
    def __new__(meta, classname, supers, classdict):
        for k,v in classdict.items():
            if type(v) is types.FunctionType:
                classdict[k] = memoization(v)
        return type.__new__(meta, classname, supers, classdict)

class MyMath(metaclass=MyMathMeta):
    def fib(self,n):
        '''
        Returns the nth # of Fibonacci's
        '''
        if n==0 or n==1: return 1
        return self.fib(n-1) + self.fib(n-2)

    def fact(self, n):
        '''
        Returns n!
        '''
        if n==0: return 1
        return self.fact(n-1) * n

def stack_trace(f):
    def _f(*args, **kwargs):
        traceback.print_stack()
        return f(*args, **kwargs)
    return _f

def dummy_wrapper(f):
    def _f(*args,**kwargs): return f(*args,**kwargs)
    return _f
    
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@dummy_wrapper
@stack_trace
def f(a, b):
    return a + b

class _logging:
    def __init__(self, fname):
        self.fdata = open(fname, 'a')
    def __call__(self, f):
        def _f(*args, **kwargs):
            self.fdata.write('Called {} with arguments: {} {}\n'.format(f, args, kwargs))
            self.fdata.flush()
            return f(*args, **kwargs)
        return _f

logging = _logging('log.txt')

@logging
def f(a, b): return a + b
