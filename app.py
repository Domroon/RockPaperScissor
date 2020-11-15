import random
import time
import sys

POSSIBLE_MOVES = ["rock", "paper", "scissor"]
MAX_SCORE = 3
SPECIAL_CHARACTER = "!§$%&/()=?{[]}-_<>|´`"
NUMBER_CHARACTER = "0123456789"
UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyzäöüß"
PASSWORD_LENGTH = 8


class Game:
    def __init__(self, player_1, player_2):
        self.player_1_is_user = False
        self.player_2_is_user = False

        if player_1.__class__ == User:
            self.user_1 = player_1
            self.computer_1 = None
            self.player_1_is_user = True
        elif player_1.__class__ == Computer:
            self.computer_1 = player_1
            self.user_1 = None
            self.player_1_is_user = False

        if player_2.__class__ == User:
            self.user_2 = player_2
            self.computer_2 = None
            self.player_2_is_user = True
        elif player_2.__class__ == Computer:
            self.computer_2 = player_2
            self.user_2 = None
            self.player_2_is_user = False

    def round(self):
        # user_1 against computer_2
        if self.player_1_is_user and not self.player_2_is_user:
            self.player_against_computer()

        # user_1 against user_2
            # self.player_against_player()

        # computer_1 against computer_2
            # self.computer_against_computer()

    def player_against_computer(self):
        # user and computer take their choices
        while True:
            try:
                self.user_1.choice = input("Please take your choice: ")
                break
            except ValueError as error:
                print(error)
        self.computer_2.make_choice()
        self.round_animation()
        print(f"{self.user_1.choice} against {self.computer_2.choice}")
        winner = self.get_winner()
        if winner is None:
            print("Undecided!")
        else:
            winner.add_point()
            if winner is self.user_1:
                print("You win!")
            else:
                print("You loose!")
        print(f"User score: {self.user_1.score}")
        print(f"computer score: {self.computer_2.score}")

    @staticmethod
    def round_animation():
        speed = 0.5
        time.sleep(speed)
        print("Rock!")
        time.sleep(speed)
        print("Paper!")
        time.sleep(speed)
        print("Scissor!")
        time.sleep(speed)

    def get_winner(self):
        # user_1 against computer_2
        if self.player_1_is_user and not self.player_2_is_user:
            choice_user = self.user_1.choice
            choice_computer = self.computer_2.choice
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

    def __init__(self, name, password, email):
        self.score = 0
        self.name = name
        self.password = password
        self._choice = "nothing"
        self.email = email
        self.looses = None
        self.wins = None
        self.played_rounds = None

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

        if not have_upper_case:
            raise ValueError("Password needs at least one upper-case-letter")

        # check lower_case
        have_lower_case = False
        for letter in LOWER_CASE:
            if letter in password:
                have_lower_case = True

        if not have_lower_case:
            raise ValueError("Password needs at least one lower-case-letter")

        # check special_sign
        have_special_sign = False
        for letter in SPECIAL_CHARACTER:
            if letter in password:
                have_special_sign = True

        if not have_special_sign:
            raise ValueError("Password needs at least one special sign")

        # check number
        have_number_sign = False
        for letter in NUMBER_CHARACTER:
            if letter in password:
                have_number_sign = True

        if not have_number_sign:
            raise ValueError("Password needs at least one number")

        # check password length
        if len(password) >= 8:
            self._password = password
        else:
            raise ValueError("Password needs at least 8 character")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        # check for '@'- and '.'- sign
        if '@' not in email:
            raise ValueError("Email needs an '@'")

        if '.' not in email:
            raise ValueError("Email needs an '.'")
        else:
            self._email = email

    def show_statistics(self):
        print(f'looses: {self.looses}')
        print(f'wins: {self.wins}')
        print(f'played rounds: {self.played_rounds}')


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
            user = User(input("name: "), input("password: "), input("email: "))
            break
        except ValueError as err:
            print(err)
    # if the object not exists in the user_test_file
    #   then save object in text-file
    # (make user_save-method)
    return user


def save_user(user):
    user_list = open("user_list.txt", "a")
    user_list.write('\n' +
                    user.name + ' ' +
                    user.password + ' ' +
                    user.email)
    user_list.close()


def load_user(username, user_password):
    user_list = open("user_list.txt", "r")

    # find the right line
    user_to_load = None
    for line in user_list:
        if username in line:
            user_to_load = line

    # extract the data that's separate by spaces
    # and save it to individual elements in a list
    # called user_data
    user_data = user_to_load.rsplit(' ')
    login_name = user_data[0]
    password = user_data[1]
    email = user_data[2]

    if login_name != username:
        raise ValueError('Wrong user-name or user does not exist.')

    if password != user_password:
        raise ValueError('Wrong password!')
    else:
        user = User(login_name, password, email)
    user_list.close()
    return user


def login_user():
    while True:
        try:
            user = load_user(input("name: "), input("password: "))
            break
        except ValueError as err:
            print(err)
    return user


def login_screen():
    print('1 - Login')
    print('2 - Register')
    print('3 - End')
    user_choice = int(input())

    if user_choice == 1:
        user = login_user()
        print(f'Welcome back, {user.name}!')
        return user
    elif user_choice == 2:
        user = register()
        save_user(user)
        print(f'Welcome {user.name}. Let\'s play our first game!')
        return user
    elif user_choice == 3:
        sys.exit()
    else:
        raise ValueError("Your number must be between 1-3!")


def start_screen(player_1, player_2):
    print('1 - Player VS Computer')
    print('2 - Player VS Computer')
    print('3 - Computer VS Computer')
    user_choice = int(input())

    if user_choice == 1:
        player_1 = Computer()
        while True:
            try:
                game = Game(player_1, login_screen())
                return game
            except ValueError as err:
                print(err)


def main():
    # for Testing
    print('Welcome to the Game "Rock, Paper or Scissor!"')
    user = User("Max", "Asdf65464!!", "Max@web.de")
    computer = Computer()
    game = Game(user, computer)
    game.round()
    print("Thank you for gaming!")


if __name__ == '__main__':
    main()
