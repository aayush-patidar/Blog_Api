from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from . import schemas
from fastapi import HTTPException,Depends,status
from fastapi.security.oauth2 import OAuth2PasswordBearer
oauth_scheme=OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY="a33bcf6ed175125b9751111aa8a6aae8c0863cf70d25660cfdb567414894cb00"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def access_token(data:dict):
    to_encode=data.copy()
    exp_time=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"]=int(exp_time.timestamp())
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:str,credentials_exception):
    try:
        #  in this we get this email and usrname from wthat we enter in that login form payload 
        check=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM,])
        email=check.get("email")
        name=check.get("username")
        if not email:
            raise credentials_exception
        token_data=schemas.TokenData(username=name,email=email)
        return token_data
    except JWTError as e:
        raise credentials_exception

def current_user(token:str=Depends(oauth_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not Verified",headers={"WWW-Authenticate":"Bearer"})
    return verify_token(token,credentials_exception)


