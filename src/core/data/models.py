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


class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True)
    sneaker_id = Column(Integer, ForeignKey("sneaker.id"), nullable=False)
    platform = Column(Enum(Platform))
    position = Column(Integer)
    url = Column(Text, nullable=False)


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
