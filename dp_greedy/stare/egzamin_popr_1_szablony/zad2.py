from zad2testy import runtests
from math import sqrt, ceil

inf = float('inf')


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(G, n):
    vert = [Node(i) for i in range(n)]
    A = []
    for w, u, v in G:
        if find_set(vert[u]) != find_set(vert[v]):
            A.append((w, u, v))
            union(vert[u], vert[v])

    flag = True
    for i in range(1, n):
        if find_set(vert[0]) != find_set(vert[i]):
            flag = False

    day_diff = A[-1][0] - A[0][0]
    return flag, day_diff


def highway(A):
    G = []
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            w = ceil(sqrt((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2))
            G.append((w, i, j))
    G.sort()
    ans = inf
    for s in range(len(G)):
        f, g = kruskal(G[s:], n)
        if f:
            ans = min(ans, g)
    return ans


runtests(highway)
