from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def partition(L):
    s = s_end = Node() #smaller
    e = e_end = Node() #equal
    q = q_end = Node() #greater
    ptr = L
    while ptr:
        if ptr.value < L.value:
            s_end.next = ptr
            s_end = ptr
        elif ptr.value == L.value:
            e_end.next = ptr
            e_end = ptr
        else:
            q_end.next = ptr
            q_end = ptr
        ptr = ptr.next
    s_end.next, e_end.next, q_end.next = None, None, None
    return s.next, e.next, e_end, q.next


def attach(L, L_end, P, P_end):
    if L is None:
        return P, P_end
    if P is None:
        return L, L_end
    L_end.next = P
    return L, P_end


def qsort_rec(L):
    if L is None or L.next is None:
        return L, L
    p, e, e_end, q = partition(L)
    p, p_end= qsort_rec(p)
    q, q_end = qsort_rec(q)
    e, e_end = attach(e, e_end, q, q_end)
    p, p_end = attach(p, p_end, e, e_end)
    return p, p_end

def qsort(L):
    L, _ = qsort_rec(L)
    return L

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
