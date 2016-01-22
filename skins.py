class stack:
  def __init__(self, dim=10):
    self.dimension = dim
    self.top = 0
    self.data = []
  def is_empty(self): return self.top == 0
  def is_full(self): return self.top == (self.dimension-1)
  def __str__(self):
    return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}".\
        format(self.top, self.dimension, self.data)

class Skin(type):
  def __new__(meta, name, supers, clsdict):
    def become(self, to_add, to_remove):
      import types
      for m in to_remove:
        try:
          #self.__dict__.pop(m)
          delattr(self, m.__name__)
        except AttributeError: pass
      for m in to_add:
        #self.__dict__[m.__name__] = m
        setattr(self, m.__name__, types.MethodType(m, self))
    clsdict['become'] = become
    return type.__new__(meta, name, supers, clsdict)

def push(self, x):
  self.data.append(x)
  self.top += 1

def pop(self):
  self.data.pop()
  self.top -= 1

stack = Skin('stack', (), dict(stack.__dict__))

if __name__ == '__main__':
  s = stack(5) # 5 is the stack dimension
  print(s)
  trend = True
  for i in range(-1,14):
    if s.is_empty(): 
      s.become({push}, {pop})
      trend = True
    elif s.is_full(): 
      s.become({pop}, {push})
      trend = False
    s.push(i) if trend else s.pop()
    print(s)
