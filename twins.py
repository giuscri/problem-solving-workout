import inspect

def Twins(supers):
    class metacls(type):
        def __new__(meta, clsname, sps, clsdict):
            def __init__(self, *args):
                nargs = dict()
                for cls in supers:
                    nargs[cls.__name__] = \
                       len(inspect.signature(cls.__init__).parameters) -1
                self.wrapped_instances = dict()
                for cls in supers:
                    na = nargs[cls.__name__]
                    self.wrapped_instances[cls.__name__] = \
                       cls(*args[:na])
                    args = args[na:]
            clsdict['__init__'] = __init__

            def __getattr__(self, name):
                for n,wi in self.wrapped_instances.items():
                    res = getattr(wi, name, None)
                    if res is not None: return res
            clsdict['__getattr__'] = __getattr__

            def __setattr__(self, name, value):
                if name == 'wrapped_instances':
                    self.__dict__[name] = value
                else:
                    for n,wi in self.wrapped_instances.items():
                        res = getattr(wi, name, None)
                        if res is None: continue
                        wi.__dict__[name] = value
            clsdict['__setattr__'] = __setattr__

            return type.__new__(meta, clsname, sps, clsdict)
    return metacls

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student:
    def __init__(self, cv):
        self.cv = cv
    def add_exam(self, name, mark):
        self.cv[name] = mark
    def average(self):
        return sum(self.cv.values())/len(self.cv)

class Worker:
    def __init__(self, salary):
        self.daily = salary
    def deduction(self, percentage):
        return self.daily*percentage/100
    def salary(self,percentage):
        return (self.daily-self.deduction(percentage))*365

class WorkingStudent(metaclass=Twins([Person,Student,Worker])): pass

if __name__ == '__main__':
    w = WorkingStudent('Walter', 25, dict({'PA':28, 'LP':30}), 100)
    print("The working student {} is {} years old".format(w.name,w.age))
    w.add_exam('TSP', 30)
    print("His current curriculum is:")
    for exam, mark in w.cv.items():
        print(" · {:3} :- {}".format(exam, mark))
    print("... and his current average is {:.2f}".format(w.average()))
    print("Last but not least. He is currently earning {}€".format(w.salary(10)))
