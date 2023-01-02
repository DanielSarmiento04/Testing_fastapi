from pydantic import BaseModel

class Item(BaseModel):
    # id: int
    name: str
    price: float
    is_offered: bool | None = None