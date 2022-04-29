from app.configs.database import db
from sqlalchemy import ForeignKey, Integer, String, Column, Boolean
from marshmallow import Schema, fields

class Tag(db.Model):

    __tablename__ = "tags"

    alert_tag = Column(Boolean)
    tag_id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)
    data_id = Column(Integer, ForeignKey("datas.data_id"))
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))

class TagSchema(Schema):

    tag = fields.String()
    alert_tag = fields.Boolean()

        