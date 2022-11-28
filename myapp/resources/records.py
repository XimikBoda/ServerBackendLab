from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from datetime import datetime

#from myapp.views import bd_users

from myapp.db import db
from myapp.models.records import RecordsModel
from myapp.schemas import RecordSchema

blp = Blueprint("record", __name__, description = "Operations on records")


@blp.route("/records/<int:record_id>")
class Records(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        return RecordsModel.query.get_or_404(record_id)

@blp.route("/records")
class RecordsList(MethodView):
    @blp.response(200, RecordSchema(many=True))
    def get(self):
        args = request.args.to_dict()

        id_user = int(-1)
        id_category = int(-1)
        if 'id_user' in args:
                id_user = int(args['id_user'])
        if 'id_category' in args:
                id_category = int(args['id_category'])
        
        ret = []

        if id_user==-1:
            abort(400, messages="Need id_user")

        query = RecordsModel.query.filter(id_user==id_user)

        if id_category != -1:
            query = query.filter(id_category==id_category)

        return query.all()

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_d):
        record = RecordsModel(**request_d)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(400, message="record is already exists")

        return record