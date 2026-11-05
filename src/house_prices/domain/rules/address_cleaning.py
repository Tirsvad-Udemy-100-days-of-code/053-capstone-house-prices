"""Cleaning of raw address text."""

## @file address_cleaning.py
## @brief Pure function that turns raw address text into a single clean line.


## @brief Remove newlines, pipes and surplus whitespace from an address.
## @param raw Address text as found on the page.
## @return The address on one line with single spaces.
def clean_address(raw: str) -> str:
    """Return raw on one line without pipes and with single spaces."""
    return " ".join(raw.replace("|", " ").split())
