from myapp.db import db


class CurrenciesModel(db.Model):
    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    coefficient = db.Column(db.Float, nullable=False)

    records = db.relationship(
        "RecordsModel",
        back_populates="currencies",
        lazy="dynamic"    
    )