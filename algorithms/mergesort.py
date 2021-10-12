from random import randint

def mergesort(T):
    if len(T) < 2: return
    mid = len(T)//2
    L = T[:mid]
    R = T[mid:]
    mergesort(L)
    mergesort(R)
    i = j = k = 0
    while k < len(T):
        if j >= len(R) or ( i < len(L) and L[i][0] <= R[j][0]):
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1

n = 10
T = [(randint(1,5), randint(1, 100)) for _ in range(n)]
print(T)
print(sorted(T))
mergesort(T)
print(T)
