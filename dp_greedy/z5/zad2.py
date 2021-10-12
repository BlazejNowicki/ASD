def subset_sum(W, s):
    if s > sum(W): return False
    T = [False]*(s+1)
    T[0] = True
    for v in W:
        for i in range(s, v-1, -1):
            if T[i-v] == True:
                T[i] = True
    return T[s]

T = [7,8,2]
for s in range(5, 30):
    print(s, subset_sum(T, s))
