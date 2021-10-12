from math import inf
from zad1testy import runtests


def DFS(G, u):
    n = len(G)
    visited = [-1]*n
    parent = [None]*n
    DFS_visit(G, u, visited, parent, 0)
    return visited, parent

def DFS_visit(G, u, visited, parent, dist):
    visited[u] = dist
    for i in G[u]:
        if visited[i] == -1:
            DFS_visit(G, i, visited, parent, dist+1)
            parent[i] = u

def max_index(T):
    index = 0
    for i in range(1, len(T)):
        if T[index] < T[i]:
            index = i
    return index

def best_root(L):
    n = len(L)
    visited, _ = DFS(L, 0)
    path_beg = max_index(visited)
    visited, parent = DFS(L, path_beg)
    ptr = max_index(visited)
    l = visited[ptr]
    for _ in range(l//2):
        ptr = parent[ptr] 
    return ptr


runtests(best_root)
