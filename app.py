import random
import time

POSSIBLE_MOVES = ["rock", "paper", "scissor"]
MAX_SCORE = 3
SPECIAL_CHARACTER = ["!§$%&/()=?{[]}-_<>|´`"]
NUMBER_CHARACTER = ["0123456789"]
UPPER_CASE = ["ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖ"]
LOWER_CASE = ["abcdefghijklmnopqrstuvwxyzäöß"]
PASSWORD_LENGTH = 8


class Game:
    def __init__(self, user, computer):
        self.user = user
        self.computer = computer

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
        self._password = None
        self._choice = "nothing"

    def add_point(self):
        self.score += 1

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, move):
        if move not in POSSIBLE_MOVES:
            raise ValueError(f'You can choose between {" / ".join(POSSIBLE_MOVES)}')
        self._choice = move

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # password needs:
        # letter in upper and lower case
        # at least one special sign
        # at least one number
        if len(password) >= 8:
            self._password = password
        else:
            raise ValueError("Password needs at least 8 character")


class Computer:
    def __init__(self):
        self.score = 0
        self.choice = "nothing"

    def add_point(self):
        self.score = self.score + 1

    def make_choice(self):
        self.choice = random.choice(POSSIBLE_MOVES)


def test():
    user = User("Max")
    try:
        user.password = "asdf"
    except ValueError as err:
        print(err)

    if user.password is None:
        print("User password is incorrect")
    else:
        print("You can use this password")


def main():
    test()
    '''
    print('Welcome to the Game "Rock, Paper or Scissor!"')
    name = input("Name: ")
    print(f"Hello {name}! Lets start the Game!")
    user = User(name)
    computer = Computer()
    game = Game(user, computer)
    while user.score < MAX_SCORE and computer.score < MAX_SCORE:
        game.round()
    print("Thank you for gaming!")
    '''

if __name__ == '__main__':
    main()
