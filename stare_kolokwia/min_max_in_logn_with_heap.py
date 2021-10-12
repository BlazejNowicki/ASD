from random import randint


parent = lambda i: (i-1)//2
left = lambda i: 2*i+1
right = lambda i: 2*i+2
max_key = lambda a, b: a[0] > b[0]
min_key = lambda a, b: a[0] < b[0]

def swap(A, B, a, b):
    value_a, pointer_a = B[A[a][1]]
    value_b, pointer_b = B[A[b][1]]
    B[A[a][1]] = (value_a, pointer_b)
    B[A[b][1]] = (value_b, pointer_a)
    A[a], A[b] = A[b], A[a]


def heapify(A, B, i, compare):
    l = left(i)
    r = right(i)
    if l < len(A) and compare(A[l], A[i]):
        selected = l
    else:
        selected = i
    if r < len(A) and compare(A[r], A[selected]):
        selected = r
    if selected != i:
        swap(A, B, selected, i)
        heapify(A, B, selected, compare)

def init(A, B, compare):
    for i in range(parent(len(A)-1), -1, -1):
        heapify(A, B, i, compare)

def move_to_place(A, B, compare):
    i = len(A)-1
    p = parent(i)
    while p>=0 and compare(A[i], A[p]):
        swap(A, B, p, i)
        i = p
        p = parent(i)

def insert(A, B, x):
    A.append( (x, len(A)) )
    B.append( (x, len(B)) )
    move_to_place(A, B, max_key)
    move_to_place(B, A, min_key)

# def remove(A, B):
#     swap(A[0][1], len(A)-1)

if __name__ == "__main__":
    n = 7
    MIN = [(randint(1, 100), i) for i in range(n)]
    MAX = MIN[:]
    # print(MIN)
    init(MAX, MIN, max_key)
    init(MIN, MAX, min_key)
    print(MAX)
    print(MIN)
    insert(MAX, MIN, 69)
    insert(MAX, MIN, 420)
    insert(MAX, MIN, -1)
    print(MAX)
    print(MIN)
    