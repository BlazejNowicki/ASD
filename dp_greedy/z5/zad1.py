# Problem plecakowy o złożoności wielomianowej względem liczby przedmiotów i sumy zysków
inf  = float("inf")

def knap_sack(W, P, max_w):
    n = len(W)
    sum_p = sum(P)
    T = [[inf for _ in range(sum_p+1)] for _ in range(n)]
    for i in range(0,n):
        for j in range(sum_p):
            if P[i] >= j:
                T[i][j] = min(T[i-1][j], W[i])
            else:
                T[i][j] = min(T[i-1][j], T[i-1][j - P[i]]+W[i])
    best = 0
    for i in range(sum_p):
        if T[n-1][i] <= max_w:
            best = max(best, i)
    return best

W = [1, 8, 2, 4, 2] # Wagi przedmiotów
P = [4, 3, 4, 3, 1] # Zysk ze spakowania danego przedmiotu
print(knap_sack(W, P, 9)) # Limit wagi
