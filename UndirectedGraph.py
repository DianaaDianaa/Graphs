class UndirectedGraph:
    def __init__(self, nout, edges=0):
        self._nout = nout
        self._edges = edges

    @property
    def nout(self):
        return self._nout

    @property
    def edges(self):
        return self._edges

    @nout.setter
    def nout(self, value):
        self._nout = value

    @edges.setter
    def edges(self, value):
        self._edges = value

    def __str__(self):
        return str(self.nout)
