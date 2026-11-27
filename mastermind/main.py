from unittest.mock import patch

from .classes.game import Game
from .classes.code import Code
from .utils import colton_dict


def _score_counts(secret: str, guess: str) -> tuple[int, int, int]:
    secret_pegs = [colton_dict[colour] for colour in secret.split(",")]
    guess_pegs = [colton_dict[colour] for colour in guess.split(",")]
    with patch.object(Code, "generate_code", return_value=secret_pegs):
        code = Code(len(secret_pegs))
    feedback = code.score(guess_pegs)
    return feedback.exact, feedback.wrong_position, feedback.wrong_colour


def run_scoring_tests() -> None:
    """Run the required examples and repeated-colour scoring assertions."""
    assert _score_counts(
        "red,blue,green,yellow,white,white",
        "red,yellow,black,green,white,white",
    ) == (3, 2, 1)
    assert _score_counts(
        "red,red,blue,blue,green,yellow",
        "red,blue,red,black,black,yellow",
    ) == (2, 2, 2)
    assert _score_counts(
        "red,red,blue,green,yellow,white",
        "red,blue,white,black,white,black",
    ) == (1, 2, 3)

def main():
    """Start a Mastermind game."""
    game = Game()

    game.play()

if __name__ == "__main__":
    run_scoring_tests()
    main()