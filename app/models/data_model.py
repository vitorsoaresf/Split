from app.configs.database import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from marshmallow import Schema, fields


class Data(db.Model):
    """Data class.

    This class represents some information about patients.


    Attributes:
        data_id: A unique integer value identifying the data.
        status: A boolean value.
        description: A string field to describe any conditions about the patient.
        date: A datetime field to indicate when the patient was created.

        patient_id: A integer value indicating the patient id.
        category_id: A foreign key to the category table.
    """

    __tablename__ = "datas"

    data_id = Column(Integer, primary_key=True)
    status = Column(Boolean)
    description = Column(String(256))
    date = Column(DateTime)

    patient_id = Column(Integer, db.ForeignKey("patients.patient_id"))
    category_id = Column(Integer, db.ForeignKey("categories.category_id"))

    patient = db.relationship("Patient", back_populates="datas", uselist=False)

    tags = db.relationship("Tag", back_populates="data", uselist=True)


class DataSchema(Schema):
    """Data schema.

    This class represents the schema of the data class.
    Will check values and validate them.

    Attributes:
        data_id: An integer field to identify the data.
        status: A boolean value.
        description: A string field to describe any conditions about the patient.
        date: A datetime field to indicate when the patient was created.

        patient_id: A integer value indicating the patient id.
        category_id: A foreign key to the category table.

    """

    data_id = fields.Integer()
    status = fields.Boolean()
    description = fields.String()
    date = fields.String()

    patient_id = fields.Integer()
    category_id = fields.Integer()
