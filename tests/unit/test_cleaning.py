import pytest

from house_prices.domain.errors.scrape_error import ScrapeError
from house_prices.domain.rules.address_cleaning import clean_address
from house_prices.domain.rules.price_cleaning import clean_price


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("$2,895+/mo", "$2,895"),
        ("$2,798+ 1bd", "$2,798"),
        ("$1914+ 1 bd", "$1914"),
        ("$3,000", "$3,000"),
        ("  $1,200/mo  ", "$1,200"),
    ],
)
def test_clean_price_keeps_only_dollar_amount(raw: str, expected: str) -> None:
    assert clean_price(raw) == expected


def test_clean_price_raises_when_no_amount() -> None:
    with pytest.raises(ScrapeError):
        clean_price("call us")


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (
            "Parkmerced | 3711 19th Ave, San Francisco, CA",
            "Parkmerced 3711 19th Ave, San Francisco, CA",
        ),
        ("\n  12 Main St,\n   Oakland, CA  \n", "12 Main St, Oakland, CA"),
        ("A  |  B", "A B"),
        ("", ""),
    ],
)
def test_clean_address_gives_single_clean_line(raw: str, expected: str) -> None:
    assert clean_address(raw) == expected
