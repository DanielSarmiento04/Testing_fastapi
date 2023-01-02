from fastapi import APIRouter, Depends, HTTPException, status
from ..models.User import User, UserDataBase
from ..dependencies import oauth2_scheme, OAuth2PasswordRequestForm
from ..database.users import fake_users_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(oauth2_scheme)],
)

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

async def get_active_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@router.get("/")
def init():
    return {"module": "users"}

@router.get("/me")
async def read_users_me(current_user:User=Depends(get_active_current_user)):
    return current_user



@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    print(user_dict)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = UserDataBase(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


def fake_hash_password(password: str):
    return "fake_hashed_" + password

# @router.post("/token")
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


