from random import randint, shuffle, seed


def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i+1] = T[i+1], T[r]
    return i+1


def median_of_five(T, p, r, step):
    itr = p+step
    while itr <= r:
        rev = itr-step
        while rev >= p and T[rev] > T[rev+step]:
            T[rev], T[rev+step] = T[rev+step], T[rev]
            rev -= step
        itr += step
    median_index = p+(((itr-p)//step-1)//2)*step
    T[p], T[median_index] = T[median_index], T[p]


def select(T, p, r):
    step = 1
    while r-p >= step:
        for i in range(p, r, step*5):
            median_of_five(T, i, min(r, i+step*5-1), step)
        step *= 5
    T[p], T[r] = T[r], T[p]


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

n = 10
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
