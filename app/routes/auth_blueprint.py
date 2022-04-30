from flask import Blueprint
from app.controllers import auth_controller

bp = Blueprint("auth", __name__, "/auth")

bp.get("")(auth_controller.login)