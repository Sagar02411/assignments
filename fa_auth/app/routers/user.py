from fastapi import APIRouter
from fastapi import Depends
from app.utils.dependencies import (
    get_current_user
)
router = APIRouter(tags=["Users"])

@router.get("/me")
def current_user(user=Depends(get_current_user)):
    return {
        "message": f"Welcome {user}"
    }