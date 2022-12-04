from myapp.db import db
from sqlalchemy import func


class RecordsModel(db.Model):
    __tablename__ = "records"

    id = db.Column(db.Integer, primary_key=True)

    id_user = db.Column(
        db.Integer, 
        db.ForeignKey("users.id"),
        unique=False,
        nullable=False)

    id_category = db.Column(
        db.Integer, 
        db.ForeignKey("categories.id"),
        unique=False,
        nullable=False)

    
    id_currency = db.Column(
        db.Integer, 
        db.ForeignKey("currencies.id"),
        unique=False,
        nullable=False,
        server_default='1')
    
    date_and_time = db.Column(db.TIMESTAMP, server_default=func.now())

    sum = db.Column(db.Float(precision=2), unique=False, nullable=False)

    users = db.relationship("UsersModel",  back_populates="records")
    categories = db.relationship("CategoriesModel",  back_populates="records")
    currencies = db.relationship("CurrenciesModel",  back_populates="records")
