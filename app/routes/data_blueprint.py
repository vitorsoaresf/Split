from flask import Blueprint
from app.controllers import data_controller

bp = Blueprint("datas", __name__, url_prefix="/datas")

bp.post("")(data_controller.create_data)
bp.get("")(data_controller.get_data)
bp.get("/<int:data_id>")(data_controller.get_data_specific)
bp.patch("/<int:data_id>")(data_controller.update_data)
bp.delete("/<int:data_id>")(data_controller.delete_data)
