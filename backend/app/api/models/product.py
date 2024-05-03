from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship

from backend.app.database import Base


class ProductType(Base):
    __tablename__ = "product_types"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

    products = relationship("Product", back_populates="product_type")


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    title = Column(Integer, index=True)
    product_code = Column(Integer, unique=True)
    rating = Column(Integer)
    reviews = Column(Integer)
    discount_price = Column(Float)
    price = Column(Float)
    wish_count = Column(Integer)
    available = Column(Boolean)

    product_types = relationship("ProductType", back_populates="product")
