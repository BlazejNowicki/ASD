from queue import deque


def euler(T):
    n = len(T)
    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m = 0
        for j in range(n):
            if T[i][j] == 1:
                G[i][j] = T[i][j]
                m += 1
        if m == 0 or m % 2 == 1:  # WKW
            return None

    ans = []  # lista na szukany cykl
    v = [0]*n
    q = deque([0])
    while q:
        t = q[-1]
        # znajdź indeks sąsiada dla ostatniego wierzchołka na stosie
        while v[t] < n and (G[v[t]][t] != 1 or G[t][v[t]] != 1):
            v[t] += 1
        if v[t] < n:  # dodaj znaleziony wierzchołek na stos i usuń krawędź
            G[v[t]][t] = 0
            q.append(v[t])
        else:  # wierzchołek przetworzony, usuń ze stosu, dodaj do cyklu
            ans.append(q.pop())
    return ans