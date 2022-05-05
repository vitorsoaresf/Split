from app.configs.database import db
from marshmallow import Schema, fields
from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime
from datetime import datetime


class Comment(db.Model):
    """Comment model.

    This model represents comments about patients.

    Attributes:
        comment_id: A integer value indicating the comment id.
        comment: A string value indicating the comment.
        date_time: A datetime value indicating the date and time of the comment.
        user_id: A integer value indicating the user id who
                 created the comment.
        patient_id: A integer value indicating the data where
                    the comment is attached.
    """

    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True)  # ou comment_id
    comment = Column(Text, nullable=False)  # não está no diagrama.
    date_time = Column(DateTime, default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)

    patient = db.relationship(
        "Patient", back_populates="comments", uselist=False
    )

    user = db.relationship("User", back_populates="comments", uselist=False)

    category = db.relationship("Category", back_populates="comments", uselist=False)


class CommentSchema(Schema):
    """Comment model schema.

    This model represents the schema of comments about patients.
    Will check values and validate them.

    Attributes:
        comment_id: A unique integer value identifying the data.
        comment: A string value with comment.
        date_time: A string value with the date and time of the comment.
        user_id: A integer value indicating the user id who
                 created the comment.
        patient_id: A integer value indicating the pattient who the
                 comment is attached.
        category_id: A integer value indicating the category where the
                 comment is attached.
    """

    comment_id = fields.Integer()
    comment = fields.String()
    date_time = fields.DateTime()
    user_id = fields.Integer()
    patient_id = fields.Integer()
    category_id = fields.Integer()