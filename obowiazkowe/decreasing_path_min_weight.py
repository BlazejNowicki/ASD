from queue import PriorityQueue
inf = float("inf")

class Vertex:
    def __init__(self):
        self.history = [(inf, None),(inf, None)] # (długość ścieżki, wskaźnik do krawędzi z której przyszło)

class Edge:
    def __init__(self, u, v, w):   # (u -> v)
        self.u = u
        self.v = v
        self.w = w
        self.prev = None
    
    def __lt__(self, other):
        return self.w < other.w

def find_path(T, n):
    E = []
    for u,v,w in T:
        E.append(Edge(u,v,w))
        E.append(Edge(v,u,w))
    E.sort(reverse=True)
    V = [Vertex() for _ in range(n)]
    V[0].path = 0
    for e in E:
        if e.w < V[e.v].history:
            V[e.v].history.append((e.w, e))
            e.prev = p
        break


# edge - (u,v,w)
IN = [(0,1,30), (0,6,5),(5,6,4),(1,5,20),(2,5,10),(1,2,40),(2,4,5),(3,4,2),(2,3,8)]
find_path(IN,7)