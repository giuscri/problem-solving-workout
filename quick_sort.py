import random

def traced(f):
    def _f(*args, **kwargs):
        ## Ignoring kwargs while tracing, sorry...
        print('[!] Called \"{}\" with {}'\
                 .format(f.__name__, args))
        ret = f(*args, **kwargs)
        print('[!] Returned {}'.format(ret))
        return ret 
    return _f

def quick_sort(A):
    '''
    Very naif implementation
    of quick-sort
    '''
    A = A[:]
    if len(A)<=1: return A
    pivot = A[0]
    return quick_sort([x for x in A if x < pivot]) + \
              [x for x in A if x==pivot] + \
                 quick_sort([x for x in A if x > pivot])

#@traced
def partition(A, p, q):
    pivot = A[p]
    smaller = p
    for i in range(p,q):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = q - 1
    for i in range(q - 1, smaller - 1, -1):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A, larger

#@traced
def _quick_sort(A, p, q):
    _, pivot_index = partition(A, p, q)
    if p < pivot_index:
        _quick_sort(A, p, pivot_index)
    if pivot_index + 1 < q:
        _quick_sort(A, pivot_index + 1, q)
    return A
