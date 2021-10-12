# Szybsze kiedy wagi krawędzi mają małe ogranicznie
from collections import deque


def BFS_dist(G, s):
    n = len(G)
    dist = [-1]*n
    q = deque()
    q.append((0, s, 0))
    while q:
        w, u, d = q.popleft()
        if dist[u] == -1:
            if w == 0:
                dist[u] = d
                for v, w in G[u]:
                    q.append((w-1, v, d+1))
            else:
                q.append((w-1, u, d+1))
    print(dist)


def edge_list_to_adjacency_list(G, n):
    GG = [list() for _ in range(n)]
    for w, u, v in G:
        GG[u].append((v,w))
        GG[v].append((u,w))
    return GG
    
L = [(2,0,5),(4,5,7),(5,7,6),(2,6,4),(1,4,5),(1,4,3),(1,3,2),(2,2,1),(2,1,3)]
N = 8
G = edge_list_to_adjacency_list(L, N)
BFS_dist(G, 0)
