# Błażej Nowicki
# Do implementacji algorytmu z wykładu wprowadzamy modyfikacje: W tablicy P (która służyła do odtworzenia ciągu wynikowego)
# zamiast pamiętać tylko jeden indeks poprzedniego elementu w ciągu, pamiętamy wszystkie poprawne. 
# Zapisujemy je w liście odpowiadającej danemu indeksowi 


def printAllLIS(A):
    n = len(A)
    F=[1]*n
    P=[ [] for _ in range(n) ]
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i]:
                if F[j]+1 > F[i]:
                    F[i] = F[j]+1
                    P[i] = [j]
                elif F[j]+1 == F[i]:
                    P[i].append(j)
    return printsolution(A, P, F, max(F))

def printsolution_rec(A, P, i, result, couter):
    if couter == 1:
        result[0] = A[i]
        for j in range(len(result)):
            print(result[j], end=" ")
        print()
        return 1
    else:
        sum = 0
        for prev_index in P[i]:
            result[couter-1] = A[i]
            sum += printsolution_rec(A, P, prev_index, result, couter-1)
    return sum

def printsolution(A, P, F, max_len):
    result = [0]*max_len
    sum = 0
    for i in range(len(F)):
        if F[i] == max_len:
            sum += printsolution_rec(A, P, i, result, max_len)
    return sum


if __name__ == "__main__":
    A = [3, 5, 4, 7, 11, 15, 24, 12, 1, 8, 10, 2, 6, 13]
    # A = [3, 5, 4, 7, 13, 1, 8, 10, 12, 11]
    # A = [2, 1, 4, 3, 6, 5, 8, 7]
    # A = [2, 1, 4, 3]
    print("Number of LIS`s:", printAllLIS(A))
    