"""Selenium implementation of the FormSubmitter port."""

from typing import Literal

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from house_prices.constants import (
    FORM_CONFIRMATION_XPATH,
    FORM_INPUT_COUNT,
    FORM_INPUT_SELECTOR,
    FORM_SUBMIT_XPATH,
    FORM_TIMEOUT_SECONDS,
)
from house_prices.domain.entities.listing import Listing
from house_prices.domain.errors.form_error import FormError

## @file selenium_form_submitter.py
## @brief Fills and submits the Google Form with Selenium.


## @class SeleniumFormSubmitter
## @brief FormSubmitter that drives a browser through an injected driver.
class SeleniumFormSubmitter:
    """Fills and submits the form once per listing through a Selenium driver."""

    ## @brief Create the submitter.
    ## @param driver The browser driver; the caller owns and quits it.
    ## @param form_url Address of the form.
    ## @param timeout_seconds Seconds to wait for each form element.
    def __init__(
        self,
        driver: WebDriver,
        form_url: str,
        timeout_seconds: float = FORM_TIMEOUT_SECONDS,
    ) -> None:
        """Store the driver, the form address and the wait time."""
        ## The browser driver.
        self._driver = driver
        ## Address of the form.
        self._form_url = form_url
        ## Explicit wait that polls the page.
        self._wait = WebDriverWait(driver, timeout_seconds)

    ## @brief Submit one response.
    ## @param listing The listing to record.
    ## @throws FormError When the browser fails or an element does not appear.
    def submit(self, listing: Listing) -> None:
        """Open the form, type address, price and link, and submit."""
        try:
            self._driver.get(self._form_url)
            self._fill(listing)
            self._click_submit()
            self._wait.until(
                lambda drv: drv.find_elements(By.XPATH, FORM_CONFIRMATION_XPATH)
            )
        except WebDriverException as err:
            message = f"Could not submit {listing.link} to the form"
            raise FormError(message) from err

    ## @brief Type the three values into the inputs, in form order.
    ## @param listing The listing to type.
    def _fill(self, listing: Listing) -> None:
        """Type address, price and link into the first three text inputs."""
        inputs = self._wait.until(self._inputs_ready)
        values = (listing.address, listing.price, listing.link)
        for element, value in zip(inputs, values, strict=False):
            element.send_keys(value)

    ## @brief Return the text inputs once all are shown and enabled.
    ## @param drv The driver being polled.
    ## @return The inputs, or False while the page is still loading.
    @staticmethod
    def _inputs_ready(drv: WebDriver) -> list[WebElement] | Literal[False]:
        """Return the form inputs when the page can be typed into."""
        found = drv.find_elements(By.CSS_SELECTOR, FORM_INPUT_SELECTOR)
        if len(found) >= FORM_INPUT_COUNT and all(
            element.is_displayed() and element.is_enabled() for element in found
        ):
            return found
        return False

    ## @brief Click the submit button once it is present.
    def _click_submit(self) -> None:
        """Click the submit button."""
        buttons = self._wait.until(
            lambda drv: drv.find_elements(By.XPATH, FORM_SUBMIT_XPATH)
        )
        buttons[0].click()
