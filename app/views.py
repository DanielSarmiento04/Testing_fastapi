from app import app
from typing import Union
from app.decorators.decorators import auth_required
from app.models.Item import Item
from app.models.User import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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