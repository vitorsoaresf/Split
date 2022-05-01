from http import HTTPStatus
from flask import request, current_app, jsonify
from sqlalchemy.orm import Session
from app.models.address_model import Address, AddressSchema
from app.models.patient_model import Patient, PatientSchema
from app.models.workspace_model import Workspace, WorkspaceSchema


def create_patient():
    session: Session = current_app.db.session
    data = request.json

    workspace_id = data.pop("workspace_id")
    workspace = Workspace.query.get(workspace_id)
    schemaWorkspace = WorkspaceSchema()
    if not workspace:
        # raise Exception
        return {"error": "Workspace not found"}

    address = data.pop("address")

    schemaAddress = AddressSchema()
    schemaAddress.load(address)

    # possivel erro de endereco com dados errados errado

    res_address = Address(**address)

    schema = PatientSchema()

    session.add(res_address)
    session.commit()

    data["address_id"] = res_address.address_id
    data["workspace_id"] = workspace_id

    schema.load(data)
    patient = Patient(**data)

    session.add(patient)
    session.commit()

    return {
        "_id": patient.patient_id,
        "name": patient.name,
        "gender": patient.gender,
        "cpf": patient.cpf,
        "profession": patient.profession,
        "marital_status": patient.marital_status,
        "responsible_guardian": patient.responsible_guardian,
        "responsible_contact": patient.responsible_contact,
        "birth_date": patient.birth_date,
        "workspace": schemaWorkspace.dump(workspace),
        "address": schemaAddress.dump(address),
    }


def get_patients():
    patients = Patient.query.all()

    # ele não retorna as amarrações com o ADDRESS e o WORKSPACE
    return jsonify(PatientSchema(many=True).dump(patients)), HTTPStatus.OK


# implementar esse metodo
def get_patient_specific(id: int):
<<<<<<< HEAD
    patient = Patient.query.get_or_404(id, description="Patienc not found!")
    workspace_id = patient.pop("workspace_id")
    workspace = Workspace.query.get_or_404(workspace_id, description="Workspace not found!")
    patient["workspace"] = workspace.name
    return jsonify(patient), 200

=======
    patient = Patient.query.get(id)
    schemaAddress = AddressSchema()

    if not patient:
        return {"msg": "Patient not Found"}, HTTPStatus.NOT_FOUND

    address = Address.query.get(patient.address_id)

    return {
        "_id": patient.patient_id,
        "name": patient.name,
        "gender": patient.gender,
        "cpf": patient.cpf,
        "profession": patient.profession,
        "marital_status": patient.marital_status,
        "responsible_guardian": patient.responsible_guardian,
        "responsible_contact": patient.responsible_contact,
        "birth_date": patient.birth_date,
        "workspace_id": patient.workspace_id,
        "address": schemaAddress.dump(address),
    }, HTTPStatus.OK
>>>>>>> b42826bcce0a5411e2e1cf084c0e58de145c421b


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

    return schema.dump(patient), HTTPStatus.OK
