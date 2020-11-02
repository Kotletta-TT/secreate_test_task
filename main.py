from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from warehouse import schemas, crud
from warehouse.database import SessionLocal
from warehouse.schemas import Product, Category

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/products/', response_model=List[schemas.Product], description='Get all products')
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.post('/product/', response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=product.sku)
    if db_product:
        raise HTTPException(status_code=400, detail='Product already exists')
    return crud.create_product(db=db, product=product)


@app.get('/product/{id}/', response_model=schemas.Product)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id=id)
    return product


@app.get('/product/', response_model=schemas.Product)
def get_product_by_sku(sku: str, db: Session = Depends(get_db)):
    product = crud.get_product_by_sku(db, sku=sku)
    return product


@app.post('/category/', response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail='Category already exists')
    return crud.create_category(db=db, category=category)


@app.delete('/product/{id}/')
def delete_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=id)
    if db_product:
        return crud.delete_product(db=db, id=id)


@app.delete('/product/')
def delete_product_by_sku(sku: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=sku)
    if db_product:
        return crud.delete_product(db=db, sku=sku)


@app.put('/product/', response_model=schemas.Product)
def update_product_by_sku(sku: str, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=sku)
    if db_product:
        return crud.update_product_by_sku(db=db, sku=sku, product=product)


@app.put('/product/{id}/', response_model=schemas.Product)
def update_product_by_id(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=id)
    if db_product:
        return crud.update_product_by_id(db=db, id=id, product=product)
