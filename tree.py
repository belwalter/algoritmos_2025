from typing import Any





class Tree:

    class __nodeTree:

        def __init__(self, value: Any):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value: Any):
        print(f'insertar value {value}')
        def __insert(root, value):
            if root is None:
                print('lugar libre insertar raiz')
                return Tree.__nodeTree(value)
            elif value < root.value:
                print(f'vamos a la izquierda ->padre {root.value}')
                root.left = __insert(root.left, value)
            else:
                print(f'vamos a la derecha ->padre {root.value}')
                root.right = __insert(root.right, value)

            return root

        self.root = __insert(self.root, value)


arbol = Tree()

arbol.insert(19)
arbol.insert(7)
arbol.insert(31)
arbol.insert(11)
print(arbol.root.value, arbol.root.left.value, arbol.root.right.value)

