from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer, String

from .users_workspaces_table import users_workspaces


class User(db.Model):
    """User class.

    This class represents information about users.

    Attributes:
        user_id: A unique integer value identifying the data.
        name: A string value with user name.
        profession_code: A string value with user profession code.
        cpf: A string value with user cpf.
        phone: A string value with user phone.
        email: A string value with user email.
        profession: A string value with user profession.
        password_hash: A string value with user password hash.

    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    profession_code = Column(String, nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    phone = Column(String(11), nullable=False)
    email = Column(String, nullable=False, unique=True)
    profession = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    address_id = Column(
        Integer,
        ForeignKey("address.address_id"),
        nullable=False,
        unique=True,
    )
    workspaces = db.relationship(
        "Workspace",
        secondary=users_workspaces,
        back_populates="users",
    )

    address = db.relationship("Address", back_populates="user")

    comments = db.relationship("Comment", back_populates="user", uselist=True)


class UserSchema(Schema):
    """User schema.

    This class represents the schema of the user class.
    Will check values and validate them.

    Attributes:
        user_id: A unique integer value identifying the data.
        name: A string value with user name.
        profession_code: A string value with user profession code.
        cpf: A string value with user cpf.
        phone: A string value with user phone.
        email: A string value with user email.
        profession: A string value with user profession.
    """

    user_id = fields.Integer()
    name = fields.String()
    profession_code = fields.String()
    cpf = fields.String()
    phone = fields.String()
    email = fields.String()
    profession = fields.String()
    password_hash = fields.String()
