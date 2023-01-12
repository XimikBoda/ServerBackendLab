from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    coefficient = fields.Float(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    id_user = fields.Int(required=True)
    id_category = fields.Int(required=True)
    id_currency = fields.Int(required=False)
    date_and_time = fields.DateTime("%Y.%m.%d, %H:%M:%S", required=False)
    sum = fields.Float(required=True)

