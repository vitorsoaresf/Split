from flask import Blueprint, Flask
from .user_route import bp as bp_user
from .patient_route import bp as bp_patient

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_patient)

    app.register_blueprint(bp_api)
