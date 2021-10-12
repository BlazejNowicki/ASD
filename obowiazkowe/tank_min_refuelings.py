def min_refuelings(S, t, L):
    n = len(S)
    counter = 0
    max_range = L
    for i in range(n):
        if max_range >= t:
            return counter
        elif max_range < S[i]:
            return -1
        elif (i+1<n and max_range < S[i+1]) or (i+1==n and max_range < t):
            counter += 1
            max_range = S[i]+L
    return counter 


if __name__ == "__main__":
    S = [4,6,7,8,10,13,18,20]
    # S = [5,6,10,11,18]
    t = 21
    L = 5
    print(min_refuelings(S, t, L))