from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    """User model"""
    id: int
    name: str
    joined: date