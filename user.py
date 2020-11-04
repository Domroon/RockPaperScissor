class User:

    def __init__(self, name):
        self.score = 0
        self.name = name
        self._choice = "nothing"
        self.have_win = False

    def add_point(self):
        self.score = self.score + 1

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, move):
        if move not in ["rock", "paper", "scissor"]:
            raise ValueError('You can choose between "rock", "paper" or "scissor"')
        self._choice = move
