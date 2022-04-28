from datetime import datetime
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
    hospitalization_date = Column(Date, default=datetime.now().strftime("%d %m %Y"))

    # pode mudar conforme a necessidade
    cpf = Column(String)

    profession = Column(String)
    marital_status = Column(String)
    responsible_guardian = Column(String)
    responsible_contact = Column(String)

    # Formato Date não aceita 01/01/01 - formatar para date no marshemelow
    # Coloquei como String só para efeturar o POST, mas estava com formato de Date
    birth_date = Column(String)

    workspace_id = Column(Integer, ForeignKey("workspaces.workspace_id"))
    address_id = Column(Integer, ForeignKey("address.address_id"))

    # não tratei a lista de alergias no POST e seu relacionamento com essa tabela Allergy
    allergies = relationship(
        "Allergy", secondary=patients_allergies, back_populates="patients"
    )

    workspace = relationship("Workspace", back_populates="patients")

    address = db.relationship(
        "Address", cascade="all,delete", back_populates="patient", uselist=False
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
