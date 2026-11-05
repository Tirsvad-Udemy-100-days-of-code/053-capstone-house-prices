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

## @var FORM_URL_ENV_VAR
## @brief Name of the environment variable that holds the form address.
FORM_URL_ENV_VAR: Final[str] = "FORM_URL"
