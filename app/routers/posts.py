from fastapi import HTTPException,status,Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. database import get_db
from .. import models,schemas,oauth

router=APIRouter(
    prefix="/post",
    tags=["Posts"]
)

@router.get("/",response_model=List[schemas.PostRespo])
def get_post(db:Session=Depends(get_db),current=Depends(oauth.current_user)):
    post=db.query(models.Posts).all()
    return post

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostRespo)
def post_blog(post:schemas.Newpost,db:Session=Depends(get_db),current=Depends(oauth.current_user)):
    post=models.Posts(**post.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post

@router.get("/{id}",response_model=schemas.PostRespo)
def get_post(id:int,db:Session=Depends(get_db),current=Depends(oauth.current_user)):
    post=db.query(models.Posts).filter(models.Posts.id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return post

@router.put("/{id}",response_model=schemas.PostRespo)
def update_post(id:int,post:schemas.Newpost,db:Session=Depends(get_db),current=Depends(oauth.current_user)):
    update_post=db.query(models.Posts).filter(models.Posts.id==id).update(post.model_dump())
    if not update_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.commit()
    get_post=db.query(models.Posts).filter(models.Posts.id==id).first()

    return get_post

@router.delete("/{id}")
def del_post(id:int,db:Session=Depends(get_db),current=Depends(oauth.current_user)):
    post=db.query(models.Posts).filter(models.Posts.id==id).delete()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    db.commit()
    return post


