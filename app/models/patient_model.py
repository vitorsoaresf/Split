from datetime import datetime
from app.configs.database import db
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .patient_allergie_table import patients_allergies
from marshmallow import Schema, fields


class Patient(db.Model):

    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hospitalization_date = Column(DateTime, default=datetime.now().strftime("%d/%m/%Y"))
    cpf = Column(String,nullable=False)
    profession = Column(String)
    marital_status = Column(String)
    responsible_guardian = Column(String)
    responsible_contact = Column(String)
    internation = Column(Boolean)
    #Fix in controllers
    birth_date = Column(DateTime)

    workspace_id = Column(Integer, ForeignKey("workspaces.workspace_id"))
    address_id = Column(Integer, ForeignKey("address.address_id"))

    # não tratei a lista de alergias no POST e seu relacionamento com essa tabela Allergy
    allergies = relationship(
        "Allergy", secondary=patients_allergies, back_populates="patients"
    )
    workspace = relationship("Workspace", back_populates="patients")

    address = db.relationship(
        "Address", back_populates="patient", uselist=False
    )


class PatientSchema(Schema):

    patient_id = fields.Integer()
    name = fields.String()
    gender = fields.String()
    hospitalization_date = fields.Date()
    cpf = fields.String()
    profession = fields.String()
    marital_status = fields.String()
    responsible_guardian = fields.String()
    responsible_contact = fields.String()
    birth_date = fields.String()
    allergies = fields.List(fields.String())
