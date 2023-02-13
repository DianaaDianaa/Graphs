class UndirectedTextFileRepository:
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def length(self):
        f = open(self._file_name, "rt")
        length = 0
        for line in f.readlines():
            length = length + 1
        f.close()
        return length

    def save_file(self, nout, edges):
        f = open(self._file_name, "wt")
        f.write(str(len(nout)) + " " + str(edges) + " " + '\n')
        for pair in nout.items():
            for i in range(len(pair[1])):
                if pair[0] < pair[1][i]:
                    f.write(str(pair[0]) + " " + str(pair[1][i]) + '\n')
        f.close()

    def load_graph(self):
        f = open(self._file_name, "rt")
        nout = {}
        line = f.readline().split()
        nr_of_vertices = int(line[0])
        nr_of_edges = int(line[1])
        for k in range(nr_of_vertices):
            nout[k] = []
        for k in range(nr_of_edges):
            line = f.readline().split()
            a = int(line[0])
            b = int(line[1])
            nout[a].append(b)
            nout[b].append(a)
        f.close()
        return nout, nr_of_edges

#d = {0 : [1], 1: [0,2], 2: [1], 3: [4], 4: [3], 5: []}
