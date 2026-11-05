"""Command line entry point and composition root."""

import argparse
import logging
import os
import sys
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver

from house_prices.application.ports.page_fetcher import PageFetcher
from house_prices.application.use_cases.fill_form import FillForm
from house_prices.application.use_cases.scrape_listings import ScrapeListings
from house_prices.constants import FORM_URL_ENV_VAR
from house_prices.domain.entities.listing import Listing
from house_prices.domain.errors.form_error import FormError
from house_prices.domain.errors.scrape_error import ScrapeError
from house_prices.infrastructure.beautifulsoup_listing_parser import (
    BeautifulSoupListingParser,
)
from house_prices.infrastructure.chrome_driver_factory import create_chrome_driver
from house_prices.infrastructure.requests_page_fetcher import RequestsPageFetcher
from house_prices.infrastructure.selenium_form_submitter import (
    SeleniumFormSubmitter,
)

## @file cli.py
## @brief Parses the command line and wires scraper and form filler together.

## Logger of the command line.
_LOG = logging.getLogger(__name__)
## Exit code for success.
EXIT_OK = 0
## Exit code for a failed scrape or form submission.
EXIT_FAILURE = 1
## Exit code for a usage error such as a missing FORM_URL.
EXIT_USAGE = 2
## Name of the screenshot file written by --screenshot-dir.
SCREENSHOT_NAME = "form-filled.png"


## @brief Build the argument parser.
## @return The parser for the command line.
def build_parser() -> argparse.ArgumentParser:
    """Return the argument parser."""
    parser = argparse.ArgumentParser(
        prog="house_prices",
        description="Scrape rentals and record each one in a Google Form.",
    )
    parser.add_argument(
        "--scrape-only",
        action="store_true",
        help="print the scraped lists and stop; no browser, no FORM_URL",
    )
    parser.add_argument(
        "--headless", action="store_true", help="run the browser without a window"
    )
    parser.add_argument(
        "--screenshot-dir",
        type=Path,
        default=None,
        help="save a PNG of the browser after the run into this folder",
    )
    return parser


## @brief Write the scraped lists to standard output.
## @param listings The scraped listings.
def print_listings(listings: Sequence[Listing]) -> None:
    """Write the links, addresses and prices, one list after another."""
    count = len(listings)
    sys.stdout.write(
        f"There are {count} links to individual listings in total:\n"
        f"{[item.link for item in listings]}\n\n"
        f"After having been cleaned up, the {count} addresses are:\n"
        f"{[item.address for item in listings]}\n\n"
        f"After having been cleaned up, the {count} prices are:\n"
        f"{[item.price for item in listings]}\n"
    )


## @brief Fill the form with every listing and optionally save a screenshot.
## @param listings The listings to record.
## @param form_url Address of the form.
## @param headless Run the browser without a window.
## @param screenshot_dir Folder for the screenshot, or None for no screenshot.
## @param driver_factory Creates the browser driver.
## @return The number of responses submitted.
## @throws FormError When a response cannot be submitted.
def run_form(
    listings: Sequence[Listing],
    form_url: str,
    headless: bool,
    screenshot_dir: Path | None,
    driver_factory: Callable[[bool], WebDriver],
) -> int:
    """Submit every listing and return how many were submitted."""
    driver = driver_factory(headless)
    try:
        count = FillForm(SeleniumFormSubmitter(driver, form_url)).execute(listings)
        if screenshot_dir is not None:
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            driver.save_screenshot(str(screenshot_dir / SCREENSHOT_NAME))
        return count
    finally:
        driver.quit()


## @brief Run the program.
## @param argv Command line arguments without the program name.
## @param fetcher Port that gets the page; defaults to the HTTP fetcher.
## @param driver_factory Creates the browser driver; defaults to Chrome.
## @param environ Environment variables; defaults to the process environment.
## @return The process exit code.
def main(
    argv: Sequence[str] | None = None,
    *,
    fetcher: PageFetcher | None = None,
    driver_factory: Callable[[bool], WebDriver] = create_chrome_driver,
    environ: Mapping[str, str] | None = None,
) -> int:
    """Scrape the listings and, unless --scrape-only, record them in the form."""
    args = build_parser().parse_args(argv)
    env = os.environ if environ is None else environ
    form_url = env.get(FORM_URL_ENV_VAR, "")
    if not args.scrape_only and not form_url:
        _LOG.error("Environment variable %s is not set", FORM_URL_ENV_VAR)
        return EXIT_USAGE
    page_fetcher = fetcher if fetcher is not None else RequestsPageFetcher()
    try:
        listings = ScrapeListings(page_fetcher, BeautifulSoupListingParser()).execute()
        if args.scrape_only:
            print_listings(listings)
            return EXIT_OK
        count = run_form(
            listings, form_url, args.headless, args.screenshot_dir, driver_factory
        )
    except (ScrapeError, FormError) as err:
        _LOG.error("%s", err, exc_info=err.__cause__ is not None)
        return EXIT_FAILURE
    _LOG.info("Submitted %d responses", count)
    return EXIT_OK
