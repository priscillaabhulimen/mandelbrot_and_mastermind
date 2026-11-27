from .classes.game import Game
from .tests.test_code import run_scoring_tests

def main():
    """Start a Mastermind game."""
    game = Game()

    game.play()

if __name__ == "__main__":
    run_scoring_tests()
    main()