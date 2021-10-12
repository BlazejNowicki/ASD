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

