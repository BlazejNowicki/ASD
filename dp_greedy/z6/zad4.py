inf = float("inf")


def min_jumps(A):
    n = len(A)
    s = sum(A)
    T = [[inf for _ in range(n)] for _ in range(s+1)]
    T[A[0]][0] = 0
    for i in range(n-1):
        for j in range(s+1):
            if T[j][i] < inf:
                for k in range(1, j+1):
                    if i+k < n and j-k >= 0:
                        T[j-k+A[i+k]][i+k] = min(T[j-k+A[i+k]][i+k], T[j][i]+1)
        pass    
    ans = inf
    for i in range(s):
        ans = min(ans, T[i][n-1])
    if ans < inf:
        return ans
    else:
        return None

# T = [2, 4, 3, 2, 5, 3, 3, 4, 5, 3, 4, 1, 1]
T = [4, 1, 3, 0]
print(min_jumps(T))