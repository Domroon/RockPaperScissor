import random

class Npc:
    def __init__(self):
        self._score = 0
        self.move = [
            "rock",
            "paper",
            "scissor"
        ]
        self._choice = "nothing"

    @property
    def score(self):
        return self._score

    def add_point(self):
        self._score = self.score + 1

    def make_choice(self):
        self._choice = self.move[random.randint(0, 2)]

    @property
    def choice(self):
        return self._choice
