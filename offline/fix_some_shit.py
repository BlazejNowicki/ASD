from random import randint, shuffle, seed


def partition(T, p, r, x):
    i = p-1
    j = p
    while j < r:
        if T[j] == x:
            T[j], T[r] = T[r], T[j]
        else:
            if T[j] < x:
                i += 1
                T[i], T[j] = T[j], T[i]
            j += 1
    T[r], T[i+1] = T[i+1], T[r]
    return i+1


n = 25
T = list(range(n))
shuffle(T)
partition(T, 0, n-1, 17)
print(T)
