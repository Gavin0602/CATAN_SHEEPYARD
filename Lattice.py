class Lattice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sign = (x, y)
        self.num = 0
        self.resource = "None"
        self.isRobbed = False

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "] (" + str(self.num) + ", " + self.resource + ")"

    def set_number(self, num):
        self.num = num

    def set_resource(self, res):
        self.resource = res
