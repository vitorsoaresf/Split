from flask import Blueprint
from .user_blueprint import bp as bp_user
from .workspace_blueprint import bp as bp_workspace
from .patient_blueprint import bp as bp_patient
from .tag_blueprint import bp as bp_tag
from .data_blueprint import bp as bp_data
from .comment_blueprint import bp as bp_comment
from .auth_blueprint import bp as bp_auth
from .categorie_blueprint import bp as bp_categorie

bp_api = Blueprint("api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_auth)
bp_api.register_blueprint(bp_user)
bp_api.register_blueprint(bp_workspace)
bp_api.register_blueprint(bp_patient)
bp_api.register_blueprint(bp_tag)
bp_api.register_blueprint(bp_data)
bp_api.register_blueprint(bp_comment)
bp_api.register_blueprint(bp_categorie)
