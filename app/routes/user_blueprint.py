from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("")(user_controller.get_users)
bp.post("")(user_controller.create_user)
bp.get("/<int:id>")(user_controller.get_user_specific)
bp.delete("/<int:id>")(user_controller.delete_user)
bp.patch("/<int:id>")(user_controller.update_user)
bp.post("/login")(user_controller.login)
