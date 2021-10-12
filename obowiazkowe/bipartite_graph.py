from queue import deque


def is_biparte_visit(G, beg, color):
    n = len(G)
    queue = deque([beg])
    color[beg] = 0

    while queue:
        u = queue.pop()
        for i in range(n):
            if G[u][i] == 1 and color[i] == -1:
                queue.appendleft(i)
                color[i] = (color[u]+1) % 2
            elif G[u][i] == 1 and color[i] == color[u]:
                return False
    return True


def is_biparte(G):
    n = len(G)
    color = [-1]*n
    for v in range(n):
        if color[v] == -1:
            if not is_biparte_visit(G, v, color):
                return False
    return True


if __name__ == "__main__":

    G = [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]]

    print(is_biparte(G))
