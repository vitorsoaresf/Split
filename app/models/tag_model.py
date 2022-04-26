from app.configs.database import db
from sqlalchemy import ForeignKey, Integer, String, Column, Boolean
# from marshmallow import Schema, fields, validate, validates

class Tag(db.Model):

    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)
    data_id = Column(Integer, ForeignKey("datas.data_id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    alert_tag = Column(Boolean)

# class TagSchema(Schema):

#     tag = fields.String()
#     alert_tag = fields.Boolean()

#     @validates("tag")
#     def valida_n_char():
        