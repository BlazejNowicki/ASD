from queue import PriorityQueue

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]

def huffman( S, F ):
    n = len(F)
    T = [None]*n

    pq = PriorityQueue()
    for i in range(n):
        pq.put((F[i], i))
    
    while True:
        L = pq.get()
        if pq.empty():
            break
        R = pq.get()
        T.append(("0", -1))
        pq.put((L[0]+R[0], len(T)-1))
        T[L[1]] = ("0", len(T)-1)
        T[R[1]] = ("1", len(T)-1)

    for i in range(n):
        print(S[i],":",end=' ')
        code = []
        j = i
        while T[j][1] > 0:
            code.append(T[j][0])
            j = T[j][1]
        for c in range(len(code)-1, -1, -1):
            print(code[c],end='')
        print()

huffman( S, F )