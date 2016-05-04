import re
import types
import time

def tracer(f):
    ncalls = 0
    def _f(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        print('Calling #{} to {}'.format(f.__name__, ncalls))
        f(*args, **kwargs)
    return _f


class Person:
    #@tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    #@tracer
    def give_raise(self, percent):
        self.pay = int(self.pay + self.pay*percent*0.01)

    #@tracer
    def last_name(self):
        return re.split('\s+', self.name)[-1]

class PersonMeta(type):
    def __new__(meta, classname, supers, classdict):
        for k,v in classdict.items():
            if type(v) is types.FunctionType:
                classdict[k] = tracer(v)
        return type.__new__(meta, classname, supers, classdict)

#Person = PersonMeta('Person', (), dict(Person.__dict__))

def decorate_all(decorator):
    class Meta(type):
        def __new__(meta, classname, supers, classdict):
            for k,v in classdict.items():
                if type(v) is types.FunctionType:
                    classdict[k] = tracer(v)
            return type.__new__(meta, classname, supers, classdict)
    return Meta

Person = decorate_all(tracer)('Person', (), dict(Person.__dict__))

class Cat:
    cached_names = []
    cached_instances = []

    def __new__(cls, name):
        if name in cls.cached_names:
            return cls.cached_instances[cls.cached_names.index(name)]
        time.sleep(2)
        cls.cached_names.append(name)
        cls.cached_instances.append(super(Cat, cls).__new__(cls))
        return cls.cached_instances[-1]

    def __init__(self, name):
        self.name = name

    def meow(self):
        return 'Meow!, my name is {}'.format(self.name)

class Meta(type):
    def __new__(meta_cls, cls_name, supers, cls_dict):
        cls_dict['meow'] = lambda self: 'A classic: meow!'
        return super(Meta, meta_cls).__new__(meta_cls, cls_name, supers, cls_dict)

    def __init__(cls, cls_name, supers, cls_dict):
        cls.answer = 42

    def __call__(cls, *args, **kwargs):
        #...

cls = Meta('cls', (), {})
