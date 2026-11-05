import re
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from house_prices.domain.errors.scrape_error import ScrapeError
from house_prices.infrastructure.beautifulsoup_listing_parser import (
    BeautifulSoupListingParser,
    get_addresses,
    get_links,
    get_prices,
)

FIXTURE = Path(__file__).parent.parent / "fixtures" / "zillow_clone.html"
CARD_COUNT = 44
PRICE_FORMAT = re.compile(r"^\$[\d,]+$")


@pytest.fixture
def soup() -> BeautifulSoup:
    return BeautifulSoup(FIXTURE.read_text(encoding="utf-8"), "html.parser")


def test_lists_have_equal_length_equal_to_card_count(soup: BeautifulSoup) -> None:
    assert len(get_links(soup)) == CARD_COUNT
    assert len(get_addresses(soup)) == CARD_COUNT
    assert len(get_prices(soup)) == CARD_COUNT


def test_parse_returns_one_listing_per_card() -> None:
    listings = BeautifulSoupListingParser().parse(FIXTURE.read_text(encoding="utf-8"))

    assert len(listings) == CARD_COUNT


def test_prices_match_dollar_format(soup: BeautifulSoup) -> None:
    assert all(PRICE_FORMAT.match(price) for price in get_prices(soup))


def test_addresses_have_no_newline_pipe_or_outer_whitespace(
    soup: BeautifulSoup,
) -> None:
    for address in get_addresses(soup):
        assert "\n" not in address
        assert "|" not in address
        assert address == address.strip()


def test_links_start_with_http(soup: BeautifulSoup) -> None:
    assert all(link.startswith("http") for link in get_links(soup))


def test_parse_raises_when_counts_differ() -> None:
    html = (
        '<div class="PropertyCardWrapper"><span>$1,000</span></div>'
        '<div class="StyledPropertyCardDataWrapper"><a href="http://x">l</a></div>'
    )

    with pytest.raises(ScrapeError):
        BeautifulSoupListingParser().parse(html)


def test_parse_raises_when_page_has_no_listings() -> None:
    with pytest.raises(ScrapeError):
        BeautifulSoupListingParser().parse("<html></html>")
