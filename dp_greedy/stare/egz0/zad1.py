from zad1testy import runtests


def counting_sort(A, k):
    length = len(A)
    B = [None]*length
    C = [0]*k
    for i in range(length):
        C[A[i][0]] = C[A[i][0]]+1
    for i in range(1, k):
        C[i] = C[i-1] + C[i]
    for i in range(length-1, -1, -1):
        B[C[A[i][0]]-1] = A[i]
        C[A[i][0]] -= 1
    return B


def tanagram(x, y, t):
    if len(x) != len(y):
        return False
    n = len(x)
    A = []
    B = []
    for i in range(n):
        A.append((ord(x[i])-ord('a'), i))
        B.append((ord(y[i])-ord('a'), i))
    k = ord('z')-ord('a')+1
    A = counting_sort(A, k)
    B = counting_sort(B, k)
    for i in range(n):
        if abs(A[i][1]-B[i][1]) > t:
            return False
    return True


runtests(tanagram)