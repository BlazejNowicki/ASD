# Bitonic travelling salesman problem
from math import sqrt
INF = 10.0**3


def dist(T, a, b):
    return sqrt((T[b][0]-T[a][0])**2 + (T[b][1]-T[a][1])**2)


def tspf(i, j, F, T):
    if F[i][j] < INF:
        return F[i][j]

    if i == j-1:
        best = INF
        for k in range(j-1):
            best = min(best, tspf(k, j-1, F, T)+dist(T, k, j))
        F[j-1][j] = best
    else:
        F[i][j] = tspf(i, j-1, F, T) + dist(T, j-1, j)
    return F[i][j]


if __name__ == "__main__":
    T = [(1, 3), (2, 1), (6, 1), (8, 2), (9, 4), (7, 6), (5, 4), (3, 5)]
    n = len(T)
    T.sort()
    print(T)
    F = [[INF] * n for _ in range(n)]
    F[0][1] = dist(T, 0, 1)
    ans = INF
    for i in range(n-1):
        ans = min(ans, tspf(i, n-1, F, T)+dist(T, i, n-1))
    print(ans)
