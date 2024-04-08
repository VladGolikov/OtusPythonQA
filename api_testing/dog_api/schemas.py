schema_all_breeds = {
    "type": "object",
    "properties": {
        "message": {"type": "object"},
        'status': {"type": "string"}
    },
    "required": ["message", "status"]}


schema_random_image = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        'status': {"type": "string"}
    },
    "required": ["message", "status"]}
