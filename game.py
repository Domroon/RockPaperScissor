from user import User
from npc import Npc
import time

class Game:
    def __init__(self):
        self.user = User("Nobody")
        self.npc = Npc()

    def startcreen(self):
        print("Welcome to the Game \"Rock , Paper or Scissor!\"")
        self.user.set_name(input("Name: "))
        print(f"Hello {self.user.get_name()}! Lets start the Game!")

    def round(self):
        # user and npc take their choices
        while True:
            try:
                self.user.set_choice(input("Please take your choice: "))
                break
            except ValueError as error:
                print(error)
        self.npc.set_choice()
        self.round_animation()
        print(f"{self.user.get_choice()} against {self.npc.get_choice()}")
        winner = self.get_winner()
        if winner is None:
            print("Undecided!")
        else:
            winner.set_one_point()
            if winner is self.user:
                print("You win!")
            else:
                print("You loose!")
        print(f"User score: {self.user.score}")
        print(f"Npc score: {self.npc.score}")

    def round_animation(self):
        time.sleep(1)
        print("Rock!")
        time.sleep(1)
        print("Paper!")
        time.sleep(1)
        print("Scissor!")
        time.sleep(1)

    def get_winner(self):
        choice_user = self.user.choice
        choice_npc = self.npc.choice
        if choice_user == "rock":
            if choice_npc == "paper":
                return self.npc
            elif choice_npc == "scissor":
                return self.user
            else:
                return None
        elif choice_user == "paper":
            if choice_npc == "scissor":
                return self.npc
            elif choice_npc == "stone":
                return self.user
            else:
                return None
        elif choice_user == "scissor":
            if choice_npc == "rock":
                return self.npc
            elif choice_npc == "paper":
                return self.user
            else:
                return None
        else:
            raise ValueError()
