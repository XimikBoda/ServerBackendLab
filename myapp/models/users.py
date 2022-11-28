from myapp.db import db


class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    records = db.relationship(
        "RecordsModel",
        back_populates="users",
        lazy="dynamic"    
    )