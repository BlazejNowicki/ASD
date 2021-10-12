from random import randint


class Node():
    def __init__(self, v=0, n=None):
        self.value = v
        self.next = n


def print_list(ptr):
    while ptr:
        print(ptr.value, end=" ")
        ptr = ptr.next
    print()


def add_item(head, last, item):
    if head is None:
        head = last = item
    else:
        last.next = item
        last = last.next
    return head, last

def split(LL):
    if LL is None:
        return None, None
    even_head = even_last = odd_head = odd_last = None
    while LL:
        if LL.value%2==0:
            even_head, even_last = add_item(even_head , even_last, LL)
        else:
            odd_head, odd_last = add_item(odd_head, odd_last, LL)
        LL = LL.next
    even_last.next = odd_last.next = None
    return even_head, odd_head

if __name__ == "__main__":
    LL = None
    n = 10
    T = [randint(1, 99) for _ in range(n)]
    for val in reversed(T):
        LL = Node(val, LL)
    print("RAW:  ", end="")
    print_list(LL)
    odd_head, even_head = split(LL)
    print("ODD:  ", end="")
    print_list(odd_head)
    print("EVEN: ", end="")
    print_list(even_head)
