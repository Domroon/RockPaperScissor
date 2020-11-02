class User:

    def __init__(self, name):
        self.score = 0
        self.name = name
        self.choice = "nothing"

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def set_choice(self, move):
        try:
            if move == "rock":
                self.choice = move
            elif move == "paper":
                self.choice = move
            elif move == "scissor":
                self.choice = move
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input")

    def get_choice(self):
        return self.choice
