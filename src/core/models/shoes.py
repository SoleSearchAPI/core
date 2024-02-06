import re
from datetime import datetime
from typing import List, Optional

from beanie import Document, Indexed

from core.models.details import Audience, Images, Links, Prices


class Sneaker(Document):
    """
    Represents information about a shoe.

    Attributes:
    - brand (Optional[str]): The shoe manufacturer.
    - sku (Indexed[str]): Stock Keeping Unit, format typically differs by retailer.
    - name (Optional[str]): Product name.
    - colorway (Optional[str]): Colorway of the shoe.
    - audience (Optional[List[Audience]]): See src.models.details.Audience.
    - releaseDate (Optional[datetime]): Release date as datetime, which is converted to a native MongoDB date type.
    - released (Optional[bool]): Whether the product has been released yet.
    - images (Optional[Images]): See src.models.details.Images.
    - links (Optional[Links]): See src.models.details.Links.
    - prices (Optional[Prices]): See src.models.details.Prices.
    - sizes (Optional[List[float]]): List of available sizes, in US Men's.
    - description (Optional[str]): Long-form product description.
    """

    brand: Optional[str] = None
    sku: Indexed(str, unique=True)
    name: Optional[str] = None
    colorway: Optional[str] = None
    audience: Optional[List[Audience]] = None
    releaseDate: Optional[datetime] = None
    released: Optional[bool] = None
    images: Optional[Images] = None
    links: Optional[Links] = None
    prices: Optional[Prices] = None
    sizes: Optional[List[float]] = None
    description: Optional[str] = None

    class Settings:
        name = "sneakers"
        keep_nulls = True
        # bson_encoders = {}

    def validate(self) -> None:
        """Validation will vary by brand, and should be implemented in each brand's respective class."""
        raise NotImplementedError("Validation not implemented for this brand.")


class StadiumGoods(Sneaker):
    stadiumGoodsId: str = None  # The stadiumgoods.com id in the Redux state


# sku: Usually of the form (ABC123-456) for Nike
# brand: Brand or collaborator if product is a collaboration, eg 'Jordan' or 'Off-White'
# name: Product name (generally includes title, subtitle, and colorway)


class Nike(Sneaker):
    threadId: str = None  # The Nike.com threadId in the React state
    productId: str = None  # The Nike.com productId in the React state
    silhouette: str = None  # Silhoutte of the shoe (eg 'Jordan 1 High', 'Jordan 6')

    def validate(self) -> None:
        if not self.sku or len(self.sku) == 0:
            raise ValueError("Nike SKU is required.")
        valid_sku = re.compile(r"^[a-zA-Z0-9]{6}-[a-zA-Z0-9]{3}$")
        if not valid_sku.match(self.sku):
            raise ValueError(f"Nike SKU '{self.sku}' is invalid.")


# masterId: The id of the shoe, shared by all of its colorways
# productId: The id of this specific colorway


class Puma(Sneaker):
    masterId: str  # The Puma.com masterId in the Next.js state
    productId: str  # The Puma.com productId in the Next.js state

    def validate(self) -> None:
        if not self.sku or len(self.sku) == 0:
            raise ValueError("Puma SKU is required.")
        valid_sku = re.compile(r"^[0-9]{6}_[0-9]{2}$")
        if not valid_sku.match(self.sku):
            raise ValueError(f"Puma SKU '{self.sku}' is invalid.")


class Adidas(Sneaker):
    pass
