from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    """User model"""
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserDataBase(User):
    """User model with password"""
    hashed_password : str