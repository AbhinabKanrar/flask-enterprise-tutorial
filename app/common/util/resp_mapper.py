from flask import jsonify


def create_resp(data, status):
    return jsonify(data.__dict__), status