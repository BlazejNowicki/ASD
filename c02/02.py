def mergesort(T):
    while True:
        # list of elements that break the ascending order
        breakpoints = [0]
        for i in range(len(T)-1):
            if T[i]>T[i+1]:
                breakpoints.append(i+1)
        if len(breakpoints) == 1:
            break
        breakpoints.append(len(T))
        # updated copy of T with n/2 breakpoints
        T = merge(T, breakpoints)
    return T

def merge(T, BP):
    TT = [0]*len(T)
    for i in range(0,len(BP)-2, 2):
        b,m,e = BP[i], BP[i+1], BP[i+2]
        for j in range(b,e):
            if m>=BP[i+2] or (b<BP[i+1] and T[b]<T[m]):
                TT[j]=T[b]
                b += 1
            else:
                TT[j]=T[m]
                m += 1
    for i in range(e,len(TT)):
        TT[i]=T[i]
    return TT


if __name__ == "__main__":
    T = [2,3,6,5,8,4,6,5,8,2,3,5,6,9,8,7]
    print(T)
    print(sorted(T))
    print(mergesort(T))
