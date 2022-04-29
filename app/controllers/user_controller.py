from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.user_model import User, UserSchema
from app.models.workspace_model import Workspace, WorkspaceSchema
from sqlalchemy.orm import Session
from app.models import Address, AddressSchema
from app.configs.database import db


def create_user():
    session: Session = current_app.db.session
    data = request.json

    address = data.pop("address")
    schema = AddressSchema()
    schema.load(address)

    res_address = Address(**address)

    schema = UserSchema()
    schema.load(data)

    user = User(**data)

    session.add(res_address)
    session.commit()

    user.address_id = res_address.address_id

    session.add(user)
    session.commit()

    return {
        "_id": user.user_id,
        "name": user.name,
        "profession": user.profession,
        "cpf": user.cpf,
        "phone": user.phone,
        "email": user.email,
        "profession_code": user.profession_code,
        "address": address,
    }, HTTPStatus.CREATED


def get_users():
    schemaAddress = AddressSchema()

    users = User.query.all()

    list_users = []
    for user in users:
        address = Address.query.get(user.address_id)

        result_user = {
            "_id": user.user_id,
            "name": user.name,
            "profession": user.profession,
            "cpf": user.cpf,
            "phone": user.phone,
            "email": user.email,
            "profession_code": user.profession_code,
            "address": schemaAddress.dump(address),
        }

        list_users.append(result_user)

    return jsonify(list_users), HTTPStatus.OK


def get_user_specific(id: int):
    user = User.query.get(id)
    schemaAddress = AddressSchema()

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    address = Address.query.get(user.address_id)

    return {
        "_id": user.user_id,
        "name": user.name,
        "profession": user.profession,
        "cpf": user.cpf,
        "phone": user.phone,
        "email": user.email,
        "profession_code": user.profession_code,
        "address": schemaAddress.dump(address),
    }, HTTPStatus.OK


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


def get_user_workspaces(id: int):
    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    return (
        jsonify(
            [
                {"name": wk["name"], "workspace_id": wk["workspace_id"]}
                for wk in WorkspaceSchema(many=True).dump(user.workspaces)
            ]
        ),
        200,
    )
