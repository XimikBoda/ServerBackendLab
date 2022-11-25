from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort

from datetime import datetime

from jsonschema import validate

#from myapp.views import bd_users

from myapp.db import db_users, db_categories, db_records, db_records_shema

blp = Blueprint("record", __name__, description = "Operations on records")


@blp.route("/records/<int:record_id>")
class Records(MethodView):
    def get(self, record_id):
        try:
            return db_records[record_id]
        except KeyError:
            abort(404, messages="record is not found")

@blp.route("/records")
class RecordsList(MethodView):
    def get(self):
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
                abort(400, messages="wrong parametrs")
            else:
                ret = db_records

        return jsonify(ret)

    def post(self):
        request_d = request.get_json()
        try:
            validate(request_d, db_records_shema)
        except:
            abort(400, messages="json is wrong")

        last_id = db_records[-1]["id"]
        if "id" in request_d:
            if request_d["id"] <= last_id:
                abort(400, messages="record_id is wrong")
        else:
            request_d["id"] = last_id + 1

        if "date_and_time" not in request_d:
            request_d["date_and_time"] = datetime.now().strftime("%Y.%m.%d, %H:%M:%S")

        db_records.append(request_d)

        return db_records[-1]