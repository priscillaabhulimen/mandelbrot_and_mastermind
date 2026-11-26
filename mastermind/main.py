from .classes.game import Game

def main():
    """Start a Mastermind game."""
    game = Game()

    game.play()

if __name__ == "__main__":
    main()