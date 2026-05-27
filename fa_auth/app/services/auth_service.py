from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import (hash_password,verify_password,create_access_token)
from app.core.email import(send_verification_email)
from uuid import uuid4
from datetime import datetime
from datetime import timedelta

def register_user(data, db: Session):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:

        return {
            "message": "Email already exists"
        }

    if data.password != data.confirm_password:

        return {
            "message": "Passwords do not match"
        }
    
    verification_token = str(uuid4())
    expiry = datetime.utcnow() + timedelta(minutes=15)

    new_user = User(
        name=data.name,
        email=data.email,
        phone=data.phone,
        hashed_password=hash_password(data.password),
        verification_token = verification_token,
        token_expiry = expiry, 
        is_verified = False
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    send_verification_email(new_user.email, verification_token)

    return {
        "message": "Registration Successfull. Verify your Email"
    }
def verify_email(token, db: Session):
    user = db.query(User).filter(User.verification_token == token).first()
    if not user:
        return {
            "message": "Invalid token"
            }

    if user.token_expiry < datetime.utcnow():
        return {
            "message": "Token expired"
            }
 
    user.is_verified = True
    user.verification_token = None
    user.token_expiry = None
 
    db.commit()
 
    return {
        "message":
        "Email verified successfully"
    }

def login_user(data, db: Session):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:

        return {
            "message": "User not found"
        }
    if not verify_password(data.password,user.hashed_password):

        return {
            "message": "Invalid credentials"
        }
    
    if not user.is_verified:
        return {
            "message": "Please verify your email before logging in"
        }

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }