def lis(A):
    n = len(A)
    F=[1]*n
    P=[-1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[j]+1 > F[i]:
                F[i] = F[j]+1
                P[i] = j
    return(max(F), F, P)

def printsolution_rec(A, P, i):
    if P[i] != -1:
        printsolution_rec(A, P, P[i])
    print(A[i], end=' ')

def printsolution(A, P, F):
    m = 0
    for i in range(1, len(F)):
        if F[i] > F[m]:
            m = i
    printsolution_rec(A, P, m)
    print()


if __name__ == "__main__":
    # A = [3, 5, 4, 7, 11, 15, 24, 12, 1, 8, 10, 2, 6, 13]
    A = [3, 5, 4, 7, 11, 1, 8, 10, 12, 6]
    tmp, F, P = lis(A)
    print(tmp)
    printsolution(A, P, F)