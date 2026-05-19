from fastapi import FastAPI, Depends, HTTPException,  File, UploadFile, Response
from sqlalchemy.orm import Session
from service import services, schemas
from dbservices import models 
from dbservices.models import Hospital, Doctor, Patients
from dbservices.db_config import get_db, create_table, Base, engine
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import IO
import filetype
import os

import asyncio
from uuid import uuid4
import boto3
from botocore.exceptions import ClientError
import magic
from magic import libmagic 
from loguru import logger

from dotenv import load_dotenv
load_dotenv()

Base.metadata.create_all(bind=engine)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# from dbservices.db_config import Base
# print(Base.metadata.tables.keys())

@app.get("/")
def homepage():
    return "Home Page"

@app.post("/hospital", response_model=schemas.Hospital)
def create_new_hospital(data: schemas.HospitalCreate, db: Session = Depends(get_db)):

    return services.create_hospital(db, data)

@app.get("/hospitals", response_model=list[schemas.Hospital])
def get_all_hospital(db: Session = Depends(get_db)):

    return services.get_hospitals(db)

@app.get("/hospitals/{hospital_id}", response_model=schemas.Hospital)
def get_hospital_by_id(hospital_id : int, db: Session = Depends(get_db)):
    hospital_queryset = services.get_hospital(db, hospital_id)
    if not hospital_queryset:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital_queryset

@app.put("/hospitals/{hospital_id}", response_model=schemas.Hospital)
def update_hospital(hospital_id: int, data: schemas.HospitalCreate, db: Session = Depends(get_db)):

    db_update= services.update_hospital(db, hospital_id, data)
    if not db_update:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return db_update

@app.patch("/hospitals/{hospital_id}", response_model=schemas.Hospital)
def partial_update_hospital(hospital_id: int, data: schemas.HospitalUpdate, db: Session = Depends(get_db)):
    
    updated_hospital = services.patch_hospital(db, hospital_id, data)
    if not updated_hospital:
        raise HTTPException(status_code=404, detail="Hsopital not found")
    return updated_hospital

@app.delete("/hospitals/{hospital_id}", response_model=schemas.Hospital)
def delete_hospital(hospital_id: int, db: Session = Depends(get_db)):

    delete_entry = services.delete_hospital(db, hospital_id)
    if not delete_entry:
        raise HTTPException(status_code=404, detail="Hospital not found")   
    return delete_entry

@app.post("/doctor", response_model=schemas.Doctor)
def create_new_doctor(data: schemas.DoctorCreate, db: Session = Depends(get_db)):

    return services.create_doctor(db, data)

@app.get("/doctors", response_model=list[schemas.Doctor])
def get_all_hospital(db: Session = Depends(get_db)):

    return services.get_doctors(db)

@app.put("/doctors/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(doctor_id: int, data: schemas.DoctorCreate, db: Session = Depends(get_db)):

    db_update= services.update_doctor(db, doctor_id, data)
    if not db_update:
        raise HTTPException(status_code=404, detail="Doc not found")
    return db_update

@app.post("/patient", response_model=schemas.Patient)
def create_new_patient(data: schemas.PatientCreate, db: Session = Depends(get_db)):

    return services.create_patient(db, data)


# @app.get("/upload")
# def upload():
#     s3 = client('s3')
#     bucketName = "vb-python-intern-s3demo"
#     response = s3.generate_presigned_post(
#                 Bucket=bucketName,
#                 Key="data/",
#                 Conditions=None,
#                 ExpiresIn=3600
#             )
    
#     return {"url": response["url"], "fields": response["fields"]}


# @app.post("/uploadFile/")
# async def upload_file(file : UploadFile):
#     upload_directory = "./uploads"
#     file_location = f"./{upload_directory}/{file.filename}"

#     s3 = client('s3')
#     obj = boto3.client("s3")
#     obj.upload_file(
#         Filename=file.filename,
#         Bucket="vb-python-intern-s3demo",
#         Key="data/"
#     )
    
#     return {"filename" : f"{file.filename} saved at : {file_location}"}

session = boto3.Session(
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
)

KB = 1024
MB = 1024 * KB

SUPPORTED_FILE_TYPES = {
    'image/png': 'png',
    'image/jpeg': 'jpg',
    'application/pdf': 'pdf'
}

AWS_BUCKET = 'vb-python-intern-s3demo'

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket = s3.Bucket(AWS_BUCKET)

async def s3_upload(contents: bytes, key: str):
    logger.info(f'Uploading {key} to s3')
    bucket.put_object(Key=key, Body=contents)
    
    
async def s3_download(key: str):
    try:
        return s3.Object(bucket_name=AWS_BUCKET, key=key).get()['Body'].read()
    except ClientError as err:
        logger.error(str(err))


@app.post('/upload')
async def upload(file: UploadFile | None = None):
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='No file found!!'
        )

    contents = await file.read()
    size = len(contents)

    if not 0 < size <= 1 * MB:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Supported file size is 0 - 1 MB'
        )

    file_type = magic.from_buffer(buffer=contents, mime=True)
    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Unsupported file type: {file_type}. Supported types are {SUPPORTED_FILE_TYPES}'
        )
    file_name = f'{uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}'
    await s3_upload(contents=contents, key=f"Anshika/{file_name}")
    return {'file_name': file_name}


@app.get('/download')
async def download(file_name: str | None = None):
    if not file_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='No file name provided'
        )

    contents = await s3_download(key=file_name)
    return Response(
        content=contents,
        headers={
            'Content-Disposition': f'attachment;filename={file_name}',
            'Content-Type': 'application/octet-stream',
        }
    )
