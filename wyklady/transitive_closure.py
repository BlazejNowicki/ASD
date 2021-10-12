from copy import deepcopy

def transitive_closure(G):
    GG = deepcopy(G)
    n = len(GG)
    for t in range(n):
        for u in range(n):
            for w in range(n):
                GG[u][w] = max(GG[u][w], min(GG[u][t], GG[t][w]))
    return GG

G = [[0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1, 0]]

GG = transitive_closure(G)
for row in GG:
    print(row)
