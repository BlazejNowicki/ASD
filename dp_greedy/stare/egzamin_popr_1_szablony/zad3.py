from zad3testy import runtests


def DFS(G, u, visited, order):
    visited[u] = True
    for i in range(len(G)):
        if (G[u][i] == 1 or G[i][u] == 2) and not visited[i]:
            DFS(G, i, visited, order)
    order.append(u)


def tasks(T):
    n = len(T)
    visited = [False]*n
    order = []
    for i in range(n):
        if not visited[i]:
            DFS(T, i, visited, order)
    return order[::-1]


runtests(tasks)
