# Ispired by this post
#    http://blog.codinghorror.com/why-cant-programmers-program/

def fizzbuzz(a, b):
    for x in range(a, b):
        if x%3==0:
            print('Fizz',end='')
        if x%5==0:
            print('Buzz',end='')
        if x%3!=0 and x%5!=0:
            print(x,end='')
        # Very conservative way
        # of formatting stuff ... :-)
        print()
