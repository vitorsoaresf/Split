from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Tag(db.Model):
    """Tag model.
    
    This model represents a tag of patients.
    
    Attributes:
        tag_id: A integer value indicating the tag id.
        tag: A string value indicating the tag name.
        data_id: A integer value indicating the data where the tag is attached.
        patient_id: A integer value indicating the patient where the tag is attached.
        alert_tag: A boolean value indicating if the tag is an alert tag.
    
    """

    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)
    data_id = Column(Integer, ForeignKey("datas.data_id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    alert_tag = Column(Boolean)


class TagSchema(Schema):
    """Tag model schema.
    
    This model represents the schema of tag of patients.
    Will check values and validate them.
    
    Attributes:
        tag_id: A integer value indicating the tag id.
        tag: A string value indicating the tag name.
        data_id: A integer value indicating the data where the tag is attached.
        patient_id: A integer value indicating the patient where the tag is attached.
        alert_tag: A boolean value indicating if the tag is an alert tag.
    """

    tag_id = fields.Integer()
    tag = fields.String()
    data_id = fields.Integer()
    patient_id = fields.Integer()
    alert_tag = fields.Boolean()