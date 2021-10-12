def DFS(G, visited, order, time, u):
    visited[u] = True
    for v in range(len(G)):
        if G[u][v] == 1 and not visited[v]:
            time = DFS(G, visited, order, time, v)
    order[u] = time
    time += 1
    return time


def keep_connected(G):
    n = len(G)
    visited = [False]*n
    order = [-1]*n
    time = 0

    for i in range(n):
        if not visited[i]:
            time = DFS(G, visited, order, time, i)
    return order


G = [[0, 1, 1, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 1, 0]]

print(keep_connected(G))
