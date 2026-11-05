"""Port for submitting one listing to the form."""

from typing import Protocol

from house_prices.domain.entities.listing import Listing

## @file form_submitter.py
## @brief Port that records one listing as one form response.


## @class FormSubmitter
## @brief Port: records one listing as one form response.
class FormSubmitter(Protocol):
    """Records one listing as one form response."""

    ## @brief Submit one response.
    ## @param listing The listing to record.
    ## @throws FormError When the form cannot be filled or submitted.
    def submit(self, listing: Listing) -> None:
        """Record listing as one form response."""
        ...
