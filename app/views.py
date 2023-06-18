from . import app
from .routers import items, users
from fastapi import Depends, status, HTTPException
from .models.User import User, UserDataBase
from .dependencies import oauth2_scheme, OAuth2PasswordRequestForm
from .database.users import fake_users_db


app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def index():
    '''
        This is the main test route, the purpose of this route is to test the
        connection to the server.
    '''
    return {"message": "Hello World"}
