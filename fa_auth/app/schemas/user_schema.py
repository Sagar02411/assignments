from pydantic import BaseModel
from pydantic import EmailStr

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    confirm_password: str
    # verification_token:str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True