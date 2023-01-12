from flask.views import MethodView
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from myapp.db import db
from myapp.models.currencies import CurrenciesModel
from myapp.schemas import CurrencySchema

blp = Blueprint("currencies", __name__, description = "Operations on currencies")

blp.route("/currencies/<int:category_id>")
class Currencies(MethodView):
    @blp.response(200, CurrencySchema)
    @jwt_required()
    def get(self, category_id):
        return CurrenciesModel.query.get_or_404(category_id)

@blp.route("/currencies")
class CurrenciesList(MethodView):
    @blp.response(200, CurrencySchema(many=True))
    @jwt_required()
    def get(self):
        return CurrenciesModel.query.all()

    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    @jwt_required()
    def post(self, request_d):
        category = CurrenciesModel(**request_d)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Currency name is already exists")

        return category
