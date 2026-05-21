from sqlalchemy import Column, String,Boolean,TIMESTAMP,Integer
from database import Base
from sqlalchemy.sql.expression import text
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    verification_token = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default = text('now()'))