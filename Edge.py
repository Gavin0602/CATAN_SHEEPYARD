class Edge:
    def __init__(self, i1, i2):
        self.i1 = i1
        self.i2 = i2

    def __str__(self):
        return "[" + str(self.i1) + ", " + str(self.i2) + "]"
