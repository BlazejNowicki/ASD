# O(V*E)
INF = float("inf")

def bellman_ford(G, s):
    n = len(G)
    dist = [INF]*n
    parent = [None]*n
    dist[s] = 0
    for _ in range(n-1):
        for u in range(n):
            for v, w  in G[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
    for u in range(n):
        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                print("Graf zawiera ujemny cykl")
                return None
    return dist, parent




if __name__ == "__main__":
    G = [[],
         [(2, 1), (0, 2)],
         [(3, 2)],
         [(1, -2), (0, 3)]]
    print(bellman_ford(G, 3))
