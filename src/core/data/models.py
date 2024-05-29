from typing import Optional

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from core.data.enums import Audience, Platform

Base = declarative_base()


class Sneaker(Base):
    __tablename__ = "sneaker"

    id = Column(Integer, primary_key=True)
    brand = Column(Text)
    sku = Column(Text)
    name = Column(Text)
    colorway = Column(Text)
    audience = Column(Enum(Audience))
    release_date = Column(DateTime)
    description = Column(Text)
    stockx_id = Column(Text)
    stadium_goods_id = Column(Text)
    source = Column(Enum(Platform))
    date_added = Column(DateTime)
    last_scraped = Column(DateTime)
    links = relationship("Link", backref="sneaker")
    prices = relationship("Price", backref="sneaker")
    images = relationship("Image", backref="sneaker")
    sneaker_sizes = relationship("SneakerSize", backref="sneaker")

    def merge(self, other: Optional["Sneaker"] = None):
        if other:
            stockx_images = [
                img for img in other.images if img.platform == Platform.STOCKX
            ]
            if stockx_images:
                self.images = stockx_images

            if len(other.colorway) > len(self.colorway):
                self.colorway = other.colorway


class Link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    sneaker_id = Column(Integer, ForeignKey("sneaker.id"), nullable=False)
    platform = Column(Enum(Platform), nullable=False)
    url = Column(Text, nullable=False)


class Price(Base):
    __tablename__ = "price"

    sneaker_id = Column(
        Integer, ForeignKey("sneaker.id"), nullable=False, primary_key=True
    )
    size_id = Column(Integer, ForeignKey("size.id"), nullable=False, primary_key=True)
    platform = Column(Enum(Platform))
    amount = Column(BigInteger, nullable=False)
    size = relationship("Size", backref="prices")

    def merge(self, target):
        if self.platform == target.platform:
            if target.amount > 0:
                # TODO: Add price history record in SQL?
                self.amount = target.amount


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    sneaker_id = Column(Integer, ForeignKey("sneaker.id"), nullable=False)
    platform = Column(Enum(Platform), nullable=False)
    is_primary = Column(Boolean)
    url = Column(Text, nullable=False)

    def merge(self, target):
        if target.url and target.platform:
            for preference in [
                Platform.stockx,
                Platform.goat,
                Platform.retail,
                Platform.stadium_goods,
            ]:
                if preference == self.platform:
                    break
                if preference == target.platform:
                    self.url = target.url
                    self.platform = target.platform
                    break
            # TODO: save the changes to the current model


class Size(Base):
    __tablename__ = "size"

    id = Column(Integer, primary_key=True)
    size = Column(Integer, unique=True, nullable=False)
    sneaker_sizes = relationship("SneakerSize", backref="size")


class SneakerSize(Base):
    __tablename__ = "sneaker_size"

    sneaker_id = Column(Integer, ForeignKey("sneaker.id"), primary_key=True)
    size_id = Column(Integer, ForeignKey("size.id"), primary_key=True)


class Token(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True)
    platform = Column(Enum(Platform))
    type = Column(Text)
    value = Column(Text, nullable=False)
    expires = Column(DateTime)


class SitemapLink(Base):
    __tablename__ = "sitemap_link"

    url = Column(Text, primary_key=True)
    platform = Column(Enum(Platform))
    last_seen = Column(DateTime)
    scraped = Column(Boolean)
    ignored = Column(Boolean)
    error = Column(Boolean)


class Useragent(Base):
    __tablename__ = "useragent"

    id = Column(Integer, primary_key=True)
    useragent = Column(Text)
