class Skin(type):
    def __new__(meta, classname, supers, classdict):
        def become(self, adding, removing):
            '`adding` and `removing` are iterables of function objs'
            for m in removing:
                if m in self.__dict__: self.__dict__.pop(m.__name__)
            for m in adding:
                self.__dict__[m.__name__] = m.__get__(self)
        classdict['become'] = become
        return type.__new__(meta, classname, supers, classdict)

class stack(metaclass=Skin):
  def __init__(self, dim=10):
    self.dimension = dim
    self.top = 0
    self.data = []
  def is_empty(self): return self.top == 0
  def is_full(self): return self.top == (self.dimension-1)
  def __str__(self):
    return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}" \
        .format(self.top, self.dimension, self.data)

if __name__ == "__main__":

  def push(self, element):
    self.data += [element]
    self.top += 1
  def pop(self):
    ret = self.data[-1]
    self.data = self.data[:-1]
    self.top -= 1
    return ret

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
