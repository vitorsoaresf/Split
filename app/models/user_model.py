from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from marshmallow import Schema, fields
from .users_workspaces_table import users_workspaces


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
        Integer,
        ForeignKey("address.address_id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    workspaces = db.relationship(
        "Workspace",
        cascade="all,delete",
        secondary=users_workspaces,
        back_populates="users",
    )

    address = db.relationship("Address", cascade="all,delete", back_populates="user")


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
