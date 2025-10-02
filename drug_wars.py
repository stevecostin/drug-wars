from game import Game
from player import Player

def main():
    print("Welcome to Drug Wars!\n")
    print("How many players are there?")
    player_count: int = int(input())
    print()

    players: list = []

    for player_number in range(player_count):
        print(f"Please enter the street name for player {player_number + 1}:")
        name: str = input()
        print(f"Please enter the age for player {player_number + 1}:")
        age: int = int(input())
        print()

        players.append(Player(name, age))

    game: Game = Game(*players)
    game.start()


if __name__ == '__main__':
    main()