from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.user_model import User, UserSchema
from app.models.workspace_model import WorkspaceSchema
from sqlalchemy.orm import Session
from app.models import Address, AddressSchema
from werkzeug.security import generate_password_hash


def create_user():
    session: Session = current_app.db.session
    data = request.json
    



    address_schema = AddressSchema()
    user_schema = UserSchema()

    try:
        address = data.pop("address")

        password = data.pop("password")
        password_hash = generate_password_hash(password)
        data["password_hash"] = password_hash

        address_schema.load(address)
        new_address = Address(**address)
        user_schema.load(data)

        session.add(new_address)
        session.commit()

        #Normalization
        data['name'] = data['name'].title()
        data['email'] = data['email'].casefold()
        data['profession'] = data['profession'].title()
        data['function'] =  data['function'].title()

        new_user = User(**data)
        new_user.address_id = new_address.address_id

        session.add(new_user)
        session.commit()
    except:
        return {"msg": "Error creating user", "user": data, "address": AddressSchema.dump(new_address)}, HTTPStatus.BAD_REQUEST
    
    return {
        "_id": new_user.user_id,
        "name": new_user.name,
        "profession": new_user.profession,
        "cpf": new_user.cpf,
        "phone": new_user.phone,
        "email": new_user.email,
        "profession_code": new_user.profession_code,
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
        "workspaces": WorkspaceSchema(many=True, only=["name", "workspace_id"]).dump(user.workspaces)
    }, HTTPStatus.OK


def update_user(id: int):
    session: Session = current_app.db.session
    data = request.get_json()

    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND
    
    for key, value in data.items():

        if key == "password":
            value_hash = generate_password_hash(value)
            setattr(user,key, value_hash)
        else:
            setattr(user, key, value)

    session.commit()

    return UserSchema(exclude=["password_hash"]).dump(user), HTTPStatus.OK


def delete_user(id: int):
    session: Session = current_app.db.session

    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    session.delete(user)
    session.commit()

    return {"msg": f"User {user.name} deleted"}, HTTPStatus.OK



