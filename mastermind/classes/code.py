import random
from mastermind.utils import colours,ntocol_dict,colton_dict
from mastermind.classes.feedback import Feedback

class Code():
    """Generates and stores a secret code and scores guesses."""

    def __init__(self, c_length: int = 6):
        """Generate a code on initialisation."""
        self._secret = self.generate_code(c_length)

    def generate_code(self, c_length: int = 6 ) -> list[int]:
        """Generate integer pegs within the available colour range."""
        return [random.randint(1,len(colours)) for _ in range(c_length)]

    def get_color(self, i: int) -> str:
        """Return the corresponding colour for an integer peg."""
        return ntocol_dict[i]

    def get_number(self, color: str) -> int:
        """Return the corresponding integer for a colour."""
        return colton_dict[color]

    def reveal(self) -> str:
        """Return the secret code as colour names."""
        return ", ".join(self.get_color(peg).title() for peg in self._secret)

    def score(self, guess: list[int]) -> Feedback:
        """Score a guess against the secret code."""
        guess_res = self._compare_pegs(guess)
        return Feedback(guess_res[0], guess_res[1], guess_res[2])

    def _compare_pegs(self, guess: list[int]) -> tuple:
        """Count exact, misplaced, and incorrect pegs."""
        #exact match, wrong location, wrong color
        results = [0, 0, 0]
        rem_sec = []
        rem_guess = []

        """Checks and increments the count of exact matches"""
        for i in range(len(guess)):
            if self._secret[i] == guess[i]:
                results[0] += 1
            else:
                rem_sec.append(self._secret[i])
                rem_guess.append(guess[i])

        """Compares the remainder after exact matches for the colours in the wrong position
        It removes valid colours and incrents the wrong position count"""
        for peg in rem_guess.copy():
            if peg in rem_sec:
                results[1] += 1
                rem_guess.remove(peg)
                rem_sec.remove(peg)

        
        """The rest of the guess is therefore incorrect colours entirely
        and sets the incorrect colour count"""
        results[2] = len(rem_guess)
        return tuple(results)