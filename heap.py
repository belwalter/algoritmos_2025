

class Heap:

    def __init__(self):
        self.elements = []
    
    def size(self):
        return len(self.elements)

    def add(self, value):
        self.elements.append(value)
        self.flotar(self.size()-1)
    
    def remove(self):
        last = self.size() -1
        self.intercambio(0, last)
        value = self.elements.pop()
        self.hundir(0)
        return value

    def flotar(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.intercambio(index, father)
            index = father
            father = (index - 1) // 2

    def hundir(self, index):
        hijo_izq = (2 * index) + 1
        control = True
        while control and hijo_izq < self.size():
            hijo_der = hijo_izq + 1

            mayor = hijo_izq
            if hijo_der < self.size():
                if self.elements[hijo_der] > self.elements[mayor]:
                    mayor = hijo_der

            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.intercambio(index, mayor)
                index = mayor
                hijo_izq = (2 * index) + 1
            else:
                control = False


    def intercambio(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def heapsort(self):
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result



h = Heap()

h.add(1)
h.add(0)
h.add(33)
h.add(19)
h.add(5)
h.add(1)
h.add(3)
h.add(9)


list_sort = h.heapsort()

print(list_sort)
print(h.elements)


