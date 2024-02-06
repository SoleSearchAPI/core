from datetime import datetime
from enum import Enum
from typing import List, Optional

from beanie import Document, Indexed
from pydantic import BaseModel


class SiteMapLink(Document):
    def __init__(
        self,
        url: str,
        lastScraped: datetime,
        lastSeenOnSitemap: datetime,
        scraped: bool,
    ):
        self.url = url
        self.lastScraped = lastScraped
        self.lastSeenOnSitemap = lastSeenOnSitemap
        self.scraped = scraped

    url: Indexed(str, unique=True)
    lastScraped: datetime
    lastSeenOnSitemap: datetime
    scraped: bool


class Audience(str, Enum):
    UNISEX = "Unisex"
    MEN = "Men"
    WOMEN = "Women"
    BOYS = "Boys"
    GIRLS = "Girls"
    KIDS = "Kids"
    TODDLER = "Toddler"


class Links(BaseModel):
    retail: str | None = None  # Link to the retail page
    stockx: str | None = None  # Link to the StockX listing
    goat: str | None = None  # Link to the GOAT listing
    stadium_goods: str | None = None  # Link to the Stadium Goods listing


class Prices(BaseModel):
    retail: float | None = None  # The brand's price / MSRP
    stockx: float | dict | list | None = None  # Current price on stockX
    goat: float | dict | list | None = None  # Current price on GOAT
    stadium_goods: float | dict | list | None = (
        None  # Prices on Stadium Goods (per-size pricing)
    )


class Images(BaseModel):
    original: str | None = None  # Link to the head-on, full size image
    alternateAngles: List[str] | None = (
        None  # Links to other angles of the product, if available
    )


class Sizes(BaseModel):
    # sizes stores all available sizes converted to US Men's.
    # Methods are provided for converting to other sizes.
    # If a size is not available, it is not included in the list.
    sizes: List[str] | None = None
