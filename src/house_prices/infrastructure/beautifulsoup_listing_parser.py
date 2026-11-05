"""BeautifulSoup implementation of the ListingParser port."""

from bs4 import BeautifulSoup

from house_prices.constants import (
    ADDRESS_SELECTOR,
    LINK_SELECTOR,
    PRICE_MARKER,
    PRICE_SELECTOR,
)
from house_prices.domain.entities.listing import Listing
from house_prices.domain.errors.scrape_error import ScrapeError
from house_prices.domain.rules.address_cleaning import clean_address
from house_prices.domain.rules.price_cleaning import clean_price

## @file beautifulsoup_listing_parser.py
## @brief Parses the listings page with BeautifulSoup.


## @brief Collect the link of every listing card.
## @param soup The parsed page.
## @return The href values in page order.
def get_links(soup: BeautifulSoup) -> list[str]:
    """Return the link of every listing card, in page order."""
    return [
        str(tag["href"]) for tag in soup.select(LINK_SELECTOR) if tag.has_attr("href")
    ]


## @brief Collect the cleaned address of every listing card.
## @param soup The parsed page.
## @return The cleaned addresses in page order.
def get_addresses(soup: BeautifulSoup) -> list[str]:
    """Return the cleaned address of every listing card, in page order."""
    return [clean_address(tag.get_text()) for tag in soup.select(ADDRESS_SELECTOR)]


## @brief Collect the cleaned price of every listing card.
## @param soup The parsed page.
## @return The cleaned prices in page order.
## @throws ScrapeError When a price text holds no dollar amount.
def get_prices(soup: BeautifulSoup) -> list[str]:
    """Return the cleaned price of every listing card, in page order."""
    return [
        clean_price(tag.get_text())
        for tag in soup.select(PRICE_SELECTOR)
        if PRICE_MARKER in tag.get_text()
    ]


## @class BeautifulSoupListingParser
## @brief ListingParser that reads the page with BeautifulSoup.
class BeautifulSoupListingParser:
    """Parses the listings page into listings with BeautifulSoup."""

    ## @brief Parse the page.
    ## @param html The HTML text of the page.
    ## @return The listings in page order.
    ## @throws ScrapeError When no listing is found or the counts differ.
    def parse(self, html: str) -> list[Listing]:
        """Return the listings found in html, in page order."""
        soup = BeautifulSoup(html, "html.parser")
        all_links = get_links(soup)
        all_addresses = get_addresses(soup)
        all_prices = get_prices(soup)
        counts = {len(all_links), len(all_addresses), len(all_prices)}
        if len(counts) != 1 or counts == {0}:
            message = (
                f"Inconsistent page: {len(all_links)} links, "
                f"{len(all_addresses)} addresses, {len(all_prices)} prices"
            )
            raise ScrapeError(message)
        return [
            Listing(link=link, price=price, address=address)
            for link, price, address in zip(
                all_links, all_prices, all_addresses, strict=True
            )
        ]
