from zad1testy import runtests
from collections import deque
from queue import PriorityQueue

INF = float('inf')


def dijkstra(G, s, f):
    n = len(G)
    qq = PriorityQueue()
    weight = [INF]*n
    visited = [False]*n
    qq.put((0, s))
    qq.put((0, n//3+s))
    qq.put((0, 2*n//3+s))
    weight[s] = weight[n//3+s] = weight[2*n//3+s] = 0
    while not qq.empty():
        _, t = qq.get()
        visited[t] = True
        for u, w in G[t]:
            if not visited[u] and weight[t]+w < weight[u]:
                weight[u] = weight[t] + w
                qq.put((weight[u], u))
    ans =  min(weight[f], weight[n//3+f], weight[2*n//3+f])
    if ans < INF:
        return ans
    else:
        return None


def islands(G, A, B):
    n = len(G)
    # 8 - 0, 5 - 1, 1 - 2
    GG = [[] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            if i != j and G[i][j] == 8:
                GG[n+i].append((j, 8))
                GG[2*n+i].append((j, 8))
            if i != j and G[i][j] == 5:
                GG[i].append((n+j, 5))
                GG[2*n+i].append((n+j, 5))
            if i != j and G[i][j] == 1:
                GG[i].append((2*n+j, 1))
                GG[n+i].append((2*n+j, 1))

    return dijkstra(GG, A, B)


runtests(islands)
