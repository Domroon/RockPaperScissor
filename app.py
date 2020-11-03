from game import Game

# Willkommensnachricht
# Eingabe des Namens
# Anzeige Schere Stein Papier
# Anzeige verloren oder gewonnen
# Ausgabe von Punktestand NPC - Spieler
# Wiederholen wenn einer noch keine 3 Punkte hat

def main():
    game = Game()
    max_rounds = 3
    for round in range(max_rounds):
        game.round()
if __name__ == '__main__':
    main()
