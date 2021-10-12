INF = 10**4


class PriorityQueue:
    def __init__(self) -> None:
        self.contents = []

    def put(self, item):
        self.contents.append(item)

    def get(self):
        self.contents.sort()
        return self.contents.pop()

    def empty(self):
        return not self.contents


def dijkstra(G, s, f):
    n = len(G)
    qq = PriorityQueue()
    parent = [None]*n
    limit = [0]*n
    visited = [False]*n
    qq.put((INF, s))
    limit[s] = INF
    while not qq.empty() and not visited[f]:
        _, t = qq.get()
        visited[t] = True
        for u, w in G[t]:
            if not visited[u] and limit[t] >= w and limit[u] < w:
                limit[u] = w
                parent[u] = t
                qq.put((limit[u], u))

    while f is not None:
        print(f, end=' ')
        f = parent[f]
    print()


# 3 4 2 0
G = [[(1, 11), (2, 15)],
     [(4, 100)],
     [(4, 12), (5, 3)],
     [],
     [(3, 1), (5, 13)],
     [(3, 15)]]
dijkstra(G, 0, 3)

# 5 2 4 3 0
G = [[(1, 100), (3, 20)],
     [(2, 5)],
     [(5, 10)],
     [(4, 20)],
     [(2, 20)],
     []]
dijkstra(G, 0, 5)
