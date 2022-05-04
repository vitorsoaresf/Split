from http import HTTPStatus
from flask import jsonify
from sqlalchemy.orm import Session
from app.configs.database import db
from app.models import Category


def get_categories():

    session : Session = db.session

    categories = session.query(Category).all()

    return jsonify([categorie.category for categorie in categories]), HTTPStatus.OK

