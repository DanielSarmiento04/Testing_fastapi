from app import app
from typing import Union
from app.decorators.decorators import auth_required
from app.models.Item import Item
from app.models.User import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from app.database.users import fake_users_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)

    return {"access_token": form_data.username, "token_type": "bearer"}





@app.get('/')
def index(): 
    return {"message": "Hello World"}

@app.get("/items/{id}")
async def read_item(id: int, q: Union[str, None] = None):
    return {"item_id": id, "q": q}


@app.get("/items/{id}/name")
async def read_item_name(id: int):
    return {"item_id": id, "name": "Foo Bar"}

@app.put("/items/{id}")
def update_item(id: int, item: Item):
    return {"item": item, "item_id": id}


@app.post(r"/no_validate")
def no_validate(item: Item):
    return {"item": item}

@app.post(r"/validate")
@auth_required
async def no_validate(item: Item):
    return {"item": item}

@app.post("/user/create")
async def create_user(user: User):
    return {"user": user}

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}