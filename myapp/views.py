from flask import abort, jsonify, request
from jsonschema import validate
from datetime import datetime

from myapp import app

db_users = [
    {
        "id": 0,
        "name": "NULL user"
    }
]

db_users_shema = {
    "type": "object",
    "properties": {
        "id": {"type": "number",
            "minimum": 0,
            },
        "name": {
            "type": "string",
            },
        "additionalProperties": False
    },
    "required": ["name"]
}      

db_categories = [
    {
        "id": 0,
        "name": "Empty"
    }
]

db_categories_shema = {
    "type": "object",
    "properties": {
        "id": {"type": "number",
            "minimum": 0,
            },
        "name": {
            "type": "string",
            },
        "additionalProperties": False
    },
    "required": ["name"]
} 

db_records = [
    {
        "id": 0,
        "id_user": 0,
        "id_category": 0,
        "date_and_time": "",
        "sum": 0
    }
]
db_records_shema = {
    "type": "object",
    "properties": {
        "id": {"type": "number",
            "minimum": 0,
            },
        "id_user": {
            "type": "number",
            "minimum": 0,
            },
        "id_category": {
            "type": "number",
            "minimum": 0,
            },
        "date_and_time": {
            "type": "string",
            },
        "sum": {
            "type": "number",
            "minimum": 0,
            },
        "additionalProperties": False
    },
    "required": ["id_user", "id_category"]
} 


@app.route("/test")
def test():
    return "<p>Test page</p>"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": db_users})

@app.route("/users", methods=["POST"])
def add_users():
    request_d = request.get_json()
    try:
        validate(request_d, db_users_shema)
    except:
        abort(400)

    last_id = db_users[-1]["id"]
    if "id" in request_d:
        if request_d["id"] <= last_id:
            abort(400)
    else:
        request_d ["id"] = last_id + 1

    db_users.append(request_d)

    return db_users[-1]


@app.route("/categories", methods=["GET"])
def get_categories():
    return jsonify({"categories": db_categories})

@app.route("/categories", methods=["POST"])
def add_categories():
    request_d = request.get_json()
    try:
        validate(request_d, db_categories_shema)
    except:
        abort(400)

    last_id = db_categories[-1]["id"]
    if "id" in request_d:
        if request_d["id"] <= last_id:
            abort(400)
    else:
        request_d ["id"] = last_id + 1

    db_categories.append(request_d)

    return db_categories[-1]

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