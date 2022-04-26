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
