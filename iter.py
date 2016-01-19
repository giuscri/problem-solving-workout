import re

class UpDownFile:
    def __init__(self, fname):
        with open(fname, 'r') as f:
            self.ws = re.split('\W+', f.read().strip())
        self.ix = 0

    def __iter__(self):
        self.ix = 0
        return self

    def __next__(self):
        if self.ix >= len(self.ws):
            raise StopIteration()
        ret = self.ws[self.ix]
        self.ix += 1
        return ret

    def ungetw(self):
        if self.ix-1 < 0:
            raise StopIteration()
        self.ix -= 1
