"""Creates the Chrome driver used to fill the form."""

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

from house_prices.constants import (
    CHROME_BIN_ENV_VAR,
    CHROME_WINDOW_SIZE,
    CHROMEDRIVER_PATH_ENV_VAR,
)

## @file chrome_driver_factory.py
## @brief Builds a Chrome WebDriver, headless when asked.


## @brief Create a Chrome driver.
## @param headless Run without a window (needed in a container).
## @return A started Chrome driver; the caller quits it.
## @note CHROME_BIN and CHROMEDRIVER_PATH, when set, name the binaries to use.
def create_chrome_driver(headless: bool) -> WebDriver:
    """Return a Chrome driver, headless when requested."""
    options = Options()
    chrome_bin = os.environ.get(CHROME_BIN_ENV_VAR)
    if chrome_bin:
        options.binary_location = chrome_bin
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={CHROME_WINDOW_SIZE}")
    driver_path = os.environ.get(CHROMEDRIVER_PATH_ENV_VAR)
    service = Service(executable_path=driver_path) if driver_path else Service()
    return webdriver.Chrome(options=options, service=service)
