from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from dbservices.database import Base
from fastapi import UploadFile,File
 
class Doctor(Base):
    __tablename__ = "doctors"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialization = Column(String)
    appointments = relationship("Appointment", back_populates="doctor",cascade="all, delete")
 
 
class Patient(Base):
    __tablename__ = "patients"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    image_file = Column(String,nullable=False)
    appointments = relationship("Appointment", back_populates="patient",cascade="all, delete")
 
 
class Appointment(Base):
    __tablename__ = "appointments"
 
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    time = Column(DateTime(timezone=True))
 
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")