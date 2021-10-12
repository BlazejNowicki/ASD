from random import randint

def partition(T, p, r, key):
    x = key(T[r])
    i = p-1
    for j in range(p, r):
        if key(T[j]) <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def quicksort(T, p, r, key):
    while p < r:
        q = partition(T, p, r, key)
        if q-p < r-q:
            quicksort(T, p, q-1, key)
            p = q+1
        else:
            quicksort(T, q+1, r, key)
            r = q-1

def sum_sort(A, B, n):
    C = [0]*n
    for i in range(n):
        temp_sum = 0
        for j in range(n*i, n*(i+1)):
            temp_sum += A[j]
        C[i] = (temp_sum, i)
    quicksort(C, 0, n-1, lambda a: a[0])
    # C.sort(key=lambda a: a[0]) # zastąpić quicksortem
    for i in range(n**2):
        B[i] = A[i%n+n*C[i//n][1]]



if __name__ == "__main__":
    n = 5
    A = [randint(1, 9) for _ in range(n**2)]
    B = [0]*(n**2)
    print(A)
    print(B)
    sum_sort(A, B, n)
    print(B)

# n = 100
# T = [randint(1, 100) for _ in range(n)]
# print(sorted(T))
# quicksort(T, 0, n-1, key=lambda a:a)
# print(T)
    
