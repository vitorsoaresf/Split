from http import HTTPStatus

from app.models.address_model import Address, AddressSchema
from app.models.allergy_model import AllergySchema
from app.models.patient_model import Patient, PatientSchema
from app.models.tag_model import TagSchema
from app.models.workspace_model import Workspace, WorkspaceSchema
from app.services.address_service import svc_create_address, svc_update_address
from app.services.allergy_service import svc_create_allergy, svc_update_allergy
from app.services.tag_service import (
    svc_create_alert_tag,
    svc_create_tag,
    svc_update_delete_tag,
)
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required


@jwt_required()
def create_patient() -> dict:
    """Create a new patient

    A controller to let the user create a new patient.

    Args:
        Receive no args.
        Get the name, gender, patient_code, profession, marital_status, responsible_guardian,
        responsible_contact, birth_date, workspace, address and tags from request.

    Returns:
        A json with the patient. HTTPStatus.CREATED if the patient was created.

    Raises:
        Error: if the workspace was not found.

    """

    session: Session = current_app.db.session
    data = request.json

    tags = data.pop("tags", [])
    alerts = data.pop("alerts", [])

    # Normalization
    data["name"] = data["name"].title()
    data["profession"] = data["profession"].title()
    data["responsible_guardian"] = data["responsible_guardian"].title()

    workspace_id = data.pop("workspace_id")
    workspace = Workspace.query.get(workspace_id)
    if not workspace:
        # raise Exception
        return {"error": "Workspace not found"}

    try:
        patient_address = data.pop("address", {})
        address = svc_create_address(patient_address, session)

        data["address_id"] = address.address_id

        allergies = data.pop("allergies", [])
        list_allergies = svc_create_allergy(allergies, session)

        data["workspace_id"] = workspace_id

        PatientSchema().load(data)
        patient = Patient(**data)

        patient.allergies.extend(list_allergies)

        session.add(patient)
        session.commit()

        svc_create_tag(tags, patient, session)
        svc_create_alert_tag(alerts, patient, session)
        session.commit()

    except:
        return {"error": "Error creating patient"}, HTTPStatus.BAD_REQUEST

    return {
        "_id": patient.patient_id,
        "name": patient.name,
        "gender": patient.gender,
        "patient_code": patient.patient_code,
        "profession": patient.profession,
        "marital_status": patient.marital_status,
        "responsible_guardian": patient.responsible_guardian,
        "responsible_contact": patient.responsible_contact,
        "birth_date": patient.birth_date,
        "workspace": WorkspaceSchema().dump(patient.workspace),
        "address": AddressSchema().dump(patient.address),
        "allergies": AllergySchema(many=True, only=["name"]).dump(patient.allergies),
        "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(patient.tags),
    }, HTTPStatus.CREATED


def get_patients():
    patients = Patient.query.all()

    # ele não retorna as amarrações com o ADDRESS e o WORKSPACE
    return (
        jsonify(
            [
                {
                    "_id": patient.patient_id,
                    "name": patient.name,
                    "gender": patient.gender,
                    "patient_code": patient.patient_code,
                    "profession": patient.profession,
                    "marital_status": patient.marital_status,
                    "responsible_guardian": patient.responsible_guardian,
                    "responsible_contact": patient.responsible_contact,
                    "birth_date": patient.birth_date,
                    "workspace": WorkspaceSchema().dump(patient.workspace),
                    "address": AddressSchema().dump(patient.address),
                    "allergies": AllergySchema(many=True, only=["name"]).dump(
                        patient.allergies
                    ),
                    "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(
                        patient.tags
                    ),
                }
                for patient in patients
            ]
        ),
        HTTPStatus.OK,
    )


def get_patient_specific(id: int):
    patient = Patient.query.get(id)

    if not patient:
        return {"msg": "Patient not Found"}, HTTPStatus.NOT_FOUND

    address = Address.query.get(patient.address_id)

    return {
        "_id": patient.patient_id,
        "name": patient.name,
        "gender": patient.gender,
        "patient_code": patient.patient_code,
        "profession": patient.profession,
        "marital_status": patient.marital_status,
        "responsible_guardian": patient.responsible_guardian,
        "responsible_contact": patient.responsible_contact,
        "birth_date": patient.birth_date,
        "workspace": WorkspaceSchema().dump(patient.workspace),
        "address": AddressSchema().dump(patient.address),
        "allergies": AllergySchema(many=True, only=["name"]).dump(patient.allergies),
        "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(patient.tags),
    }, HTTPStatus.OK


@jwt_required()
def delete_patient(id: int):
    session: Session = current_app.db.session
    patient = Patient.query.get(id)

    if not patient:
        # raise Exception
        return {"error": "Patient not Found"}

    session.delete(patient)
    session.commit()

    schema = PatientSchema()
    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def update_patient(id: int):
    session: Session = current_app.db.session
    data = request.json

    patient = Patient.query.get(id)
    if not patient:
        return {"msg": "Patient not Found"}, HTTPStatus.NOT_FOUND

    try:
        address = data.pop("address", {})
        address_id = patient.address_id
        svc_update_address(address_id, address, session)
        tags = data.pop("tags", [])
        alerts = data.pop("alert", [])
        svc_update_delete_tag(tags, alerts, patient, session)
        allergies = data.pop("allergies", [])
        svc_update_allergy(patient, allergies, session)

        for key, value in data.items():
            setattr(patient, key, value)

        session.commit()

    except:
        return {"error": "Error updating patient"}, HTTPStatus.BAD_REQUEST

    return {
        "_id": patient.patient_id,
        "name": patient.name,
        "gender": patient.gender,
        "patient_code": patient.patient_code,
        "profession": patient.profession,
        "marital_status": patient.marital_status,
        "responsible_guardian": patient.responsible_guardian,
        "responsible_contact": patient.responsible_contact,
        "birth_date": patient.birth_date,
        "workspace": WorkspaceSchema().dump(patient.workspace),
        "address": AddressSchema().dump(patient.address),
        "allergies": AllergySchema(many=True, only=["name"]).dump(patient.allergies),
        "tags": TagSchema(many=True, only=["tag", "alert_tag"]).dump(patient.tags),
    }, HTTPStatus.OK
