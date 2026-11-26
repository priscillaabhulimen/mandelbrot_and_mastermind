import random
from ..utils import colours, ntocol_dict
from abc import ABC, abstractmethod

class Player(ABC):
    """Abstract base class representing a Mastermind player."""

    def __init__(self, name: str, sec_length: int):
        """Initialise the player with a name."""
        self._name = name
        self._sec_length = sec_length

    @abstractmethod
    def get_guess(self) -> str:
        """Return the player's next guess."""
        pass

class HumanPlayer(Player):
    def __init__(self, name: str, sec_length: int):
        super().__init__(name, sec_length) 

    def get_guess(self) -> str:
       return input(f"Guess (should be {self._sec_length} colours): ")
        

class ComputerPlayer(Player):
    def __init__(self, sec_length: int):
        super().__init__("XJ9", sec_length) 

    def get_guess(self) -> str:
        guess_int = [random.randint(1,len(colours)) for _ in range(self._sec_length)]
        return ",".join([ntocol_dict[n] for n in guess_int])
