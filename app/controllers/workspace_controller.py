from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.user_model import UserSchema
from app.models.workspace_model import Workspace, WorkspaceSchema
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
    workspace.users = user

    session.add(workspace)
    session.commit()

    return {
        "name": workspace.name,
        "local": workspace.local,
        "owner": schemaUser.dump(user),
    }, HTTPStatus.CREATED


def get_workspaces():
    workspaces = Workspace.query.all()

    return jsonify(WorkspaceSchema(many=True).dump(workspaces)), HTTPStatus.OK


def get_specific_workspace(id: int):
    workspace = Workspace.query.get(id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    return WorkspaceSchema().dump(workspace), HTTPStatus.OK


def update_workspace(id: int):
    session: Session = current_app.db.session

    data = request.json

    workspace = Workspace.query.get(id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(workspace, key, value)

    session.commit()

    return jsonify(workspace), HTTPStatus.OK


def delete_workspace(id: int):
    session: Session = current_app.db.session

    workspace = Workspace.query.get(id)

    if not workspace:
        return {"msg": "Workspace not Found"}, HTTPStatus.NOT_FOUND

    session.delete(workspace)
    session.commit()

    return {"msg": f"Workspace {workspace.name} deleted"}, HTTPStatus.OK
