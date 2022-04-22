from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String


@dataclass
class User(db.Model):

    __tablename__ = "users"
    user_id: int
    name: str
    crm: str
    cpf: str
    city: str
    phone: str
    email: str

    user_id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    crm = Column(String(9), nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    city = Column(String(30), nullable=False)
    phone = Column(String(11), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
