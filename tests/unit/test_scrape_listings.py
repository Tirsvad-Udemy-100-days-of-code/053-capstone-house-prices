from pathlib import Path

from house_prices.application.use_cases.scrape_listings import ScrapeListings
from house_prices.infrastructure.beautifulsoup_listing_parser import (
    BeautifulSoupListingParser,
)

FIXTURE = Path(__file__).parent.parent / "fixtures" / "zillow_clone.html"


class FakePageFetcher:
    def __init__(self, html: str) -> None:
        self._html = html

    def fetch(self) -> str:
        return self._html


def test_execute_returns_listings_from_fetched_page() -> None:
    html = FIXTURE.read_text(encoding="utf-8")
    use_case = ScrapeListings(FakePageFetcher(html), BeautifulSoupListingParser())

    listings = use_case.execute()

    assert len(listings) == 44
    assert all(item.link.startswith("http") for item in listings)
