from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields


@dataclass
class User(db.Model):
    user_id: int
    name: str
    registro: str
    cpf: str
    city: str
    phone: str
    email: str
    funcao: str

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    registro = Column(String, nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    city = Column(String, nullable=False)
    phone = Column(String(11), nullable=False)
    email = Column(String, nullable=False, unique=True)
    funcao = Column(String, nullable=False)

    workspaces = db.relationship(
        "Workspace", secondary="users_workspaces", back_populates="users", uselist=True
    )

    address = db.relationship("Address", back_populates="address_id")
    # medico, enfermeiro, farmaceutico e nutricionista pode ser tabela ou verificação mesmo
    # numero de registro
    # patch,post e delete data, comments,category,
    # get somente patients, workspaces e users


class UserSchema(Schema):
    """User schema.

    This class represents the schema of the user class.
    Will check values and validate them.

    Attributes:
        user_id: An integer field to identify the user.
        name: An string field to identify the user.
        crm: An sequence number field to job identify the user.
        cpf: An sequence number field to identify the user.
        city: An string to identify where the user lives
        phone: An string to identify phone user
        email: An string to identify email user
    """

    user_id = fields.Integer()
    name = fields.String()
    registro = fields.String()
    cpf = fields.String()
    city = fields.String()
    phone = fields.String()
    email = fields.String()
    funcao = fields.String()
