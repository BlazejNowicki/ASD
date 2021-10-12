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
    # parent = [None]*n
    dist = [INF]*n
    visited = [-1]*n
    qq.put((0, INF, s))
    dist[s] = 0
    while not qq.empty():
        d,l,t = qq.get()
        if visited[t] < l:
            visited[t] = l
            for u, w in G[t]:
                if not visited[u] and dist[t]+w < dist[u]:
                    dist[u] = dist[t] + w
                    parent[u] = t
                    qq.put((dist[u], u))
    if dist[f] < INF:
        return dist[f]
    else:
        return None


if __name__ == "__main__":
    # G = [(1, 0, 1), (5, 1, 2), (3000, 2, 3), (9, 3, 4),
    #      (8, 4, 5), (12, 0, 5), (7, 1, 5), (6, 2, 5), (4, 2, 4)]
    G = [(10,0,2),(15,0,1),(20,2,3),(4,2,1),(10,1,3),(1,3,4),(5,1,4)]
    N = 5
    G = edge_list_to_adjacency_list(G, N)
    pass
    # for i in range(N):
    #     print(dijkstra(G,0,i))
