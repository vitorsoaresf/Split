from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("")(user_controller.get_user)
