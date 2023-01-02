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
    return {"message": "Hello World"}

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     print(user_dict)
#     if not user_dict:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     user = UserDataBase(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

#     return {"access_token": user.username, "token_type": "bearer"}


# def fake_hash_password(password: str):
#     return "fake_hashed_" + password
# @app.get("/items2/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}


# def fake_hash_password(password: str):
#     return "fake_hashed_" + password

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     """
#         This endpoint is  used to validate the OAuth2 scheme
#     """
#     # Get the data user schema  from the database | None
#     user_dict = fake_users_db.get(form_data.username)
#     # Validate. Is there a User with that username?
#     if not user_dict:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     # Validate. Is the password correct?
#     # Get the user schema
#     user = UserDataBase(**user_dict)
#     real_password = user.hashed_password

#     hashed_password = fake_hash_password(form_data.password)
#     if hashed_password != real_password:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return {"access_token": user.username, "token_type": "bearer"}

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     # Get the user schema from the database | None
#     user = fake_users_db.get(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, 
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     return User(**user)

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     # Discriminate the disabled users 
#     if current_user.disabled:
#         # return current_user
#         raise HTTPException(
#             status_code=status.HTTP_406_NOT_ACCEPTABLE, 
#             detail="Inactive user",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return current_user


# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     # Get the User by the bearer token
#     return current_user

# @app.get('/')
# def index(): 
#     return {"message": "Hello World"}

# @app.get("/items/{id}")
# async def read_item(id: int, q: Union[str, None] = None):
#     return {"item_id": id, "q": q}


# @app.get("/items/{id}/name")
# async def read_item_name(id: int):
#     return {"item_id": id, "name": "Foo Bar"}

# @app.put("/items/{id}")
# def update_item(id: int, item: Item):
#     return {"item": item, "item_id": id}


# @app.post(r"/no_validate")
# def no_validate(item: Item):
#     return {"item": item}

# @app.post(r"/validate")
# @auth_required
# async def no_validate(item: Item):
#     return {"item": item}

# @app.post("/user/create")
# async def create_user(user: User):
#     return {"user": user}

# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}