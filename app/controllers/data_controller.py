from http import HTTPStatus

from app.models import Data, DataSchema
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.patient_model import PatientSchema

from app.models.tag_model import Tag, TagSchema
from app.services.tag_service import svc_create_alert_tag, svc_create_tag


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
        svc_create_alert_tag(tags, new_data, session)     
        session.commit()
        return schema.dump(new_data), HTTPStatus.CREATED

    except:
        return {"error": "Invalid request"}, HTTPStatus.BAD_REQUEST


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
                    "tags": TagSchema(many=True, only=["tag"]).dump(data.tags),
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
    schema = DataSchema()

    data = Data.query.get(data_id)
    print(">>>>>", data)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    return {
        "data_id": data.data_id,
        "status": data.status,
        "description": data.description,
        "date": data.date,
        "patient": PatientSchema().dump(data.patient),
        "tags": TagSchema(many=True, only=["tag", "alert"]).dump(data.tags),
    }, HTTPStatus.OK


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
    schema = DataSchema()
    schema.load(data)
    tags = data.pop("tags", [])
    alerts = data.pop("alerts", [])
    data = Data.query.get(data_id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND
    
    svc_create_tag(tags, data, session)
    svc_create_alert_tag(alerts, data, session)

    for key, value in data_req.items():
        setattr(data, key, value)

    session.commit()

    return schema.dump(data), HTTPStatus.OK


def delete_data(data_id: int) -> dict:
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

    data = Data.query.get(data_id)

    if not data:
        return {"msg": "Data not Found"}, HTTPStatus.NOT_FOUND

    session.delete(data)
    session.commit()

    return {"msg": f"{data} deleted"}, HTTPStatus.OK
