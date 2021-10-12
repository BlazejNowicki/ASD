from zad2testy import runtests

inf = float('inf')

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0     # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0     # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane

def max_subtree(ptr, k):
    ptr.X = [-inf for _ in range(k+1)]
    ptr.X[0] = 0
    ans = -inf
    if ptr.left is not None:
        ans = max(ans, max_subtree(ptr.left, k))
        for i in range(k):
            ptr.X[i+1] = max(ptr.X[i+1], ptr.left.X[i] + ptr.leftval)

    if ptr.right is not None:
        ans = max(ans, max_subtree(ptr.right, k))
        for i in range(k):
            ptr.X[i+1] = max(ptr.X[i+1], ptr.right.X[i] + ptr.rightval)
    
    if ptr.right is not None and ptr.left is not None:
        for s in range(2, k+1):
            for i in range(1, s):
                ptr.X[s] = max(ptr.X[s], ptr.left.X[i-1] + ptr.right.X[s-i-1] + ptr.rightval + ptr.leftval)
    ans = max(ans, ptr.X[k])
    return ans

def valuableTree(T, k):
    return max_subtree(T, k)


runtests(valuableTree)
