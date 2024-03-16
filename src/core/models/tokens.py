from datetime import datetime
from typing import Optional

from beanie import Document


class Token(Document):
    id: str
    value: str
    expires: Optional[datetime] = None

    class Settings:
        name = "OAuth"
