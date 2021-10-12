INF = 10**5

def edge_list_to_adjacency_matrix(G, n):
    GG = [[-1 for _ in range(n)] for _ in range(n)]
    for w,u,v in G:
        GG[u][v] = w
        GG[v][u] = w
    return GG

def min_dist(dist, visited):
    min = INF
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min:
            min = dist[i]
            min_index = i
    return min_index

def dijkstra(G,s,f):
    n = len(G)
    dist = [INF]*n
    dist[s] = 0
    visited = [False]*n
    
    while not visited[f]:
        u = min_dist(dist, visited)
        visited[u] = True
        for v in range(n):
            if G[u][v] >= 0 and not visited[v] and dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
    return dist[f]

if __name__ == "__main__":
    G = [(1, 0, 1), (5, 1, 2), (3000, 2, 3), (9, 3, 4),
         (8, 4, 5), (12, 0, 5), (7, 1, 5), (6, 2, 5), (4, 2, 4)]
    N = 6
    G = edge_list_to_adjacency_matrix(G, N)
    print(dijkstra(G,0,3))
