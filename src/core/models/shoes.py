import re
from datetime import datetime
from typing import List

from pydantic import BaseModel

from core.models.details import Audience, Images, Links, Prices, Sizes


class Shoe(BaseModel):
    brand: str | None = None  # The shoe manufacturer
    sku: str | None = None  # Stock Keeping Unit, format typically differs by brand
    name: str | None = None  # Product name
    colorway: str | None = None  # Colorway of the shoe
    audience: List[Audience] | None = None  # See src.models.details.Audience
    releaseDate: datetime | None = None  # Release date in epoch time (milliseconds)
    released: bool | None = None  # true if product is available yet, false otherwise
    images: Images | None = None  # See src.models.details.Images
    links: Links | None = None  # See src.models.details.Links
    prices: Prices | None = None  # See src.models.details.Prices
    sizes: Sizes | None = None  # See src.models.details.Sizes
    description: str | None = None  # Long-form product description

    # def validate(self) -> None:
    #     """Validation will vary by brand, and should be implemented in each brand's respective class."""
    #     raise NotImplementedError("Validation not implemented for this brand.")


# sku: Usually of the form (ABC123-456) for Nike
# brand: Brand or collaborator if product is a collaboration, eg 'Jordan' or 'Off-White'
# name: Product name (generally includes title, subtitle, and colorway)


class Nike(Shoe):
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


class Puma(Shoe):
    masterId: str  # The Puma.com masterId in the Next.js state
    productId: str  # The Puma.com productId in the Next.js state

    def validate(self) -> None:
        if not self.sku or len(self.sku) == 0:
            raise ValueError("Puma SKU is required.")
        valid_sku = re.compile(r"^[0-9]{6}_[0-9]{2}$")
        if not valid_sku.match(self.sku):
            raise ValueError(f"Puma SKU '{self.sku}' is invalid.")


class Adidas(Shoe):
    pass
