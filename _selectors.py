def private(*private_attributes):
    def f(cls):
        class c:
            def __init__(self, *args, **kwargs):
                self.wrapped_instance = cls(*args,**kwargs)
                self.private_attributes = private_attributes

            def __getattr__(self, name):
                return getattr(self.wrapped_instance, name)

            def __setattr__(self, name, value):
                if name in ['wrapped_instance', 'private_attributes']:
                    self.__dict__[name] = value
                else:
                    setattr(self.wrapped_instance, name, value)
        return c
    return f

def selectors(d):
    def f(cls):
        class c:
            def __init__(self, *args, **kwargs):
                self.wrapped_instance = cls(*args, **kwargs)

                if getattr(self.wrapped_instance, 'private_attributes', None) is None:
                    raise TypeError('attempt to decorate a non `private`-decorated class')

                camelize = lambda s: s[:1].upper() + s[1:]

                def make_getter(name):
                    return lambda: getattr(self.wrapped_instance, name)

                def make_setter(name):
                    return lambda value: setattr(self.wrapped_instance, name, value)

                for name in d['get']:
                    if name not in self.wrapped_instance.private_attributes:
                        raise TypeError('attempt to add a selector for a non private attribute: {}'.format(name))
                    setattr(self, 'get{}'.format(camelize(name)), make_getter(name))

                for name in d['set']:
                    if name not in self.wrapped_instance.private_attributes:
                        raise TypeError('attempt to add a selector for a non private attribute: {}'.format(name))
                    setattr(self, 'set{}'.format(camelize(name)), make_setter(name))

            def __getattr__(self, name):
                if name in self.wrapped_instance.private_attributes:
                    raise TypeError('private attribute fetch: {}'.format(name))
                return getattr(self.wrapped_instance, name)

            def __setattr__(self, name, value):
                if name == 'wrapped_instance':
                    self.__dict__[name] = value
                elif name in self.wrapped_instance.private_attributes:
                    raise TypeError('private attribute set: {}'.format(name))
                else:
                    setattr(self.wrapped_instance, name, value)
        return c
    return f
