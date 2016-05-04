import os
import re
import time

def memory_consumption(f):
    def _f(*args, **kwargs):
        pid = os.getpid()
        # before
        with open('/proc/{}/status'.format(pid)) as fl:
            lns = fl.read().strip().split('\n')
        for ln in lns:
            if re.match('VmSize', ln):
                bfr_sz = int(re.search('\d+', ln).group(0))
        r = f(*args, **kwargs)
        # after
        with open('/proc/{}/status'.format(pid)) as fl:
            lns = fl.read().strip().split('\n')
        for ln in lns:
            if re.match('VmSize', ln):
                aftr_sz = int(re.search('\d+', ln).group(0))
        fmt = '*** Memory consumption of {}: {}'
        print(fmt.format(f.__name__, aftr_sz-bfr_sz))
        return r
    return _f

@memory_consumption
def f():
    lst = [x for x in range(2**25)]
    return lst

if __name__ == '__main__':
    f()
