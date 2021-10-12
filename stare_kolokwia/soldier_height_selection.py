from random import randint

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[r], T[i+1] = T[i+1], T[r]
    return i+1

def linearselect(T, p, r, k):
    p = 0
    r = len(T)-1
    while True:
        # select(T, p, r)
        q = partition(T, p, r)
        if q == k:
            return T[q]
        elif k < q:
            r = q-1
        else:
            p = q+1

def selection(T: list, p: int, q:int):
    linearselect(T, 0, len(T)-1, p)
    linearselect(T, p, len(T)-1, q)
    print(T)
    return T[p:q+1]



if __name__ == "__main__":
    n = 20
    T = [randint(150, 200) for _ in range(n)]
    p, q = 4, 8
    print(T)
    print(sorted(T))
    print(selection(T, p, q))