from dbservices.models import Hospital, Doctor, Patients
from sqlalchemy.orm import Session
from service.schemas import HospitalCreate, HospitalUpdate, DoctorCreate, Hospital, PatientCreate
import boto3


def create_hospital(db: Session, data: HospitalCreate):
    
    hospital_instance = Hospital(name=data.name)
    db.add(hospital_instance)
    db.commit()
    db.refresh(hospital_instance)
    return hospital_instance

def get_hospitals(db: Session):
    
    return db.query(Hospital).all()

def get_hospital(db: Session, hospital_id : int):
    
    return db.query(Hospital).filter(Hospital.id == hospital_id).first()

def update_hospital(db: Session, hospital_id: int, data: HospitalCreate):
    
    hospital_queryset = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if hospital_queryset:
        for key, value in data.model_dump().items():
            setattr(hospital_queryset, key, value)
        db.commit()
        db.refresh(hospital_queryset)
    return hospital_queryset

def patch_hospital(db: Session, hospital_id: int, data: HospitalCreate):

    hospital_queryset = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital_queryset:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(hospital_queryset, key, value)

    db.commit()
    db.refresh(hospital_queryset)
    return hospital_queryset

def delete_hospital(db: Session, hospital_id: int):
    
    hospital_queryset = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if hospital_queryset:
        db.delete(hospital_queryset)
        db.commit()
    return hospital_queryset

def create_doctor(db: Session, data: DoctorCreate):
    
    doc_instance = Doctor(**data.dict())
    db.add(doc_instance)    
    db.commit()
    db.refresh(doc_instance)
    return doc_instance

def get_doctors(db: Session):
    
    return db.query(Doctor).all()

def update_doctor(db: Session, doctor_id: int, data: DoctorCreate):
    
    doctor_queryset = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if doctor_queryset:
        for key, value in data.model_dump().items():
            setattr(doctor_queryset, key, value)
        db.commit()
        db.refresh(doctor_queryset)
    return doctor_queryset

def create_patient(db: Session, data: PatientCreate):
    
    obj = Patients(**data.dict())
    db.add(obj)    
    db.commit()
    db.refresh(obj)
    return obj

