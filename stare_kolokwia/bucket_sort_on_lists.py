from random import uniform
from math import floor

class Node():
    def __init__(self, v=0, n=None):
        self.value = v
        self.next = n

def print_list(ptr):
    ptr = ptr.next
    while ptr:
        print("{:.2f}".format(ptr.value), end=" ")
        ptr = ptr.next
    print()

def add_to_list(LL, ptr):
    tmp = ptr.next
    while LL.next and LL.next.value <= ptr.value:
        LL = LL.next
    ptr.next = LL.next
    LL.next = ptr
    return tmp

def bucket_sort(ptr, n):
    S = [ Node() for _ in range(n)]
    ans = ptr
    ptr = ptr.next
    while ptr:
        ptr = add_to_list(S[floor(ptr.value/10*n)], ptr)
    ptr = ans
    for l in S:
        tmp = l.next
        while tmp:
            ptr.next = tmp
            ptr = ptr.next
            tmp = tmp.next
    return ans


if __name__ == "__main__":
    LL = None
    n = 20
    T = [uniform(0.0, 9.9) for _ in range(n)]
    for val in reversed(T):
        LL = Node(val, LL)
    LL = Node(0, LL)
    print("RAW:  ", end="")
    print_list(LL)
    bucket_sort(LL, n)
    print("PROG: ", end="")
    print_list(LL)
    print("AUTO: ", end="")
    for v in sorted(T):
        print("{:.2f}".format(v), end=" ")
    print()
