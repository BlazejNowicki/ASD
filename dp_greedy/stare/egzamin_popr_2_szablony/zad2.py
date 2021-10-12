from zad2testy import runtests


def inside(T, old, new):
    return T[old][0] <= T[new][0] and T[new][1] <= T[old][1]


def tower(A):
    n = len(A)
    F = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if inside(A, j, i):
                F[i] = max(F[i], F[j]+1)
    return max(F)


runtests(tower)
