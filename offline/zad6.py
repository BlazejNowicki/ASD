# Błażej Nowicki
#
# \/-- rozwiązanie z wykładu
# Wprowadzamy funkcję: f(i, j) - minimalny koszt ścieżek kończących się na miastach o indeksach i, j
# takich, że 0 <= i < j oraz każde miasto 0...i...j należy do dokładnie jednej ze ścieżek
# Rozwiązanie problemu: min( f(i, n-1) + d(i, n-1) )
# Rekurencyjna zależność: f(i, j) = f(i, j-1)+d(j-1, j) dla i < j-1                   (a)
#                         f(j-1, j) = min( f(k, j-1)+d(k,j) ) po k: 0 <= k < j-1      (b)
# /\--
# Wartości funkcji zapamiętujemy w F[][], gdzie f(i, j) = F[j][i] (odwrócone aby można było łatwo zaalokować tablice trójkątną zamiast kwadratowej)
# W celu wypisania rozwiązania zaczniemy on miasta n-1, dopinając miasta n-2 ... 0 odpowiednio z lewej albo prawej strony aż do utworzenia pełnej pętli
# To z której strony należy je dopiąć można wywnioskować "cofając się" w zależości rekurencyjnej, wykorzystując wartości zapisane w F[][].
# Odwrócenie zależości (a):
#   (i, j) -> (i, j-1)-> (i, j-2) -> ... -> (i, i+1)
#   Miasta j-1 ... i+1 przypinamy z jednej strony (np z lewej)
# Odwrócenie zależności (b):
#   (i, i+1) ->  (k, i)
#   Miasto i przypinamy z drugiej strony (odpowiednio z prawej)
#   Aby podczas wypisywania nie trzeba było szukać ponownie k to wykożystujemy wolne miejsce na przekątnej i zapisujemy dla f(j-1, j) F[j][j] = k
# W drugim przypadku następuje zmiana kolejności argumentów funkcji, co odpowiada zamianie miejsc ścieżek, zatem przy wypisywaniu musimy zamienić końce
# nowo tworzonej pętli, lewy staje się prawym, a drugi odwrotnie.
# Struktura którą wykożystamy do tworzenia takiej pętli to tablica którą będziemy wypełniać od początku i od tyłu co reprezenuje dwa końce.
#
# Złożoność całego algorytmu: O(n^2)
# Złożoność funkcji wypisującej: O(n)

from math import *

C = [["Wrocław", 0, 2], ["Warszawa", 4, 3], ["Gdańsk", 2, 4], ["Kraków", 3, 1]]


def bitonicTSP(C):
    C.sort(key=lambda x: x[1])
    n = len(C)
    F = [[None] * (i+1) for i in range(n)]
    F[1][0] = dist(C, 0, 1)
    ans = tspf(0, n-1, F, C)+dist(C, 0, n-1)
    for i in range(1, n-1):
        ans = min(ans, tspf(i, n-1, F, C)+dist(C, i, n-1))
    print(ans)
    read(F, C)

# dystans pomiędzy miastami a i b
def dist(T, a, b):
    return sqrt((T[b][1]-T[a][1])**2 + (T[b][2]-T[a][2])**2)

# funkcja z wykładu z modyfikacją zapamiętującą k
def tspf(i, j, F, T):
    if F[j][i] is not None:
        return F[j][i]
    if i == j-1:
        best = tspf(0, j-1, F, T)+dist(T, 0, j)
        F[j][j] = 0
        for k in range(1, j-1):
            tmp = tspf(k, j-1, F, T)+dist(T, k, j)
            if tmp < best:
                best = tmp
                F[j][j] = k
        F[j][j-1] = best
    else:
        F[j][i] = tspf(i, j-1, F, T) + dist(T, j-1, j)
    return F[j][i]

# dodanie elementu do pętli
def add(W, x, conf, l, p):
    if conf:
        p -= 1
        W[p] = x
    else:
        l += 1
        W[l] = x
    return l, p


def read(F, T):
    n = len(T)
    W = [0]*n  # tworzona pętla
    W[n-1] = n-1
    l, p = -1, n-1  # lewy i prawy indeks do pętli
    i, j = F[n-1][n-1], n-1
    conf = False  # czy końce są zamienione miejscami
    while j > 0:
        while j > i+1:
            l, p = add(W, j-1, conf, l, p)
            j -= 1
        l, p = add(W, i, not conf, l, p)
        conf = not conf
        j, i = i, F[j][j]

    # wypisanie pętli
    for i in range(n-1, -1, -1):
        print(T[W[(p+i) % n]][0], ", ", sep="", end=" ")
    print(T[W[p-1]][0])


bitonicTSP(C)
