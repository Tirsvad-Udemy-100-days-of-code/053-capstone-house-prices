from pathlib import Path
from typing import cast

import pytest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from house_prices.constants import (
    FORM_CONFIRMATION_XPATH,
    FORM_INPUT_SELECTOR,
    FORM_SUBMIT_XPATH,
    FORM_URL_ENV_VAR,
)
from house_prices.presentation.cli import (
    EXIT_FAILURE,
    EXIT_OK,
    EXIT_USAGE,
    SCREENSHOT_NAME,
    main,
)

FIXTURE = Path(__file__).parent.parent / "fixtures" / "zillow_clone.html"


class FakeFetcher:
    def fetch(self) -> str:
        return FIXTURE.read_text(encoding="utf-8")


def forbidden_driver_factory(headless: bool) -> None:
    raise AssertionError("browser must not be opened")


def test_main_exits_2_when_form_url_missing() -> None:
    code = main(
        [],
        fetcher=FakeFetcher(),
        driver_factory=forbidden_driver_factory,  # type: ignore[arg-type]
        environ={},
    )

    assert code == EXIT_USAGE


def test_main_scrape_only_prints_lists_without_browser(
    capsys: pytest.CaptureFixture[str],
) -> None:
    code = main(
        ["--scrape-only"],
        fetcher=FakeFetcher(),
        driver_factory=forbidden_driver_factory,  # type: ignore[arg-type]
        environ={},
    )

    out = capsys.readouterr().out
    assert code == EXIT_OK
    assert "There are 44 links to individual listings in total:" in out
    assert "the 44 addresses are:" in out
    assert "the 44 prices are:" in out


class FakeElement:
    def __init__(self, driver: "FakeDriver", is_submit: bool) -> None:
        self._driver = driver
        self._is_submit = is_submit

    def send_keys(self, value: str) -> None:
        self._driver.typed.append(value)

    def click(self) -> None:
        if self._is_submit:
            self._driver.submits += 1

    def is_displayed(self) -> bool:
        return True

    def is_enabled(self) -> bool:
        return True


class FakeDriver:
    def __init__(self, *, fail_get: bool = False) -> None:
        self.typed: list[str] = []
        self.submits = 0
        self.quit_called = False
        self.screenshots: list[str] = []
        self._fail_get = fail_get

    def get(self, url: str) -> None:
        if self._fail_get:
            raise WebDriverException("boom")

    def find_elements(self, by: str, value: str) -> list[FakeElement]:
        if value == FORM_INPUT_SELECTOR:
            return [FakeElement(self, False) for _ in range(3)]
        if value in (FORM_SUBMIT_XPATH, FORM_CONFIRMATION_XPATH):
            return [FakeElement(self, value == FORM_SUBMIT_XPATH)]
        return []

    def save_screenshot(self, filename: str) -> bool:
        Path(filename).write_bytes(b"png")
        self.screenshots.append(filename)
        return True

    def quit(self) -> None:
        self.quit_called = True


ENV = {FORM_URL_ENV_VAR: "https://forms.example/test"}


def test_main_submits_one_response_per_listing_and_quits_driver() -> None:
    driver = FakeDriver()

    code = main(
        ["--headless"],
        fetcher=FakeFetcher(),
        driver_factory=lambda headless: cast(WebDriver, driver),
        environ=ENV,
    )

    assert code == EXIT_OK
    assert driver.submits == 44
    assert len(driver.typed) == 44 * 3
    assert driver.quit_called


def test_main_quits_driver_and_exits_1_when_form_error() -> None:
    driver = FakeDriver(fail_get=True)

    code = main(
        [],
        fetcher=FakeFetcher(),
        driver_factory=lambda headless: cast(WebDriver, driver),
        environ=ENV,
    )

    assert code == EXIT_FAILURE
    assert driver.quit_called


def test_main_saves_screenshot_into_screenshot_dir(tmp_path: Path) -> None:
    driver = FakeDriver()
    target = tmp_path / "shots"

    code = main(
        ["--screenshot-dir", str(target)],
        fetcher=FakeFetcher(),
        driver_factory=lambda headless: cast(WebDriver, driver),
        environ=ENV,
    )

    assert code == EXIT_OK
    assert (target / SCREENSHOT_NAME).read_bytes() == b"png"
    assert driver.quit_called
