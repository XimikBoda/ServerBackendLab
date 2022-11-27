from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

#from myapp.views import bd_users

from myapp.db import db_users, db_categories, db_records
from myapp.schemas import CategorySchema

blp = Blueprint("categories", __name__, description = "Operations on categories")

blp.route("/categories/<int:category_id>")
class Categories(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        try:
            return db_categories[category_id]
        except KeyError:
            abort(404, messages="Category is not found")


@blp.route("/categories")
class CategoriesList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return jsonify(db_categories)

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_d):
        last_id = db_categories[-1]["id"]
        if "id" in request_d:
            if request_d["id"] <= last_id:
                abort(400, messages="category_id is wrong")
        else:
            request_d ["id"] = last_id + 1

        db_categories.append(request_d)

        return db_categories[-1]
