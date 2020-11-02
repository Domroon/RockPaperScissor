from User import User
from Npc import Npc
# import random
import time

print("Welcome to the Game Rock, Paper or Scissor!\n")

user = User(input("Name: "))
computer = Npc()

print(f"Hello {user.get_name()}. Lets start the Game!")

# while(user.get_score() < 3 and computer.get_score() < 3):

user.set_choice("mist")
print(user.get_choice())
print(computer.get_choice())

time.sleep(1)
print("Rock")
time.sleep(2)
print("Paper")
time.sleep(2)
print("Scissor")
time.sleep(2)

# Willkommensnachricht
# Eingabe des Namens
# Anzeige Schere Stein Papier
# Anzeige verloren oder gewonnen
# Ausgabe von Punktestand NPC - Spieler
# Wiederholen wenn einer noch keine 3 Punkte hat
