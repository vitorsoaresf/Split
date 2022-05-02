from http import HTTPStatus

from app.configs.database import db
from app.models.user_model import User
from flask import request
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash


def login():
    """Login a user.
    
    A controller to login a user and return a JWT token.
    
    Args:
        Receive no args.
        Get the email and password from request.
        
    Returns:
        A json with the user and the JWT token. HTTPStatus.OK if the user was logged in.
        
    Raises:
        HTTPStatus.UNAUTHORIZED: If the user is not found.
    """

    data: dict = request.get_json()

    session : Session = db.session

    try:

        user_email = data.pop("email")

        user_password = data.pop("password")

        user : User = session.query(User).filter_by(email = user_email).first()

        if not check_password_hash(user.password_hash, user_password): 

            raise ValueError
        
        return {"token": "abacaxi"}, HTTPStatus.OK
    
    except:

        return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED









