from random import random
from math import floor


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# Działa tylko przy rozkładzie normalnym
def bucket_sort(T):
    n = len(T)
    B = [[] for _ in range(n)]
    for v in T:
        B[floor(v*n)].append(v)
    for i in range(n):
        insertion_sort(B[i])
    i = 0
    for k in range(n):
        for v in B[k]:
            T[i] = v
            i += 1

n = 10
T = [random() for _ in range(n)]
print(T)
print(sorted(T))
# insertion_sort(T)
bucket_sort(T)
print(T)