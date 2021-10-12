class Node:
    def __init__(self, v=0, n=None):
        self.value=v
        self.next=n

def merge_lists(A,B):
    C_head=C=Node()
    while A and B:
        if A.value < B.value:
            C.next = A
            A = A.next
        else:
            C.next = B
            B = B.next
        C = C.next
    if A:
        C.next=A
    else:
        C.next=B
    while C.next:
        C=C.next
    #C-pointer to the last element
    return C_head.next, C

def split(L):
    if not L:
        return None,None
    a=L
    while L.next and L.value <= L.next.value:
        L=L.next
    tmp=L.next
    L.next=None
    return a,tmp

def merge_sort(L):
    is_sorted=False
    while not is_sorted:
        sorted_part=None
        is_sorted=True
        while L:
            left,L=split(L)
            right,L=split(L)
            if right:
                is_sorted=False
            x,i=merge_lists(left, right)
            i.next=sorted_part
            sorted_part=x
        L=sorted_part
    return sorted_part


def print_list(A):
    if not A:
        print("None", end='')
    while A:
        print(A.value , end=' ')
        A = A.next
    print()

if __name__ == "__main__":
    LL=None
    for i in reversed([5,6,7,2,3,1,8,9,4,4,7]):
        LL = Node(i, LL)
    print_list(LL)
    print_list(merge_sort(LL))
