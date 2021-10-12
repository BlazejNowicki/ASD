from zad1testy import runtests

inf = float('inf')

def zbigniew(A):
    n = len(A)
    s = sum(A)
    T = [[inf for _ in range(n)] for _ in range(s)]
    T[A[0]][0] = 0
    for i in range(n-1):
        for j in range(s):
            if T[j][i] < inf:
                for k in range(1, j+1):
                    if i+k < n and j-k >= 0:
                        T[j-k+A[i+k]][i+k] = min(T[j-k+A[i+k]][i+k], T[j][i]+1)
    ans = inf
    for i in range(s):
        ans = min(ans, T[i][n-1])
    if ans < inf:
        return ans
    else:
        return None
       

runtests( zbigniew ) 
