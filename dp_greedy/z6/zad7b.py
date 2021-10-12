def binary_search(T, x):
    l = 0
    r = len(T)-1
    while l < r:
        mid = (l+r)//2
        if T[mid][0] >= x:
            r = mid
        else:
            l = mid+1
    return T[l][0] == x, l


def connect_segments(L, a, b):
    T = [(a,0)]
    L.sort(key=lambda x: x[1])

    for ai, bi, w in L:
        flag, index = binary_search(T, ai)
        if flag and T[-1][0] == bi and T[-1][1] > T[index][1]+w:
            T[-1] = (bi, T[index][1]+w) 
        elif flag and T[-1][0] != bi:
            T.append((bi, T[index][1]+w))

    flag, index = binary_search(T, b)
    if flag:
        return T[index][1]
    else:
        return None


T = [(1, 3, 1), (1, 2, 1), (1, 4, 1), (2, 5, 1),
     (3, 6, 1), (4, 5, 1), (2, 10, 1)]
a = 1
for b in range(1, 13):
    print("a: {} b: {} - {}".format(a, b, connect_segments(T, a, b)))
