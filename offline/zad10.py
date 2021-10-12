# Błażej Nowicki
# Algorytm analogiczny do algorytmu Dijkstry. Dla każdego wierzchołka v będziemy wyznaczać maksymalną pojemność ścieżki z wierchołka s do v (limit[v]). 
# Tworzymy kolejkę priorytetową typu max, tylko zamiast odległości umieszczmy oszacowania pojemności.
# Z przetwarzanego wierzchołka przeprowadzamy odpowiednik relaksacji, 
# czyli sprawdzmy czy możemy dla każdego sąsiedniego nieodwiedzonego wierzchołka przedłużyć scieżkę i uzyskać większą pojemność. 
# Wyjęcie z kolejki oznacza, że pojemność nie może się już zwiększyć(ponieważ wszystkie inne wierchołki maja mniejsze pojemności).
# Złożoność obliczeniowa: ElogV (E - liczba oszacowań równa liczbie krawędzi razy logV - potrzebne do obsługi kolejki priorytetowej) 
# Złożoność pamięciowe: V (liniowej długości tablice limit, parent, visited i kolejka priorytetowa)

from copy import deepcopy
from queue import PriorityQueue
INF = float('inf')


def max_extending_path(G, s, f):
    n = len(G)
    qq = PriorityQueue()
    parent = [None]*n
    limit = [0]*n
    visited = [False]*n
    qq.put((1/INF, s))
    limit[s] = INF
    while not qq.empty() and not visited[f]:
        _, t = qq.get()
        visited[t] = True
        for u, w in G[t]:
            if not visited[u] and limit[u] < min(limit[t], w):
                limit[u] = min(limit[t], w)
                parent[u] = t
                qq.put((1/limit[u], u))

    if limit[f] > 0:
        ans = []
        while f is not None:
            ans.append(f)
            f = parent[f]
        return ans[::-1]
    else:
        return None


# sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
# funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
s = 0
t = 3
C = 3


GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)


if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)


capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")
