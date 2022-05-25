import random


class Dice:
    def __init__(self, game_type):
        self.game_type = game_type

    def roll(self):
        if self.game_type == 0:
            return random.randint(1, 6) + random.randint(1, 6)
        return 0
