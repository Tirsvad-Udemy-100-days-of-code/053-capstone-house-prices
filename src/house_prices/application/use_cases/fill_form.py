"""Use case: record every listing in the form."""

from collections.abc import Iterable

from house_prices.application.ports.form_submitter import FormSubmitter
from house_prices.domain.entities.listing import Listing

## @file fill_form.py
## @brief Use case that submits one form response per listing.


## @class FillForm
## @brief Submits one form response per listing.
class FillForm:
    """Submits one form response per listing."""

    ## @brief Create the use case.
    ## @param submitter Port that submits one response.
    def __init__(self, submitter: FormSubmitter) -> None:
        """Store the port the use case works through."""
        ## Port that submits one response.
        self._submitter = submitter

    ## @brief Run the use case.
    ## @param listings The listings to record, in order.
    ## @return The number of responses submitted.
    ## @throws FormError When a response cannot be submitted.
    def execute(self, listings: Iterable[Listing]) -> int:
        """Submit each listing in order and return how many were submitted."""
        count = 0
        for listing in listings:
            self._submitter.submit(listing)
            count += 1
        return count
