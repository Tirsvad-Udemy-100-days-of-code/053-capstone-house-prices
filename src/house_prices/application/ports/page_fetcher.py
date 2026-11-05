"""Port for getting the listings page."""

from typing import Protocol

## @file page_fetcher.py
## @brief Port that returns the HTML of the listings page.


## @class PageFetcher
## @brief Port: gets the HTML of the listings page.
class PageFetcher(Protocol):
    """Gets the HTML of the listings page."""

    ## @brief Fetch the page.
    ## @return The HTML text.
    ## @throws ScrapeError When the page cannot be fetched.
    def fetch(self) -> str:
        """Return the HTML text of the page."""
        ...
