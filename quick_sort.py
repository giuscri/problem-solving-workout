import random

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
