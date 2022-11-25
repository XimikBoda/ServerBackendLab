db_users = [
    {
        "id": 0,
        "name": "NULL user"
    }
]

db_categories = [
    {
        "id": 0,
        "name": "Empty"
    }
]

db_records = [
    {
        "id": 0,
        "id_user": 0,
        "id_category": 0,
        "date_and_time": "",
        "sum": 0
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