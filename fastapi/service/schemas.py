from pydantic import BaseModel
from typing import Optional


class HospitalDetails(BaseModel):
    name: str
    class Config:
        from_attributes = True
        
class HospitalCreate(HospitalDetails):
    pass

class HospitalUpdate(HospitalDetails):
    name: Optional[str] = None

class Hospital(HospitalDetails):
    id: int
    class Config:
        from_attributes = True

class DoctorDetails(BaseModel):
    name: str
    class Config:
        from_attributes = True
    
class DoctorCreate(DoctorDetails):
    pass

class DoctorUpdate(DoctorDetails):
    name: Optional[str] = None
    

class Doctor(DoctorDetails):
    id: int

    class Config:
        from_attributes = True

class PatientDetails(BaseModel):
    name: str
    age: int
    disease: str
    doctor_id : int 
    # image_file : str | None
    # image_path : str
    
class PatientCreate(PatientDetails):
    pass

class PatientUpdate(PatientDetails):
    name: Optional[str] = None
    age: Optional[int] = None
    disease: Optional[str] = None
    doctor_id: Optional[int] = None
    
    class Config:
        # orm_mode = True
        from_attributes = True
        
class Patient(PatientDetails):
    id : int
    
    class Config:
        # orm_mode = True
        from_attributes = True