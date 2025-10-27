from typing import Any, Optional

from list_ import List

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            return self.value
    
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight
    
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
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            if self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        delete_value = g.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def deep_sweep(self, value) -> None:
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        


g = Graph()

g.insert_vertex('A')
g.insert_vertex('I')
g.insert_vertex('B')
g.insert_vertex('Z')
g.insert_vertex('G')

g.insert_edge('A', 'Z', 14)
g.insert_edge('A', 'G', 4)
g.insert_edge('I', 'A', 20)
g.insert_edge('A', 'B', 7)
g.insert_edge('B', 'Z', 144)
g.insert_edge('B', 'A', 40)
g.insert_edge('G', 'A', 24)
# g.insert_edge('B', 'I', 11)

g.show()
print()

# vertex = g.delete_vertex('A', 'value')
# print(f'deleted vertex: {vertex}')

g.deep_sweep('A')

# print()
# for vertex in g:
#     print(vertex.value, vertex.visited)
# g.show()
# print('segundo barrido')
# g.deep_sweep('I')

# es_adyacente(vértice, destino). Devuelve verdadero (true) si el destino es un nodo adyacente
# al vértice;
# adyacentes(vértice). Realiza un barrido de los nodos adyacentes al vértice;

# existe _paso(grafo, vértice origen, vértice destino). Devuelve verdadero (true) si es posible ir des-
# de el vértice origen hasta el vértice destino, caso contrario retornará falso (false);

# barrido_profundidad(grafo, vértice inicio). Realiza un barrido en profundidad del grafo a par-
# tir del vértice de inicio;

# barrido_amplitud(grafo, vértice inicio). Realiza un barrido en amplitud del grafo a partir del
# vértice de inicio;