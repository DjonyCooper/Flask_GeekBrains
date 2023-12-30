from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    secret: str