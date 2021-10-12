from copy import deepcopy
from collections import deque

def euler( G ):
    n = len(G)
    E = deepcopy(G)
    cycle = deque()

    def dfs_visit(u):
        for v in range(n):
            if G[u][v] == 1 and E[u][v] == 1:
                E[u][v] = 0
                E[v][u] = 0
                dfs_visit(v)
                cycle.appendleft(v)

    for i in range(n):
        cnt = 0
        for j in range(n):
            if G[i][j] == 1:
                cnt += 1
        if cnt%2 != 0 or cnt == 0:
            return None

    dfs_visit(0)

    cycle.appendleft(cycle[len(cycle)-1])
    cycle = list(deque(cycle))
    return cycle  
  
  
G = [[0, 1, 1, 0, 0, 0],
      [1, 0, 1, 1, 0, 1],
      [1, 1, 0, 0, 1, 1],
      [0, 1, 0, 0, 0, 1],
      [0, 0, 1, 0, 0, 1],
      [0, 1, 1, 1, 1, 0]]

G2 = [[0, 1, 0, 0, 1, 0],
      [1, 0, 1, 0, 1, 1],
      [0, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 0, 1],
      [1, 1, 1, 0, 0, 1],
      [0, 1, 1, 1, 1, 0]]

G3 = [[0, 1, 1, 0, 0],
      [1, 0, 1, 1, 1],
      [1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 1, 0, 1, 0]]

G4 = [[0, 1, 1, 1, 1],
      [1, 0, 1, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 1, 0]]

G5 = [[0, 1, 1, 1, 1],
      [1, 0, 1, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0]]

if __name__ == "__main__":
    print(euler(G))
    print(euler(G2))
    print(euler(G3))
    print(euler(G4))
    print(euler(G5))
