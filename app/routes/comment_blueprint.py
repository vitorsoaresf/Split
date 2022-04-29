from flask import Blueprint
from app.controllers import comment_controller

bp = Blueprint("comments", __name__, url_prefix="/comments")

bp.post("")(comment_controller.create_comment)
bp.delete("/<int:id>")(comment_controller.delete_comment)
bp.patch("/<int:id>")(comment_controller.update_comment)
