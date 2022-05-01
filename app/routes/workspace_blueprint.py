from flask import Blueprint
from app.controllers import workspace_controller

bp = Blueprint("workspace", __name__, url_prefix="/workspaces")

bp.get("")(workspace_controller.get_workspaces)
bp.post("")(workspace_controller.create_workspace)
bp.get("/<int:id>")(workspace_controller.get_specific_workspace)
bp.post("/<int:workspace_id>")(workspace_controller.add_user_to_workspace)
bp.delete("/<int:workspace_id>")(workspace_controller.delete_workspace)
bp.get("/<int:workspace_id>/patients")(workspace_controller.
                                       get_workspace_patients_categories)
