class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


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

def predecessor(tree, key):
    root = tree.root
    # Puste drzewo
    if root is None:
        return -1
    # Znajdź wartość w drzewie
    while root.key != key:
        if root.key < key:
            if root.right is None:
                return -1
            else:
                root = root.right
        else:
            if root.left is None:
                return -1
            else:
                root = root.left
    
    if root.left is not None:
        # Szukaj poprzednika w dół drzewa
        ptr = root.left
        while ptr.right is not None:
            ptr = ptr.right
        return ptr.key
    else: 
        # Szukany element to korzeń bez lewej gałęzi
        if root.parent is None:
            return -1
        
        # Szukaj poprzednika w górę drzewa
        prev = root
        ptr = root.parent
        while ptr.left.key == prev.key:
            ptr = ptr.parent
            prev = prev.parent
            if ptr is None: # Element najmniejszy
                return -1
        # wpp
        return ptr.key



if __name__ == "__main__":
    T = BSTtree()
    print("INSERTING")
    for v in [32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]:
        print(v, insert(T, v))
    print(sorted([32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]))
    print("PREDECESSOR")
    for v in [32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]:
        print(v,predecessor(T, v))
