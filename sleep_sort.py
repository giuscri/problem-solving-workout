import threading
import time

def sleepsort(lst):
    assert len(list(filter(lambda x: x < 0, lst))) == 0

    ts = []
    res = []
    lk = threading.Condition()

    def f(sleeptime, res, lk):
        time.sleep(sleeptime/1000)
        with lk:
            #res.append(sleeptime)
            print(sleeptime, end=' ')
            lk.notify()

    for x in lst:
        ts.append(threading.Thread(target=f, args=(x, res, lk)))
        ts[-1].start()

    all_done = lambda: len(list(filter(lambda t: t.is_alive(), ts))) == 0

    with lk:
        lk.wait_for(all_done)

    print()

if __name__ == '__main__':
    sleepsort([7, 2 ,100, 1, 9, 45, 2, 33, 7, 77, 25])
    sleepsort([333, 222 ,112, 777, 901, 455, 256, 313, 125, 625, 825, 999, 316])
    sleepsort([1000, 10, 10.5, 100, 22, 77, 700, 3.145, 2000, 150, 35, 287, 4, 7, 777, 2525, 255, 256, 25])
