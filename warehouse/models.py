from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Product(Base):
    __tablename__ = 'warehouse_products'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(200), index=True, nullable=False)
    sku = Column(String(15), index=True, unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey('warehouse_category.id'))
    category = relationship('Category')
    balance = Column(Integer, nullable=False, default=0)
    reserve = Column(Integer, nullable=False, default=0)


class Category(Base):
    __tablename__ = 'warehouse_category'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(200))
