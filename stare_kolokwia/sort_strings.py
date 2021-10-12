from random import shuffle

def get_index(string, pos):
    if len(string) < pos:
        return 0
    else:
        return ord(string[pos-1])-ord('a')+1

def counting_sort(A, B, position):
    length = len(A)
    C = [0]*7
    for i in range(length):
        C[get_index(A[i], position)] += 1
    for i in range(1, 7):
        C[i] = C[i-1] + C[i]
    for i in range(length-1, -1, -1):
        B[C[get_index(A[i], position)]-1] = A[i]
        C[get_index(A[i], position)] -= 1


def sort_string(A, B):
    max_len = 0
    for s in A:
        max_len = max(max_len, len(s))
    for sort_index in range(max_len, 0, -1):
        counting_sort(A, B, sort_index)
        for i in range(len(A)):
            A[i] = B[i]
    
s = ["aaa", "a", "bca", "bcabca", "bcc", "dbced", "e"]

# shuffle(s)
ss = ["" for _ in range(len(s))]
print(s)
sort_string(s, ss)
print(s)