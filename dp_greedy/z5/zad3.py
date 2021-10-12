def longest_subsequence(A, B):
    n = len(A)
    m = len(B)
    T = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[j-1] == B[i-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j-1], T[i-1][j], T[i][j-1])

A = list("AGGTAB")
B = list("GXTXAYB")
print(longest_subsequence(A, B)) # 4 - "GTAB"