from app.configs.database import db
from sqlalchemy import Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass

@dataclass
class Comment(db.Model):

    comment: str

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True) # ou comment_id
    comment = Column(Text, nullable=False) # não está no diagrama.
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    data_id = Column(Integer, ForeignKey("datas.id"), nullable=False)

