import unittest
from unittest.mock import patch

from mastermind.classes.code import Code
from mastermind.utils import colton_dict


def score_counts(secret: str, guess: str) -> tuple[int, int, int]:
    secret_pegs = [colton_dict[colour] for colour in secret.split(",")]
    guess_pegs = [colton_dict[colour] for colour in guess.split(",")]
    with patch.object(Code, "generate_code", return_value=secret_pegs):
        code = Code(len(secret_pegs))
    feedback = code.score(guess_pegs)
    return feedback.exact, feedback.wrong_position, feedback.wrong_colour


class TestCode(unittest.TestCase):
    def test_assignment_example(self):
        assert score_counts(
            "red,blue,green,yellow,white,white",
            "red,yellow,black,green,white,white",
        ) == (3, 2, 1)

    def test_repeated_secret_colours(self):
        assert score_counts(
            "red,red,blue,blue,green,yellow",
            "red,blue,red,black,black,yellow",
        ) == (2, 2, 2)

    def test_repeated_guess_colours_are_counted_once(self):
        assert score_counts(
            "red,red,blue,green,yellow,white",
            "red,blue,white,black,white,black",
        ) == (1, 2, 3)


def run_scoring_tests() -> None:
    """Run the required scoring assertions before starting the game."""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCode)
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        raise AssertionError("Mastermind scoring tests failed.")
