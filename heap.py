from typing import Any

class HeapMax:

    def __init__(self):
        self.elements = []
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def attention(self) -> Any:
        value = self.remove()
        return value


class HeapMin:

    def __init__(self):
        self.elements = []
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def remove(self) -> Any:
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def attention(self) -> Any:
        value = self.remove()
        return value

    def change_priority(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)

# priority_queue = HeapMin()

# priority_queue.arrive('x', 1)
# priority_queue.arrive('b', 2)
# priority_queue.arrive('a', 2)
# priority_queue.arrive('f', 1)
# priority_queue.arrive('y', 1)
# priority_queue.arrive('j', 2)
# priority_queue.arrive('z', 3)
# print(priority_queue.elements)

# while priority_queue.size() > 0:
#     print(priority_queue.attention())

# h = HeapMin()
# h.add(19)
# h.add(5)
# h.add(1)
# h.add(3)
# h.add(9)


# list_sort = h.heapsort()

# print(list_sort)
# print(h.elements)


