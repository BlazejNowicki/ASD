def mergesort(T):
    l=len(T)
    if l==1:return T,0
    A,x = mergesort(T[:l//2])
    B,y = mergesort(T[l//2:])
    inv_counter=x+y
    i=j=0
    for k in range(l):
        if j>=len(B) or ( i<len(A) and A[i] <= B[j] ):
            T[k]=A[i]
            i += 1
        else:
            T[k]=B[j]
            j += 1
            inv_counter += len(A)-i
    return T, inv_counter

def inversions(T):
    _, ans = mergesort(T)
    return ans

if __name__ == "__main__":
    # not sure it always works
    test = [
        [10,22,3,4,5,6,8,16],
        [1,2,3,4,67],
        [3, 2],
        [1],
        [4,3,2,6],
        [1,2,2,4]
    ]
    ans = [
        11,
        0,
        1,
        0,
        3,
        0
    ]
    for i, t in enumerate(test):
        print('array: {}, result: {}, expected: {}'.format(t, inversions(t), ans[i]))
