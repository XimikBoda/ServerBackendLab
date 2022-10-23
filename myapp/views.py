from crypt import methods
from warnings import catch_warnings
from flask import abort, jsonify, request
from jsonschema import validate

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

