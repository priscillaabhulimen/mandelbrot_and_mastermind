import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from mastermind.main import main, run_scoring_tests
else:
    from .main import main, run_scoring_tests


if __name__ == "__main__":
    run_scoring_tests()
    main()
