from typing import Any, Optional
from queue_ import Queue

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values)
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

    def search(self, value: Any) -> __nodeTree:
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

    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)


arbol = BinaryTree()

arbol.insert('F', 'f')
arbol.insert('B', 'b')
arbol.insert('K', 'k')
arbol.insert('E', 'e')
arbol.insert('H', 'h')
arbol.insert('J', 'j')
arbol.insert('R', 'r')
arbol.insert('I', 'i')
arbol.insert('A', 'a')


# pos = arbol.search('F')
# if pos is not None:
#     arbol.delete('F')
#     arbol.insert('C', 'c')

delete_value, deleter_other_values = arbol.delete('K')
if delete_value is not None:
    print(delete_value, deleter_other_values)


# arbol.in_order()
# # delete_value = arbol.delete('F')

# # if delete_value is not None:
# #     print(f'valor eliminado {delete_value}')
# # else:
# #     print('valor no encontrado')
# # print()
# arbol.by_level()


# # arbol.insert(11)

# # pos = arbol.search(19)
# # print(pos)
# arbol.in_order()

# from super_heroes_data import superheroes

# for super_hero in superheroes:
#     arbol.insert(super_hero['name'], super_hero)

# arbol.villain_in_order()

# print()
# pos = arbol.search("Thanos")
# if pos is not None:
#     print(pos.value, pos.other_values)
