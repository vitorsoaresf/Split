from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String


class Address(db.Model):
    """Address model.
    
    This class represents information about addresses.
    This class is used to store addresses of patients and users.
    
    Attributes:
        address_id: A unique integer value identifying the address.
        street: A string value indicating the street name.
        cep: A string value indicating the CEP code.
        number_house: A string value indicating the house number.
        complement: A string value indicating other information about address.
    
    """

    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    cep = Column(String(8), nullable=False)
    number_house = Column(String, nullable=False)
    complement = Column(String, nullable=False)

    user = db.relationship("User", back_populates="address", uselist=False)

    patient = db.relationship("Patient", back_populates="address", uselist=False)


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
