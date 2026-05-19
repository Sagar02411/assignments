from sqlalchemy.orm import Session
import dbservices.models as models, service.schemas as schemas
 
def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    obj = models.Doctor(**doctor.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
 
def get_doctors(db: Session):
    return db.query(models.Doctor).all()
 
def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
 
def update_doctor(db: Session, doctor_id: int, doctor: schemas.DoctorUpdate):
    obj = get_doctor(db, doctor_id)
    if not obj:
        return None
 
    for key, value in doctor.dict(exclude_unset=True).items():
        setattr(obj, key, value)
 
    db.commit()
    db.refresh(obj)
    return obj
 
def delete_doctor(db: Session, doctor_id: int):
    obj = get_doctor(db, doctor_id)
    if not obj:
        return None
 
    db.delete(obj)
    db.commit()
    return obj

def create_patient(db: Session, patient: schemas.PatientCreate):
    obj = models.Patient(**patient.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
 
def get_patients(db: Session):
    return db.query(models.Patient).all()
 
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()
 
def update_patient(db: Session, patient_id: int, patient: schemas.PatientUpdate):
    obj = get_patient(db, patient_id)
    if not obj:
        return None
 
    for key, value in patient.dict(exclude_unset=True).items():
        setattr(obj, key, value)
 
    db.commit()
    db.refresh(obj)
    return obj
 
def delete_patient(db: Session, patient_id: int):
    obj = get_patient(db, patient_id)
    if not obj:
        return None
 
    db.delete(obj)
    db.commit()
    return obj
 
def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    obj = models.Appointment(**appointment.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
 
def get_appointments(db: Session):
    return db.query(models.Appointment).all()
 
def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
 
def update_appointment(db: Session, appointment_id: int, data: schemas.AppointmentUpdate):
    obj = get_appointment(db, appointment_id)
    if not obj:
        return None
 
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
 
    db.commit()
    db.refresh(obj)
    return obj
 
def delete_appointment(db: Session, appointment_id: int):
    obj = get_appointment(db, appointment_id)
    if not obj:
        return None
 
    db.delete(obj)
    db.commit()
    return obj