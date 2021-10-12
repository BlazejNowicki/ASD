def binary_search(T, x):
    l = 0
    r = len(T)-1
    while l < r:
        mid = (l+r)//2
        if T[mid] >= x:
            r = mid
        else:
            l = mid+1
    return T[l] == x 


def connect_segments(L, a, b):
    T = [a]
    n = len(L)
    L.sort(key=lambda x: x[1])
    for ai, bi in L:
        if binary_search(T, ai) and T[-1] != bi:
            T.append(bi)
        if T[-1] == b:
            return True
    return False


T = [(1,3),(1,2),(1,4),(2,5),(3,6),(4,5),(2,10)]
a = 1
for b in range(1, 13):
    print("a: {} b: {} - {}".format(a, b, connect_segments(T, a, b)))