# Błażej Nowicki
# Do implementacji algorytmu z wykładu wprowadzamy modyfikacje: W tablicy P (która służyła do odtworzenia ciągu wynikowego)
# zamiast pamiętać tylko jeden indeks poprzedniego elementu w ciągu, pamiętamy wszystkie poprawne.
# Zapisujemy je w liście odpowiadającej danemu indeksowi. Ciągi wypisujemy rekurecnyjnie z użyciem tablicy
# pomocniczej result (na wartości z ciągów) i zmiennej counter (do modyfikowania pól result)


def printAllLIS(A):
    n = len(A)
    F = [1]*n  # długość najdłuższego poprawnego ciągu kończącego się na A[i]
    # odnośniki do elemenów poprzedzających A[i] w ciągach wynikowych
    P = [[] for _ in range(n)]
    begs = [0]  # lista z indeksami elemenów od których należy zacząć wypisywanie
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                if F[j]+1 > F[i]:
                    F[i] = F[j]+1
                    P[i] = [j]
                elif F[j]+1 == F[i]:
                    P[i].append(j)
        if F[i] > F[begs[0]]:
            begs = [i]
        elif F[i] == F[begs[0]]:
            begs.append(i)

    # wypisz i policz wszystkie ciągi
    sum = 0
    max_len = F[begs[0]]
    for begin_index in begs:
        sum += printsolution(A, P, begin_index, [0]*max_len, max_len)
    return sum


def printsolution(A, P, i, result, couter):
    if couter == 1:
        result[0] = A[i]
        for j in range(len(result)):
            print(result[j], end=" ")
        print()
        return 1

    sum = 0
    for prev_index in P[i]:
        result[couter-1] = A[i]
        sum += printsolution(A, P, prev_index, result, couter-1)
    return sum


if __name__ == "__main__":
    # A = [3, 5, 4, 7, 11, 15, 24, 12, 1, 8, 10, 2, 6, 13]
    # A = [3, 5, 4, 7, 13, 1, 8, 10, 12, 11]
    # A = [2, 1, 4, 3, 6, 5, 8, 7]
    # A = [2, 1, 4, 3]
    n = 2
    A = [10*k+i for k in range(n) for i in range(n, 0, -1)]
    print(A)
    print("Number of LISs:", printAllLIS(A))
