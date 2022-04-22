from app.configs.database import db
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields


class Category(db.Model):
    """Category model.

    This model represents a category of patients diseases.

    Attributes:
        category_id: A integer value indicating the category id.
        category: A string value indicating the category name.
    """
    
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    category = Column(String(100), nullable=False)
    

class CategorySchema(Schema):
    """Category model schema.
    
    This model represents the schema of category of patients diseases.
    Will check values and validate them.
    
    Attributes:
        category_id: A integer value indicating the category id.
        category: A string value indicating the category name.
    """
    
    category_id = fields.Integer()
    category = fields.String()