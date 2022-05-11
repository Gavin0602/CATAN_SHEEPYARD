class Lattice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.num = 0
        self.resources = "None"

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "] (" + str(
            self.num) + ", " + self.resources + ")"

    def set_number(self, num):
        self.num = num

    def set_resources(self, res):
        self.resources = res
