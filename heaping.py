# A more traditional/textbooky approach
# to heaps and heapsorting

def list_to_heap(A):
    # Copying list A, avoiding side effects
    A = A[:]
    first_leaf_index = len(A)//2
    for i in range(first_leaf_index - 1, -1, -1):
        A = update_heap(A, i, len(A) - 1)
    return A

def update_heap(A, i, j):
    # Copying list A, avoiding side effects
    A = A[:]
    if 2*i + 1 == j:
        if A[i] < A[j]: A[i], A[j] = A[j], A[i]
    elif 2*i + 1 < j:
        k = 2*i + 1 if A[2*i + 1] > A[2*i + 2] else 2*i + 2
        if A[i] < A[k]:
            A[i], A[k] = A[k], A[i]
            A = update_heap(A, k, j)
    return A

def heap_sort(A):
    # Copying list A, avoiding side effects
    A = A[:]
    A = list_to_heap(A)
    for j in range(len(A) - 1, -1, -1):
        A = update_heap(A, 0, j)
        A[0], A[j] = A[j], A[0]
    return A

def is_heap(A):
    first_leaf_index = len(A)//2
    last_to_check_index = \
       first_leaf_index - 2 if len(A)%2==0 else first_leaf_index - 1

    for i in range(last_to_check_index + 1):
        if A[i] < A[2*i + 1] or \
              A[i] < A[2*i + 2]:
            return False

    if len(A)%2==0 and A[len(A)//2 - 1] < A[-1]:
        return False

    return True
