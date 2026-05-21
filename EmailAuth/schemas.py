from pydantic import BaseModel, EmailStr
from datetime import datetime

class RegisterIn(BaseModel):
    email:    EmailStr
    password: str

class LoginIn(BaseModel):
    email:    EmailStr
    password: str

# id
# name
# dob
# phone
# email
# hashed_password
# is_verified
# verification_token
# created_at
# updated_at