class Feedback():
    """Store and format feedback for a Mastermind guess."""

    def __init__(self, exact: int, wrong_position: int, wrong_colour: int):
        """Initialize the guess result counts."""
        self._exact = exact
        self._wrong_position = wrong_position
        self._wrong_colour = wrong_colour

    def message(self) -> str:
        """Return a readable description of the guess result."""
        return f"""You have:
    Exact match{"es" if self._exact != 1 else ""}: {self._exact}
    Right colour, wrong position: {self._wrong_position}
    Incorrect colours: {self._wrong_colour}
"""