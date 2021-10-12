from collections import deque


def BFS(G, s):
    n = len(G)
    q = deque()
    visited = [False]*n
    dist = [-1]*n
    parent = [None]*n
    visited[s] = True
    dist[s] = 0
    q.append(s)
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u]+1
                parent[v] = u
                q.append(v)
    return dist, parent


G = [[1, 2],
     [0, 2, 4],
     [0, 1],
     [4],
     [1, 3]]
print(BFS(G, 0))
