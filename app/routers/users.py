from fastapi import APIRouter,HTTPException,status,Depends
from ..database import get_db
from .. import models,schemas,utils
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserRespo)
def new_user(user:schemas.NewUser,db:Session=Depends(get_db)):
    hash_pass=utils.hash(user.password)
    user.password=hash_pass
    user=models.Users(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{id}",response_model=schemas.UserRespo)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user

