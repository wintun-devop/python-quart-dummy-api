""" 
#sql alchemy relation reference
https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many


"""
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func,ForeignKey
from typing import List
import datetime
import uuid,datetime

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "esm_product"
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=str(uuid.uuid4()))
    name:Mapped[str] = mapped_column(nullable=False)
    model_no:Mapped[str] = mapped_column(nullable=False, unique=True)
    price:Mapped[float] = mapped_column(nullable=True,default=0)
    qty:Mapped[int] = mapped_column(nullable=True,default=0)
    country_origin:Mapped[str] = mapped_column(nullable=True)
    description:Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updated: Mapped[datetime.datetime] = mapped_column(nullable=True,onupdate=func.now())
    order: Mapped[List["Order"]] = relationship(back_populates="product")
    
class User(Base):
    __tablename__ = "esm_user"
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=str(uuid.uuid4()))
    email:Mapped[str] = mapped_column(nullable=False,unique=True)
    password:Mapped[str] = mapped_column(nullable=False)
    username:Mapped[str] = mapped_column(nullable=False,unique=True)
    profile:Mapped[str] = mapped_column(nullable=False,default=str("profile.png"))
    permission:Mapped[str] = mapped_column(nullable=False,default=str("customer"))
    created: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updated: Mapped[datetime.datetime] = mapped_column(nullable=True,onupdate=func.now())

#Product and Order is one to Many
class Order(Base):
    __tablename__ = "esm_order"
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=str(uuid.uuid4()))
    product_id: Mapped[str] = mapped_column(ForeignKey("esm_product.id"))
    product_price:Mapped[float] = mapped_column(nullable=False)
    product_qty:Mapped[int] = mapped_column(nullable=False)
    product: Mapped["Product"] = relationship(back_populates="order")
    
    





