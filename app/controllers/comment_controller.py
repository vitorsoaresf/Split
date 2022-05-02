from http import HTTPStatus

from app.models.category_model import Category
from app.models.comment_model import Comment, CommentSchema
from app.models.patient_model import Patient
from app.models.user_model import User
from flask import current_app, request
from marshmallow.exceptions import ValidationError


def create_comment():
    """Create new Comments.
    
    A controller to let the user create comments.
    
    Args:
        Receive no args.
        Get the comment, user_id, patient_id and category_id from request.
        Set date.
        
    Returns:
        A json with the new comment. HTTPStatus.CREATED if the comment was created.
        
    Raises:
        HTTPStatus.BAD_REQUEST: If the user is not found.
        HTTPStatus.BAD_REQUEST: If the category is not found.
        HTTPStatus.BAD_REQUEST: If the patient is not found.    
    """
    
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
        return (
            {
                "msg": """Error creating comment,
                      give the give the appropriate keys""",
                "appropriate_keys": {
                    "comment": "string",
                    "patient_id": "integer",
                    "user_id": "integer",
                    "category_id": "integer",
                },
            },
            HTTPStatus.BAD_REQUEST,
        )


def update_comment(id: int):
    """Update a comment.
    
    A controller to let the user update a comment.
    
    Args:
        id: The id of the comment to be updated.
        
    Returns:
        A json with the updated comment. HTTPStatus.OK if the comment was updated.
        
    Raises:
        HTTPStatus.BAD_REQUEST: If the comment is not found.
    """
    
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
        return (
            {
                "msg": """Error updating comment,
                      give the give the appropriate keys""",
                "appropriate_keys": {"comment": "string"},
            },
            HTTPStatus.BAD_REQUEST,
        )


def delete_comment(id: int):
    """Delete a comment.

    Args:
        id: The id of the comment to be deleted.

    Returns:
        A json with a msg: string with the name and a message. HTTPStatus.OK if the comment was deleted.
        
    Raises:
        HTTPStatus.BAD_REQUEST: If the comment is not found.
    """
    
    session = current_app.db.session

    comment = Comment.query.get(id)
    if not comment:
        return {"error": "Comment not Found"}, HTTPStatus.BAD_REQUEST

    session.delete(comment)
    session.commit()

    return {"msg": "Comment deleted"}, HTTPStatus.OK
