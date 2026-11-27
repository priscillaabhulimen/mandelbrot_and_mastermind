import random
from ..utils import colours, ntocol_dict
from abc import ABC, abstractmethod

class Player(ABC):
    """Abstract base class representing a Mastermind player."""

    def __init__(self, name: str, sec_length: int):
        """Initialise the player with a name."""
        self._name = name
        self._sec_length = sec_length

    @property
    def name(self) -> str:
        """Return the player's display name."""
        return self._name

    @abstractmethod
    def get_guess(self) -> str:
        """Return the player's next guess."""
        pass

class HumanPlayer(Player):
    """Represent a player who enters guesses through the terminal."""

    def __init__(self, name: str, sec_length: int):
        """Initialize a named human player."""
        super().__init__(name, sec_length) 

    def get_guess(self) -> str:
        """Prompt the human player for a guess."""
        valid_colours = ", ".join(sorted(colours))
        return input(
            f"Guess {self._sec_length} comma-separated colours "
            f"({valid_colours}): "
        )
        

class ComputerPlayer(Player):
    """Represent a player that generates random guesses."""

    def __init__(self, sec_length: int):
        """Initialize the computer player."""
        super().__init__("XJ9", sec_length) 

    def get_guess(self) -> str:
        """Generate a random comma-separated colour guess."""
        guess_int = [random.randint(1,len(colours)) for _ in range(self._sec_length)]
        return ",".join([ntocol_dict[n] for n in guess_int])
