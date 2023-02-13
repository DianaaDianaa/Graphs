from file_repo import TextFileRepository
from undirected_file_repo import UndirectedTextFileRepository
from repo import Repository


class UI:
    def __init__(self, file_name, undirected_file_name):
        self._file_name = file_name
        self._undirected_file_name = undirected_file_name
        self._repo = Repository()

    def menu(self):
        print("1: Display the graph.")
        print("2: Given two vertices, find out whether there is an edge from the first one to the second one.")
        print("3: Get the in degree and the out degree of a specified vertex.")
        print("4: Read a graph.")
        print("5: Add an edge.")
        print("6: Remove an edge.")
        print("7: Add a vertex.")
        print("8: Remove a vertex.")
        print("9: Change the cost of an edge.")
        print("10: Make a copy of the graph.")
        print("11: Generate a random graph of 7 vertices and 20 edges.")
        print("12: Generate a random graph of 6 vertices and 40 edges.")
        print("13: Find the connected components of an undirected graph using a breadth-first traversal of the graph.")
        print("14: Find the lowest cost walk between two given vertices.")
        print("15: Given an undirected graph, find a Hamiltonian cycle.")
        print("0: exit")

    def main(self):
        self._repo.graph.din, self._repo.graph.dout, self._repo.graph.dcosts = TextFileRepository(
                self._file_name).load_graph()
        self._repo.undirected_graph.nout, self._repo.undirected_graph.edges = UndirectedTextFileRepository(
            self._undirected_file_name).load_graph()
        while True:
            self.menu()
            option = input("Enter option: ")
            try:
                if option == "1":
                    print(self._repo.graph)
                elif option == "2":
                    vertex1 = int(input("1st vertex: "))
                    vertex2 = int(input("2nd vertex: "))
                    if self._repo.is_edge(vertex1, vertex2):
                        print("There IS an edge from the first one to the second one.")
                    else:
                        print("There ISN'T any edge from the first one to the second one.")
                elif option == "3":
                    vertex = int(input("vertex: "))
                    in_degree, out_degree = self._repo.in_out_degree(vertex)
                    print("in degree: ", in_degree, " out degree: ", out_degree)
                elif option == "4":
                    vertices_number = int(input("number of vertices: "))
                    edges_number = int(input("number of edges: "))
                    edges_list = []
                    for i in range(edges_number):
                        print("edge", i + 1, "and the cost: ")
                        vertex1 = int(input("vertex1: "))
                        vertex2 = int(input("vertex2: "))
                        cost = int(input("cost: "))
                        if vertex1 < 0 or vertex1 >= vertices_number or vertex2 < 0 or vertex2 >= vertices_number or \
                                cost < 0:
                            raise KeyError("Vertex not in range or invalid cost.")
                        edges_list.append([vertex1, vertex2, cost])
                    self._repo.read_graph(vertices_number, edges_number, edges_list)
                elif option == "5":
                    vertex1 = int(input("vertex1: "))
                    vertex2 = int(input("vertex2: "))
                    cost = int(input("cost: "))
                    self._repo.add_edge(vertex1, vertex2, cost)
                elif option == "6":
                    print("the edge's vertices:")
                    vertex1 = int(input("vertex1: "))
                    vertex2 = int(input("vertex2: "))
                    self._repo.remove_edge(vertex1, vertex2)
                elif option == "7":
                    self._repo.add_vertex()
                elif option == "8":
                    vertex = int(input("vertex: "))
                    self._repo.remove_vertex(vertex)
                elif option == "9":
                    print("the edge's vertices:")
                    vertex1 = int(input("vertex1: "))
                    vertex2 = int(input("vertex2: "))
                    new_cost = int(input("new cost: "))
                    self._repo.change_cost(vertex1, vertex2, new_cost)
                elif option == "10":
                    self._repo.copy_graph()
                    print("Graph successfully copied!")
                elif option == "11":
                    self._repo.generate_random_graph(7, 20)
                    TextFileRepository("random_graph1.txt").save_file(self._repo.random_graph.din,
                                                                      self._repo.random_graph.dcosts)
                elif option == "12":
                    self._repo.generate_random_graph(6, 40)
                    TextFileRepository("random_graph2.txt").save_file(self._repo.random_graph.din,
                                                                      self._repo.random_graph.dcosts)
                elif option == "13":
                    connected_components = self._repo.connected_components()
                    print("The connected components are:")
                    i = 1
                    for connected_component in connected_components:
                        print("Component", i, "is:", connected_component)
                        i += 1
                elif option == "14":
                    source = int(input("source vertex: "))
                    dest = int(input("destination vertex: "))
                    dist, successors = self._repo.backwards_Dijkstra(source, dest)
                    if dist == -1:
                        print("There is no walk!")
                    else:
                        min_cost_path = self._repo.min_cost_path(successors, source, dest)
                        print("The minimum cost path between", source, "and", dest, "is:", min_cost_path)
                        print("The minimum cost is:", dist[source])
                elif option == "15":
                    if self._repo.find_hamiltonian_cycle() == -1:
                        print("There is no Hamiltonian cycle.")
                    else:
                        print("The following connected component has a Hamiltonian cycle:")
                        print(self._repo.find_hamiltonian_cycle())
                elif option == "0":
                    return
            except Exception as e:
                print(e)
            TextFileRepository(self._file_name).save_file(self._repo.graph.din, self._repo.graph.dcosts)


x = UI("graph10k.txt", "undirected_graph1.txt")
x.main()
