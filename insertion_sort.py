import random
import time

def timed(f):
    def _f(*args, **kwargs):
        before = time.time()
        f(*args, **kwargs)
        after = time.time()
        print('Elapsed {} seconds when computing {}' \
                 .format(after-before, f.__name__, *args))
    return _f

@timed
def insertion_sort(A):
    B = []
    for x in A:
        j = 0
        while j < len(B):
            if B[j] >= x:
                break
            else:
                j += 1
        B = B[:j] + [x] + B[j:]
    return B

@timed
def _insertion_sort(A):
    for i in range(1, len(A)):
        to_insert = A[i]
        j = i - 1
        while j >= 0 and A[j] >= to_insert:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = to_insert
    return A
