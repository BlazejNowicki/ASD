# O(n*k)
from random import randint

def counting_sort(A, k, key=lambda x:x):
    length = len(A)
    C = [0]*k
    B = [None]*length
    for i in range(length):
        C[key(A[i])] = C[key(A[i])]+1
    for i in range(1, k):
        C[i] = C[i-1] + C[i]
    for i in range(length-1, -1, -1):
        B[C[key(A[i])]-1] = A[i]
        C[key(A[i])] -= 1
    return B

n = 10
k = 10
T = [randint(1, k-1) for _ in range(n)]
print(T)
W = counting_sort(T, k)
print(W)
print(sorted(T))