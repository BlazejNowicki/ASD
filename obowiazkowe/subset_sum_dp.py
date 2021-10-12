def subset_sum(W, x):  # W - weights , x - desired sum
    n = len(W)
    F = [[False for _ in range(x+1)] for _ in range(n+1)]
    for i in range(n+1):
        F[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if j < W[i-1]:
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = F[i-1][j] or F[i - 1][j-W[i-1]]
    # for i in range(n + 1):
    #     for j in range(sum + 1):
    #         print(F[i][j], end=" ")
    #     print()
    return F[n][x]


if __name__ == '__main__':
    w = [3, 34, 4, 12, 5, 2]
    sum = 38
    if (subset_sum(w, sum)):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")
