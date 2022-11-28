from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

#from myapp.views import bd_users

from myapp.db import db
from myapp.models.users import UsersModel
from myapp.schemas import UserSchema

blp = Blueprint("user", __name__, description = "Operations on user")

@blp.route("/users/<int:user_id>")
class Users(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UsersModel.query.get_or_404(user_id)


@blp.route("/users")
class UsersList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UsersModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_d):
        user = UsersModel(**request_d)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="User name is already exists")

        return user