from Edge import *
from Vertex import *
from Lattice import *
import random


class Map:
    def __init__(self, size, map_type):
        self.map_type = map_type
        self.size = size

        # {(x, y) : Lattice}
        self.grid = self.generate_grid()

        # {(x, y, n) : Vertex}
        self.vertices = self.generate_vertices()
        self.join_vertices()

        # {(vertex1_sign, vertex2_sign) : Edge}
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
            lattice = grid[pos]
            resource = res_list[r]
            lattice.set_resource(resource)
            r += 1
            if resource != "SAND":
                lattice.set_number(num_list[n])
                n += 1

    def generate_numbers(self):
        if self.map_type == 0:
            result = []
            total = self.get_total_lattice() - 2
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
            total = self.get_total_lattice() - 2
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

    def get_total_lattice(self):
        radius = self.size - 1
        total = radius * 2 + 1
        for i in range(radius):
            total += (self.size + i) * 2
        return total

    def get_total_edges(self):
        total = 0
        d = self.size * 2 - 1
        for i in range(self.size, d + 1):
            total += 3 * i + 1
        return total * 2 - d - 1

    def generate_vertices(self):
        result = {}
        for key in self.grid:
            for n in range(6):
                vertex = Vertex(key, n)
                result[vertex.sign] = vertex
        return result

    def join_vertices(self):
        vertices = self.vertices
        for key in vertices:
            if key[2] == 0:
                if key[1] >= 0 and (key[0], key[1] + 1) in self.grid:
                    vertices[(key[0], key[1] + 1, 4)].join(vertices[key])
                elif key[1] < 0 and (key[0] + 1, key[1] + 1) in self.grid:
                    vertices[(key[0] + 1, key[1] + 1, 4)].join(vertices[key])

            elif key[2] == 1:
                if key[1] >= 0:
                    if (key[0], key[1] + 1) in self.grid:
                        vertices[(key[0], key[1] + 1, 3)].join(vertices[key])
                    elif (key[0] + 1, key[1]) in self.grid:
                        vertices[(key[0] + 1, key[1], 5)].join(vertices[key])

                elif key[1] < 0 and (key[0] + 1, key[1] + 1) in self.grid:
                    vertices[(key[0] + 1, key[1] + 1, 3)].join(vertices[key])

            elif key[2] == 2:
                if key[1] > 0 and (key[0] + 1, key[1] - 1) in self.grid:
                    vertices[(key[0] + 1, key[1] - 1, 0)].join(vertices[key])

                elif key[1] <= 0:
                    if (key[0], key[1] - 1) in self.grid:
                        vertices[(key[0], key[1] - 1, 0)].join(vertices[key])
                    elif (key[0] + 1, key[1]) in self.grid:
                        vertices[(key[0] + 1, key[1], 4)].join(vertices[key])

            elif key[2] == 3:
                if key[1] > 0 and (key[0] + 1, key[1] - 1) in self.grid:
                    vertices[(key[0] + 1, key[1] - 1, 5)].join(vertices[key])
                elif key[1] <= 0 and (key[0], key[1] - 1) in self.grid:
                    vertices[(key[0], key[1] - 1, 5)].join(vertices[key])

    def generate_edges(self):
        result = {}
        for key in self.grid:
            for n in range(6):
                sign1 = (key[0], key[1], n)
                sign2 = (key[0], key[1], (n + 1) % 6)
                vertex1 = self.vertices[sign1].find_root_sign()
                vertex2 = self.vertices[sign2].find_root_sign()

                if (vertex1, vertex2) in result or (vertex2, vertex1) in result:
                    continue

                result[(vertex1, vertex2)] = Edge(self.vertices[vertex1], self.vertices[vertex2])

        return result

    def get_resources(self, vertex: Vertex):
        result = []
        root_sign = vertex.find_root_sign()
        for sign in self.vertices:
            v = self.vertices[sign]
            root = v.find_root_sign()
            if root == root_sign:
                resource = self.grid[v.lattice].resource
                if resource != "SAND":
                    result.append(resource)
        return result
