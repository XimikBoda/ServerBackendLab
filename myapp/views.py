from flask import jsonify, request
from flask_smorest import abort, Api
from datetime import datetime

from myapp import app

from myapp.db import db

from myapp.resources.users import blp as UsersBlp
from myapp.resources.categories import blp as CategoriesBlp
from myapp.resources.records import blp as RecordsBlp

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = ""
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

api = Api(app)

api.register_blueprint(UsersBlp)
api.register_blueprint(CategoriesBlp)
api.register_blueprint(RecordsBlp)


@app.route("/test")
def test():
    return "<p>Test page</p>"

