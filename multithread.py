import threading

can_consume = True
data = [1 for x in range(5)]

def infinite_loop(f):
    def _f():
        while True: f()
    return _f

@infinite_loop
def f():
    while can_consume and len(data) > 0:
        print('[Consuming] {}'.format(data))
        data.pop()
    global can_consume
    can_consume = False

@infinite_loop
def g():
    while not can_consume and len(data) < 5:
        print('[Reloading] {}'.format(data))
        data.append(1)
    global can_consume
    can_consume = True

ts = []
ts.append(threading.Thread(target=f))
ts.append(threading.Thread(target=g))

for t in ts: t.start()
