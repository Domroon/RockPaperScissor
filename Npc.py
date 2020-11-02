import random

class Npc:
    def __init__(self):
        self.score = 0
        self.choice = [
            "rock",
            "paper",
            "scissor"
        ]

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_choice(self):
        return self.choice[random.randint(0, 2)]
