class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.count = 1


class BSTtree:
    def __init__(self):
        self.root = None


def insert(tree, key):
    root = tree.root
    if root is None:
        tree.root = BSTNode(key)
        return True
    prev = None
    while root is not None:
        if root.key == key:
            return False
        prev = root
        prev.count += 1
        if root.key < key:
            root = root.right
        else:
            root = root.left
    new = BSTNode(key)
    if prev.key < key:
        prev.right = new
    else:
        prev.left = new
    new.parent = prev
    return True

def find_ith(tree, s):
    ptr = tree.root
    if s > ptr.count:
        return -1
    while ptr.right is not None or ptr.left is not None:
        if ptr.left is not None and ptr.left.count + 1 == s:
            return ptr.key
        if ptr.left is not None and ptr.left.count >= s:
            ptr = ptr.left
        else:
            if ptr.left is not None:
                s -= ptr.left.count
            ptr = ptr.right
            s -= 1
    return ptr.key


if __name__ == "__main__":
    T = BSTtree()
    print("INSERTING")
    for v in [32, 3, 21, 16, 1, 20, 38, 35, 6, 4]:
        print(v, insert(T, v))
    for i in range(1, 11):
        print(find_ith(T, i))
    # print(sorted([32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]))
    # print("PREDECESSOR")
    # for v in [32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]:
    #     print(v,predecessor(T, v))
