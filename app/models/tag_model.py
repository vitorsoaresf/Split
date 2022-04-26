from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import ForeignKey, Integer, String, Column, Date, Boolean


@dataclass
class Tag(db.Model):

    tag: str

    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)
    data_id = Column(Integer, ForeignKey("datas.data_id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"))
    alert_tag = Column(Boolean)
