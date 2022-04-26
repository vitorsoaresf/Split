from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.workspace_model import Workspace, WorkspaceSchema
from sqlalchemy.orm import Session


def create_workspace():
    session: Session = current_app.db.session
    data = request.json

    workspace = Workspace(**data)

    schema = WorkspaceSchema()

    schema.load(data)

    session.add(workspace)
    session.commit()

    response = schema.dump(workspace)

    return response, HTTPStatus.CREATED


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
