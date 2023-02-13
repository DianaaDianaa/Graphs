class TextFileRepository:
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

    def save_file(self, din, dcosts):
        f = open(self._file_name, "wt")
        f.write(str(len(din)) + " " + str(len(dcosts)) + " " + '\n')
        for pair in dcosts.items():
            f.write(str(pair[0][0]) + " " + str(pair[0][1]) + " " + str(pair[1]) + '\n')
        f.close()

    def load_graph(self):
        f = open(self._file_name, "rt")
        din = {}
        dout = {}
        dcosts = {}
        line = f.readline().split()
        nr_of_vertices = int(line[0])
        nr_of_edges = int(line[1])
        for k in range(nr_of_vertices):
            din[k] = []
            dout[k] = []
        for k in range(nr_of_edges):
            line = f.readline().split()
            a = int(line[0])
            b = int(line[1])
            c = int(line[2])
            dcosts[(a, b)] = c
            it_exists = 0
            for i in dout[a]:
                if i == b:
                    it_exists = 1
            if it_exists == 0:
                dout[a].append(b)
            else:
                it_exists = 0
            for i in din[b]:
                if a == i:
                    it_exists = 1
            if it_exists == 0:
                din[b].append(a)
        f.close()
        return din, dout, dcosts
