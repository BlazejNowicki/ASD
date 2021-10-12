from collections import deque


inf = float('inf')

def highway_min_cost(G, s, t):
    n = len(G)
    visited = [False]*n
    dist = [inf]*n
    dq = deque()
    dq.append((s, 0))
    while dq:
        u, c = dq.popleft()
        if not visited[u]:
            visited[u] = True
            dist[u] = c
            for v, cv in G[c]:
                if not visited[v] and cv == 1:
                    dq.append((v, c+1))
                elif not visited[v] and cv == 0:
                    dq.appendleft((v, c))


# UWAGA - nietestowane*

# *bo mi się nie chciało

