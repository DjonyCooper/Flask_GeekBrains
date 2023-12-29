from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    status: str
    description: Optional[str] = None