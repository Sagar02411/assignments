from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    is_verified = Column(Boolean,default=False)
    verification_token = Column(String)
    token_expiry = Column(DateTime,nullable=True)