import sys

class TailRecursionException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_recursion(f):
    def _f(*args, **kwargs):
        frm = sys._getframe()
        if frm.f_back and frm.f_back.f_back \
           and frm.f_back.f_back.f_code == frm.f_code:
            raise TailRecursionException(args, kwargs)
        else:
            while True:
                try:
                    return f(*args, **kwargs)
                except TailRecursionException as e:
                    args = e.args
                    kwargs = e.kwargs
    return _f

@tail_recursion
def tfact(n, acc=1):
    if n == 0: return acc
    return tfact(n-1, n * acc)
