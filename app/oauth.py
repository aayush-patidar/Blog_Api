from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone


SECRET_KEY="a33bcf6ed175125b9751111aa8a6aae8c0863cf70d25660cfdb567414894cb00"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def access_token(data:dict):
    to_encode=data.copy()
    exp_time=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"]=int(exp_time.timestamp())
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:str):
    jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM,])