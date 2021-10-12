class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# definicja tree jako klasy aby uniknąć zwracania referencji do root np podczas uswania elementu który jest korzeniem
class BSTtree: 
    def __init__(self):
        self.root = None


def insert(tree, key):
    root = tree.root
    if root is None:
        # Drzewo puste
        tree.root = BSTNode(key)
        return True
    # Sprawdź czy klucz już sie pojawił w drzewie i znajdź miejsce na nowy element
    prev = None
    while root is not None:
        if root.key == key:
            return False
        prev = root
        if root.key < key:
            root = root.right
        else:
            root = root.left
    # Wstaw nowy element
    new = BSTNode(key)
    if prev.key < key:
        prev.right = new
    else:
        prev.left = new
    new.parent = prev
    return True


def remove(tree, key):
    root = tree.root
    # Drzewo puste
    if root is None:
        return False
    # Znajdź wartość w drzewie
    while root.key != key:
        if root.key < key:
            if root.right is None:
                return False
            else:
                root = root.right
        else:
            if root.left is None:
                return False
            else:
                root = root.left

    if root.left is None and root.right is None:  # Liść
        if root.parent is None:  # Tylko jeden wierzchołek w grafie
            tree.root = None
        elif root.parent.left is None or root.parent.left.key != root.key:  # czy do parenta przychodzimy z prawej
            root.parent.right = None
        else:
            root.parent.left = None
    elif root.left is None:  # Można przepiąć z prawej
        if root.parent is None:
            tree.root = root.right
            root.right.parent = None
        elif root.parent.left is None or root.parent.left.key != root.key:
            root.parent.right = root.right
            root.right.parent = root.parent
        else:
            root.parent.left = root.right
            root.right.parent = root.parent
    elif root.right is None:  # Można przepiąć z lewej
        if root.parent is None:
            tree.root = root.left
            root.left.parent = None
        elif root.parent.left is None or root.parent.left.key != root.key:
            root.parent.right = root.left
            root.left.parent = root.parent
        else:
            root.parent.left = root.left
            root.left.parent = root.parent
    else:  # Wyszukaj i zamień z poprzednikiem
        ptr = root.left
        while ptr.right is not None:
            ptr = ptr.right
        root.key = ptr.key
        if ptr.key == root.left.key:
            root.left = ptr.left
        else:
            ptr.parent.right = ptr.left
        if ptr.left is not None:
            ptr.left.parent = ptr.parent
    return True


if __name__ == "__main__":
    T = BSTtree()
    print("INSERTING")
    for v in [32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]:
        print(v, insert(T, v))
    print("REMOVING")
    for v in [32, 1, 20, 38, 35, 32, 3, 3, 6, 4, 32, 3, 21, 16, 1, 20, 3, 38, 35, 6, 16, 4]:
        print(v, remove(T, v))
