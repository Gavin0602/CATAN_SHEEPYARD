class Intersection:
    def __init__(self, pos, num):
        # pos (lattice, num)
        self.positions = [(pos, num)]
        self.adjacent = [pos[0]]

    def merge(self, other):
        for pos in other.positions:
            self.positions.append(pos)
