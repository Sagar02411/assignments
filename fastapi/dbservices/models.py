from dbservices.db_config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, null

# print(Base.metadata.tables.keys())

class Patients(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    name = Column(String, index=True)
    age = Column(Integer)
    disease = Column(String)
    # image_file = Column(String, nullable=True, default=None)
    doctors = relationship("Doctor", back_populates="patients", cascade="all, delete")

    # @property
    # def image_path(srlf)

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    patients = relationship("Patients", back_populates = "doctors", cascade="all, delete")

class Hospital(Base):
    __tablename__ = "hospitals"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
