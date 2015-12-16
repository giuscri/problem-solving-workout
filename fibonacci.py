import time

class Fibonacci:
    def __init__(self, max_index):
        self.max_index = max_index
        self.cache = [1,1]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.max_index: raise StopIteration
        if self.index <= len(self.cache):
            return self.cache[self.index - 1]
        self.cache.append(self.cache[-2] + self.cache[-1])
        ## Simulating hard computation,
        ## when caching was not helpful
        time.sleep(2)
        return self.cache[-1]

fibs = Fibonacci(5)

if __name__ == '__main__':
    for n in fibs: print(n)
