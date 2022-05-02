from http import HTTPStatus
from flask import request, current_app, jsonify
from sqlalchemy.orm import Session
from app.models.address_model import Address, AddressSchema
from app.models.allergy_model import Allergy, AllergySchema
from app.models.comment_model import CommentSchema
from app.models.data_model import DataSchema
from app.models.patient_model import Patient, PatientSchema
from app.models.tag_model import Tag, TagSchema
from app.models.workspace_model import Workspace, WorkspaceSchema


def create_patient() -> dict:
    """Create a new patient
    
    A controller to let the user create a new patient.
    
    Args:
        Receive no args.
        Get the name, gender, patient_code, profession, marital_status, responsible_guardian, 
        responsible_contact, birth_date, workspace, address and tags from the request.
    
    Returns:
        A json with the patient. HTTPStatus.CREATED if the patient was created.
        
    Raises:
        Error: if the workspace was not found.
        
    """
    
    session: Session = current_app.db.session
    data = request.json

    tags = data.pop("tags", [])
    alerts = data.pop("alerts", [])

    #Normalization
    data['name'] = data['name'].title()
    data['profession'] = data['profession'].title()
    data['responsible_guardian'] = data['responsible_guardian'].title()

    workspace_id = data.pop("workspace_id")
    workspace = Workspace.query.get(workspace_id)
    schemaWorkspace = WorkspaceSchema()
    if not workspace:
        # raise Exception
        return {"error": "Workspace not found"}

    address = data.pop("address", {})

    schemaAddress = AddressSchema()
    if address:
        schemaAddress.load(address)

    allergies = data.pop("allergies", [])

    list_allergies = []
    for allergy in allergies:
        
        #Normalization
        allergy = allergy.casefold()

        al = Allergy.query.filter_by(name=allergy).first()

        if not al:
            obj = {"name": allergy}

            schemaAllergy = AllergySchema()
            schemaAllergy.load(obj)

            al = Allergy(**obj)

            session.add(al)
            session.commit()

        list_allergies.append(al)

    # possivel erro de endereco com dados errados errado

    schema = PatientSchema()

    if address:
        res_address = Address(**address)
        session.add(res_address)
        session.commit()
        data["address_id"] = res_address.address_id

    data["workspace_id"] = workspace_id

    schema.load(data)
    patient = Patient(**data)

    patient.allergies.extend(list_allergies)

    session.add(patient)
    session.commit()


    for tag in tags:
        obj = {
            "tag": tag,
            "patient_id": patient.patient_id,
            "alert_tag": False,
        }
        new_tag = Tag(**obj)
        session.add(new_tag)
        patient.tags.append(new_tag)

    for alert in alerts:
        obj = {
            "tag": alert,
            "patient_id": patient.patient_id,
            "alert_tag": True,
        }
        new_tag = Tag(**obj)
        session.add(new_tag)
        patient.tags.append(new_tag)

    session.commit()

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
        "workspace": schemaWorkspace.dump(workspace),
        "address": schemaAddress.dump(address),
        "allergies": AllergySchema(many=True).dump(list_allergies),
        "tags": TagSchema(many=True).dump(patient.tags),
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
                    "allergies": AllergySchema(many=True).dump(patient.allergies),
                }
                for patient in patients
            ]
        ),
        HTTPStatus.OK,
    )


# implementar esse metodo
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
        "workspace_id": patient.workspace_id,
        "address": AddressSchema().dump(address),
        "datas": DataSchema(many=True).dump(patient.datas),
        "comments": CommentSchema(many=True).dump(patient.comments),
    }, HTTPStatus.OK


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


def update_patient(id: int):
    session: Session = current_app.db.session
    schema = PatientSchema()
    data = request.json

    patient = Patient.query.get(id)

    if not patient:
        return {"msg": "Patient not Found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(patient, key, value)

    session.commit()

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
        "workspace_id": patient.workspace_id,
        "address": AddressSchema().dump(patient.address),
        "datas": DataSchema(many=True).dump(patient.datas),
        "comments": CommentSchema(many=True).dump(patient.comments),
    }, HTTPStatus.OK
