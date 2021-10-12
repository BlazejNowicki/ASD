def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

# def quicksort(T, p, r):
#     if p<r:
#         q = partition(T, p, r)
#         quicksort(T, p, q-1)
#         quicksort(T, q+1, r)


def quicksort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q-p < r-q:
            quicksort(T, p, q-1)
            p = q+1
        else:
            quicksort(T, q+1, r)
            r = q-1


if __name__ == "__main__":
    T = [6, 5, 3, 2, 36, 93, 7, 8, 2, 5]
    print(sorted(T))
    quicksort(T, 0, len(T)-1)
    print(T)
