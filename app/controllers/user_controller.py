import datetime
from http import HTTPStatus
from app.models import Address, AddressSchema
from app.models.user_model import User, UserSchema
from app.models.workspace_model import WorkspaceSchema
from app.services.address_service import svc_create_address, svc_update_address
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


def create_user() -> dict:
    """Create new Users.

    A controller to create new users.

    Args:
        Receive no args.
        Get the name, profession, cpf, phone, email, profession_code, password and address from request.

    Returns:
        A json with the new user. HTTPStatus.CREATED if the user was created.

    Raises:
        HTTPStatus.BAD_REQUEST: If the request is not valid.

    """

    session: Session = current_app.db.session
    data = request.json

    user_schema = UserSchema()

    try:
        address = data.pop("address")
        new_address = svc_create_address(address, session)
        password = data.pop("password")
        password_hash = generate_password_hash(password)
        data["password_hash"] = password_hash

        user_schema.load(data)

        # Normalization
        data["name"] = data["name"].title()
        data["email"] = data["email"].casefold()
        data["profession"] = data["profession"].title()

        new_user = User(**data)
        new_user.address_id = new_address.address_id

        session.add(new_user)
        session.commit()

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

    except KeyError:
        return {
            "msg": "Error creating user",
            "user": data,
            "address": AddressSchema().dump(new_address),
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_users() -> dict:
    """Get all users.

    A controller to get all users.

    Args:
        Receive no args.

    Returns:
        A json with all users. HTTPStatus.OK if users was found.

    Raises:

    """
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


@jwt_required()
def get_user_specific(id: int) -> dict:
    """Get a specific user.

    A controller to get a specific user.

    Args:
        Receive the id of the user.

    Returns:
        A json with the user. HTTPStatus.OK if the user was found.

    Raises:


    """

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
        "workspaces": WorkspaceSchema(many=True, only=["name", "workspace_id"]).dump(
            user.workspaces
        ),
    }, HTTPStatus.OK


@jwt_required()
def update_user(id: int) -> dict:
    """Update a specific user.

    A controller to update a specific user.

    Args:
        Receive the id of the user.

    Returns:
        A json with the user. HTTPStatus.OK if the user was found.

    Raises:
        HTTPStatus.NOT_FOUND: If the user was not found.

    """

    session: Session = current_app.db.session
    data = request.get_json()

    # Normalization
    if "name" in data.keys():
        data["name"] = data["name"].title()
    if "email" in data.keys():
        data["email"] = data["email"].casefold()
    if "profession" in data.keys():
        data["profession"] = data["profession"].title()

    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    if "address" in data.keys():
        new_address = data.pop("address")
        address_id = user.address_id
        svc_update_address(address_id, new_address, session)

    try:
        for key, value in data.items():
            if key == "password":
                value_hash = generate_password_hash(value)
                setattr(user, key, value_hash)
            else:
                setattr(user, key, value)

        session.commit()

        return {
                "_id": user.user_id,
                "name": user.name,
                "profession": user.profession,
                "cpf": user.cpf,
                "phone": user.phone,
                "email": user.email,
                "profession_code": user.profession_code,
                "address": AddressSchema().dump(user.address),
            }, HTTPStatus.OK
    except:
        return {"msg": "Error updating user"}, HTTPStatus.BAD_REQUEST



@jwt_required()
def delete_user(id: int) -> str:
    """Delete a specific user.

    A controller to delete a specific user.

    Args:
        Receive the id of the user.

    Returns:
        A json with a msg: string with the name and a message. HTTPStatus.OK if the user was deleted.

    Raises:
        HTTPStatus.NOT_FOUND: If the user was not found.

    """
    # credentials_user = get_jwt_identity()

    # print(">>>> ", credentials_user)
    session: Session = current_app.db.session

    user = User.query.get(id)

    if not user:
        return {"msg": "User not Found"}, HTTPStatus.NOT_FOUND

    session.delete(user)
    session.commit()

    return {"msg": f"User {user.name} deleted"}, HTTPStatus.OK


def login():

    data: dict = request.get_json()

    session: Session = current_app.db.session

    try:

        user_email = data.pop("email")

        user_password = data.pop("password")

        user: User = session.query(User).filter_by(email=user_email).first()

        if not user:
            raise ValueError

        if not user.verify_password(user_password):
            raise ValueError

        access_token = create_access_token(identity=UserSchema().dump(user), expires_delta=datetime.timedelta(days=366))
        return {"access_token": access_token}, HTTPStatus.OK

    except:
        return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
