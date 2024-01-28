from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class SiteMapLink(BaseModel):
    url: str
    scraped: bool
    lastScraped: datetime


class Audience(str, Enum):
    UNISEX = "Unisex"
    MEN = "Men"
    WOMEN = "Women"
    BOYS = "Boys"
    GIRLS = "Girls"
    KIDS = "Kids"
    TODDLER = "Toddler"


class Links(BaseModel):
    retail: str = None  # Link to the retail page
    stockx: str = None  # Link to the StockX listing
    goat: str = None  # Link to the GOAT listing


class Prices(BaseModel):
    retail: float = None  # The brand's price / MSRP
    stockx: float = None  # Current price on stockX
    goat: float = None  # Current price on GOAT


class Images(BaseModel):
    original: str = None  # Link to the head-on, full size image
    alternateAngles: List[
        str
    ] = None  # Links to other angles of the product, if available


class Sizes(BaseModel):
    # sizes stores all available sizes converted to US Men's.
    # Methods are provided for converting to other sizes.
    # If a size is not available, it is not included in the list.
    sizes: List[int] = None
