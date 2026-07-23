from fastapi import APIRouter,HTTPException,status,Depends
from .. database import get_db
from sqlalchemy.orm import Session
from .. import models,schemas,utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post("/",response_model=schemas.TokenRespo)
def login(user:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user1=db.query(models.Users).filter(models.Users.email==user.username).first()
    if not user1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not utils.verify(user.password,user1.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return {
            "access_token": "...",
            "token_type": "bearer"
    }
    