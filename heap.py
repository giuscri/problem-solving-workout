## I wrote this pool of f's instinctively,
## though the result is not very efficient ...

import math

def list_to_heap(A):
    assert len(A)>0, 'Cannot make heap out of an empty list'
    root = max(A)
    A = A[:]
    A.remove(root)

    B = list(map(lambda p: p[1], \
       filter(lambda p: True if p[0]%2==0 else False, enumerate(A))))
    C = list(map(lambda p: p[1], \
       filter(lambda p: True if p[0]%2==1 else False, enumerate(A))))

    ## Base case
    if len(A)<=2: return [root] + B + C

    return [root] + combine_heaps(list_to_heap(B), list_to_heap(C))

def heap_sort(A):
    B = []
    A = list_to_heap(A)
    while len(A) >= 2:
        B.append(A[0])
        A = list_to_heap(A[1:])
    B.append(A[0])
    return list(reversed(B))

def combine_heaps(A, B):
    if len(A)==1 and len(B)==1:
        return A + B
    C = []
    i, j = 0, 0
    for inc in [2**i for i in range(math.ceil(math.log2(len(A))) +1)]:
        i, j = j, j+inc
        C += A[i:j] + B[i:j]
    return C

def is_heap(A):
    mid_index = len(A)//2 if len(A)%2==1 else len(A)//2 - 1
    for i in range(mid_index):
        if A[i] < A[2*i + 1] or A[i] < A[2*i + 2]:
            return False
    if len(A)%2==0 and A[mid_index] < A[-1]:
        return False
    return True

if __name__ == '__main__':
    lst = [2,1,3,4,2,1,2,9021,-131]
    print(sorted(lst))
    print(heap_sort(lst))
    assert heap_sort(lst) == sorted(lst)
