# Longest increasing subsequence O(nlogn)
def CeilIndex(tail, A, l, r, key):
    while (r - l > 1):

        m = l + (r - l)//2
        if (A[tail[m]] >= key):
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLength(A, size):
    tailTable = [0 for i in range(size + 1)]
    pTable = [None]*size
    len = 1
    for i in range(1, size):
        if (A[i] < A[tailTable[0]]):
            tailTable[0] = i

        elif (A[i] > A[tailTable[len-1]]):
            pTable[i] = tailTable[len-1]
            tailTable[len] = i
            len += 1

        else:
            index = CeilIndex(tailTable, A, -1, len-1, A[i])
            pTable[i] = pTable[tailTable[index]]
            tailTable[index] = i

    tmp = tailTable[len-1]
    ans = []
    while tmp is not None:
        ans.append(A[tmp])
        tmp = pTable[tmp]
    return ans[::-1]


A = [3, 5, 4, 7, 11, 1, 8, 10, 2, 6]
# A = [2,1,4,3]


n = len(A)

print("Length of Longest Increasing Subsequence is ",
      LongestIncreasingSubsequenceLength(A, n))

