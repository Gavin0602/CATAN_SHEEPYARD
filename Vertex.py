class Vertex:
    def __init__(self, lattice, n):

        # (x, y)
        self.lattice = lattice
        self.n = n

        # (x, y, n)
        self.sign = (lattice[0], lattice[1], n)

        # (x, y, n)
        self.unionSign = self.sign

        # Vertex
        self.union = self

    def __str__(self):
        return str(self.sign) + "->" + str(self.union)

    def join(self, other):
        self.unionSign = other.sign
        self.union = other

    def find_root_vertex(self):
        if self.sign == self.unionSign:
            return self

        root = self.union
        while root.unionSign != root.sign:
            root = root.union
        return root

    def find_root_sign(self):
        return self.find_root_vertex().sign
