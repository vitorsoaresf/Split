from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.user_model import User
from sqlalchemy.orm import Session
from app.configs.database import db


def create_user():
    session: Session = current_app.db.session
    data = request.json

    user = User(**data)

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.CREATED


def get_user():

    users = User.query.all()

    print(">>>>>>>. ", users)

    # serializer_users = [user for user in users]
    # print(serializer_users)

    return jsonify(users)


def get_user_specific(id: int):
    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    return jsonify(user)


def update_user(id: int):
    session: Session = current_app.db.session

    data = request.json

    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(user, key, value)

    session.commit()

    return jsonify(user), HTTPStatus.OK


def delete_user(id: int):
    session: Session = current_app.db.session

    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    session.delete(user)
    session.commit()

    return {"msg": f"User {user.name} deleted"}, HTTPStatus.OK
