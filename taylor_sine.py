from functools import *
from math import *

def myfact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        if i%2 !=0: yield fact

def mysin(x,n):
    g=myfact(n)
    #return sum([(x**i)/next(g) for i in range(1,n//2+1)])
    lst = [(x**i)/next(g) for i in range(1,n//2+1, 2)]
    lst = zip(lst, [1 if i%2==0 else -1 for i in range(len(lst))])
    return sum([x*y for x,y in lst])
