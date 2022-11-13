from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    """User model"""
    username : str
    full_name : str | None  = None # optional
    email : str | None = None  # optional
    disabled: bool | None = False

class UserDataBase(User):
    """User model with password"""
    hashed_password : str