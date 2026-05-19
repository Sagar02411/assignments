from pydantic import BaseModel
from fastapi import UploadFile,File
from typing import Optional
from datetime import datetime

class DoctorBase(BaseModel):
    name: str
    specialization: str
 
class DoctorCreate(DoctorBase):
    pass
 
class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
 
class Doctor(DoctorBase):
    id: int
    class Config:
        orm_mode = True
class PatientBase(BaseModel):
    name: str
    age: int
    
class PatientCreate(PatientBase):
    photo:str
    
 
class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
 
class Patient(PatientBase):
    id: int
    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    time: datetime
 
class AppointmentCreate(AppointmentBase):
    pass
 
class AppointmentUpdate(BaseModel):
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None
    time: Optional[datetime] = None
 
class Appointment(AppointmentBase):
    id: int
    class Config:
        orm_mode = True