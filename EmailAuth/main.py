from fastapi import FastAPI, Response, HTTPException, Depends
import smtplib
from email.mime.text import MIMEText
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas import LoginIn, RegisterIn
from database import get_db, engine, Base, SessionLocal
from models import User
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from uuid import uuid4

app = FastAPI()

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASS = os.getenv("GMAIL_PASSWORD")
BASE_URL = os.getenv("BASE_URL")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

Base.metadata.create_all(bind=engine)

pwd = CryptContext(schemes=["bcrypt"])

def create_jwt(email: str, expires_in_hours: int = 2) -> str:
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(hours=expires_in_hours)
    }
    print(payload)
    return jwt.encode(payload, SECRET_KEY, ALGORITHM)

def send_verification_email(to_email: str, token: str):
    msg = {}
    link = f"{BASE_URL}/verify?token={token}"
    msg["Subject"] = "Verification"
    msg  = MIMEText(f"hellllloooooooooooooo\n{link}")  
    msg["From"] = GMAIL_USER
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(GMAIL_USER, GMAIL_PASS)
        s.sendmail(GMAIL_USER, to_email, msg.as_string())

@app.get("/verify")
def verify(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(400, "Invalid @ 1st try")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(400, "User not found")
    if user.is_verified:
        raise HTTPException(400, "Email verified")
    user.is_verified = True
    db.commit()
    return {"message": "verifie"}

@app.post("/register")
def register(data: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(400, "Email already there")
    user = User(
        email = data.email,
        hashed_password = pwd.hash(data.password),
    )
    db.add(user)
    db.commit()
    verification_jwt = create_jwt(data.email, expires_in_hours=2)
    send_verification_email(data.email, verification_jwt)
    return {"message": "Check email"}

# @app.get("/")
# def homepage():
#     return {"message": "Home Page"}

@app.post("/login")
def login(data: LoginIn, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(404, "User not registered")
    if not pwd.verify(data.password, user.hashed_password):
        raise HTTPException(401, "Wrong password")
    if not user.is_verified:
        raise HTTPException(404, "verify first")
    session_jwt = create_jwt(data.email, expires_in_hours=2)
    return {"access_token": "user log in succesfull"}