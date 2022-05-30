from Map import *
from Dice import *
from Player import *


class Game:
    def __init__(self, players: list[Player], m: Map, dice: Dice):
        self.map = m
        self.players = players
        self.turn = 0
        self.score_board = {}
        self.dice = dice
        for player in players:
            self.score_board[player] = 0

    def before_game(self, players):
        for player in players:
            print(player.name + "'s turn")
            vertex = self.select_vertex()
            while True:
                edge = self.select_road()
                if edge.i1 == vertex or edge.i2 == vertex:
                    break
                print("road did not connected to house")
            player.house.append(vertex)
            player.road.append(edge)
            if edge.i1 not in player.vertices:
                player.vertices.append(edge.i1)
            if edge.i2 not in player.vertices:
                player.vertices.append(edge.i2)
            player.resources += self.map.get_resources(vertex)

    def start(self):
        self.before_game(self.players)
        self.players.reverse()
        self.before_game(self.players)
        self.players.reverse()

        while True:
            player = self.players[self.turn % len(self.players)]
            others = self.players[:]
            others.remove(player)
            while True:
                print("1\tbuild house")
                print("2\tbuild road")
                print("3\tbuild city")
                print("0\tend turn")
                choice = input("Your choice: ")

                if choice == "1":
                    player.build_house(self.select_vertex(), others)

                elif choice == "2":
                    player.build_road(self.select_road(), others)

                elif choice == "3":
                    player.build_city(self.select_vertex())

                elif choice == "0":
                    break

            if self.end():
                break
            self.turn += 1

    def end(self):
        for player in self.score_board:
            self.score_board[player] = player.get_point()
        road_board = {}
        road_list = []
        for player in self.players:
            length = player.longest_road()
            road_board[player] = length
            road_list.append(length)
        longest = road_board[max(road_list)]
        longest_player = []
        for player in road_board:
            if road_board[player] == longest:
                longest_player.append(player)
        for player in longest_player:
            self.score_board[player] += 2
        for player in self.score_board:
            if self.score_board[player] >= 20:
                print(player.name + " win!")
                return True
        return False

    def no_man_vertex(self, vertex):
        for player in self.players:
            if vertex in player.house or vertex in player.city:
                print("vertex already selected by player " + player.name)
                return False
        return True

    def no_man_road(self, edge):
        for player in self.players:
            if edge in player.road:
                print("edge already selected by player " + player.name)
                return False
        return True

    def select_vertex(self):
        while True:
            vertex_sign = tuple(input("select vertex"))
            if vertex_sign in self.map.vertices:
                vertex = self.map.vertices[vertex_sign].find_root_vertex()
                if self.no_man_vertex(vertex):
                    return vertex
                continue

            print("vertex not in map")

    def select_road(self):
        while True:
            vertex1_sign = tuple(input("select vertex1"))
            vertex2_sign = tuple(input("select vertex2"))
            if vertex1_sign in self.map.vertices and vertex2_sign in self.map.vertices:
                vertex1 = self.map.vertices[vertex1_sign].find_root_vertex()
                vertex2 = self.map.vertices[vertex2_sign].find_root_vertex()
                e1 = (vertex1.sign, vertex2.sign)
                e2 = (vertex2.sign, vertex1.sign)
                if e1 in self.map.edges:
                    edge = self.map.edges[e1]
                    if self.no_man_road(edge):
                        return edge
                elif e2 in self.map.edges:
                    edge = self.map.edges[e2]
                    if self.no_man_road(edge):
                        return edge
                continue

            print("edge not in map")
