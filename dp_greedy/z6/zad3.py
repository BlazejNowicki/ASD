def ferry_loading(T, L):
    n = len(T)
    prev_slice = [[False for _ in range(L+1)] for _ in range(L+1)]
    prev_slice[L][L] = True
    cur_slice = [[False for _ in range(L+1)] for _ in range(L+1)]
    k = 0
    free_space = True
    while free_space:
        free_space = False
        for i in range(L+1):
            for j in range(L+1):
                if i+T[k] <= L:
                    cur_slice[i][j] = prev_slice[i+T[k]][j] 
                if j+T[k] <= L:
                    cur_slice[i][j] = prev_slice[i][j+T[k]] or cur_slice[i][j] 
                if cur_slice[i][j]:
                    free_space = True
        prev_slice, cur_slice = cur_slice, prev_slice
        for i in range(L+1):
            for j in range(L+1):
                cur_slice[i][j] = False
        k += 1
        if k == n: 
            return (n if free_space else n-1)
    return k-1


# T = [1,3,12,5,7,2,2,3]
T = [1,3,12,5,1]
L = 12
print(ferry_loading(T, L)) # 6