from random import randint


def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

# kopiec binarny typu max
def heapify(A, i, length):
    l = left(i)
    r = right(i)
    if l < length and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < length and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, largest, length)


def build_heap(A):
    length = len(A)
    for i in range(parent(len(A)-1), -1, -1):
        heapify(A, i, length)


def heapsort(A):
    build_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, 0, i)

def increase_key(A, i, key):
    if key < A[i]:
        raise Exception("new key is smaller than current key")
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        t = parent(i)
        A[t], A[i] = A[i], A[t]
        i = t

# uwaga: zakłada ze cała tablica A jest kopcem
def insert(A, key):
    A.append(key)
    increase_key(A, len(A)-1, key)


def print_heap(T):
    t = 2
    for i in range(1, len(T)+1):
        print(T[i-1], end="\t")
        if i == t-1:
            t *= 2
            print('')
    print()


if __name__ == "__main__":
    n = 25
    T = [randint(1, 100) for _ in range(n)]
    build_heap(T)
    # heapsort(T)
    print_heap(T)
    K = [randint(1,100) for _ in range(5)]
    print(K)
    for i in K:
        insert(T, i)
    print_heap(T)


