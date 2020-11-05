from typing import List

from fastapi import FastAPI, Depends, HTTPException
from smart_env.env import ENV
from sqlalchemy.orm import Session

from warehouse import schemas, crud
from warehouse.database import SessionLocal, Base, engine
from warehouse.schemas import Product, Category

app = FastAPI()

if ENV.TEST:
    Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/products/', response_model=List[schemas.Product], description='Get all products')
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_products = crud.get_products(db, skip=skip, limit=limit)
    if db_products:
        return db_products
    raise HTTPException(status_code=400, detail='No one product, please create product')


@app.get('/products/{category_id}', response_model=List[schemas.Product], description='Get products by category')
def get_products_by_category(category_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_products = crud.get_products_by_category(db, category_id=category_id, skip=skip, limit=limit)
    if db_products:
        return db_products
    raise HTTPException(status_code=400, detail='Not products in category or you input category_id incorrect')


@app.post('/product/', response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=product.sku)
    if db_product:
        raise HTTPException(status_code=400, detail='Product already exists')
    return crud.create_product(db=db, product=product)


@app.get('/product/{id}/', response_model=schemas.Product)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=id)
    if db_product:
        return db_product
    raise HTTPException(status_code=400, detail='No such id or you input incorrect id')


@app.get('/product/', response_model=schemas.Product)
def get_product_by_sku(sku: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=sku)
    if db_product:
        return db_product
    raise HTTPException(status_code=400, detail='No such SKU or you input incorrect SKU')


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
    raise HTTPException(status_code=400, detail='No such product, or incorrect input id')


@app.delete('/product/')
def delete_product_by_sku(sku: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=sku)
    if db_product:
        return crud.delete_product(db=db, sku=sku)
    raise HTTPException(status_code=400, detail='No such product, or incorrect input SKU')


@app.put('/product/', response_model=schemas.Product)
def update_product_by_sku(sku: str, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=sku)
    if db_product:
        return crud.update_product_by_sku(db=db, sku=sku, product=product)
    raise HTTPException(status_code=400, detail='No such product, or incorrect input parameters')


@app.put('/product/{id}/', response_model=schemas.Product)
def update_product_by_id(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=id)
    if db_product:
        return crud.update_product_by_id(db=db, id=id, product=product)
    raise HTTPException(status_code=400, detail='No such product, or incorrect input parameters')
