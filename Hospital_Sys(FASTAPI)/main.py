from fastapi import FastAPI, Depends, HTTPException,UploadFile,File,status
from sqlalchemy.orm import Session
import dbservices.models as models, service.schemas as schemas, service.services as services
from dbservices.database import engine, SessionLocal, Base
import os
from fastapi.staticfiles import StaticFiles
import shutil
import boto3
import magic
from loguru import logger
from uuid import uuid4
 
Base.metadata.create_all(bind=engine)
# KB = 1024
# MB = 1024 * KB
# SUPPORTED_FILE_TYPES ={
#     'image/png': 'png',
#     'image/jpeg': 'jpg',
#     'application/pdf': 'pdf'
# }
# AWS_BUCKET = 'vb-python-intern-s3demo'
# s3 = boto3.resource('s3')
# bucket = s3.Bucket(AWS_BUCKET)

# async def s3_upload(contents:bytes, key:str):
#     logger.info(f"Uploading {key} to s3")
#     bucket.put_object(Key=key, Body=contents)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app.mount("/files",StaticFiles(directory=UPLOAD_DIR), name="files")

@app.post("/doctors")
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return services.create_doctor(db, doctor)
 
@app.get("/doctors")
def get_doctors(db: Session = Depends(get_db)):
    return services.get_doctors(db)
 
@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    obj = services.get_doctor(db, doctor_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return obj
 
@app.patch("/doctors/{doctor_id}")
def update_doctor(doctor_id: int, doctor: schemas.DoctorUpdate, db: Session = Depends(get_db)):
    obj = services.update_doctor(db, doctor_id, doctor)
    if not obj:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return obj
 
@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    obj = services.delete_doctor(db, doctor_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Deleted successfully"}
 
@app.post("/patients")
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return services.create_patient(db, patient)
 
@app.get("/patients")
def get_patients(db: Session = Depends(get_db)):
    return services.get_patients(db)
 
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    obj = services.get_patient(db, patient_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Patient not found")
    return obj
 
@app.patch("/patients/{patient_id}")
def update_patient(patient_id: int, patient: schemas.PatientUpdate, db: Session = Depends(get_db)):
    obj = services.update_patient(db, patient_id, patient)
    if not obj:
        raise HTTPException(status_code=404, detail="Patient not found")
    return obj
 
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    obj = services.delete_patient(db, patient_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Deleted successfully"}
 
@app.post("/appointments")
def create_appointment(app_data: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return services.create_appointment(db, app_data)
 
@app.get("/appointments")
def get_appointments(db: Session = Depends(get_db)):
    return services.get_appointments(db)
 
@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    obj = services.get_appointment(db, appointment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return obj
 
@app.patch("/appointments/{appointment_id}")
def update_appointment(appointment_id: int, data: schemas.AppointmentUpdate, db: Session = Depends(get_db)):
    obj = services.update_appointment(db, appointment_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return obj
 
@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    obj = services.delete_appointment(db, appointment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Deleted successfully"}

# @app.post("/uploadfile/")
# def create_upload_file(file: UploadFile):
#     print(f"filr {file}")
#     print(f"type {type(file)}")
#     read
#     path ""
#     return {"filename": file.filename}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)
    
    if not filename:
        raise HTTPException(status_code=400, detail="File not selected")
    
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Creating an S3 access object
    obj = boto3.client("s3")
    # Uploading a png file to S3 in 
    # 'mygfgbucket' from local folder
    obj.upload_file(
        Filename=file_path,
        Bucket="vb-python-intern-s3demo",
        Key=f"Devansh/{filename}"
    )

    return{
        "message":"File Uploaded successfully",
        "fileName":filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }
    

@app.get("/get-file/{filename}")
def get_file_from_s3(filename: str):
    obj = boto3.client("s3")

    try:
        url = obj.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": "vb-python-intern-s3demo",
                "Key": f"Devansh/{filename}"
            },
            ExpiresIn=3600 
        )
        return {"file_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @app.post("/upload2")
# async def upload(file: UploadFile | None = None):
#     if not file:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail='No file found'
#         )
#     contents =await file.read()
#     size = len(contents)

#     if not 0 < size <= 1 * MB:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail='No file found')
    
#     file_type = magic.from_buffer(buffer=contents, mime =True)
#     if file_type not in SUPPORTED_FILE_TYPES:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail='UNSUPPORTED FILE TYPE'
#         ) 

#     await s3_upload(contents=contents,key=f'Devansh/{uuid4()}.{SUPPORTED_FILE_TYPES[file_type]}')
