import pytest
import requests

from house_prices.domain.errors.scrape_error import ScrapeError
from house_prices.infrastructure.requests_page_fetcher import RequestsPageFetcher


class FakeResponse:
    def __init__(self, text: str, status_code: int) -> None:
        self.text = text
        self._status_code = status_code

    def raise_for_status(self) -> None:
        if self._status_code >= 400:
            raise requests.HTTPError(str(self._status_code))


def test_fetch_sends_user_agent_and_accept_language(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sent: dict[str, str] = {}

    def fake_get(url: str, headers: dict[str, str], timeout: float) -> FakeResponse:
        sent.update(headers)
        return FakeResponse("<html></html>", 200)

    monkeypatch.setattr(requests, "get", fake_get)

    assert RequestsPageFetcher().fetch() == "<html></html>"
    assert "User-Agent" in sent
    assert "Accept-Language" in sent


def test_fetch_raises_scrape_error_on_http_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_get(url: str, headers: dict[str, str], timeout: float) -> FakeResponse:
        return FakeResponse("", 500)

    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(ScrapeError) as info:
        RequestsPageFetcher().fetch()
    assert isinstance(info.value.__cause__, requests.HTTPError)


def test_fetch_raises_scrape_error_on_connection_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_get(url: str, headers: dict[str, str], timeout: float) -> FakeResponse:
        raise requests.ConnectionError

    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(ScrapeError):
        RequestsPageFetcher().fetch()
