from flask import jsonify, request
from flask_smorest import abort, Api
from jsonschema import validate
from datetime import datetime

from myapp import app


from myapp.db import db_users, db_categories, db_records, db_users_shema, db_categories_shema, db_records_shema

from myapp.resources.users import blp as UsersBlp
from myapp.resources.categories import blp as CategoriesBlp

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






@app.route("/test")
def test():
    return "<p>Test page</p>"


@app.route("/records", methods=["GET"])
def get_records():
    args = request.args.to_dict()

    id_user = int(-1)
    id_category = int(-1)
    if 'id_user' in args:
            id_user = int(args['id_user'])
    if 'id_category' in args:
            id_category = int(args['id_category'])
    
    ret = []

    if id_user!=-1:
        if id_category != -1:
            for el in db_records:
                if el['id_user'] == id_user and el['id_category'] == id_category:
                    ret.append(el)
        else:
            for el in db_records:
                if el['id_user'] == id_user:
                    ret.append(el)
    else:
        if id_category != -1:
            abort(400)
        else:
            ret = db_records

    return jsonify({"records": ret})

@app.route("/records", methods=["POST"])
def add_records():
    request_d = request.get_json()
    try:
        validate(request_d, db_records_shema)
    except:
        abort(400)

    last_id = db_records[-1]["id"]
    if "id" in request_d:
        if request_d["id"] <= last_id:
            abort(400)
    else:
        request_d["id"] = last_id + 1

    if "date_and_time" not in request_d:
        request_d["date_and_time"] = datetime.now().strftime("%Y.%m.%d, %H:%M:%S")

    db_records.append(request_d)

    return db_records[-1]