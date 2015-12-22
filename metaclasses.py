import types

class Counter(type):

    def decorator(f):
        ncalls = 0
        def _f(*args, **kwargs):
            nonlocal ncalls
            print('{} already called {} time(s)'.format(f.__name__, ncalls))
            ncalls += 1
            return f(*args, **kwargs)
        return _f

    def __new__(meta, classname, supers, classdict):
        f__init__ = classdict['__init__']
        classdict['__init__'] = meta.decorator(f__init__)
        return type.__new__(meta,classname,supers,classdict)

class MultiTriggeredMethod(type):

    def decorator(f):
        ncalls = 0
        def _f(*args, **kwargs):
            nonlocal ncalls
            ncalls += 1
            if ncalls-1 >= 1: return f(*args, **kwargs)
        return _f

    def __new__(meta, classname, supers, classdict):
        for k,v in classdict.items():
            if type(v) is types.FunctionType:
                classdict[k] = meta.decorator(classdict[k])
        return type.__new__(meta,classname,supers,classdict)

class WorkerMeta(type):
    def __new__(meta, classname, supers, classdict):
        ps = [
            ('day_salary',8),
            ('week_salary', 8*5),
            ('month_salary', 8*5*4),
            ('year_salary', 8*5*4*12),
        ]

        for pname,ptimes in ps:
            def build_get_and_set(ptimes):
                class _Descriptor:
                    def __get__(self, instance, owner):
                        return instance.pay_per_hour*ptimes
                    def __set__(self, instance, value):
                        instance.pay_per_hour = value/ptimes
                return _Descriptor
            classdict[pname] = build_get_and_set(ptimes)()

        return type.__new__(meta, classname, supers, classdict)


class Person(metaclass=MultiTriggeredMethod):
    def __init__(self, name, lastname, birthday):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday

    def __repr__(self):
        if self is None: return None
        items = list(self.__dict__.items())
        items.sort(key=lambda p: p[0])
        s = '{}('.format(self.__class__.__name__)
        for k,v in items:
            s += '{}={}, '.format(k,v)
        s = s[:-2] + ')'
        return s

    def meow(self): return 'Meow'
