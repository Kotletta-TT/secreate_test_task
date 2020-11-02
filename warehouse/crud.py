from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_sku(db: Session, sku: str):
    return db.query(models.Product).filter(models.Product.sku == sku).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_category_by_name(db: Session, name: int):
    return db.query(models.Category).filter(models.Category.name == name).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, sku=product.sku, balance=product.balance,
                                category_id=product.category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_product_by_id(db: Session, id: int):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def delete_product_by_sku(db: Session, sku: str):
    db_product = db.query(models.Product).filter(models.Product.sku == sku).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product_by_sku(db: Session, sku: str, product: schemas.ProductUpdate):
    new_params = product.dict()
    db_product = db.query(models.Product).filter(models.Product.sku == sku).first()
    for key, value in new_params.items():
        if value and hasattr(db_product, key):
            setattr(db_product, key, value)
    db.commit()
    return db_product


def update_product_by_id(db: Session, id: int, product: schemas.ProductUpdate):
    new_params = product.dict()
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    for key, value in new_params.items():
        if value and hasattr(db_product, key):
            setattr(db_product, key, value)
    db.commit()
    return db_product
