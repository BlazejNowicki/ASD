from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(L):
    s = s_end = Node()
    q = q_end = Node()
    ptr = L.next
    while ptr:
        if ptr.value < L.value:
            s_end.next = ptr
            s_end = ptr
        else:
            q_end.next = ptr
            q_end = ptr
        ptr = ptr.next
    s_end.next = None
    q_end.next = None
    L.next = None
    return s.next, q.next


def get_last(L):
    if L:
        while L.next:
            L = L.next
    return L


def qsort(L):
    if L is None or L.next is None:
        return L
    p, q = partition(L)
    p = qsort(p)
    q = qsort(q)
    t = get_last(p)
    if t:
        t.next = L
    else:
        p = L
    L.next = q
    return p


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next
print("OK")
