# Błażej Nowicki
# Dla każdego wierzchołka sprawdzamy jaki najkrótrzy cykl przez niego przechodzi. W algorytmie Dijkstry jeśli podczas szukania nieodwiedzonych sąsiadów
# trafimy na wierchołek już przetworzony który nie jest dla niego 'parentem' to wiemy że istnieje do niego inna ścieżka, a zatem także cykl.
# Jego waga to suma wag wierzchołków i łączącej je krawędzi. W ten sposób znajdziemy wszystkie cykle, które mają szansę być najkrótrze i zapamiętujemy najlepszy.
# Jeśli kandydaci mają taką samą wagę to bierzemy ten krótrzy pod względem liczby krawędzi aby uniknąć sytuacji gdzie jedną krawędź o wadze 0 wybrano dwa razy.
# Złożoność: V^3 (dla każdego wierzchołka(V) Dijkstra w wersji macierzowej(V^2))

from copy import deepcopy
from math import inf


def min_dist(dist, visited):
    min = inf
    for i in range(len(dist)):
        if visited[i] == -1 and dist[i] <= min:
            min = dist[i]
            min_index = i
    return min_index


def parent_to_cycle(parent, u):
    ans = []
    while u != -1:
        ans.append(u)
        u = parent[u]
    return ans


def min_cycle_from_vertex(G, s):
    n = not_visited = len(G)
    dist = [inf]*n
    dist[s] = 0
    visited = [-1]*n
    parent = [-1]*n
    min_w = inf
    min_v = (-1, -1)
    while not_visited > 0:
        u = min_dist(dist, visited)
        visited[u] = visited[parent[u]]+1
        not_visited -= 1
        for v in range(n):
            if G[u][v] >= 0 and visited[v] == -1 and dist[v] > dist[u] + G[u][v]:
                dist[v] = dist[u] + G[u][v]
                parent[v] = u
            elif G[u][v] >= 0 and visited[v] >= 0 and parent[u] != v and min_w > dist[u] + dist[v] + G[u][v]:
                min_v = (u, v)
                min_w = dist[u] + dist[v]+G[u][v]
    min_l = visited[min_v[0]]+visited[min_v[1]] + 1
    return min_w, min_l, min_v, parent


def min_cycle(G):
    n = len(G)
    min_l = inf
    min_w = inf
    for i in range(n):
        w, l, v, p = min_cycle_from_vertex(G, i)
        if w < min_w or (w == min_w and l < min_l):
            min_w = w
            min_l = l
            min_v = v
            min_p = p
    if min_l < inf:
        #tu mozna normalnie skleić listy for'em ale wolałem nie wydłużać już kodu
        c = parent_to_cycle(min_p, min_v[0])[::-1] + parent_to_cycle(min_p, min_v[1])[:-1] 
        return c
    return []

# sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
# funkcja zwraca prawidłowy wynik


G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]


LEN = 7


GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)


if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")