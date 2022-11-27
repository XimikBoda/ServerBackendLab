from flask import jsonify, request
from flask_smorest import abort, Api
from datetime import datetime

from myapp import app


from myapp.db import db_users, db_categories, db_records, db_users_shema, db_categories_shema, db_records_shema

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

api = Api(app)

api.register_blueprint(UsersBlp)
api.register_blueprint(CategoriesBlp)
api.register_blueprint(RecordsBlp)


@app.route("/test")
def test():
    return "<p>Test page</p>"

