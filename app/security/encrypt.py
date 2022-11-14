from jose import JWTError, jwt
from dotenv import dotenv_values

config = dotenv_values(".env")
# to get a string like this run:
# openssl rand -hex 3
SECRET_KEY = config.get("SECRET_TOKEN")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30