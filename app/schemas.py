from pydantic import BaseModel,EmailStr
from typing import Optional


class BasePost(BaseModel):
    title: str
    content: str
    publish: Optional[bool] = True
    rating: Optional[int] = None

    class Config:
        orm_mode = True  # Allow interaction with ORM models


class CreatePost(BasePost):
    pass  # No extra fields are needed; reusing BasePost fields


class UpdatePost(BaseModel):
    title: Optional[str] = None  # Fields are optional for partial updates
    content: Optional[str] = None
    publish: Optional[bool] = None
    rating: Optional[int] = None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    # name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True  # Allow interaction with ORM models

class UserOut(BaseModel):
    id: int
    # name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allow interaction with ORM models

class UserLogin(BaseModel):
    # name: str
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None
