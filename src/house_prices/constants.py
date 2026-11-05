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

## @var FORM_TIMEOUT_SECONDS
## @brief Seconds to wait for a form element before giving up.
FORM_TIMEOUT_SECONDS: Final[float] = 10.0

## @var FORM_INPUT_SELECTOR
## @brief CSS selector for the short-answer inputs of the form, in page order.
FORM_INPUT_SELECTOR: Final[str] = 'input[type="text"]'

## @var FORM_INPUT_COUNT
## @brief Number of short-answer inputs the form has (address, price, link).
FORM_INPUT_COUNT: Final[int] = 3

## @var FORM_SUBMIT_XPATH
## @brief XPath of the submit button of the form.
FORM_SUBMIT_XPATH: Final[str] = '//span[text()="Submit"]/ancestor::div[@role="button"]'

## @var FORM_CONFIRMATION_XPATH
## @brief XPath of the text that confirms the response was recorded.
FORM_CONFIRMATION_XPATH: Final[str] = (
    '//*[contains(text(), "Your response has been recorded")]'
)

## @var CHROME_BIN_ENV_VAR
## @brief Name of the environment variable that holds the Chrome binary path.
CHROME_BIN_ENV_VAR: Final[str] = "CHROME_BIN"

## @var CHROMEDRIVER_PATH_ENV_VAR
## @brief Name of the environment variable that holds the chromedriver path.
CHROMEDRIVER_PATH_ENV_VAR: Final[str] = "CHROMEDRIVER_PATH"

## @var CHROME_WINDOW_SIZE
## @brief Window size used by the headless browser.
CHROME_WINDOW_SIZE: Final[str] = "1280,1024"
