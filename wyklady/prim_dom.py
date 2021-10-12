from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.wage = float('inf')

def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def prim(V, E): #lista krawedzi
    n = len(V)
    vs = [False for i in range(n)]
    A = []
    pq = PriorityQueue()
    
    for i in range(n):
        V[i] = Node(V[i])

    vs[0] = True
    V[0].wage = 0
    for i in range(n):
        pq.put((V[i].wage, V[i].val))

    while not pq.empty():
        _,t = pq.get()
        vs[t] = True
        for e in E:
            w = e[0]
            if t == e[1]:
                u = V[e[2]]
                if w < u.wage and vs[u.val] == False:
                    u.wage = w
                    u.parent = t
                    # vs[u.val] = True
                    pq.put((w, u.val))
                    A.append((t,u.val))

            elif t == e[2]:
                u = V[e[1]]
                if w < u.wage and vs[u.val] == False:
                    u.wage = w
                    u.parent = t
                    # vs[u.val] = True
                    A.append((t,u.val))
                    pq.put((w,u.val))

    return A



#[waga krawedzi, wierzcholek 1, wierzcholek 2]
e = [[2, 0, 1], [3, 1, 2], [1, 2, 3], [2, 6, 2], [1, 0, 6], [6, 0, 5], [5, 4, 6], [8, 4, 5], [7, 3, 4],]
v = [0, 1, 2, 3, 4, 5, 6]
r = prim(v,e)
print(r)
