from app.configs.database import db
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields


class User(db.Model):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    crm = Column(String(9), nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    city = Column(String(30), nullable=False)
    phone = Column(String(11), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)

    workspaces = db.relationship(
        "Workspace", secondary="users_workspaces", back_populates="users", uselist=True
    )


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
    crm = fields.String()
    cpf = fields.String()
    city = fields.String()
    phone = fields.String()
    email = fields.String()
