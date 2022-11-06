from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    # id: int
    name: str
    price: float
    is_offered: Union[bool, None] = None