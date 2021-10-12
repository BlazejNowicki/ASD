def partition(T, index, p, r):
    x = T[index[r]]
    i = p-1
    for j in range(p, r):
        if T[index[j]] <= x:
            i += 1
            index[i], index[j] = index[j], index[i]
    index[i+1], index[r] = index[r], index[i+1]
    return i+1


def quicksort(T, index, p, r):
    while p < r:
        q = partition(T, index, p, r)
        if q-p < r-q:
            quicksort(T, index, p, q-1)
            p = q+1
        else:
            quicksort(T, index, q+1, r)
            r = q-1

def dominance(P):
    if not P:
        return []
    index = list(range(len(P)))
    quicksort(P, index, 0, len(P)-1)
    S = [index[0]]
    min_value = P[index[0]][1]
    for i in index:
        if P[i][1] < min_value:
            S.append( i )
            min_value = P[i][1]
    return S


if __name__ == "__main__":
    T = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]
    print(T)
    print(dominance(T))