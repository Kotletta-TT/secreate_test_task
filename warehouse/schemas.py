from typing import List

from fastapi import Query
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    sku: str
    balance: int


class ProductCreate(ProductBase):
    category_id: int


class ProductUpdate(BaseModel):
    name: str = Query(None)
    sku: str = Query(None)
    category_id: int = Query(None)
    balance: int = Query(None)
    reserve: int = Query(None)


class Product(ProductBase):
    id: int
    name: str
    sku: str
    category_id: int
    balance: int
    reserve: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    name: str


class Category(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True
