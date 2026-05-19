from fastapi import FastAPI, HTTPException, Depends
from databases import Database
from models import SessionLocal, Hospital



app = FastAPI()
db = SessionLocal()

@app.get("/home")
def read_root():
    return {"hello": "world"}
