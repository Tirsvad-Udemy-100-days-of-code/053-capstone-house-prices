"""The rental listing value object."""

from dataclasses import dataclass

## @file listing.py
## @brief The Listing value object.


## @class Listing
## @brief One rental listing with a clean price and address.
@dataclass(frozen=True, slots=True)
class Listing:
    """One rental listing with a clean price and address."""

    ## Absolute address of the listing page.
    link: str
    ## Price in the form "$1,234".
    price: str
    ## Single-line address without pipes or extra whitespace.
    address: str
