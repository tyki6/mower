import sys

from src.game import Game

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need one argument")
        exit()
    try:
        game = Game(sys.argv[1])
    except Exception as e:
        print("An error has occurred.")
        print(e)
        exit()
    while not game.is_finish():
        game.play_turn()
    game.print_result()
