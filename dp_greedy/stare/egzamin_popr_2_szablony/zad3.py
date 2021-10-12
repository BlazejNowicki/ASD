from zad3testy import runtests
from collections import deque

def merge_two(L, R):
    new = end = None
    while L is not None or R is not None:
        if R is None or (L is not None and L.val < R.val):
            if new is None:
                new = end = L
            else:
                end.next = L
                end = end.next
            L = L.next
        else:
            if new is None:
                new = end = R
            else:
                end.next = R
                end = end.next
            R = R.next
    end.next = None
    return new

    
def tasks(T):
    Q = deque()
    for l in T:
        Q.append(l)
    
    while True:
        left = Q.popleft()
        if not Q:
            return left
        right = Q.popleft() 
        new = merge_two(left, right)
        Q.append(new)


runtests( tasks )
