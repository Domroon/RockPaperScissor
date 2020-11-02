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
        self.is_undecided = False
        self.user.set_choice(input("Please take your choice: "))
        self.npc.set_choice()
        self.round_animation()
        print(f"{self.user.get_choice()} against {self.npc.get_choice()}")
        self.result_check()
        if self.is_undecided:
            print("Undecided!")
        elif self.result_check:
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

    def result_check(self):
        if self.user.get_choice() == self.npc.get_choice():  # undecided
            self.is_undecided = True
        elif self.user.get_choice() == "rock":               # rock against paper or scissor
            if self.npc.get_choice() == "paper":
                return False
            elif self.npc.get_choice() == "scissor":
                return True
        elif self.user.get_choice() == "paper":              # paper against scissor or stone
            if self.npc.get_choice() == "scissor":
                return False
            elif self.npc.get_choice() == "stone":
                return True
        elif self.user.get_choice() == "scissor":            # scissor against rock or spaper
            if self.npc.get_choice() == "rock":
                return False
            elif self.npc.get_choice() == "paper":
                return True
