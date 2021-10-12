def longest_common_subsequence(S1, S2):
    n1 = len(S1)
    n2 = len(S2)
    T = [[0 for _ in range(n1+1)] for _ in range(n2+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if S1[i-1] == S2[j-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            print(T[i][j], end=" ")
        print()
    return T[n1][n2]


if __name__ =="__main__":
    S1 = "ABCBDAB"
    S2 = "BDCABAB"
    print(longest_common_subsequence(S1, S2))