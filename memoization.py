def memoization(f):

    cache = {
        'in': [],
        'out': [],
    }

    def _f(*args):
        if (f,args) in cache['in']:
            print('## cached value for {}'.format(args))
            ix = cache['in'].index((f,args))
            return cache['out'][ix]

        res = f(*args)
        cache['in'].append((f,args))
        cache['out'].append(res)
        return res
    return _f

@memoization
def sum(x,y):
    if x==0: return y

    return sum(x-1, y+1)

@memoization
def fact(n):
    if n <= 1: return 1

    return n*fact(n-1)

@memoization
def fibo(n):
    if n==0: return 0
    if n==1: return 1

    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    print("sum({0},{1})  => {2}".format(9,5,sum(9,5)))
    print("sum({0},{1})  => {2}".format(7,7,sum(7,7)))
    print("sum({0},{1}) => {2}".format(10,4,sum(10,4)))
    print("sum({0},{1}) => {2}".format(1,13,sum(1,13)))
    print("sum({0},{1}) => {2}".format(7,25,sum(7,25)))

    print("fibo({0})   => {1}".format(5,fibo(5)))
    print("fibo({0})   => {1}".format(7,fibo(7)))
    print("fibo({0})  => {1}".format(25,fibo(25)))

    print("fact({0})   => {1}".format(5,fact(5)))
    print("fact({0})   => {1}".format(7,fact(7)))
    print("fact({0})  => {1}".format(10,fact(10)))
