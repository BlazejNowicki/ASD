from queue import PriorityQueue
INF = 10**4


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
    weight[s] = 0
    while not qq.empty() and not visited[f]:
        _, t = qq.get()
        visited[t] = True
        for u, w in G[t]:
            if not visited[u] and weight[t]+w < weight[u]:
                weight[u] = weight[t] + w
                parent[u] = t
                qq.put((weight[u], u))
    if weight[f] < INF:
        return weight[f]
    else:
        return None


if __name__ == "__main__":
    G = [(1, 0, 1), (5, 1, 2), (3000, 2, 3), (9, 3, 4),
         (8, 4, 5), (12, 0, 5), (7, 1, 5), (6, 2, 5), (4, 2, 4)]
    # G = [] 
    N = 6
    G = edge_list_to_adjacency_list(G, N)
    for i in range(N):
        print(dijkstra(G,0,i))
