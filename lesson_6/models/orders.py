from typing import Optional
from pydantic import BaseModel


class Order(BaseModel):
    id: int
    id_user: int
    id_product: int
    date: str
    status: str