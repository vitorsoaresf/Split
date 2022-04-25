from app.configs.database import db
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields


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
    name = Column(String(256))
    local = Column(String(256))


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
    name = fields.String()
    local = fields.String()
