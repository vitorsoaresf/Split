from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import ForeignKey, Integer, String, Column, Date, Boolean

@dataclass
class Patient(db.Model):

    tag: str

    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False)
    data_id = Column(Integer, ForeignKey("datas.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id")) #verificar nomes da coluna id na tabelas patients e datas
    alert_tag = Column(Boolean)
