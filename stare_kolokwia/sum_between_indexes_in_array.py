from random import randint

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def select(T, p, r, i):
    while True:
        q = partition(T, p, r)
        if q == i:
            return T[i]
        elif q > i:
            r = q-1
        else:
            p = q+1


def find_sum(T, beg, end, n):
    select(T, 0, n-1, beg)
    select(T, beg, n-1, end)
    sum_of_range=0
    for i in range(beg, end+1):
        sum_of_range += T[i]
    return sum_of_range

if __name__ == "__main__":
    n = 10
    T = [randint(1, 20) for _ in range(n)]
    print(T)
    print(find_sum(T, 3, 3, n))
    # print(sorted(T))
    # print(partition(T, 0, n-1))