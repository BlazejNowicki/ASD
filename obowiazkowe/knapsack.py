def knapsack(W, P, MaxW):
    MaxW = min(sum(W), MaxW)
    n = len(W)
    F = [[0]*(MaxW+1) for _ in range(n)]
    for w in range(W[0], MaxW+1):
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, MaxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w-W[i]]+P[i])
    return F[n-1][MaxW], F, MaxW


def getsolution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]
        return []
    if w >= W[i] and F[i][w] == F[i-1][w-W[i]]+P[i]:
        return getsolution(F, W, P, i-1, w-W[i]) + [i]
    return getsolution(F, W, P, i-1, w)


if __name__ == "__main__":
    P = [10, 8, 4, 5, 3, 7]
    W = [4, 5, 12, 9, 1, 13]
    max_capacity = 24
    max_value, F, max_capacity= knapsack(W, P, max_capacity)
    print(max_value)
    print(getsolution(F, W, P, len(P)-1, max_capacity))
