"""HTTP implementation of the PageFetcher port."""

import requests

from house_prices.constants import (
    REQUEST_HEADERS,
    REQUEST_TIMEOUT_SECONDS,
    ZILLOW_CLONE_URL,
)
from house_prices.domain.errors.scrape_error import ScrapeError

## @file requests_page_fetcher.py
## @brief Fetches the listings page with the requests library.


## @class RequestsPageFetcher
## @brief PageFetcher that requests the page with browser headers.
class RequestsPageFetcher:
    """Fetches the listings page over HTTP with browser headers."""

    ## @brief Create the fetcher.
    ## @param url Address of the page.
    ## @param header HTTP headers to send (User-Agent and Accept-Language).
    ## @param timeout_seconds Seconds to wait for the response.
    def __init__(
        self,
        url: str = ZILLOW_CLONE_URL,
        header: dict[str, str] | None = None,
        timeout_seconds: float = REQUEST_TIMEOUT_SECONDS,
    ) -> None:
        """Store the address, headers and timeout."""
        ## Address of the page.
        self._url = url
        ## HTTP headers sent with the request.
        self._header = dict(REQUEST_HEADERS) if header is None else header
        ## Seconds to wait for the response.
        self._timeout_seconds = timeout_seconds

    ## @brief Fetch the page.
    ## @return The HTML text.
    ## @throws ScrapeError When the request fails or the status is an error.
    def fetch(self) -> str:
        """Return the HTML text of the page."""
        try:
            response = requests.get(
                self._url, headers=self._header, timeout=self._timeout_seconds
            )
            response.raise_for_status()
        except requests.RequestException as err:
            message = f"Could not fetch {self._url}"
            raise ScrapeError(message) from err
        return response.text
