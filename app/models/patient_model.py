from app.configs.database import db
from sqlalchemy import Integer, String, Column, Date, ForeignKey
from sqlalchemy.orm import relationship
from .patient_allergie_table import patients_allergies
from marshmallow import Schema, fields, validate, validates


class Patient(db.Model):

    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hospitalization_date = Column(Date)
    patient_code = Column(String)
    city = Column(String)
    profession = Column(String)
    marital_status = Column(String)
    responsible_guardian = Column(String)
    responsible_contact = Column(String)
    birth_date = Column(Date)
    workspace_id = Column(Integer, ForeignKey("workspaces.workspace_id"))
    allergies = relationship(
        "Allergy", secondary=patients_allergies, back_populates="patients"
    )

    workspace = relationship("Workspace", back_populates="patients")


class PatientSchema(Schema):

    patient_id = fields.Integer()
    name = fields.String()
    gender = fields.String()
    hospitalization_date = fields.Date()
    patient_code = fields.String()
    city = fields.String()
    profession = fields.String()
    marital_status = fields.String()
    responsible_guardian = fields.String()
    responsible_contact = fields.String()
    birth_date = fields.Date()
    allergies = fields.List(fields.String())
