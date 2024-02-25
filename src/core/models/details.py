import os
from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from beanie import Document
from pydantic import BaseModel
from pymongo import ASCENDING, IndexModel


class SiteMapLink(Document):
    url: str
    lastSeenOnSitemap: datetime
    scraped: bool
    isSneaker: Optional[bool] = None
    error: Optional[bool] = None

    class Settings:
        name = os.environ.get("SOLESEARCH_STOCKX_LINKS_COLLECTION", "stockx-links")
        indexes = [IndexModel([("url", ASCENDING)])]


class Audience(str, Enum):
    """
    The target audience for the product.

    Options:
    - Unisex
    - Men
    - Women
    - Boys
    - Girls
    - Kids
    - Toddler
    """

    UNISEX = "Unisex"
    MEN = "Men"
    WOMEN = "Women"
    BOYS = "Boys"
    GIRLS = "Girls"
    KIDS = "Kids"
    TODDLER = "Toddler"


class Links(BaseModel):
    """
    Links to the product on various sites.

    Attributes:
    - retail (Optional[str]): Link to the retail page.
    - stockx (Optional[str]): Link to the StockX listing.
    - goat (Optional[str]): Link to the GOAT listing.
    - stadium_goods (Optional[str]): Link to the Stadium Goods listing.
    - flight_club (Optional[str]): Link to the Flight Club listing.
    """

    retail: Optional[str] = None
    stockx: Optional[str] = None
    goat: Optional[str] = None
    stadium_goods: Optional[str] = None
    flight_club: Optional[str] = None


class Prices(BaseModel):
    """
    Prices for the product on various sites.

    Attributes:
    - retail (Optional[float]): The brand's price / MSRP.
    - stockx (Optional[float]): Current price on StockX.
    - goat (Optional[float]): Current price on GOAT.
    - stadium_goods (Optional[Union[float, dict, list]]): Prices on Stadium Goods (per-size pricing).
    - flight_club (Optional[float]): Current price on Flight Club.
    """

    retail: Optional[float] = None
    stockx: Optional[Any] = None
    goat: Optional[Any] = None
    stadium_goods: Optional[Any] = None
    flight_club: Optional[Any] = None


class Images(BaseModel):
    """
    Various images of the product.

    Attributes:
    - original (Optional[str]): Link to the default, full size image.
    - alternateAngles (Optional[List[str]]): Links to other angles of the product, if available.
    """

    original: Optional[str] = None
    alternateAngles: Optional[List[str]] = None
