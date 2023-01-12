import os
from flask_jwt_extended import JWTManager
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request
from flask_smorest import abort, Api
from datetime import datetime

from myapp import app

from myapp.db import db
from myapp.models.currencies import CurrenciesModel

from myapp.resources.users import blp as UsersBlp
from myapp.resources.categories import blp as CategoriesBlp
from myapp.resources.records import blp as RecordsBlp
from myapp.resources.currencies import blp as CurrenciesBlp

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = ""
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

db.init_app(app)

with app.app_context():
    db.create_all()

    try:
        currency_default_data = CurrenciesModel(name='UAH', id=1, coefficient=1)
        db.session.add(currency_default_data)
        db.session.commit()
    except IntegrityError:
        pass

api = Api(app)

jwt = JWTManager(app)

api.register_blueprint(UsersBlp)
api.register_blueprint(CategoriesBlp)
api.register_blueprint(RecordsBlp)
api.register_blueprint(CurrenciesBlp)

@app.route("/test")
def test():
    return "<p>Test page</p>"

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
   return (
       jsonify({"message": "The token has expired.", "error": "token_expired"}),
       401,
   )

@jwt.invalid_token_loader
def invalid_token_callback(error):
   return (
       jsonify(
           {"message": "Signature verification failed.", "error": "invalid_token"}
       ),
       401,
   )

@jwt.unauthorized_loader
def missing_token_callback(error):
   return (
       jsonify(
           {
               "description": "Request does not contain an access token.",
               "error": "authorization_required",
           }
       ),
       401,
   )
