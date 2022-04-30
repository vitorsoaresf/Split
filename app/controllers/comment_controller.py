from http import HTTPStatus
from flask import current_app, request
from app.models.comment_model import Comment, CommentSchema
from app.models.user_model import User
from app.models.patient_model import Patient
from app.models.category_model import Category
from marshmallow.exceptions import ValidationError


def create_comment():
    session = current_app.db.session
    data = request.json

    comment_schema = CommentSchema()

    try:
        comment_schema.load(data)

        user = User.query.get(data["user_id"])
        if not user:
            return {"error": "User not Found"}, HTTPStatus.BAD_REQUEST

        get_category = Category.query.get(data["category_id"])
        if not get_category:
            return {"error": "Category not Found"}, HTTPStatus.BAD_REQUEST
        
        get_patient = Patient.query.get(data["patient_id"])
        if not get_patient:
            return {"error": "Patient not Found"}, HTTPStatus.BAD_REQUEST

        comment = Comment(**data)

        session.add(comment)
        session.commit()

        return comment_schema.dump(comment), HTTPStatus.CREATED

    except ValidationError:
        return {
            "msg": """Error creating comment,
                      give the give the appropriate keys""",
            "appropriate_keys": {
                                "comment": "string",
                                'patient_id': "integer",
                                'user_id': "integer",
                                'category_id': "integer"
                                }
            }, HTTPStatus.BAD_REQUEST


def update_comment(id: int):
    session = current_app.db.session
    data = request.json

    comment_schema = CommentSchema()

    try:
        comment_schema.load(data)

        comment = Comment.query.get(id)
        if not comment:
            return {"error": "Comment not Found"}, HTTPStatus.BAD_REQUEST

        comment.comment = data["comment"]

        session.commit()

        return comment_schema.dump(comment), HTTPStatus.OK

    except ValidationError:
        return {
            "msg": """Error updating comment,
                      give the give the appropriate keys""",
            "appropriate_keys": {"comment": "string"}
            }, HTTPStatus.BAD_REQUEST


def delete_comment(id: int):
    session = current_app.db.session

    comment = Comment.query.get(id)
    if not comment:
        return {"error": "Comment not Found"}, HTTPStatus.BAD_REQUEST

    session.delete(comment)
    session.commit()

    return {"msg": "Comment deleted"}, HTTPStatus.OK
