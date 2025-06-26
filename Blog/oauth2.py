from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import generate_token


oauth_scheme =OAuth2PasswordBearer(tokenUrl='user/login') # tokenUrl is the endpoint where the token is generated

def get_current_user(token:str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
    
    return generate_token.verify_token(token,credentials_exception)