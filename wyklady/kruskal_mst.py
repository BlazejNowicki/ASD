from queue import PriorityQueue

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def find_set(x):
    if x!= x.parent:
        x.parent = find_set(x.parent)
    return x.parent

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(G,n):
    vert = [Node(i) for i in range(n)]
    A = []
    for w,u,v in sorted(G):
        if find_set(vert[u]) != find_set(vert[v]):
            A.append((w,u,v))
            union(vert[u], vert[v])
    return A

if __name__ == "__main__":
    # Graf reprezentowany przez listę krawędzi z wagami (w(u,v), u,v)
    G = [(1,0,1),(5,1,2),(3000, 2,3),(9,3,4),(8,4,5),(12,0,5),(7,1,5),(6,2,5),(4,2,4)]
    N = 6
    print(kruskal(G,N))
