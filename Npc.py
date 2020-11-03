import random

class Npc:
    def __init__(self):
        self.score = 0
        self.move = [
            "rock",
            "paper",
            "scissor"
        ]
        self.choice = "nothing"

    def get_score(self):
        return self.score

    def set_one_point(self):
        self.score = self.score + 1

    def set_choice(self):
        self.choice = self.move[random.randint(0, 2)]

    def get_choice(self):
        return self.choice
