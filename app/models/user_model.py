from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    profession_code = Column(String, nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    phone = Column(String(11), nullable=False)
    email = Column(String, nullable=False, unique=True)
    profession = Column(String, nullable=False)

    address_id = Column(
        Integer, ForeignKey("address.address_id"), nullable=False, unique=True
    )

    workspaces = db.relationship(
        "Workspace", secondary="users_workspaces", back_populates="users", uselist=True
    )

    address = db.relationship("Address", back_populates="user")
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
    profession_code = fields.String()
    cpf = fields.String()
    phone = fields.String()
    email = fields.String()
    profession = fields.String()
