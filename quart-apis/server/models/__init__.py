from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
import datetime
import uuid,datetime

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "esm_product"
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=str(uuid.uuid4()))
    name:Mapped[str] = mapped_column(nullable=False)
    model_no:Mapped[str] = mapped_column(nullable=False, unique=True)
    description:Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updated: Mapped[datetime.datetime] = mapped_column(nullable=True,onupdate=func.now())
    
    
class User(Base):
    __tablename__ = "esm_user"
    id:Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=str(uuid.uuid4()))
    email:Mapped[str] = mapped_column(nullable=False,unique=True)
    password:Mapped[str] = mapped_column(nullable=False)
    username:Mapped[str] = mapped_column(nullable=False,unique=True)
    profile:Mapped[str] = mapped_column(nullable=False,default=str("profile.png"))
    created: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updated: Mapped[datetime.datetime] = mapped_column(nullable=True,onupdate=func.now())
