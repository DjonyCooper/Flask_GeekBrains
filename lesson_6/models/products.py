from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: int
    description: Optional[str] = None