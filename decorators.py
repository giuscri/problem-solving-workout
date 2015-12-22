import time

def decorator(cls):
    class wrapper:
        def __init__(self, *args, **kwargs):
            print('Creating instance of {}...'.format(cls.__name__))
            self.wrapped = cls(*args, **kwargs)
        def __getattr__(self, name):
            print('Fetching {} from {}'.format(name, self.wrapped))
            return getattr(self.wrapped, name)
        def __setattr__(self, name, value):
            if name == 'wrapped':
                self.__dict__[name] = value
            else:
                print('Setting {} of {} to {}'\
                         .format(name, self.wrapped, value))
                setattr(self.wrapped, name, value)
    return wrapper

class timer:
    def __init__(self, f):
        self.f = f
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.f(*args, **kwargs)
        stop = time.time()
        self.alltime += stop-start
        return ret

def Tracer(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = cls(*args, **kwargs)
        def __getattr__(self, attribute):
            self.fetches += 1
            return getattr(self.wrapped, attribute)
    return Wrapper

@Tracer
class Person:
    def __init__(self, name):
        self.name = name

@timer
def listcomp(N):
    return [x*2 for x in range(N)]

@decorator
class C:
    def __init__(self, x, y): self.attr = 'spam'
    def f(self, a, b): print('*** f({}, {})'.format(a, b))

class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    def __getattr__(self, attribute):
        return getattr(self.instance, attribute)
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
            return self.instance
        else:
            print('{} is a singleton!'.format(self.cls.__name__))

@Singleton
class Person:
    def __init__(self, name):
        self.name = name

def Private(*private_attributes):
    def onDecorator(cls):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)
            def __getattr__(self, attribute):
                if attribute not in private_attributes:
                    return getattr(self.wrapped, attribute)
                else:
                    raise TypeError('You cannot access {}'.format(attribute))
            def __setattr__(self, attribute, value):
                if attribute == 'wrapped':
                    self.__dict__[attribute] = value
                elif attribute not in private_attributes:
                    setattr(self.wrapped, attribute, value)
                else:
                    raise TypeError('You cannot set {}'.format(attribute))
        return onInstance
    return onDecorator

@Private('secret')
class Cat:
    def __init__(self, name):
        self.name = name
        self.secret = "I'm not a real cat ..."
    meow = lambda self: print('Meow')

def log_to_stdout(f):
    def _f(*args, **kwargs):
        print('[decorator] Calling {}!'.format(f.__name__))
        return f(*args, **kwargs)
    return _f

lst = [x for x in range(42)]
@log_to_stdout
def f(lst):
    if len(lst) < 1: return
    f(lst[1:])
