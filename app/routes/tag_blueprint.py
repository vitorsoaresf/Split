from flask import Blueprint
from app.controllers import tag_controller

bp = Blueprint("tags", __name__, url_prefix="/tags")

bp.post("")(tag_controller.create_tag)
bp.delete("/<int:tag_id>")(tag_controller.delete_tag)
