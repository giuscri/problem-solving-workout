import random
import functools

def dutch_flag_partition(A, pivot_index):
    '''
    # Faster approach
    ret = [x for x in A if x < A[i]] + \
           [x for x in A if x == A[i]] + \
           [x for x in A if x > A[i]]
    '''
    pivot = A[pivot_index]
    print('pivot is {}'.format(pivot))

    print(A)

    smaller_ix = 0

    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller_ix] = A[smaller_ix], A[i]
            smaller_ix += 1

    larger_ix = len(A) - 1

    for i in range(len(A) -1, -1, -1):
        if A[i] > pivot:
            A[i], A[larger_ix] = A[larger_ix], A[i]
            larger_ix -= 1

    print(A)

if __name__ == '__main__':
    l = [random.randint(0,100) for x in range(10)]
    print(dutch_flag_partition(l, 4))
