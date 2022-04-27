from app.configs.database import db

categories_workspaces = db.Table('categories_workspaces',
        db.Column("categories_workspaces_id", db.Integer, primary_key=True),
        db.Column("category_id", db.Integer, db.ForeignKey(
                                            "categories.category_id")),
        db.Column("workspace_id", db.Integer, db.ForeignKey(
                                            "workspaces.workspace_id"))
        )
