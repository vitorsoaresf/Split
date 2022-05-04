from flask import Blueprint
from app.controllers import categorie_controller

bp = Blueprint("categories",__name__,url_prefix= "/categories")

bp.get("")(categorie_controller.get_categories)