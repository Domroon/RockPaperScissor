import time

class Game:
    def __init__(self, user, npc):
        self.user = user
        self.npc = npc

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
        self.npc.make_choice()
        self.round_animation()
        print(f"{self.user.get_choice()} against {self.npc.choice}")
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
        print(f"Npc score: {self.npc.score}")

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
            elif choice_npc == "rock":
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
