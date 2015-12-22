class MainMeta(type):
    def __init__(cls, name, bases, ns):
        cls.use_main_meta = True

class Field:
    def __init__(self, obj_type):
        self.obj_type = obj_type
    def is_valid_value(self, value):
        return isinstance(value, self.obj_type)

class EnforcerMeta(type):
    def __init__(cls, name, bases, ns):
        cls.fields = {}
        for k,v in ns.items():
            if isinstance(v, Field):
                cls.fields[k] = v

class Enforcer(metaclass=EnforcerMeta):
    def __setattr__(self, attribute, value):
        if attribute in self.fields:
            if not self.fields[attribute].is_valid_value(value):
                raise TypeError('Wow!')
        #super(Enforcer, self).__setattr__(attribute, value)
        self.__dict__[attribute] = value

class Person(Enforcer):
    name = Field(str)
    age = Field(int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

class CC:
    __slots__ = ['stack', 'hello', 'answer']
    def __init__(self):
        self.stack = 'overflow'
        self.hello = 'world'
        self.answer = 42
