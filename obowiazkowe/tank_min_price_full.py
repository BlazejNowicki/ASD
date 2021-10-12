def min_refuelings(S, P, t, L):
    n = len(S)
    min_cost = 0
    i=0
    while True:
        j = i+1
        cheapest_in_range = i+1
        while j < n and S[j]<S[i]+L:
            if P[j] < P[i]:
                break
            elif P[cheapest_in_range] >= P[j]:
                cheapest_in_range = j

if __name__ == "__main__":
    S = [4,6,7,8,10,13,18]
    P = [1,5,5,2,3,5,2]
    # S = [5,6,10,11,18]
    t = 21
    L = 4
    print(min_refuelings(S, t, L))