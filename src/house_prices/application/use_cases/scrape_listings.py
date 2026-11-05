"""Use case: scrape the listings from the page."""

from house_prices.application.ports.listing_parser import ListingParser
from house_prices.application.ports.page_fetcher import PageFetcher
from house_prices.domain.entities.listing import Listing

## @file scrape_listings.py
## @brief Use case that fetches the page and parses its listings.


## @class ScrapeListings
## @brief Fetches the listings page and parses it into listings.
class ScrapeListings:
    """Fetches the listings page and parses it into listings."""

    ## @brief Create the use case.
    ## @param fetcher Port that gets the page.
    ## @param parser Port that parses the page.
    def __init__(self, fetcher: PageFetcher, parser: ListingParser) -> None:
        """Store the ports the use case works through."""
        ## Port that gets the page.
        self._fetcher = fetcher
        ## Port that parses the page.
        self._parser = parser

    ## @brief Run the use case.
    ## @return The listings in page order.
    ## @throws ScrapeError When fetching or parsing fails.
    def execute(self) -> list[Listing]:
        """Return the listings of the page."""
        return self._parser.parse(self._fetcher.fetch())
