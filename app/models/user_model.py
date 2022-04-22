from app.configs.database import db
from sqlalchemy import Column, Integer, String


class User(db.Model):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    crm = Column(String(9), nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    city = Column(String(30), nullable=False)
    phone = Column(String(11), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
