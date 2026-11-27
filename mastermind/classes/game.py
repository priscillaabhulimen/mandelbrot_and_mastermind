from .code import Code
from ..utils import colton_dict
from .player import HumanPlayer, ComputerPlayer

class Game:
    """Run a Mastermind game with human and computer players."""

    def __init__(
            self, 
            attempts_poss: int = 15, 
            player_count: int = 1, 
            code_length: int = 6):
        """Initialize the game settings and secret code."""
        self._attempts_poss = attempts_poss
        self._player_count = player_count
        self._code_length = code_length
        self._code = Code(code_length)
        self._players = []

    def _create_players(self):
        """Create the players participating in the game."""
        self._players = []
        while True:
            try:
                p_count = int(input("Enter the number of players (1 or 2): "))
            except ValueError:
                print("Please enter 1 or 2.")
                continue
            if p_count in (1, 2):
                break
            print("The number of players must be 1 or 2.")

        self._player_count = p_count
        if p_count == 1:
            name = input("Enter your name: ")
            self._players.append(HumanPlayer(name, self._code_length))
        else:
            play_computer = self._is_hvc()
            if play_computer:
                name = input("Enter your name: ")
                self._players.append(HumanPlayer(name, self._code_length))
                self._players.append(ComputerPlayer(self._code_length))
            else:
                for i in range(p_count):
                    name = input(f"Enter name for player {i + 1}: ")
                    self._players.append(HumanPlayer(name, self._code_length))

    def _is_hvc(self) -> bool:
        """Prompt until the user chooses computer or human competition."""
        while True:
            play_computer = input("Do you want to play against the computer? (y/n): ").lower()
            if play_computer == "y":
                return True
            elif play_computer == "n":
                return False
            else:
                print("Invalid response")

    def _valid_guess(self, guess: str) -> list[int]:
        """Convert a comma-separated colour guess into integer pegs."""
        if not isinstance(guess, str):
            return []

        guess_colours = [colour.strip() for colour in guess.split(",")]
        if len(guess_colours) != self._code_length:
            return []

        guesses = []
        for col in guess_colours:
            if col.lower() not in colton_dict:
                return []
            guesses.append(colton_dict[col.lower()])
        return guesses

    def play(self) -> str:
        """Play rounds until a player wins or all attempts are exhausted."""
        if not self._players:
            self._create_players()

        for attempt in range(1, self._attempts_poss + 1):
            print(f"\nAttempt {attempt} of {self._attempts_poss}")

            for player in self._players:
                while True:
                    guess = player.get_guess()
                    guess_peg = self._valid_guess(guess)
                    if guess_peg:
                        break
                    print(
                        f"Invalid guess. Enter exactly {self._code_length} "
                        "valid comma-separated colours."
                    )

                feedback = self._code.score(guess_peg)
                print(feedback.message())
                if feedback.exact == self._code_length:
                    print(f"{player.name} wins!")
                    return player.name

        print(f"No player guessed the code. The secret was {self._code.reveal()}.")
        print("Game over.")
        return ""