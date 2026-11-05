from house_prices.application.use_cases.fill_form import FillForm
from house_prices.domain.entities.listing import Listing


class FakeFormSubmitter:
    def __init__(self) -> None:
        self.submitted: list[Listing] = []

    def submit(self, listing: Listing) -> None:
        self.submitted.append(listing)


def make_listings(count: int) -> list[Listing]:
    return [
        Listing(link=f"http://x/{i}", price="$1", address=f"a{i}") for i in range(count)
    ]


def test_execute_submits_each_listing_in_order_and_returns_count() -> None:
    submitter = FakeFormSubmitter()
    listings = make_listings(3)

    count = FillForm(submitter).execute(listings)

    assert count == 3
    assert submitter.submitted == listings


def test_execute_returns_zero_for_no_listings() -> None:
    submitter = FakeFormSubmitter()

    assert FillForm(submitter).execute([]) == 0
    assert submitter.submitted == []
