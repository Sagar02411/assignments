from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.schemas.user_schema import UserRegister

from app.schemas.auth_schema import LoginSchema #TokenSchema

from app.core.database import get_db
from app.services.auth_service import (register_user,login_user,verify_email)

router = APIRouter(tags=["Authentication"])

@router.post("/register")
def register(user: UserRegister,db: Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(data, db)

@router.get("/verify-email")
def verify(token: str ,db: Session = Depends(get_db)):
    return verify_email(token, db)
