from app.configs.database import db


users_workspaces = db.Table(
    "users_workspaces",
    db.Column("users_workspaces_id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.user_id")),
    db.Column("workspace_id", db.Integer, db.ForeignKey("workspaces.workspace_id")),
)
