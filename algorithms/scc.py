# Strongly connected components

def DFS(G, v, time, visited, order):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            time = DFS(G, u, time, visited, order)
    order[time] = v
    time += 1
    return time


def DFSUntil(G):
    n = len(G)
    order = [0]*n
    time = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            time = DFS(G, i, time, visited, order)
    return order


def DFSGroup(G, v, visited):
    tmp = []
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            tmp += DFSGroup(G, u, visited)
    return tmp + [v]


def SCC(G):
    n = len(G)
    order = DFSUntil(G)

    # Dla wersji macierzowej można bez kopiowania
    G_rev = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G_rev[v].append(u)

    # Składowe jako listy wierzchołków
    components = []
    visited = [False]*n
    for v in reversed(order):
        if not visited[v]:
            components.append(DFSGroup(G_rev, v, visited))
    return components


if __name__ == "__main__":
    G = [[1],
         [2],
         [0, 3, 5],
         [4],
         [],
         [4]]
    print(SCC(G))
    # [[1,2,0], [5], [3], [4]]
