from .database import Base
from sqlalchemy import Column,String,Integer,TIMESTAMP,text,Text,Boolean

class Users(Base):
    __tablename__="Users"
    id=Column(Integer,autoincrement=True,primary_key=True,index=True)
    username=Column(String,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    bio=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

class Posts(Base):
    __tablename__="Posts"
    id=Column(Integer,autoincrement=True,primary_key=True,index=True)
    title=Column(String,nullable=False)
    content=Column(Text,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    published=Column(Boolean,nullable=False,default=False)
