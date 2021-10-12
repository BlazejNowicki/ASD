from zad2testy import runtests

inf = float('inf')


def cost(sums, i, k, j):
    if i == 0:
        return abs(sums[j])
    else:
        return abs(sums[j] - sums[i-1])


def sums_init(tab):
    n = len(tab)
    sums = [0]*n
    sums[0] = tab[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + tab[i]
    return sums


def opt_sum(tab):
    n = len(tab)
    F = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = 0
    sums = sums_init(tab)

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            for k in range(i, j):
                F[i][j] = min(F[i][j], max(F[i][k], F[k+1][j], cost(sums, i, k, j)))

    return F[i][j]


runtests(opt_sum)
