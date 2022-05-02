from flask import current_app
from app.models.address_model import Address, AddressSchema

address_schema = AddressSchema()

def svc_create_address(address, session):
    address_schema.load(address)
    new_address = Address(**address)
    session.add(new_address)
    session.commit()
    return new_address

def svc_update_address(address_id, new_address, session):

    old_address = Address.query.get_or_404(address_id, description="Address ID not found!")

    for key, value in new_address.items():
        setattr(old_address, key, value)
    
    session.commit()

