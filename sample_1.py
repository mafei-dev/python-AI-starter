import numpy
from numpy import array


class Vertex:
    index: int = 0
    __t_data = None

    def __init__(self, pass_data) -> None:
        self.__t_data = pass_data
        self.index = -1

    def get_data(self) -> array:
        return self.__t_data

    def __str__(self) -> str:
        # print(f"data {self.__t_data}")
        return f"data {self.__t_data}";

    def get_index(self) -> int:
        return self.index

    def set_index(self, index: int) -> None:
        self.index = index


class AdjacencyMatrix:
    __matrix: array = None
    __size: int = 0

    def __init__(self, size: int) -> None:
        self.__matrix = numpy.zeros(shape=(size, size), dtype='int')
        self.__size = size

    def add_directed_edge(self, from_i: int, to_i: int, weight) -> None:
        self.__matrix[from_i, to_i] = weight

    def add_undirected_edge(self, v1: int, v2: int, weight) -> None:
        self.__matrix[v1, v2] = weight
        self.__matrix[v2, v1] = weight
        # print(self.__matrix)

    def get_edge_weight(self, x: int, y: int) -> array:
        return self.__matrix[x, y]

    def get_adjacency_list(self, sources_index: int):
        adjacency_list = []
        for i in range(self.__size):
            if self.__matrix[sources_index, i] != 0:
                adjacency_list.append(i)
        return adjacency_list


class Graph:
    __vertexes = []
    __adjacency_matrix: AdjacencyMatrix

    def __init__(self, vertexes: []) -> None:
        self.__vertexes = vertexes
        for i in range(len(vertexes)):
            self.__vertexes[i].set_index(i)

        self.__adjacency_matrix = AdjacencyMatrix(len(self.__vertexes))

    def get_vertexes(self):
        return self.__vertexes

    def create_directed_edge(self, from_index: int, to_index: int, weight) -> None:
        self.__adjacency_matrix.add_directed_edge(from_index, to_index, weight)

    def create_directed_edge_with_object(self, from_index: Vertex, to_index: Vertex, weight=1) -> None:
        self.create_directed_edge(from_index.get_index(), to_index.get_index(), weight)

    def create_undirected_edge(self, v1: int, v2: int, weight=1):
        self.__adjacency_matrix.add_undirected_edge(v1, v2, weight)

    def create_undirected_edge_with_object(self, v1: Vertex, v2: Vertex, weight=1):
        self.create_undirected_edge(v1.get_index(), v2.get_index(), weight)

    def get_adjacency_vertices(self, source_index: int):
        adjacent_indices = self.__adjacency_matrix.get_adjacency_list(source_index)
        adjacent_vertices = []
        for vertex_index in adjacent_indices:
            adjacent_vertices.append(self.__vertexes[vertex_index])
        return adjacent_vertices

    def get_adjacency_vertices_with_object(self, source: Vertex):
        return self.get_adjacency_vertices(source.get_index())

    def get_edge_weight(self, v1: Vertex, v2: Vertex):
        return self.__adjacency_matrix.get_edge_weight(v1.get_index(), v2.get_index())

    def __str__(self) -> str:
        lines: str = "Graph:"
        for vertex in self.__vertexes:
            lines += vertex.get_data().__str__()
            lines += "\n"
            adjacent_vertices = self.get_adjacency_vertices_with_object(vertex)
            if len(adjacent_vertices) > 0:
                lines += "Edge to: "
                for adj_vertex in adjacent_vertices:
                    lines += adj_vertex.get_data().__str__()
                    lines += "(w="
                    lines += f"{self.get_edge_weight(vertex, adj_vertex)}"
                    lines += ")"
            else:
                lines += "No outgoing edges"
            lines += "\n"
        return lines


v1 = Vertex("v1")
v2 = Vertex("v2")
v3 = Vertex("v3")
v4 = Vertex("v4")
vertices = [v1, v2, v3, v4]
graph = Graph(vertices)
graph.create_directed_edge_with_object(v1, v2, 3)
graph.create_directed_edge_with_object(v4, v1, 1)
graph.create_directed_edge_with_object(v2, v3, 1)
graph.create_directed_edge_with_object(v2, v4, -5)
print(graph.__str__())
