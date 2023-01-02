from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")