class DirectedGraph:
    def __init__(self, din, dout, dcosts):
        self._din = din
        self._dout = dout
        self._dcosts = dcosts

    @property
    def din(self):
        return self._din

    @property
    def dout(self):
        return self._dout

    @property
    def dcosts(self):
        return self._dcosts

    @din.setter
    def din(self, value):
        self._din = value

    @dout.setter
    def dout(self, value):
        self._dout = value

    @dcosts.setter
    def dcosts(self, value):
        self._dcosts = value

    def __str__(self):
        return "din: " + str(self.din) + "\ndout: " + str(self.dout) + "\ndcosts: " + str(self.dcosts)
