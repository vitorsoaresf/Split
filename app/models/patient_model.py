from app.configs.database import db
from sqlalchemy import Integer, String, Column, Date
from sqlalchemy.orm import relationship
from .patient_allergie_table import patients_allergies


class Patient(db.Model):

    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hospitalization_date = Column(Date)
    patient_code = Column(String)
    city = Column(String)
    profession= Column(String)
    marital_status = Column(String)
    responsible_guardian= Column(String)
    responsible_contact = Column(String)
    birth_date = Column(Date)


    allergies = relationship("Allergy",secondary=patients_allergies ,back_populates="patients")
