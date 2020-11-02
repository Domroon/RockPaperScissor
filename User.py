class User:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
