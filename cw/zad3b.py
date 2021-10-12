def CeilIndex(tail, A, l, r, key):
    while (r - l > 1):

        m = l + (r - l)//2
        if (A[tail[m]] >= key):
            r = m
        else:
            l = m
    return r


def LIS(A, size):
    tails = [0 for i in range(size + 1)]
    pTable = [None]*size
    tails[0] = 0
    len = 1
    for i in range(1, size):
        if (A[i] < A[tails[0]]):
            tails[0] = i

        elif (A[i] > A[tails[len-1]]):
            pTable[i] = tails[len-1]
            tails[len] = i
            len += 1

        else:
            index = CeilIndex(tails, A, -1, len-1, A[i])
            pTable[i] = pTable[tails[index]]
            tails[index] = i

    tmp = tails[len-1]
    while tmp is not None:
        print(A[tmp], end=' ')
        tmp = pTable[tmp]
    print()
    return len


A = [3, 5, 4, 7, 11, 1, 8, 10, 2, 6]
# A = [2,1,4,3]


n = len(A)

print("Length of Longest Increasing Subsequence is ",
      LIS(A, n))

