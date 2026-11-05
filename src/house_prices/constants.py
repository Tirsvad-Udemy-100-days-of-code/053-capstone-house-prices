"""Constants shared across the house_prices package."""

## @file constants.py
## @brief Constants shared across the house_prices package.

from typing import Final

## @var ZILLOW_CLONE_URL
## @brief Address of the Zillow clone page that lists the rentals.
ZILLOW_CLONE_URL: Final[str] = "https://appbrewery.github.io/Zillow-Clone/"

## @var REQUEST_HEADERS
## @brief HTTP headers sent with every request to the listings page.
REQUEST_HEADERS: Final[dict[str, str]] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

## @var REQUEST_TIMEOUT_SECONDS
## @brief Seconds to wait for the listings page before giving up.
REQUEST_TIMEOUT_SECONDS: Final[float] = 10.0

## @var LINK_SELECTOR
## @brief CSS selector for the link of each listing card.
LINK_SELECTOR: Final[str] = ".StyledPropertyCardDataWrapper a"

## @var ADDRESS_SELECTOR
## @brief CSS selector for the address of each listing card.
ADDRESS_SELECTOR: Final[str] = ".StyledPropertyCardDataWrapper address"

## @var PRICE_SELECTOR
## @brief CSS selector for the elements that may hold the price of a card.
PRICE_SELECTOR: Final[str] = ".PropertyCardWrapper span"

## @var PRICE_MARKER
## @brief Text that marks a span as holding a price.
PRICE_MARKER: Final[str] = "$"

## @var FORM_URL_ENV_VAR
## @brief Name of the environment variable that holds the form address.
FORM_URL_ENV_VAR: Final[str] = "FORM_URL"
