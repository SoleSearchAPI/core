from datetime import datetime
from typing import List, Optional

from beanie import Document
from pymongo import DESCENDING, IndexModel

from core.models.details import Audience, Images, Links, Prices


class Sneaker(Document):
    """
    Represents information about a shoe.

    Attributes:
    - brand (Optional[str]): The shoe manufacturer.
    - sku (Indexed[str]): The Stock Keeping Unit, format typically differs by retailer.
    - name (Optional[str]): The product name.
    - colorway (Optional[str]): Colorway of the shoe.
    - audience (Optional[Audience]): Intended audience for the shoe.
    - releaseDate (Optional[datetime]): Date and time the shoe was released.
    - released (Optional[bool]): Whether the product has been released yet.
    - images (Optional[Images]): See src.models.details.Images.
    - links (Optional[Links]): See src.models.details.Links.
    - prices (Optional[Prices]): See src.models.details.Prices.
    - sizes (Optional[List[float]]): List of available sizes, in US Men's.
    - description (Optional[str]): Long-form product description.
    - dateAdded (Optional[datetime]): Date and time the product was added to the SoleSearch database.
    - lastScraped (Optional[datetime]): Date and time the product was last scraped.
    - stadiumGoodsId (Optional[str]): The product's ID on Stadium Goods.
    - stockxId (Optional[str]): The product's ID on StockX.
    """

    brand: Optional[str] = None
    sku: Optional[str] = None
    name: Optional[str] = None
    colorway: Optional[str] = None
    audience: Optional[Audience] = None
    releaseDate: Optional[datetime] = None
    released: Optional[bool] = None
    images: Optional[Images] = None
    links: Optional[Links] = None
    prices: Optional[Prices] = None
    sizes: Optional[List[float]] = None
    description: Optional[str] = None

    dateAdded: Optional[datetime] = None
    lastScraped: Optional[datetime] = None
    stadiumGoodsId: Optional[str] = None
    stockxId: Optional[str] = None

    class Settings:
        name = "sneakers"
        keep_nulls = True
        indexes = [IndexModel([("sku", DESCENDING)], unique=True)]
