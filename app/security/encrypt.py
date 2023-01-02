from dotenv import dotenv_values

config = dotenv_values(".env")

SECRET_KEY = config.get("SECRET_TOKEN")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30