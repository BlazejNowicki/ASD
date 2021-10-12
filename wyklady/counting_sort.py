from random import randint

def counting_sort(A, B, k):
    length = len(A)
    C = [0]*k
    for i in range(length):
        C[A[i]] = C[A[i]]+1
    for i in range(1, k):
        C[i] = C[i-1] + C[i]
    for i in range(length-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

n = 10
T = [randint(1, k-1) for _ in range(n)]
W = [0]*n
print(T)
counting_sort(T, W, k)
print(W)
print(sorted(T))
k = 10