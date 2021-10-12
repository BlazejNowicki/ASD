#sortowanie przez wstawianie
#sortowanie bombelkowe

class node:
  def __init__(self, v, next=None):
    self.v = v
    self.next=next

def printl(l):
  while l is not None:
    print(l.v, end=" ")
    l = l.next
  print()

#add value to sorted list
def linsert(head,v):
  p = head = node(0, head)
  while p.next is not None and p.next.v < v:
    p = p.next
  p.next = node(v, p.next)
  return head.next

#remove maximum
def remove_max(head):
    head = to_remove = p = node(0, head)
    while p.next is not None:
        if p.next.v > to_remove.next.v:
            to_remove = p
        p = p.next
    max_val = to_remove.next.v
    to_remove.next = to_remove.next.next
    return head.next, max_val

#sort by adding largest element to new list
def lselect_sort(head):
    sorted_list = None
    while head is not None:
        head, v = remove_max(head)
        sorted_list = node(v, sorted_list)
    return sorted_list

numbers = [8, 19, 11, 45, 21, 22, 7]
# numbers = [10, 8, 5, 3, 1]
list_head = None
for x in numbers:
  list_head = node(x, list_head)

# list_head = linsert(list_head, 20)
# list_head, v = remove_max(list_head)
# print("#", v)

printl(list_head)

list_head = lselect_sort(list_head)
printl(list_head)