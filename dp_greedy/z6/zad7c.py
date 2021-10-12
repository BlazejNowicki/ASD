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


def connect_segments(L, a, b, k):
    T = [(a,0)]
    L.sort(key=lambda x: x[1])

    for ai, bi in L:
        flag, index = binary_search(T, ai)
        if flag and T[-1][0] == bi and T[-1][1] > T[index][1]+1:
            T[-1] = (bi, T[index][1]+1) 
        elif flag and T[-1][0] != bi:
            T.append((bi, T[index][1]+1))

    flag, index = binary_search(T, b)
    return flag and T[index][1] <= k


T = [(1,3),(1,2),(1,4),(2,5),(3,6),(4,5),(2,10)]
a = 1
k = 1
for b in range(1, 13):
    print("a: {} b: {} - {}".format(a, b, connect_segments(T, a, b, k)))
