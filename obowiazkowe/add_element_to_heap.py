from random import randint


def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2


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

def add_element(A, n):
    A.append(n)
    i = len(A)-1
    while i>0 and A[i] > A[parent(i)]:
        t = parent(i)
        A[i], A[t] = A[t], A[i]
        i = t

def build_heap(A):
    length = len(A)
    for i in range(parent(len(A)-1), -1, -1):
        heapify(A, i, length)


def heapsort(A):
    build_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, 0, i)


def print_heap(T):
    t = 2
    for i in range(1, len(T)+1):
        print(T[i-1], end="\t")
        if i == t-1:
            t *= 2
            print('')
    print()


if __name__ == "__main__":
    n = 10
    T = [randint(1, 100) for _ in range(n)]
    print(T)
    build_heap(T)
    print_heap(T)
    add_element(T, 90)
    print_heap(T)
    print(T)


# T = [
#             20,
#        18,      16,
#      15, 16,  13,  10,
#     9,6, 5,3, 2,6, 5,4
#     ]
