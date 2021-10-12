from random import randint, seed


def mergesort(T):
    l = len(T)
    if l == 1:
        return T
    A = mergesort(T[:l//2])
    B = mergesort(T[l//2:])
    T = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            T.append(A[i])
            i += 1
        else:
            T.append(B[j])
            j += 1
    T = T + A[i:] + B[j:]
    return T


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
    if T[i] > T[i+1]:
        print("Błąd sortowania!")
        exit()

print("OK")
