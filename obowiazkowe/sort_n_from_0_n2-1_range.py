from random import randint

def counting_sort(A, key, n):
    C = [0]*n
    B = [0]*(n*n)
    for i in range(n):
        C[key(A[i])] += 1
    for i in range(1, n):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        C[key(A[i])] -= 1
        B[C[key(A[i])]] = A[i]
    return B

def sort_linear(T, n):
    tmp = counting_sort(T, lambda a: a%n, n)
    tmp = counting_sort(tmp, lambda a: a//n, n)
    for i in range(n):
        T[i]=tmp[i]

if __name__ == "__main__":
    n = 20
    T = [randint(0, n**2-1) for _ in range(n)]
    print(T)
    sort_linear(T, n)
    print(T)
    print(sorted(T)) 