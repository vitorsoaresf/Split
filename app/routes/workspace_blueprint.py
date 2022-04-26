from flask import Blueprint
from app.controllers import workspace_controller

bp = Blueprint("workspace", __name__, url_prefix="/workspaces")

bp.get("")(workspace_controller.get_workspaces)
bp.post("")(workspace_controller.create_workspace)
