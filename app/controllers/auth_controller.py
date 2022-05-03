from http import HTTPStatus
from flask import request
from sqlalchemy.orm import Session
from app.configs.database import db
from flask_jwt_extended import create_access_token
from app.models.user_model import User, UserSchema


def login():

    data: dict = request.get_json()

    session: Session = db.session

    try:

        user_email = data.pop("email")

        user_password = data.pop("password")

        user: User = session.query(User).filter_by(email=user_email).first()

        if not user:
            raise ValueError

        if not user.verify_password(user_password):
            raise ValueError

        access_token = create_access_token(identity=UserSchema().dump(user))
        return {"access_token": access_token}, HTTPStatus.OK

    except:
        return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
