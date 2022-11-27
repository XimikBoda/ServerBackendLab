from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    id_user = fields.Int(required=True)
    id_category = fields.Int(required=True)
    date_and_time = fields.DateTime("%Y.%m.%d, %H:%M:%S", required=False)
    sum = fields.Float(required=True)

