from flask import Flask
from app.configs import database, migrations
import os
from app import routes


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)

    return app
