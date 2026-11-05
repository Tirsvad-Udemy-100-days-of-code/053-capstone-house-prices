"""Error raised when listings cannot be fetched, parsed or cleaned."""

## @file scrape_error.py
## @brief Domain error for a failed scrape.


## @class ScrapeError
## @brief Raised when a page cannot be fetched or its listings are inconsistent.
class ScrapeError(Exception):
    """Raised when a page cannot be fetched or its listings are inconsistent."""
