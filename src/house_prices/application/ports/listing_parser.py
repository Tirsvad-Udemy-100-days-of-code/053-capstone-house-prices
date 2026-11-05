"""Port for turning page HTML into listings."""

from typing import Protocol

from house_prices.domain.entities.listing import Listing

## @file listing_parser.py
## @brief Port that parses page HTML into listings.


## @class ListingParser
## @brief Port: parses page HTML into clean listings.
class ListingParser(Protocol):
    """Parses page HTML into clean listings."""

    ## @brief Parse the page.
    ## @param html The HTML text of the page.
    ## @return The listings in page order.
    ## @throws ScrapeError When the page holds inconsistent data.
    def parse(self, html: str) -> list[Listing]:
        """Return the listings found in html, in page order."""
        ...
