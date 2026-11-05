"""Run the program with ``python -m house_prices``."""

import logging
import sys

from house_prices.presentation.cli import main

## @file __main__.py
## @brief Module entry point: configures logging and runs the command line.


## @brief Configure logging and run the command line.
## @return The process exit code.
def run() -> int:
    """Configure logging and return the exit code of the command line."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    return main()


if __name__ == "__main__":
    sys.exit(run())
