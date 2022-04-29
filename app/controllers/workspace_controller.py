from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.user_model import UserSchema
from app.models.workspace_model import Workspace, WorkspaceSchema
from app.models.patient_model import Patient, PatientSchema
from sqlalchemy.orm import Session
from app.models import User


def create_workspace():
    session: Session = current_app.db.session
    data = request.json

    schemaUser = UserSchema()
    user = User.query.get(data["owner_id"])
    if not user:
        # return Exception
        return {"error": "User not Found"}, HTTPStatus.BAD_REQUEST

    schema = WorkspaceSchema()
    schema.load(data)

    workspace = Workspace(**data)
    workspace.users.append(user)

    session.add(workspace)
    session.commit()

    return {
        "name": workspace.name,
        "local": workspace.local,
        "owner": user.name,
        "workres": UserSchema(many=True).dump(workspace.users),
    }, HTTPStatus.CREATED


def get_workspaces():
    workspaces = Workspace.query.all()

    list_response = [
        {
            "name": workspace.name,
            "owner_id": workspace.owner_id,
            "workspace_id": workspace.workspace_id,
            "local": workspace.local,
            "users": UserSchema(many=True).dump(workspace.users),
        }
        for workspace in workspaces
    ]

    return jsonify(list_response), HTTPStatus.OK


def get_specific_workspace(id: int):
    workspace = Workspace.query.get(id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND
    # print(workspace.patients)
    return {
        "name": workspace.name,
        "owner_id": workspace.owner_id,
        "workspace_id": workspace.workspace_id,
        "local": workspace.local,
        "users": UserSchema(many=True).dump(workspace.users),
        "patients": workspace.patients,
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


def delete_workspace(id: int):
    session: Session = current_app.db.session

    workspace = Workspace.query.get(id)

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
        "users": UserSchema(many=True).dump(workspace.users),
    }, HTTPStatus.OK
