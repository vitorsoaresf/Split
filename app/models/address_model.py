from app.configs.database import db
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields


class Address(db.Model):

    address_id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    cep = Column(String(8), nullable=False)
    number_house = Column(String, nullable=False)
    complement = Column(String, nullable=False)
    user_id = Column(
        db.Integer, db.ForeignKey("users.user_id"), nullable=False, unique=True
    )

    user = db.relationship("User", back_populates="user_id")


class AddressSchema(Schema):
    """Address schema.

    This class represents the schema of the address class.
    Will check values and validate them.

    Attributes:
        address_id: An integer field to identify the user.
        street: An string field to identify the street.
        cep: An string field to identify the street.
        number_house: An sequence number field to job identify the house's number.
        complement: An sequence string field to identify the complement from house.
    """

    address_id = fields.Integer()
    street = fields.String()
    cep = fields.String()
    number_house = fields.String()
    complement = fields.String()
