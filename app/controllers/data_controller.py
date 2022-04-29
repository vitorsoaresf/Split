from http import HTTPStatus

from app.models import Data, DataSchema
from flask import current_app, request
from sqlalchemy.orm import Session


def create_data() -> dict:
    """Create a new data.
    
    This controller will create a new data.
    
    Args:
        no args.
        
    Returns:
        A dict with the data created.
        
    Raises:
        ValidationError: If the data is not valid.
    """
    
    session: Session = current_app.db.session
    data = request.json
    schema = DataSchema()
    
    schema.load(data)
    new_data = Data(**data)

    session.add(new_data)
    session.commit()

    return schema.dump(new_data), HTTPStatus.CREATED


def get_data() -> dict:
    """Get all data.
    
    This controller will get all the data.
    
    Args:
        no args.
        
    Returns:
        A dict with all the data.
        
    Raises:
        No content: If there are no data.
    """
    schema = DataSchema(many=True)
    
    data = Data.query.all()

    return schema.dump(data), HTTPStatus.OK


def get_data_specific(id: int) -> dict:
    """Get a specific data.
    
    This controller will get a specific data.
    
    Args:
        Id: The id of the data.
        
    Returns:
        A dict with the data.
        
    Raises:
        Not found: If the data is not found.
    """
    schema = DataSchema()
    
    data = Data.query.get(id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    return schema.dump(data), HTTPStatus.OK


def update_data(id: int) -> dict:
    """Update a specific data.
    
    This controller will update a specific data.
    
    Args:
        Id: The id of the data.
        
    Returns:
        A dict with the data updated.
        
    Raises:
        Not found: If the data is not found.
    """
    session: Session = current_app.db.session
    data = request.json
    schema = DataSchema()
    
    schema.load(data)
    data = Data.query.get(id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(data, key, value)

    session.commit()

    return schema.dump(data), HTTPStatus.OK


def delete_data(id: int) -> dict:
    """Delete a specific data.
    
    This controller will delete a specific data.
    
    Args:
        Id: The id of the data.
        
    Returns:
        A dict with the data deleted.
        
    Raises:
        Not found: If the data is not found.
    """
    session: Session = current_app.db.session
    
    data = Data.query.get(id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    session.delete(data)
    session.commit()

    return {"msg": f"{data} deleted"}, HTTPStatus.OK
