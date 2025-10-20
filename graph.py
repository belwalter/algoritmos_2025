from typing import Any, Optional

from list_ import List

class Graph(list):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            return self.value
    
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    CRITERION_FUNCTIONS = {}
    
    def __init__(self, is_directed=True):
        def order_by_value(item):
            return item.value
        
        self.add_criterion('value', order_by_value)
        self.is_directed = is_directed

    def add_criterion(
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(
        self
    ) -> None:
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insert_vertex(
        self,
        value: Any,
    ) -> None:
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search(origin_vertex)
        destination = self.search(destination_vertex)
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    # def delete_value(
    #     self,
    #     value,
    #     key_value: str = None,
    # ) -> Optional[Any]:
    #     index = self.search(value, key_value)
    #     return self.pop(index) if index is not None else index

    def sort_by_criterion(
        self,
        criterion_key: str = None,
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = 'value',
    ) -> int:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2


g = Graph(is_directed=False)

g.insert_vertex('A')
g.insert_vertex('I')
g.insert_vertex('B')
g.insert_vertex('Z')
g.insert_vertex('G')

g.insert_edge('A', 'Z', 14)
g.insert_edge('A', 'G', 4)
g.insert_edge('B', 'Z', 144)
g.insert_edge('B', 'I', 40)
g.insert_edge('I', 'I', 24)
g.insert_edge('I', 'Z', 11)

g.show()