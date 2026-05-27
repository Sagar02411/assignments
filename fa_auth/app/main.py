from fastapi import FastAPI
from app.core.database import (Base,engine)
from app.routers import auth
from app.routers import user

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
