from typing import Any, Optional

from heap import HeapMin
from list_ import List
from queue_ import Queue
from stack import Stack

class Graph(List):

    # vértice del grafo
    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            # value: valor del nodo (ej: "A", "B", "C").
            self.value = value
            # edges: lista de aristas que salen del vértice.
            self.edges = List()
            # Esto permite ordenar las aristas por valor o por peso.
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            # other_values: información adicional opcional.
            self.other_values = other_values
            # visited: usado en recorridos (true/false).
            self.visited = False

        def __str__(self):
            return str(self.value) #se agregó el str (string) para que muestre bien

    # arista entre dos vértices
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            # value: vértice destino (ej: "C").
            self.value = value
            # weight: peso de la arista.
            self.weight = weight
            # other_values: datos adicionales.
            self.other_values = other_values

        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'

    def __init__(self, is_directed=False):
        # Añade criterio de ordenación por valor.
        self.add_criterion('value', self._order_by_value)
        # Define si el grafo es dirigido o no dirigido.
        self.is_directed = is_directed

    # para ordenar vértices o aristas según su valor o peso.
    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight

    # Muestra todos los vértices y sus aristas
    def show(
        self
    ) -> None:
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show()

    # Crea un nodo vértice y lo agrega a la lista del grafo
    def insert_vertex(
        self,
        value: Any,
        other_values: Optional[Any] = None) -> None: #añadido el other_values
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)

    # Agrega una arista entre dos vértices
    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        # Busca los vértices por valor
        origin = self.search(origin_vertex, 'value')
        # Crea una arista destino con peso
        destination = self.search(destination_vertex, 'value')
        # La inserta en origin.edges
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            # Si el grafo NO es dirigido, agrega también la arista inversa.
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    # Elimina la arista que va de origin a destination
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

    # Elimina un vértice entero y todas las aristas que apuntan a él
    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        delete_value = self.delete_value(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    # Pone todos los vértices en estado "no visitado"
    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    # Devuelve True si existe un camino entre origin y destination (DFS recursivo)
    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            # Busca el vértice origen
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    # Marca como visitado.
                    graph[vertex_pos].visited = True
                    # Si llega al destino entonces True.
                    if graph[vertex_pos].value == destination:
                        return True
                    # Si no, continúa por vecinos recursivamente.
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            # Si agota opciones entonces False.
            return result

        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result

    # Recorrido en profundidad
    def deep_sweep(self, value) -> None:
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    # Marca el nodo
                    graph[vertex_pos].visited = True
                    # Lo imprime
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            # Llama recursivamente a todos sus vecinos no visitados.
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)

    # Recorrido en amplitud
    def amplitude_sweep(self, value)-> None:
        queue_vertex = Queue()
        # Marca todos como no visitados.
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                # Encola el vértice inicial.
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    # Desencola y muestra el nodo.
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                # Encola vecinos no visitados.
                                queue_vertex.arrive(self[destination_edge_pos])

    # Implementa el algoritmo de Dijkstra para caminos mínimos.
    def dijkstra(self, origin):
        from math import inf
        # HeapMin: guarda los vértices pendientes ordenados por distancia mínima.
        no_visited = HeapMin()
        # Stack: almacena el resultado final.
        path = Stack()
        for vertex in self:
            # distancia = 0 si es origen, distancia = infinito en otro caso
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)
        while no_visited.size() > 0:
            value = no_visited.attention()
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            # Para cada vecino
            for edge in edges:
                # calcula nuevo costo
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if pos is not None:
                        # si es menor que el actual registrado entonces lo actualiza.
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path

    # Implementa el algoritmo de Kruskal para el Árbol de Expansión Mínima (MST).
    def kruskal(self, origin_vertex):
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index

        # forest: lista de conjuntos (bosque disjunto)
        forest = []
        # edges: heap min con todas las aristas ordenadas por peso
        edges = HeapMin()

        for vertex in self:
            # Cada vértice es un árbol independiente.
            forest.append(vertex.value)
            for edge in vertex.edges:
                # Carga todas las aristas en el heap.
                edges.arrive([vertex.value, edge.value], edge.weight)

        # Extrae la arista más barata
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            # Si une dos árboles distintos entonces la une
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')

        from_vertex = search_in_forest(forest, origin_vertex)

        # Al final, devuelve la parte del MST que contiene origin_vertex
        return forest[from_vertex] if from_vertex is not None else forest
