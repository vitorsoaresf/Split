from http import HTTPStatus

from app.models.data_model import Data
from app.models.patient_model import Patient
from app.models.tag_model import Tag, TagSchema
from flask import current_app, request
from sqlalchemy.orm import Session


def create_tag() -> dict:
    """Create new Tags.
    
    A controller to let the user create tags for patients or data.
    
    Args:
        Receive no args.
        Get the name from request.
        
    Returns:
        A json with the new tag. HTTPStatus.CREATED if the tag was created.
        
    Raises:
        HTTPStatus.BAD_REQUEST: If the patient is not found.
        HTTPStatus.BAD_REQUEST: If the data is not found.
    
    """
    
    session: Session = current_app.db.session
    data = request.json

    keys = data.keys()

    if "patient_id" in keys:
        patient = Patient.query.get(data["patient_id"])

        if not patient:
            return {"error": "Patient not Found"}, HTTPStatus.BAD_REQUEST

    if "data_id" in keys:
        get_data = Data.query.get(data["data_id"])

        if not get_data:
            return {"error": "Data not Found"}, HTTPStatus.BAD_REQUEST

    schema = TagSchema()
    schema.load(data)

    #Normalization
    data['tag'] = data['tag'].casefold()

    tag = Tag(**data)

    session.add(tag)
    session.commit()

    return schema.dump(tag), HTTPStatus.CREATED


def delete_tag(tag_id: int) -> str:
    """Delete a tag.
    
    A controller to let the user delete a tag.
    
    Args:
        tag_id: The id of the tag to be deleted.
        
    Returns:
        A json with a msg: string with the name and a message. HTTPStatus.OK if the tag was deleted.
        
    Raises:
        HTTPStatus.NOT_FOUND: If the tag is not found.
    """
    
    session: Session = current_app.db.session
    tag = Tag.query.get(tag_id)

    if not tag:
        return {"error": "Tag not Found"}, HTTPStatus.BAD_REQUEST

    session.delete(tag)
    session.commit()

    return {"message": "Tag deleted"}, HTTPStatus.OK
