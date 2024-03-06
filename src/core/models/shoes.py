from datetime import datetime
from typing import List, Optional

from beanie import Document
from beanie.odm.fields import PydanticObjectId
from pydantic import BaseModel, ConfigDict, Field
from pymongo import ASCENDING, DESCENDING, TEXT, IndexModel

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
        If unknown, set to None.
        If the release date has not been announced, set to "TBD".
    - released (Optional[bool]): Whether the product has been released yet.
    - images (Optional[Images]): See src.models.details.Images.
    - links (Optional[Links]): See src.models.details.Links.
    - prices (Optional[Prices]): See src.models.details.Prices.
    - sizes (Optional[List[float]]): List of available sizes, in US Men's.
    - description (Optional[str]): Long-form product description.
    - dateAdded (Optional[datetime]): Date and time the product was added to the db.
    - lastScraped (Optional[datetime]): Date and time the product was last scraped.
    - stadiumGoodsId (Optional[str]): The product's ID on Stadium Goods.
    - stockxId (Optional[str]): The product's ID on StockX.
    """

    brand: Optional[str] = ""
    sku: Optional[str] = ""
    name: Optional[str] = ""
    colorway: Optional[str] = ""
    audience: Optional[Audience] = Audience.UNISEX
    releaseDate: Optional[datetime | str | None] = None
    images: Optional[Images] = Images()
    links: Optional[Links] = Links()
    prices: Optional[Prices] = Prices()
    sizes: Optional[List[float]] = []
    description: Optional[str] = ""

    dateAdded: Optional[datetime] = datetime.utcnow()
    lastScraped: Optional[datetime] = datetime.utcnow()
    stadiumGoodsId: Optional[str] = ""
    stockxId: Optional[str] = ""
    source: Optional[str] = ""

    class Settings:
        name = "sneakers"
        keep_nulls = True
        indexes = [
            IndexModel(
                [
                    ("sku", TEXT),
                    ("stockxId", TEXT),
                    ("stadiumGoodsId", TEXT),
                    ("brand", TEXT),
                    ("name", TEXT),
                    ("colorway", TEXT),
                    ("audience", TEXT),
                ]
            ),
            IndexModel([("releaseDate", DESCENDING)]),
            IndexModel([("links.stockx", ASCENDING)]),
        ]


class SneakerView(BaseModel):
    productId: PydanticObjectId
    brand: Optional[str] = ""
    sku: Optional[str] = ""
    name: Optional[str] = ""
    colorway: Optional[str] = ""
    audience: Optional[Audience] = Audience.UNISEX
    releaseDate: Optional[datetime | str | None] = None
    images: Optional[Images] = Images()
    links: Optional[Links] = Links()
    prices: Optional[Prices] = Prices()
    sizes: Optional[List[float]] = []
    description: Optional[str] = ""

    model_config = ConfigDict(populate_by_name=True)

    class Settings:
        projection = {
            "productId": "$_id",
            "brand": 1,
            "sku": 1,
            "name": 1,
            "colorway": 1,
            "audience": 1,
            "releaseDate": 1,
            "images": 1,
            "links": 1,
            "prices": 1,
            "sizes": 1,
            "description": 1,
        }
