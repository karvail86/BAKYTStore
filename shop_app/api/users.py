from http.client import responses
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from shop_app.dataset.models import UserProfile
from shop_app.dataset.schema import UserProfileOutSchema, UserProfileInputSchema
from shop_app.dataset.db import SessionLocal
from sqlalchemy.orm import Session


user_router = APIRouter(prefix='/users', tags=['UserProfile'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post('/', response_model=UserProfileOutSchema)
async def create_user(user: UserProfileInputSchema, db: Session = Depends(get_db)):
    user_db = UserProfile(**user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@user_router.get('/', response_model=List[UserProfileOutSchema])
async def list_user(db: Session = Depends(get_db)):
    return db.query(UserProfile).all()

@user_router.get('/{user_id}', response_model=UserProfileOutSchema)
async def detail_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.id==user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail='is not found')

    return user