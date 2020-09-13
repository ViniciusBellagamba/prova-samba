from flask import abort, make_response, jsonify


def endpoint_ex(code, msg):
    abort(make_response(jsonify(message=msg), code))


def body_validation(body):
    required_keys = ['name', 'url', 'duration', 'deleted']
    for key in required_keys:
        if key not in body.keys():
            raise endpoint_ex(400, f"BAD REQUEST: Missing key: '{key}' on request body")
        if body[key] is None:
            raise endpoint_ex(400, f"BAD REQUEST: Missing key: '{key}' value on request body")
