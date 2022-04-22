from flask import Blueprint
from .user_blueprint import bp as bp_user

bp_api = Blueprint("api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_user)
