from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .patient_allergie_table import patients_allergies


class Allergy(db.Model):
    """Allergy model.
    
    This model represents a allergy of patients.
    
    Attributes:
        allergy_id: A integer value indicating the allergy id.
        allergy: A string value indicating the allergy name.
    
    """

    __tablename__ = "allergies"

    allergy_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


    patients = relationship("Patient",secondary=patients_allergies ,back_populates="allergies")


class AllergySchema(Schema):
    """Allergy Schema.
    
    This class represents the schema of the allergy class.
    Will check values and validate them.
    
    Attributes:
        allergy_id: A unique integer value identifying the data.
        name: A string value with allergy name.
    """

    allergy_id = fields.Integer()
    name = fields.String()
