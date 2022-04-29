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
    schema.load(data)

    session.add(res_address)
    session.commit()

    patient = Patient(**data)
    patient.address_id = res_address.address_id
    patient.workspace_id = workspace.workspace_id

    session.add(patient)
    session.commit()

    return {
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
    patient = Patient.query.get_or_404(id, description="Patienc not found!")
    workspace_id = patient.pop("workspace_id")
    workspace = Workspace.query.get_or_404(workspace_id, description="Workspace not found!")
    patient["workspace"] = workspace.name
    return jsonify(patient), 200



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
