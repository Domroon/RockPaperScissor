import random
import time

POSSIBLE_MOVES = ["rock", "paper", "scissor"]
MAX_SCORE = 3
SPECIAL_CHARACTER = "!§$%&/()=?{[]}-_<>|´`"
NUMBER_CHARACTER = "0123456789"
UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyzäöüß"
PASSWORD_LENGTH = 8


class Game:
    def __init__(self, computer, user):
        self.computer = computer
        self.user = user

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

    def __init__(self, name, password):
        self.score = 0
        self.name = name
        self.password = password
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

        # check upper_case
        have_upper_case = False
        for letter in UPPER_CASE:
            if letter in password:
                have_upper_case = True

        if have_upper_case:
            pass
        else:
            raise ValueError("Password needs at least one upper-case-letter")

        if len(password) >= 8:
            self._password = password
        else:
            raise ValueError("Password needs at least 8 character")



        # check lower_case
        # check special_sign


class Computer:
    def __init__(self):
        self.score = 0
        self.choice = "nothing"

    def add_point(self):
        self.score = self.score + 1

    def make_choice(self):
        self.choice = random.choice(POSSIBLE_MOVES)


def register():
    while True:
        try:
            user = User(input("name: "), input("password: "))
            break
        except ValueError as err:
            print(err)
    # if the object not exists in the user_test_file
    #   then save object in text-file
    return user


def main():
    computer = Computer()
    game = Game(computer, register())
    print('Welcome to the Game "Rock, Paper or Scissor!"')
    print(f'Hello {game.user.name}. Lets start the game.')

    while game.user.score < MAX_SCORE and computer.score < MAX_SCORE:
        game.round()
    print("Thank you for gaming!")


if __name__ == '__main__':
    main()
