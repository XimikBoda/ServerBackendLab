from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from jsonschema import validate

#from myapp.views import bd_users

from myapp.db import db_users, db_categories, db_records, db_users_shema
from myapp.schemas import UserSchema

blp = Blueprint("user", __name__, description = "Operations on user")

@blp.route("/users/<int:user_id>")
class Users(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        try:
            return db_users[user_id]
        except KeyError:
            abort(404, messages="User is not found")


@blp.route("/users")
class UsersList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return jsonify(db_users)

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_d):
        last_id = db_users[-1]["id"]
        if "id" in request_d:
            if request_d["id"] <= last_id:
                abort(400, messages="user_id is wrong")
        else:
            request_d ["id"] = last_id + 1

        db_users.append(request_d)

        return db_users[-1]