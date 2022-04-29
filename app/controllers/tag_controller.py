from http import HTTPStatus
from flask import current_app, request
from app.models.data_model import Data
from app.models.tag_model import Tag, TagSchema
from sqlalchemy.orm import Session
from app.models.patient_model import Patient


def create_tag():
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

    tag = Tag(**data)

    session.add(tag)
    session.commit()

    return schema.dump(tag), HTTPStatus.CREATED


def delete_tag(tag_id):
    session: Session = current_app.db.session
    tag = Tag.query.get(tag_id)

    if not tag:
        return {"error": "Tag not Found"}, HTTPStatus.BAD_REQUEST

    session.delete(tag)
    session.commit()

    return {"message": "Tag deleted"}, HTTPStatus.OK
