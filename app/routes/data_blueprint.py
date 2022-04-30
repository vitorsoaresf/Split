from flask import Blueprint
from app.controllers import data_controller

bp = Blueprint("comments", __name__, url_prefix="/comments")

bp.post("")(data_controller.create_data)
bp.get("")(data_controller.get_data)
bp.get("/<int:comment_id>")(data_controller.get_data_specific)
bp.get("/<int:comment_id>")(data_controller.update_data)
bp.delete("/<int:comment_id>")(data_controller.delete_data)