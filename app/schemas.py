from pydantic import BaseModel,EmailStr,Field

class NewUser(BaseModel):
    username:str
    email:EmailStr
    password:str=Field(min_length=6,max_length=12)
    bio:str

class UserRespo(BaseModel):
    username:str
    email:EmailStr

class Newpost(BaseModel):
    title:str
    content:str
    published:bool=False

class PostRespo(Newpost):
    id:int

class login(BaseModel):
    email:EmailStr
    password:str=Field(min_length=6,max_length=12)


class TokenRespo(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    username:str
    email:EmailStr





