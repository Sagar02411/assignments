from dbservices.models import Hospital
from sqlalchemy.orm import Session
from service.schemas import HospitalCreate
# , HospitalUpdate, Hospital


def create_hospital(db: Session, data: HospitalCreate):
    
    hospital_instance = Hospital(name=data.name)
    db.add(hospital_instance)
    db.commit()
    db.refresh(hospital_instance)
    return hospital_instance
