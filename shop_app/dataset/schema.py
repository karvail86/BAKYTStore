from pydantic import BaseModel
from typing import Optional
from .models import  StatusChoices
from datetime import date

class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    age: Optional[int]
    phone_number: Optional[str]
    avatar: Optional[str]
    status: StatusChoices
    password: str
    date_register: date

class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    age: Optional[int]
    phone_number: Optional[str]
    avatar: Optional[str]
    password: str


class CategoryInputShema(BaseModel):
    category_image:str
    category_image: str


class CategoryOutShema(BaseModel):
    id: int
    category_image:str
    category_image: str

class SubCategorySchema(BaseModel):
    id: int
    subcategory_name: str
    category_id: int

class UserLoginSchema(BaseModel):
    username:str
    password: str