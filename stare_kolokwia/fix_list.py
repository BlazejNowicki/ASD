from random import randint


class Node():
    def __init__(self, v=0, n=None):
        self.value = v
        self.next = n


def print_list(ptr):
    ptr = ptr.next
    while ptr:
        print(ptr.value, end=" ")
        ptr = ptr.next
    print()


def add_to_list(LL, ptr, begin_from=None):
    if LL.value >= ptr.value:
        ptr.next = LL
        return ptr
    tmp = LL
    if begin_from:
        LL = begin_from
    while LL.next and LL.next.value < ptr.value:
        LL = LL.next
    ptr.next = LL.next
    LL.next = ptr
    return tmp


def fix_list(LL):
    to_move = None
    begin_from = None
    if LL.value > LL.next.value:
        to_move = LL
        LL = LL.next
    else:
        ptr = LL
        while ptr.next.next:
            if ptr.next.value > ptr.next.next.value:
                if ptr.value > ptr.next.next.value:
                    ptr = ptr.next
                else:
                    begin_from = ptr
                to_move = ptr.next
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
    if to_move:
        if begin_from:
            LL = add_to_list(LL, to_move, begin_from)
        else:
            LL = add_to_list(LL, to_move)
    return LL


if __name__ == "__main__":
    LL = None
    n = 10
    T = [randint(1, 99) for _ in range(n)]
    T.sort()
    T[randint(0, n-1)] = randint(1, 99)
    for val in reversed(T):
        LL = Node(val, LL)
    LL = Node(0, LL)
    print("RAW:  ", end="")
    print_list(LL)
    LL = fix_list(LL)
    print("PROG: ", end="")
    print_list(LL)
    print("AUTO: ", end="")
    for v in sorted(T):
        print(v, end=" ")
    print()
