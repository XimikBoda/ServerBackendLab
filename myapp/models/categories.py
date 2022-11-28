from myapp.db import db


class CategoriesModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    records = db.relationship(
        "RecordsModel",
        back_populates="categories",
        lazy="dynamic"    
    )