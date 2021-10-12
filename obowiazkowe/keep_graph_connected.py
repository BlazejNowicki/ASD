# Błażej Nowicki
from queue import deque


def keep_connected(G):
    def DFS(u):
        visited[u] = True
        for i in range(n):
            if G[u][i] == 1 and not visited[i]:
                DFS(i)
        ans.append(u)

    n = len(G)
    ans = []
    visited = [False]*n
    DFS(0)
    return ans


if __name__ == "__main__":
    G = [[0, 1, 1, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]

    print(keep_connected(G))
