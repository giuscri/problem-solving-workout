def even(s):
    while True:
        try:
            nxt = next(s)
            if nxt%2 != 0: continue
            yield nxt
        except StopIteration as e:
            raise e

def stopAt(s, n):
    while True:
        try:
            nxt = next(s)
        except StopIteration as e:
            raise e

        if nxt < n:
            yield nxt
        else:
            raise StopIteration()

def buffer(s, n):
    while True:
        lst = []
        try:
            for i in range(n):
                lst.append(next(s))
            yield lst
        except StopIteration as e:
            yield lst
            raise e

def conditional(s, p):
    try:
        cur = next(s)
    except StopIteration as e:
        raise e

    while True:
        try:
            nxt = next(s)
            if p(nxt): yield cur
            cur = nxt
        except StopIteration as e:
            raise e

if __name__ == '__main__':
    def fib():
       x,y = 1,1
       while True:
           yield x
           x,y = y, x+y

    even_fib = even(fib())
    for i in range(10): print(next(even_fib), end=' ')
    print()

    for i in stopAt(even(fib()), 40000000): print(i, end=' ')
    print()

    buffered_limited_fib = buffer(stopAt(fib(),3000), 5)
    for i in buffered_limited_fib: print(i)

    condfib = conditional(fib(), lambda x: (x%2 == 0))
    for i in range(10): print(next(condfib), end=' ')
    print()

    condfib2 = conditional(fib(), lambda x: (x%2 != 0))
    for i in range(15): print(next(condfib2), end=' ')
    print()
