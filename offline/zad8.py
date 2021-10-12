# Błażej Nowicki
# Szukamy cyklu Eulera w grafie nieskierowanym
# DFS z modyfikacją, że zamiast zapamiętywać odwiedzone wierzchołki, usuwamy wykorzystane krawędzie.
# Dany wierzchołek dodajemy do cyklu kiedy zostanie przetworzony, czyli kiedy nie będzie się z niego dało iść dalej.
# Na początku sprawdzmy warunek konieczny i wystarczający, jednocześnie tworząc kopię macierzy.
# Dla każdego wierzchołka będziemy rozważali wszystkich jego sąsiadów.
# W tablicy v zapisujemy dla danego wierzchołka indeks jednego wierzchołka z pozostałych na którym skończyliśmy sprawdzać sąsiedztwo
# Złożoność czasowa n^2 (musimy jeden raz sprawdzić każde pole z macierzy G i co najwyżej raz dla każdego sprawdzenia zmodyfikowac stos)
# Złożonośc pamięciowa n^2 na kopie macierzy G(można uniknąć alokowania dodatkowej pamięci przy założeniu że można zmodyfikować tablicę wejściowa
# a następnie ją przywrócić do pierwotnej formy przed zwróceniem)

from copy import deepcopy
from queue import deque

def euler(T):
    n = len(T)
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m = 0
        for j in range(n):
            if T[i][j] == 1:
                G[i][j] = T[i][j]
                m += 1
        if m == 0 or m % 2 == 1:  # WKW
            return None

    ans = []  # lista na szukany cykl
    v = [0]*n
    q = deque([0])
    while q:
        t = q[-1]
        # znajdź indeks sąsiada dla ostatniego wierzchołka na stosie
        while v[t] < n and (G[v[t]][t] != 1 or G[t][v[t]] != 1):
            v[t] += 1
        if v[t] < n:  # dodaj znaleziony wierzchołek na stos i usuń krawędź
            G[v[t]][t] = 0
            q.append(v[t])
        else:  # wierzchołek przetworzony, usuń ze stosu, dodaj do cyklu
            ans.append(q.pop())
    return ans

##############################


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")
