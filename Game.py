from User import User
from Npc import Npc
import time

class Game:
    def __init__(self):
        self.user = User("Nobody")
        self.npc = Npc()
        self.is_undecided = False

    def startcreen(self):
        print("Welcome to the Game \"Rock , Paper or Scissor!\"")
        self.user.set_name(input("Name: "))
        print(f"Hello {self.user.get_name()}! Lets start the Game!")

    def round(self):
        # user and npc take their choices
        self.user.set_choice(input("Please take your choice: "))
        self.npc.set_choice()
        self.round_animation()
        print(f"{self.user.get_choice()} against {self.npc.get_choice()}")
        self.is_winner()
        if self.is_undecided:
            print("Undecided!")
        elif self.is_winner():
            print("You win!")
        else:
            print("You loose!")

    def round_animation(self):
        time.sleep(1)
        print("Rock!")
        time.sleep(1)
        print("Paper!")
        time.sleep(1)
        print("Scissor!")
        time.sleep(1)

    def is_winner(self, choice_user, choice_npc):
        self.is_undecided = False                 # it have to be False first
        if choice_user == "rock":                 # rock against paper or scissor
            if choice_npc == "paper":
                return False
            elif choice_npc == "scissor":
                return True
        elif choice_user == "paper":              # paper against scissor or stone
            if choice_npc == "scissor":
                return False
            elif choice_npc == "stone":
                return True
        elif choice_user == "scissor":            # scissor against rock or paper
            if choice_npc == "rock":
                return False
            elif choice_npc == "paper":
                return True
        else:
            self.is_undecided = True              # if nothing match its: rock,rock or stone,stone or scissor,scissor
