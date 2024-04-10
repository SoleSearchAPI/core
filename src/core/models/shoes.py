from datetime import datetime
from typing import List, Optional

from beanie import Document
from beanie.odm.fields import PydanticObjectId
from pydantic import BaseModel, ConfigDict, Field
from pymongo import ASCENDING, DESCENDING, TEXT, IndexModel

from core.models.details import Audience, Images, Links, Prices


class Sneaker(Document):
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
    goatId: Optional[str] = ""
    tsdbId: Optional[str] = ""
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
