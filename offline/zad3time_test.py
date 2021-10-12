from random import randint, shuffle, seed
from time import time


def partition(T, p, r):
    T[p], T[r] = T[r], T[p]
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i+1] = T[i+1], T[r]
    return i+1


def median_of_five(T, p, r, step):
    for i in range(r, p, -step):
        j=p
        while j+step <= i and j+step<=r:
            if T[j] > T[j+step]:
                T[j], T[j+step] = T[j+step], T[j]
            j += step
    tmp = p+step*(((r-p)//step)//2)
    T[p], T[tmp] = T[tmp], T[p]


def select(T, p, r):
    step = 1
    while r-p >= step:
        for i in range(p, r, 5*step):
            median_of_five(T, i, min(i+5*step-1, r), step)
        step *= 5
        r = r-r % (step)


def linearselect(T, k):
    p = 0
    r = len(T)-1
    while True:
        select(T, p, r)
        q = partition(T, p, r)
        if q == k:
            return T[q]
        elif k < q:
            r = q-1
        else:
            p = q+1


seed(42)
n = 4000000
A = list(range(n))
shuffle(A)
i=randint(0, n-1)
start = time()
x = linearselect(A, i)
if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)

print("OK")
end = time()
print("Runtime:", end-start, "s")