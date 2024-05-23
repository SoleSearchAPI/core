from enum import Enum


class Platform(Enum):
    retail = "retail"
    stockx = "stockx"
    goat = "goat"
    stadium_goods = "stadium_goods"


class Audience(Enum):
    Unisex = "Unisex"
    Men = "Men"
    Women = "Women"
    Youth = "Youth"
    Toddler = "Toddler"
    Unknown = "Unknown"
