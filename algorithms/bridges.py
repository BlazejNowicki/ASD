inf  = float('inf')

def DFS(G, u, visited, low, parent, time):
    visited[u] = low[u] = time
    for v in G[u]:
        if visited[v] != -1:
            if parent[u] != v:
                low[u] = min(visited[v], low[u])
        else:
            parent[v] = u
            time, l = DFS(G, v, visited, low, parent,time+1)
            low[u] = min(low[u], l)
    return time, low[u]

def bridges(G):
    n = len(G)
    visited = [-1]*n
    low = [inf]*n
    parent = [None]*n
    DFS(G, 0, visited, low, parent, 1)
    for i in range(1,n):
        if low[i] == visited[i]:
            print(parent[i], i)

def edge_list_to_adjacency_list(G, n):
    GG = [list() for _ in range(n)]
    for u, v in G:
        GG[u].append(v)
        GG[v].append(u)
    return GG
    
L = [(0,5),(5,7),(7,6),(6,4),(4,5),(4,3),(3,2),(2,1),(1,3),(0,8)]
N = 9
G = edge_list_to_adjacency_list(L, N)
bridges(G)