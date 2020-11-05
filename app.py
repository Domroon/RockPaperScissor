import random
import time


class Game:
    def __init__(self, user, computer):
        self.user = user
        self.computer = computer

    def startcreen(self):
        print("Welcome to the Game \"Rock , Paper or Scissor!\"")
        self.user.name = input("Name: ")
        print(f"Hello {self.user.name}! Lets start the Game!")

    def round(self):
        # user and computer take their choices
        while True:
            try:
                self.user.choice = input("Please take your choice: ")
                break
            except ValueError as error:
                print(error)
        self.computer.make_choice()
        self.round_animation()
        print(f"{self.user.choice} against {self.computer.choice}")
        winner = self.get_winner()
        if winner is None:
            print("Undecided!")
        else:
            winner.add_point()
            if winner is self.user:
                print("You win!")
            else:
                print("You loose!")
        print(f"User score: {self.user.score}")
        print(f"computer score: {self.computer.score}")

    def round_animation(self):
        speed = 0.5
        time.sleep(speed)
        print("Rock!")
        time.sleep(speed)
        print("Paper!")
        time.sleep(speed)
        print("Scissor!")
        time.sleep(speed)

    def get_winner(self):
        choice_user = self.user.choice
        choice_computer = self.computer.choice
        if choice_user == "rock":
            if choice_computer == "paper":
                return self.computer
            elif choice_computer == "scissor":
                return self.user
            else:
                return None
        elif choice_user == "paper":
            if choice_computer == "scissor":
                return self.computer
            elif choice_computer == "rock":
                return self.user
            else:
                return None
        elif choice_user == "scissor":
            if choice_computer == "rock":
                return self.computer
            elif choice_computer == "paper":
                return self.user
            else:
                return None
        else:
            raise ValueError()


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


class Computer:
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


def main():
    user = User("Nobody")
    computer = Computer()
    game = Game(user, computer)
    max_score = 3

    game.startcreen()

    while True:
        game.round()
        if user.score == 3 or computer.score == 3:
            break
    print("Thank you for gaming!")


if __name__ == '__main__':
    main()
