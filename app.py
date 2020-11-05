from game import Game
from user import User
from computer import Computer

# Willkommensnachricht
# Eingabe des Namens
# Anzeige Schere Stein Papier
# Anzeige verloren oder gewonnen
# Ausgabe von Punktestand Computer - Spieler
# Wiederholen wenn einer noch keine 3 Punkte hat

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
