from queue import PriorityQueue
from zad3testy import runtests
INF = float('inf')


def min_dist(dist, visited):
    min = INF
    min_index = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min:
            min = dist[i]
            min_index = i
    return min_index


def dijkstra(G, s, f):
    n = len(G)//2
    dist = [INF]*(2*n)
    dist[s] = 0
    visited = [False]*(2*n)

    while not visited[f] and not visited[n+f]:
        u = min_dist(dist, visited)
        if u != -1:
            visited[u] = True
            for v in range(2*n):
                if G[u][v] > 0 and not visited[v] and dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
    return min(dist[f], dist[n+f])


def jumper(G, s, w):
    n = len(G)
    GG = [[0 for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            GG[i][j] = G[i][j]
            GG[n+i][j] = G[i][j]

    for i in range(n):
        for k in range(n):
            for j in range(n):
                if i != k and k != j and i != j:
                    if G[i][k] > 0 and G[k][j] > 0:
                        if GG[i][n+j] == 0:
                            GG[i][n+j] = max(G[i][k], G[k][j])
                        else:
                            GG[i][n+j] = min(max(G[i][k], G[k][j]),GG[i][n+j])
    return dijkstra(GG, s, w)


runtests(jumper)
