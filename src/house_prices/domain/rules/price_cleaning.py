"""Cleaning of raw price text."""

import re

from house_prices.domain.errors.scrape_error import ScrapeError

## @file price_cleaning.py
## @brief Pure function that reduces raw price text to the "$1,234" form.

## @var _PRICE_PATTERN
## @brief Matches a dollar amount such as "$1,234".
_PRICE_PATTERN = re.compile(r"\$[\d,]+")


## @brief Reduce raw price text to the "$1,234" form.
## @param raw Price text such as "$2,895+/mo" or "$2,798+ 1bd".
## @return The price, for example "$2,895".
## @throws ScrapeError When the text holds no dollar amount.
def clean_price(raw: str) -> str:
    """Return the dollar amount in raw, dropping "+", "/mo" and bedroom text."""
    match = _PRICE_PATTERN.search(raw)
    if match is None:
        message = f"No price found in {raw!r}"
        raise ScrapeError(message)
    return match.group()
