class User:

    def __init__(self, name):
        self.score = 0
        self.name = name
        self.choice = "nothing"
        self.have_win = False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_score(self):
        return self.score

    def set_one_point(self):
        self.score = self.score + 1

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
            print("You can choose between \"rock\", \"paper\" or \"scissor\"")

    def get_choice(self):
        return self.choice

    def set_have_win(self, result):
        self.have_win = result

    def get_have_win(self):
        return self.have_win
