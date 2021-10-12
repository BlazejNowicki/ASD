def knapsack2D(W, H, P, Lw, Lh):  # weight, height, profit, weight-limit, height-limit
    n = len(W)
    T = [[[0 for _ in range(Lw+1)] for _ in range(Lh+1)]
         for _ in range(n+1)]  # T[i][h][w]
    for i in range(1, n+1):
        for j in range(H[i-1], Lh+1):
            for k in range(W[i-1], Lw+1):
                T[i][j][k] = T[i-1][j][k]
                if j >= H[i-1] and k >= W[i-1]:
                    T[i][j][k] = max(T[i][j][k], T[i-1][j-H[i-1]][k-W[i-1]] + P[i-1])
    return T[n][Lh][Lw]

W = [1,2,3,4,5]
H = [2,1,3,2,1]
P = [2,3,5,1,7]
print(knapsack2D(W,H,P, 10, 8))
