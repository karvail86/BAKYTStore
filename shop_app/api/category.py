from shop_app.dataset.models import Category
from shop_app.dataset.schema import CategoryOutShema, CategoryInputShema
from shop_app.dataset.db import SessionLocal
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from typing import List

category_router = APIRouter(prefix='/category')

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@category_router.post('/', response_model=CategoryOutShema)
async def create_category(category: CategoryInputShema, db: Session = Depends(get_db)):
   category_db = Category(**category.dict())
   db.add(category_db)
   db.commit()
   db.refresh(category_db)
   return category_db

@category_router.get('/',response_model=List[CategoryOutShema])
async def list_category(db: Session = Depends(get_db)):
   return db.query(Category).all()


@category_router.get('/{category_id}/', response_model=CategoryOutShema)
async def detail_category(category_id: int,  db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id==category_id).first()
    if not category:
        raise HTTPException(detail='Is not category', status_code=400)

    return category

@category_router.put('/{category_id}', response_model=dict)
async def update_category(category_id: int, category: CategoryOutShema,
                          db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Is not category', status_code=400)
    for category_key, category_value in category.dict().items():
        setattr(category_db, category_key, category_value)

        db.commit()
        db.refresh(category_db)
        return {'massage': 'category update'}

@category_router.delete('/{category_id}', response_model=dict)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Is not category', status_code=400)

    db.delete(category_db)
    db.commit()
    return {'massage', 'category delete'}