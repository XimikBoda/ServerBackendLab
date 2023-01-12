from flask.views import MethodView
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256

#from myapp.views import bd_users

from myapp.db import db
from myapp.models.users import UsersModel
from myapp.schemas import UserSchema

blp = Blueprint("user", __name__, description = "Operations on user")

@blp.route("/login")
class Login(MethodView):
    def get(self):
        request_d = request.get_json()
        user = UsersModel.query.filter_by(name=request_d["name"]).first()

        if user and pbkdf2_sha256.verify(request_d["password"], user.password):
           access_token = create_access_token(identity=user.id)
           return jsonify(access_token=access_token)
        else:
            return jsonify({"msg": "Bad name or password"}), 401


#@blp.route("/login")
#class Login(MethodView):
#    @blp.response(200, UserSchema(many=True))
#    def get(self):
#        return UsersModel.query.all()

@blp.route("/registration")
class Registration(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_d):
        user = UsersModel(name=request_d["name"], password=pbkdf2_sha256.hash(request_d["password"]))

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="User name is already exists")

        return user