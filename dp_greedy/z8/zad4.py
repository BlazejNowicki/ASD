def counting_sort(A, k):
    length = len(A)
    B = [None]*length
    C = [0]*k
    for i in range(length):
        C[A[i][0]] = C[A[i][0]]+1
    for i in range(1, k):
        C[i] = C[i-1] + C[i]
    for i in range(length-1, -1, -1):
        B[C[A[i][0]]-1] = A[i]
        C[A[i][0]] -= 1
    return B


def decreasing_path(G, x, y):
    n = len(G)
    edge_list = []
    parent = [None]*n
    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                edge_list.append((G[i][j], i, j))
    edge_list = counting_sort(edge_list, len(edge_list)+1)[::-1]
    can_be_reached = [False]*n
    can_be_reached[x] = True
    for _, u, v in edge_list:
        if can_be_reached[u] and not can_be_reached[v]:
            can_be_reached[v] = True
            parent[v] = u
    ans = []
    if can_be_reached[y]:
        t = y
        while t is not None:
            ans.append(t)
            t = parent[t]
    return ans[::-1]


G = [[0, 7, 1, 0, 2],
     [7, 0, 4, 0, 6],
     [1, 4, 0, 5, 0],
     [0, 0, 5, 0, 3],
     [2, 6, 0, 3, 0]]

print(decreasing_path(G, 0, 3))