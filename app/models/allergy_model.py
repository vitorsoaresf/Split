from app.configs.database import db
from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import relationship
from .patient_allergie_table import patients_allergies


class Allergy(db.Model):

    __tablename__ = "allergies"

    allergy_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


    patients = relationship("Patient",secondary=patients_allergies ,back_populates="allergies")
