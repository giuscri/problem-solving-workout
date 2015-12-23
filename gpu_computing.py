from simd import *
import functools

@split_and_merge(11, lambda a: functools.reduce(lambda x,y: x*y, a))
def mul(l): 
  return functools.reduce(lambda x,y: x*y, l)

@split_and_merge(5, lambda a: functools.reduce(lambda x,y: y+x, a))
def reverse(l):
  return l[::-1]

if __name__ == "__main__":
  print(mul(list(range(1,101)))) # this computes 100!
  print(mul(list(range(1,31))))  # this computes 30!
  print(reverse("She sells sea shells on the sea shore. If she sells sea shells on the sea shore, where are the sea shells she sells?"))
  print(reverse("Swan swam over the pond, Swim swan swim! Swan swam back again - Well swum swan!"))
