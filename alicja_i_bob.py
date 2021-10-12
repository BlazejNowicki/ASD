from queue import PriorityQueue
INF = 10**10


def edge_list_to_adjacency_list(G, n):
    GG = [list() for _ in range(n)]
    for w, u, v in G:
        GG[u].append((v, w))
        GG[v].append((u, w))
    return GG


def dijkstra(G, s, f):
    n = len(G)
    qq = PriorityQueue()
    parent = [None]*n
    weight = [INF]*n
    visited = [False]*n
    qq.put((0, s))
    qq.put((0, n//2+s))
    weight[s] = 0
    weight[n//2+s] = 0
    while not qq.empty(): 
        _, t = qq.get()
        visited[t] = True
        for u, w in G[t]:
            if not visited[u] and weight[t]+w < weight[u]:
                weight[u] = weight[t] + w
                parent[u] = t
                qq.put((weight[u], u))
    if weight[f] < INF or weight[n//2+f] < INF:
        return min(weight[f], weight[n//2 + f])
    else:
        return None


def alice_and_bod(G, s, t):
    n = len(G)
    GG = []*(2*n)
    for u, l in enumerate(G):
        for v in l:
            GG[u].append(n+v)
            GG[n+u].append(v)
    return dijkstra(G, s, t)

G1 = [[-1, 6, 8, -1, -1, -1],
    [-1, -1, -1, -1, 3, -1],
    [-1, -1, -1, 2, 1, -1],
    [-1, -1, -1, -1, -1, 7],
    [-1, -1, -1, -1, -1, 2],
    [-1, -1, -1, -1, -1, -1]]


G2 = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
    [4, -1, 8, -1, -1, -1, -1, 11, -1],
    [-1, 8, -1, 7, -1, 4, -1, -1, 2],
    [-1, -1, 7, -1, 9, 14, -1, -1, -1],
    [-1, -1, -1, 9, -1, 10, -1, -1, -1],
    [-1, -1, 4, 14, 10, -1, 2, -1, -1],
    [-1, -1, -1, -1, -1, 2, -1, 1, 6],
    [8, 11, -1, -1, -1, -1, 1, -1, 7],
    [-1, -1, 2, -1, -1, -1, 6, 7, -1],]

print(who(G2, 0, 4))

G3 = [[-1, 5, -1, -1, -1, 10], 
    [5, -1, 5, -1, -1, 20], 
    [-1, 5, -1, 2, 7, 8], 
    [-1, -1, 2, -1, 6, -1], 
    [-1, -1, 7, 6, -1, 110], 
    [10, 20, 8, -1, 110, -1]]

print(who(G3, 0, 3))

G4 = [[-1, 100, 2, -1, -1], 
    [100, -1, 1, -1, -1], 
    [2, 1, -1, 100, 10], 
    [-1, -1, 100, -1, 100], 
    [-1, -1, 10, 100, -1]]

print(who(G4, 0, 4))
        

G5 = [[-1, 5, -1, -1, -1, 10],
     [5, -1, 3, 7, -1, -1],
     [-1, 3, -1, 4, 3, 5],
     [-1, 7, 4, -1, 8, 2],
     [-1, -1, 3, 8, -1, -1],
     [10, -1, 5, 2, -1, -1]]

print(who(G5, 0, 4))
