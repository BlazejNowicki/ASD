# O(V^3)
INF = 10**5

# Ważne przygotowanie grafu
def edge_list_to_adjacency_matrix(G, n):
    GG = [[INF for _ in range(n)] for _ in range(n)]
    for w, u, v in G:
        GG[u][v] = w
        GG[v][u] = w
    for i in range(n):
        GG[i][i] = 0
    return GG


def floyd_warshall(G):
    n = len(G)
    for t in range(n):
        for u in range(n):
            for v in range(n):
                G[u][v] = min(G[u][v], G[u][t] + G[t][v])
    return G


if __name__ == "__main__":
    G = [(1, 0, 1), (5, 1, 2), (3000, 2, 3), (9, 3, 4),
         (8, 4, 5), (12, 0, 5), (7, 1, 5), (6, 2, 5), (4, 2, 4)]
    N = 6
    G = edge_list_to_adjacency_matrix(G, N)
    D = floyd_warshall(G)
    for row in D:
        print(row)

