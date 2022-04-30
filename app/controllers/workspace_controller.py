from http import HTTPStatus

from app.models import User
from app.models.address_model import AddressSchema
from app.models.allergy_model import AllergySchema
from app.models.category_model import Category, CategorySchema
from app.models.comment_model import CommentSchema
from app.models.data_model import DataSchema
from app.models.patient_model import Patient, PatientSchema
from app.models.user_model import UserSchema
from app.models.workspace_model import Workspace, WorkspaceSchema
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from app.models.tag_model import TagSchema

def create_workspace():
    session: Session = current_app.db.session
    data = request.json

    user = User.query.get(data["owner_id"])
    if not user:
        return {"error": "User-owner not Found"}, HTTPStatus.BAD_REQUEST

    categories = data.pop("categories")

    list_categories = []
    for category in categories:
        ct = Category.query.filter_by(category=category).first()
        list_categories.append(ct)

    schema = WorkspaceSchema()
    schema.load(data)

    workspace = Workspace(**data)
    workspace.users.append(user)

    workspace.categories.extend(list_categories)

    session.add(workspace)
    session.commit()

    return {
        "name": workspace.name,
        "owner_id": workspace.owner_id,
        "workspace_id": workspace.workspace_id,
        "local": workspace.local,
        "categories": CategorySchema(many=True).dump(workspace.categories),
    }, HTTPStatus.CREATED


def get_workspaces():
    workspaces = Workspace.query.all()

    list_response = [
        {
            "name": workspace.name,
            "owner_id": workspace.owner_id,
            "workspace_id": workspace.workspace_id,
            "local": workspace.local,
            "categories": CategorySchema(many=True).dump(workspace.categories),
            "workers": UserSchema(many=True, exclude=["password_hash"]).dump(
                workspace.users
            ),
        }
        for workspace in workspaces
    ]

    return jsonify(list_response), HTTPStatus.OK


def get_specific_workspace(id: int):
    workspace = Workspace.query.get(id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    return {
        "name": workspace.name,
        "owner_id": workspace.owner_id,
        "workspace_id": workspace.workspace_id,
        "local": workspace.local,
        "categories": CategorySchema(many=True).dump(workspace.categories),
        "workers": UserSchema(many=True, exclude=["password_hash"]).dump(
            workspace.users
        ),
        "patients": [
            {   "info": {
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
                        "address": AddressSchema().dump(patient.address),
                        "tags":TagSchema(many=True).dump(patient.tags),
                        "allergies": AllergySchema(many=True).dump(patient.allergies)
                        },
                "datas": DataSchema(many=True).dump(patient.datas),
                "comments": CommentSchema(many=True).dump(patient.comments),
            }
            for patient in workspace.patients
        ],
    }, HTTPStatus.OK


def update_workspace(id: int):
    session: Session = current_app.db.session
    schema = WorkspaceSchema()
    data = request.json

    workspace = Workspace.query.get(id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(workspace, key, value)

    session.commit()

    return schema.dump(workspace), HTTPStatus.OK


def delete_workspace(workspace_id: int):
    session: Session = current_app.db.session

    workspace = Workspace.query.get(workspace_id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    session.delete(workspace)
    session.commit()

    return {"msg": f"Workspace {workspace.name} deleted"}, HTTPStatus.OK


def add_user_to_workspace(workspace_id: int):
    session: Session = current_app.db.session
    data = request.json

    user = User.query.get(data["user_id"])
    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    workspace = Workspace.query.get(workspace_id)
    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    workspace.users.append(user)

    session.commit()

    return {
        "name": workspace.name,
        "owner_id": workspace.owner_id,
        "workspace_id": workspace.workspace_id,
        "local": workspace.local,
        "workers": UserSchema(many=True, exclude=["password_hash"]).dump(
            workspace.users
        ),
    }, HTTPStatus.OK


def get_workspace_patients_categories(workspace_id: int):
    workspace = Workspace.query.get(workspace_id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    patients = workspace.patients

    workspace_categories = []
    for categorie in Category.query.all():
        if categorie.workspace_id == workspace_id:
            workspace_categories.append(categorie)

    return {
        "workspace_id": workspace.workspace_id,
        "name": workspace.name,
        "local": workspace.local,
        "owner_id": workspace.owner_id,
        "patients": PatientSchema(many=True).dump(patients),
        "categories": CategorySchema(many=True).dump(workspace_categories),
    }, HTTPStatus.OK
