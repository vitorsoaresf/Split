from flask import Blueprint, Flask
from .api_blueprint import bp_api


def init_app(app: Flask):

    app.register_blueprint(bp_api)
