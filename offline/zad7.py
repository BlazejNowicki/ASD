# Błażej Nowicki
# Stosujemy algorytm zachłanny. Reprezentujemy i tworzymy kodowanie symboli w postaci ukorzenionego drzewa, gdzie
# kodowane symbole to liście. Aby odczytac kod poruszamy się od korzenia w dół, jeśli idziemy w lewo to odpowiada temu symbol 0,
# a jeśli w prawo to 1. Drzewo powstaje przez łączenie dwóch symboli o najmniejszej częstotliwości i zastępowanie ich jednym o częstotliwości
# równej ich sumie, aż nie zostanie w kolejce jeden symbol reprezentujący korzeń (uzasadnienie poprawności na wykładzie).
# Symbole reprezentujemy w klasie Node i umieszczamy je w kolejce priorytetowej pq. T zawiera wskazania do kolejnych symboli do wypisania w
# kolejności w jakiej je otrzymaliśmy na wejściu. Kod symbolu wypisujemy "cofając się" rekurencyjnie od liścia. 
# Podczas wypisywania obliczamy długość zakodowanego napisu.
# Dla przykładowych danych:
# lewo - 0 prawo - 1 
#        #
#      /   \
#     /     \
#    /      / \
#   /     / \  \
#  /\    /\  \  \
# b  d  e  c  a  f
# Złożoność: O(n^2) - (dla ciągu F = [1,2,4,8,16,32,...] średnia długość napisu to będzie n/2 a będzie ich do wypisania n.
# Sam algorytm tworzenia drzewa jest szybszy - O(nlogn))
# Złożoność pamięciowa: O(n) ( w drzewie będzie maksymalnie 2n elementów )

from queue import PriorityQueue

S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]

class Node:
    def __init__(self, f, v=None):
        self.frequency = f
        self.value = v
        self.parent = None 
        self.side = "0"

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __str__(self):
        return str(self.value)


def print_rec(t):
    if t.parent is not None:
        l = print_rec(t.parent)
        print(t.side, end='')
        return l+1
    return 0


def huffman(S, F):
    n = len(S)
    T = []
    pq = PriorityQueue()
    for i in range(n):
        T.append(Node(F[i], S[i]))
        pq.put(T[-1])

    while True:
        left = pq.get()
        if pq.empty():
            break
        right = pq.get()
        right.side = "1"
        left.parent = right.parent = Node(left.frequency+right.frequency)
        pq.put(left.parent)

    string_length = 0
    for i in range(n):
        print(T[i], end=" : ")
        string_length += F[i]*print_rec(T[i])
        print()
    print("dlugosc napisu:", string_length)

huffman(S, F)
