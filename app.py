from User import User
from Npc import Npc
# import random

print("Welcome to the Game Rock, Paper or Scissor!\n")

user = User(input("Name: "))
computer = Npc()

print(f"Hello {user.get_name()}. Lets start the Game!")

# while(user.get_score() < 3 and computer.get_score() < 3):

user.set_choice("mist")
print(user.get_choice())
print(computer.get_choice())
