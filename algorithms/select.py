# W czasie liniowym znajduje jaki element znajdowałby się na x-tej pozycji w posortowanej tablicy
from random import randint

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def select(T, x):
    l = 0
    r = len(T)-1
    while True:
        p = partition(T, l, r)
        if p == x:
            return T[p]
        elif p < x:
            l = p+1
        else:
            r = p-1


n = 10
T = [randint(1,100) for _ in range(n)]
print(sorted(T))
for i in range(n):
    print(select(T, i), end=' ')
print()