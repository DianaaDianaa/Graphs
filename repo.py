from DirectedGraph import DirectedGraph
from random import randint
from UndirectedGraph import UndirectedGraph

class Repository:
    def __init__(self, din={}, dout={}, dcosts={}, nout={}, undirected_edges = 0):
        self._graph = DirectedGraph(din, dout, dcosts)
        self._random_graph = DirectedGraph(din, dout, dcosts)
        self._graph_copy = DirectedGraph(din, dout, dcosts)
        self._vertices_index = 0
        self._outbound_edge_index = 0
        self._inbound_edge_index = 0
        self._undirected_graph = UndirectedGraph(nout, undirected_edges)

    @property
    def graph(self):
        return self._graph

    @property
    def undirected_graph(self):
        return self._undirected_graph

    @property
    def random_graph(self):
        return self._random_graph

    @property
    def vertices_index(self):
        return self._vertices_index

    @property
    def outbound_edge_index(self):
        return self._outbound_edge_index

    @property
    def inbound_edge_index(self):
        return self._inbound_edge_index

    def is_vertex(self, vertex):
        if vertex not in range(0,len(self.graph.din)):
            return 0
        if vertex not in self.graph.din.keys():
            return 0
        return 1

    def is_edge(self, vertex1, vertex2):
        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise KeyError("Vertex not in range.")
        for vertex in self.graph.dout[vertex1]:
            if vertex == vertex2:
                return True
        return False

    def is_random_edge(self, vertex1, vertex2):
        if vertex1 not in range(0,len(self.random_graph.din)) or vertex2 not in range(0,len(self.random_graph.din)):
            raise KeyError("Vertex not in range.")
        for vertex in self.random_graph.dout[vertex1]:
            if vertex == vertex2:
                return True
        return False

    def in_out_degree(self, vertex):
        if not self.is_vertex(vertex):
            raise KeyError("Vertex not in range.")
        return len(self.graph.din[vertex]), len(self.graph.dout[vertex])

    def read_graph(self, vertices_number, edges_number, edges_list):
        if vertices_number*vertices_number > edges_number:
            raise KeyError("Too many edges for the given number of vertices.")
        self._graph.din = {}
        self._graph.dout = {}
        self._graph.dcosts = {}
        for i in range(vertices_number):
            self._graph.din[i] = []
            self._graph.dout[i] = []
        for i in range(edges_number):
            vertex1 = edges_list[i][0]
            vertex2 = edges_list[i][1]
            cost = edges_list[i][2]
            self._graph.din[vertex2].append(vertex1)
            self._graph.dout[vertex1].append(vertex2)
            self._graph.dcosts[(vertex1, vertex2)] = cost

    def add_edge(self, vertex1, vertex2, cost):
        if vertex1 < 0 or vertex1 >= len(self.graph.din) or vertex2 < 0 or vertex2 >= len(self.graph.din):
            raise KeyError("Vertex not in range.")
        if self.is_edge(vertex1, vertex2):
            raise KeyError("There already is such an edge!")
        self._graph.din[vertex2].append(vertex1)
        self._graph.dout[vertex1].append(vertex2)
        self._graph.dcosts[(vertex1, vertex2)] = cost

    def remove_edge(self, vertex1, vertex2):
        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise KeyError("Vertex not in range.")
        if not self.is_edge(vertex1, vertex2):
            raise KeyError("There is no such edge!")
        self._graph.dcosts.pop((vertex1, vertex2))
        self._graph.din[vertex2].pop(self._graph.din[vertex2].index(vertex1))
        self._graph.dout[vertex1].pop(self._graph.dout[vertex1].index(vertex2))

    def add_vertex(self):
        self._graph.din[len(self.graph.din)] = []
        self._graph.dout[len(self.graph.dout)] = []

    def remove_vertex(self, vertex):
        if not self.is_vertex(vertex):
            raise KeyError("Vertex not in range.")
        for v in self.graph.dout[vertex]:
            self.graph.din[v].remove(vertex)
            del self.graph.dcosts[(vertex, v)]
        for v in self.graph.din[vertex]:
            self.graph.dout[v].remove(vertex)
            del self.graph.dcosts[(v,vertex)]
        del self.graph.din[vertex]
        del self.graph.dout[vertex]

    def change_cost(self, vertex1, vertex2, cost):
        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise KeyError("Vertex not in range.")
        if not self.is_edge(vertex1, vertex2):
            raise KeyError("There is no such edge!")
        self._graph.dcosts[(vertex1, vertex2)] = cost

    def generate_random_graph(self, vertices_number, edges_number):
        if vertices_number*vertices_number < edges_number:
            raise KeyError("Too many edges for the given number of vertices.")
        self._random_graph.din = {}
        self._random_graph.dout = {}
        self._random_graph.dcosts = {}
        for i in range(vertices_number):
            self._random_graph.din[i] = []
            self._random_graph.dout[i] = []
        for i in range(edges_number):
            vertex1 = randint(0,vertices_number-1)
            vertex2 = randint(0,vertices_number-1)
            while self.is_random_edge(vertex1, vertex2):
                vertex1 = randint(0, vertices_number-1)
                vertex2 = randint(0, vertices_number-1)
            cost = randint(1,100)
            self._random_graph.din[vertex2].append(vertex1)
            self._random_graph.dout[vertex1].append(vertex2)
            self._random_graph.dcosts[(vertex1, vertex2)] = cost

    def copy_graph(self):
        self._graph_copy.din = self.graph.din
        self._graph_copy.dout = self.graph.dout
        self._graph_copy.dcosts = self.graph.dcosts

    def get_the_number_of_vertices(self):
        return len(self.graph.din)

    def valid_vertex_index(self):
        if self.vertices_index < len(self.graph.din):
            return True
        self._vertices_index = 0
        return False

    def valid_outbound_edge_index(self):
        if self.outbound_edge_index < len(self.graph.dout):
            return True
        self._outbound_edge_index = 0
        return False

    def valid_inbound_edge_index(self):
        if self.inbound_edge_index < len(self.graph.din):
            return True
        self._inbound_edge_index = 0
        return False

    def next_vertex(self):
        if self.valid_vertex_index():
            self._vertices_index += 1
            return self.graph.din[self.vertices_index]
        return False

    def next_outbound_edge(self, vertex):
        if self.valid_outbound_edge_index():
            self._outbound_edge_index += 1
            return self.graph.dout[vertex][self._outbound_edge_index]
        return False

    def next_inbound_edge(self, vertex):
        if self.valid_inbound_edge_index():
            self._inbound_edge_index += 1
            return self.graph.din[vertex][self._inbound_edge_index]
        return False

    def bfs(self, graph, node):
        """
        It is a breadth-first search function.
        :param graph: the undirected graph
        :param node: the node whose accessible nodes are looked for
        :return: visited (the list with the accessible nodes to the given node)
        """
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        while queue:
            s = queue.pop(0)
            for neighbour in graph.nout[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def connected_components(self):
        """
        Finds the connected components of an undirected graph.
        :return: the list of connected components
        """
        #create the list of the vertices of the undirected graph
        vertices = [i for i in range(len(self.undirected_graph.nout))]
        #the list of the connected components
        connected_components = []
        while vertices:
            #find the accessible vertices to the current vertex
            accessible = self.bfs(self.undirected_graph, vertices[0])
            #create the undirected graph of the last connected component and then add it to the connected components list
            nout = {}
            accessible.sort()
            for i in accessible:
                nout[i] = self.undirected_graph.nout[i]
            connected_component = UndirectedGraph(nout, len(nout))
            connected_components.append(connected_component)
            #we don't need to look for the vertices that are already found accessible
            for i in accessible:
                vertices.remove(i)

        return connected_components

    def backwards_Dijkstra(self, source, dest):
        if not self.is_vertex(source) or not self.is_vertex(dest):
            raise KeyError("Vertex not in range.")
        dist = {} #a map which associates, to each accessible vertex, the cost of the minimum cost walk from dest to i
        successor = {} #a map which maps each accessible vertex to its successor on a path from dest to i
        PriorityQueue = [(dest, 0)]
        dist[dest] = 0
        found = False
        while len(PriorityQueue) > 0:
            #deque the element with the minimum value of priority
            x = PriorityQueue[0][0]
            PriorityQueue.pop(0)
            for y in self.graph.din[x]:
                if y not in dist.keys() or dist[x] + self.graph.dcosts[(y,x)] < dist[y]:
                    dist[y] = dist[x] + self.graph.dcosts[(y,x)]
                    PriorityQueue.append((y, dist[y]))
                    successor[y] = x
            if x == source:
                found = True
        if found:
            return dist, successor
        return -1

    def min_cost_path(self, successors, source, dest):
        #it returns the minimum cost path
        min_cost_path = [source]
        y = source
        x = successors[y]
        min_cost_path.append(x)
        while x != dest:
            y = x
            x = successors[y]
            min_cost_path.append(x)
        min_cost_path.sort()
        return min_cost_path

    def has_hamiltonian_cycle(self, graph):
        #it checks whether an undirected graph is hamiltonian or not
        #A simple graph with n vertices in which the sum of the degrees
        #of any two non-adjacent vertices is greater than or equal to n has a Hamiltonian cycle.
        n = len(graph.nout.keys())
        #creating the dictionary with the degrees of each node
        d = {}
        for i in graph.nout.keys():
            d[i] = len(graph.nout[i])
        for i in graph.nout.keys():
            for j in graph.nout.keys():
                #if two non-adjacent vertices have the sum of the degrees less than n => no hamiltonian cycle
                if i!=j and j not in graph.nout[i]:
                    if d[i] + d[j] < n:
                        return False
        return True

    def find_hamiltonian_cycle(self):
        #it returns a hamiltonian cycle if it exists
        connected_components = self.connected_components()
        for c in connected_components:
            if self.has_hamiltonian_cycle(c):
                return c
        return -1


