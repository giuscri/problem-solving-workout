def afterLog(fname):
    def f(methd):
        def _f(*args, **kwargs):
            ret = methd(*args, **kwargs)
            print("*** I've called {}()".format(fname))
            return ret
        return _f
    return f

def beforeLog(fname):
    def f(methd):
        def _f(*args, **kwargs):
            print("*** I'm going to call {}()".format(fname))
            ret = methd(*args, **kwargs)
            return ret
        return _f
    return f

def beforePreCondition(fname):
    def f(methd):
        def _f(*args, **kwargs):
            print("*** {}() has been called with :- {}".format(fname, args[1:]))
            ret = methd(*args, **kwargs)
            return ret
        return _f
    return f

def afterPostCondition(fname):
    def f(methd):
        def _f(*args, **kwargs):
            ret = methd(*args, **kwargs)
            print("*** the value the call should return is {}() :- {}"\
                     .format(fname, ret))
            return ret
        return _f
    return f

class weaving(type):
    def __new__(metacls, cls, pca):
        clsdict = dict(cls.__dict__)
        for n,d in pca:
            if n in clsdict:
                clsdict[n] = d(n)(clsdict[n])
        return type.__new__(metacls, cls.__name__, (), clsdict)

    def __init__(metacls, cls, pca):
        return type.__init__(metacls, cls.__name__, (), dict(cls.__dict__))
