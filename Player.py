class Player:
    def __init__(self, name):
        self.name = name
        self.vertices = []
        self.resources = []
        self.road = []
        self.house = []
        self.city = []

    def __str__(self):
        return self.name

    def information(self):
        result = "resources: " + str(self.resources) + "\nhouses: "
        for house in self.house:
            result += str(house) + " "
        result += "\nroads: "
        for edge in self.road:
            result += str(edge) + " "
        result += "\ncities: "
        for city in self.city:
            result += str(city) + " "
        return result

    def build_road(self, edge, others):
        if self.resources.count("CLAY") < 1 or self.resources.count("WOOD") < 1:
            print("not enough resources")
            return

        if edge.i1 not in self.vertices and edge.i2 not in self.vertices:
            print("no valid connection")
            return

        for other in others:
            if edge in other.road:
                print("already build by player:" + str(other))
                return

        self.resources.remove("CLAY")
        self.resources.remove("WOOD")
        self.road.append(edge)
        print("successful")

        if edge.i1 not in self.vertices:
            self.vertices.append(edge.i1)
        if edge.i2 not in self.vertices:
            self.vertices.append(edge.i2)

    def build_house(self, vertex, others):
        r = [self.resources.count("CLAY"), self.resources.count("SHEEP"), self.resources.count("WHEAT"),
             self.resources.count("WOOD")]
        if 0 in r:
            print("not enough resources")
            return

        vertex = vertex.find_root_vertex()
        for other in others:
            if vertex in other.vertices:
                print("conflict place, conflict to player: " + str(other))
                return

        if vertex not in self.vertices:
            print("no valid connection")
            return

        self.resources.remove("CLAY")
        self.resources.remove("SHEEP")
        self.resources.remove("WHEAT")
        self.resources.remove("WOOD")
        self.house.append(vertex)

        print("successful")

    def build_city(self, vertex):
        if self.resources.count("ORE") < 3 or self.resources.count("WHEAT") < 2:
            print("not enough resources")
            return

        if vertex not in self.house:
            print("no house exists")
            return

        self.resources.remove("WHEAT")
        self.resources.remove("WHEAT")
        self.resources.remove("ORE")
        self.resources.remove("ORE")
        self.resources.remove("ORE")
        self.house.remove(vertex)
        self.city.append(vertex)
        print("successful")

    def longest_road(self):
        result = []
        for vertex in self.vertices:
            result.append(self.bfs(vertex))
        return max(result)

    def bfs(self, vertex):
        visited = [vertex]
        next_vertex = []
        for edge in self.road:
            if edge.i1 == vertex and edge.i2 not in visited:
                next_vertex.append(edge.i2)
            elif edge.i2 == vertex and edge.i1 not in visited:
                next_vertex.append(edge.i1)

        length = 1
        while len(next_vertex) != 0:
            found_next = False
            temp = next_vertex[:]
            next_vertex = []
            for v in temp:
                visited.append(v)
                for edge in self.road:
                    if edge.i1 == v and edge.i2 not in visited:
                        next_vertex.append(edge.i2)
                        found_next = True
                    elif edge.i2 == v and edge.i1 not in visited:
                        next_vertex.append(edge.i1)
                        found_next = True
            if found_next:
                length += 1
        return length

    def get_point(self):
        return len(self.house) + len(self.city) * 2

    def add_resources(self, res, n):
        for i in range(n):
            self.resources.append(res)
