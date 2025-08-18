from typing import Any


class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value: Any):
        def __insert(root, value):
            if root is None:
                return BinaryTree.__nodeTree(value)
            elif value < root.value:
                root.left = __insert(root.left, value)
            else:
                root.right = __insert(root.right, value)

            return root

        self.root = __insert(self.root, value)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def by_level(self):
        pass

    def search(self, value: Any):
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

arbol = BinaryTree()

arbol.insert(19)
arbol.insert(7)
arbol.insert(31)
arbol.insert(11)
arbol.insert(22)
arbol.insert(45)
arbol.insert(27)
# arbol.insert(11)

pos = arbol.search(1)
print(pos)
