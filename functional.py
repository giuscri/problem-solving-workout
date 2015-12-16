import functools

def foreach(l, cb):
    if len(l) < 1:
        return
    cb(l[0])
    return foreach(l[1:], cb)

def fact(p):
    return functools.reduce(lambda n,m: n*m, range(1,p+1))

def bigmuls(xs, ys):
    bigmuls = []
    for x in xs:
        for y in ys:
            if x*y > 25:
                bigmuls.append((x, y))
    return bigmuls

if __name__ == '__main__':
    foreach([x for x in range(10)], print)
