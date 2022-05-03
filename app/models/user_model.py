from app.configs.database import db
from marshmallow import Schema, fields, validates
from sqlalchemy import Column, ForeignKey, Integer, String
import re
from werkzeug.security import generate_password_hash, check_password_hash
from app.services.exc import (
    InvalidCPF,
    InvalidCPFFormat,
    InvalidPhone,
    InvalidPhoneFormat,
    InvalidEmail,
)

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

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)


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

    @validates("cpf")
    def validate_cpf(self, value):
        """Validate cpf.

        Validate the cpf of the user.

        Args:
            value: A string value with user cpf.

        Returns:
            A string value with user cpf.

        Raises:
            InvalidCPF: If the cpf is not valid.
            InvalidCPFFormat: If the cpf is not in the correct format.

        """

        if not value.isdigit() or len(value) != 11:
            raise InvalidCPF("Invalid CPF")

        # if not re.match(r"(^\d{3}\.\d{3}\.\d{3}\-\d{2}$)", value):
        #     raise InvalidCPFFormat("Invalid CPF")

        return value

    @validates("phone")
    def validate_phone(self, value):
        """Validate phone.

        Validate the phone of the user.

        Args:
            value: A string value with user phone.

        Returns:
            A string value with user phone.

        Raises:
            InvalidPhone: If the phone is not valid.
            InvalidPhoneFormat: If the phone format is not in the correct format.

        """

        if not value.isdigit() or len(value) != 11:
            raise InvalidPhone("Invalid Phone")

        if not re.match(r"(^[0-9]{2})?(\s|-)?(9?[0-9]{4})-?([0-9]{4}$)", value):
            raise InvalidPhoneFormat("Invalid Phone format")

        return value

    @validates("email")
    def validate_email(self, value):
        """Validate email.

        Validate the email of the user.

        Args:
            value: A string value with user email.

        Returns:
            A string value with user email.

        Raises:
            InvalidEmail: If the email is not valid.

        """

        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
            raise InvalidEmail("Invalid email")

        return value
