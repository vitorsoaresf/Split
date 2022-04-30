from http import HTTPStatus
from flask import request
from sqlalchemy.orm import Session
from app.configs.database import db
from werkzeug.security import check_password_hash

from app.models.user_model import User


def login():

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









