from DrawMap import *
from Game import *


MAP_SIZE = 4
GAME_TYPE = 0


MAP = Map(MAP_SIZE, GAME_TYPE)
DICE = Dice(GAME_TYPE)
PLAYER1 = Player("player1")
PLAYER2 = Player("player2")
# PLAYER3 = Player("player3")
# PLAYER4 = Player("player4")
PLAYERS = [PLAYER1, PLAYER2]

GAME = Game(PLAYERS, MAP, DICE)
GAME.start()
