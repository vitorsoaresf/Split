from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from marshmallow import Schema, fields
from .users_workspaces_table import users_workspaces


class Workspace(db.Model):
    """Workspace class.

    This class represents some information about workspaces.

    Attributes:
        workspace_id: A unique integer value identifying the data.
        name: A string value with workspace name.
        local: A string field with workspace address.
    """

    __tablename__ = "workspaces"

    workspace_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    local = Column(String, nullable=False)

    users = db.relationship(
        "User",
        secondary=users_workspaces,
        back_populates="workspaces",
        uselist=True
    )

    patients = db.relationship(
        "Patient",
        back_populates="workspaces",
        uselist=True
        )


class WorkspaceSchema(Schema):
    """Workspace schema.

    This class represents the schema of the workspace class.
    Will check values and validate them.

    Attributes:
        workspace_id: A unique integer value identifying the data.
        name: A string value with workspace name.
        local: A string field with workspace address.
    """

    workspace_id = fields.Integer()
    owner_id = fields.Integer()
    name = fields.String()
    local = fields.String()
