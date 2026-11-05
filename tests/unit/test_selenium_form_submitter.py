from typing import cast

import pytest
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from house_prices.constants import (
    FORM_CONFIRMATION_XPATH,
    FORM_INPUT_SELECTOR,
    FORM_SUBMIT_XPATH,
)
from house_prices.domain.entities.listing import Listing
from house_prices.domain.errors.form_error import FormError
from house_prices.infrastructure.selenium_form_submitter import (
    SeleniumFormSubmitter,
)

FORM_URL = "https://forms.example/test"
LISTING = Listing(link="http://x/1", price="$1,000", address="1 Main St")


class FakeElement:
    def __init__(
        self,
        events: list[tuple[str, str]],
        name: str,
        *,
        displayed: bool = True,
    ) -> None:
        self._events = events
        self._name = name
        self._displayed = displayed

    def is_displayed(self) -> bool:
        return self._displayed

    def is_enabled(self) -> bool:
        return True

    def send_keys(self, value: str) -> None:
        self._events.append(("type:" + self._name, value))

    def click(self) -> None:
        self._events.append(("click", self._name))


class FakeDriver:
    def __init__(
        self,
        *,
        inputs: int = 3,
        fail_get: bool = False,
        hidden_polls: int = 0,
    ) -> None:
        self.events: list[tuple[str, str]] = []
        self._inputs = inputs
        self._fail_get = fail_get
        ## Number of input lookups that still report the inputs as hidden.
        self._hidden_polls = hidden_polls

    def get(self, url: str) -> None:
        if self._fail_get:
            raise WebDriverException("boom")
        self.events.append(("get", url))

    def find_elements(self, by: str, value: str) -> list[FakeElement]:
        if value == FORM_INPUT_SELECTOR:
            displayed = self._hidden_polls <= 0
            self._hidden_polls -= 1
            return [
                FakeElement(self.events, f"input{i}", displayed=displayed)
                for i in range(self._inputs)
            ]
        if value == FORM_SUBMIT_XPATH:
            return [FakeElement(self.events, "submit")]
        if value == FORM_CONFIRMATION_XPATH:
            return [FakeElement(self.events, "confirmation")]
        raise NoSuchElementException(value)


def make(driver: FakeDriver) -> SeleniumFormSubmitter:
    return SeleniumFormSubmitter(cast(WebDriver, driver), FORM_URL, 0.01)


def test_submit_types_address_price_link_in_order() -> None:
    driver = FakeDriver()

    make(driver).submit(LISTING)

    typed = [e for e in driver.events if e[0].startswith("type:")]
    assert typed == [
        ("type:input0", "1 Main St"),
        ("type:input1", "$1,000"),
        ("type:input2", "http://x/1"),
    ]


def test_submit_clicks_submit_once_per_listing() -> None:
    driver = FakeDriver()
    submitter = make(driver)

    submitter.submit(LISTING)
    submitter.submit(LISTING)

    assert driver.events.count(("click", "submit")) == 2


def test_submit_navigates_to_form_url_per_listing() -> None:
    driver = FakeDriver()
    submitter = make(driver)

    submitter.submit(LISTING)
    submitter.submit(LISTING)

    assert driver.events.count(("get", FORM_URL)) == 2


def test_submit_raises_form_error_when_driver_fails() -> None:
    with pytest.raises(FormError) as info:
        make(FakeDriver(fail_get=True)).submit(LISTING)

    assert isinstance(info.value.__cause__, WebDriverException)


def test_submit_waits_until_inputs_are_displayed() -> None:
    driver = FakeDriver(hidden_polls=3)

    SeleniumFormSubmitter(cast(WebDriver, driver), FORM_URL, 5).submit(LISTING)

    typed = [e for e in driver.events if e[0].startswith("type:")]
    assert len(typed) == 3


def test_submit_raises_form_error_when_inputs_never_displayed() -> None:
    driver = FakeDriver(hidden_polls=10**9)

    with pytest.raises(FormError):
        make(driver).submit(LISTING)

    assert not any(e[0].startswith("type:") for e in driver.events)


def test_submit_raises_form_error_when_inputs_missing() -> None:
    driver = FakeDriver(inputs=2)

    with pytest.raises(FormError):
        make(driver).submit(LISTING)

    assert not any(e[0].startswith("type:") for e in driver.events)
