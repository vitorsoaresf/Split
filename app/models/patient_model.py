from datetime import datetime

from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .patient_allergie_table import patients_allergies


class Patient(db.Model):
    """Patient model.

    This model represents a patient.

    Attributes:
        patient_id: A unique integer value identifying the patient.
        name: A string value with patient name.
        gender: A string indication the patient gender.
        hospitalization_date: A DateTime object indicating the day this
                              patient joined the institution.
        cpf: A string value with patient cpf.
        profession: A string value with patient profession.
        marital_status: A string value with patient marital status.
        responsible_guardian: A string value with patient responsible guardian.
        responsible_contact: A string value with patient responsible contact.
        internation: A boolean value indicating if patient is internated.
        birth_date: A DateTime object indicating the patient birth date.

        workspace_id: A id indicating the workspace this patient belongs to.
        address_id: A id indicating the address information about this patient.
    """

    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hospitalization_date = Column(
        DateTime, default=datetime.now().strftime("%d/%m/%Y"))
    cpf = Column(String, nullable=False)
    profession = Column(String)
    marital_status = Column(String)
    responsible_guardian = Column(String)
    responsible_contact = Column(String)
    internation = Column(Boolean)
    # Fix in controllers
    birth_date = Column(DateTime)

    workspace_id = Column(Integer, ForeignKey("workspaces.workspace_id"))
    address_id = Column(Integer, ForeignKey("address.address_id"))

    # não tratei a lista de alergias no POST e seu relacionamento com essa
    # tabela Allergy
    allergies = relationship(
        "Allergy", secondary=patients_allergies, back_populates="patients"
    )
    workspace = relationship("Workspace", back_populates="patients")

    address = db.relationship(
        "Address", back_populates="patient", uselist=False
    )

    datas = db.relationship(
        "Data", back_populates="patient", uselist=True
    )

    commments = db.relationship(
        "Comment", back_populates="patient", uselist=True
    )

class PatientSchema(Schema):
    """Patient Schema.

    This class represents the schema of the patient class.
    Will check values and validate them.

    Attributes:
        patient_id: A unique integer value identifying the data.
        name: A string value with patient name.
        gender: A string indication the patient gender.
        hospitalization_date: A DateTime object indicating the day this
                              patient joined the institution.
        cpf: A string value with patient cpf.
        profession: A string value with patient profession.
        marital_status: A string value with patient marital status.
        responsible_guardian: A string value with patient responsible guardian.
        responsible_contact: A string value with patient responsible contact.
        internation: A boolean value indicating if patient is internated.
        birth_date: A DateTime object indicating the patient birth date.

        allergies: A list of patient allergies.
    """

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
    address_id = fields.Integer()
    workspace_id = fields.Integer()
