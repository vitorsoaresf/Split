from datetime import datetime
from http import HTTPStatus

from app.models import Data, DataSchema
from app.models.allergy_model import AllergySchema
from app.models.patient_model import PatientSchema
from app.models.tag_model import TagSchema
from app.services.tag_service import svc_create_alert_tag, svc_create_tag, svc_update_delete_tag
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required


@jwt_required()
def create_data() -> dict:
    """Create a new data.

    This controller will create a new data.

    Args:
        Receive no args.
        Get description, patient_id and user_id from request.
        Set status and date.

    Returns:
        A dict with the data created.

    Raises:
        ValidationError: If the data is not valid.
    """

    session: Session = current_app.db.session
    data = request.json
    schema = DataSchema()

    tags = data.pop("tags", [])
    alerts = data.pop("alerts", [])

    try:
        data["status"] = True
        data["date"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        schema.load(data)
        new_data = Data(**data)

        session.add(new_data)
        session.commit()

        svc_create_tag(tags, new_data, session)
        svc_create_alert_tag(alerts, new_data, session)
        session.commit()
        return schema.dump(new_data), HTTPStatus.CREATED

    except:
        return {"error": "Error creating data for patient"}, HTTPStatus.BAD_REQUEST


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

    list_data = Data.query.all()

    return (
        jsonify(
            [
                {
                    "data_id": data.data_id,
                    "status": data.status,
                    "description": data.description,
                    "date": data.date,
                    "patient": PatientSchema(only=["name"]).dump(data.patient),
                    "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(data.tags),
                }
                for data in list_data
            ]
        ),
        HTTPStatus.OK,
    )


def get_data_specific(data_id: int) -> dict:
    """Get a specific data.

    This controller will get a specific data.

    Args:
        Id: The id of the data.

    Returns:
        A dict with the data.

    Raises:
        Not found: If the data is not found.
    """

    data = Data.query.get(data_id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    return {
        "data_id": data.data_id,
        "status": data.status,
        "description": data.description,
        "date": data.date,
        "patient": PatientSchema(exclude=["allergies"]).dump(data.patient),
        "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(data.tags),
    }, HTTPStatus.OK


@jwt_required()
def update_data(data_id: int) -> dict:
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
    data_req = request.json

    tags = data_req.pop("tags", [])
    alerts = data_req.pop("alerts", [])
    data = Data.query.get(data_id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    try:
        svc_update_delete_tag(tags, alerts,  data, session)
        

        for key, value in data_req.items():
            setattr(data, key, value)

        session.commit()

    except:
        return {"error": "Error updating data"}, HTTPStatus.BAD_REQUEST

    return {
        "data_id": data.data_id,
        "status": data.status,
        "description": data.description,
        "date": data.date,
        "patient": PatientSchema(exclude=["allergies"]).dump(data.patient),
        "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(data.tags),
    }, HTTPStatus.OK


@jwt_required()
def delete_data(data_id: int) -> dict:
    """Delete a specific data.

    This controller will delete a specific data.

    Args:
        Id: The id of the data.

    Returns:
        A message with the data deleted.

    Raises:
        Not found: If the data is not found.
    """

    session: Session = current_app.db.session

    data = Data.query.get(data_id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    session.delete(data)
    session.commit()

    return {"msg": f"{data.description} deleted"}, HTTPStatus.OK
