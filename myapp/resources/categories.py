from flask.views import MethodView
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

#from myapp.views import bd_users

from myapp.db import db
from myapp.models.categories import CategoriesModel
from myapp.schemas import CategorySchema

blp = Blueprint("categories", __name__, description = "Operations on categories")

blp.route("/categories/<int:category_id>")
class Categories(MethodView):
    @blp.response(200, CategorySchema)
    @jwt_required()
    def get(self, category_id):
        return CategoriesModel.query.get_or_404(category_id)

@blp.route("/categories")
class CategoriesList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    @jwt_required()
    def get(self):
        return CategoriesModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    @jwt_required()
    def post(self, request_d):
        category = CategoriesModel(**request_d)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Category name is already exists")

        return category
