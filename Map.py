from Edge import *
from Vertex import *
from Lattice import *
import random


class Map:
    def __init__(self, size, map_type):
        self.map_type = map_type
        self.size = size
        self.grid = self.generate_grid()
        self.vertices = self.generate_vertices()
        self.edges = self.generate_edges()
        self.generate_map()

    def __str__(self):
        result = ""
        for key in self.grid:
            result += str(self.grid[key]) + "\n"
        return result

    def generate_map(self):
        num_list = self.generate_numbers()
        res_list = self.generate_resources()
        grid = self.grid

        r = 0
        n = 0
        # fill in resources and numbers
        for pos in grid:
            resource = res_list[r]
            grid[pos].resources = resource
            r += 1
            if resource != "SAND":
                grid[pos].num = num_list[n]
                n += 1

    def generate_numbers(self):
        if self.map_type == 0:
            result = []
            total = self.get_total() - 2
            each = total // 10
            remain = total % 10
            for i in range(2, 13):
                if i == 7:
                    continue
                result += [i] * each

            for i in range(remain):
                num = random.randint(2, 12)
                while num == 7:
                    num = random.randint(2, 12)
                result.append(num)

            random.shuffle(result)
            return result
        return []

    def generate_resources(self):
        if self.map_type == 0:
            result = []
            total = self.get_total() - 2
            each = total // 5
            remain = total % 5
            res_list = ["CLAY", "ORE", "WHEAT", "SHEEP", "WOOD"]
            result += ["CLAY"] * each
            result += ["ORE"] * each
            result += ["WHEAT"] * each
            result += ["SHEEP"] * each
            result += ["WOOD"] * each
            result += ["SAND"] * 2

            for i in range(remain):
                result.append(random.choice(res_list))

            random.shuffle(result)
            return result

        return []

    def generate_grid(self):
        d = self.size * 2 - 1
        grid = {}
        for y in range(self.size):
            if y == 0:
                for x in range(d):
                    grid[(x, y)] = Lattice(x, y)
                continue

            for x in range(d - y):
                grid[(x, y)] = Lattice(x, y)
                grid[(x, -y)] = Lattice(x, -y)

        return grid

    def get_total(self):
        radius = self.size - 1
        total = radius * 2 + 1
        for i in range(radius):
            total += (self.size + i) * 2
        return total

    def generate_vertices(self):
        result = {}
        for key in self.grid:
            for n in range(6):
                vertex = Vertex(key, n)
                result[vertex.sign] = vertex
        return result

    def join_vertices(self):

        return

    def generate_edges(self):
        result = {}
        for key in self.grid:
            for n in range(6):
                sign1 = (key[0], key[1], n)
                sign2 = (key[0], key[1], (n + 1) % 6)
                vertex1 = self.vertices[sign1].find_root()
                vertex2 = self.vertices[sign2].find_root()

                if (vertex1, vertex2) in result or (vertex2, vertex1) in result:
                    continue

                result[(vertex1, vertex2)] = Edge(self.vertices[vertex1], self.vertices[vertex2])

        return result



