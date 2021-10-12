from queue import PriorityQueue
INF = 10**4


def edge_list_to_adjacency_list(G, n):
    GG = [list() for _ in range(n)]
    for w, u, v in G:
        GG[u].append((v, w))
        GG[v].append((u, w))
    return GG


def prim(G):
    n = len(G)
    qq = PriorityQueue()
    parent = [None]*n
    weight = [INF]*n
    visited = [False]*n
    qq.put((0, 0))
    weight[0] = 0
    while not qq.empty():
        _, t = qq.get()
        visited[t] = True
        for u, w in G[t]:
            if not visited[u] and w < weight[u]:
                weight[u] = w
                parent[u] = t
                qq.put((w, u))

    return parent


if __name__ == "__main__":
    G = [(1, 0, 1), (5, 1, 2), (3000, 2, 3), (9, 3, 4),
         (8, 4, 5), (12, 0, 5), (7, 1, 5), (6, 2, 5), (4, 2, 4)]
    N = 6
    G = edge_list_to_adjacency_list(G, N)
    print("MST - parents:", prim(G))
