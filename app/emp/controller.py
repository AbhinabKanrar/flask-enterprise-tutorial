from flask import Blueprint, request, jsonify
from app.common.domain.schema.generic_response import ResponseSchema

import app.emp.service as service


emp = Blueprint('emp', __name__, url_prefix='/emp')

@emp.route('/view', methods=['GET'])
def see():
    return "emp"

@emp.route('/save', methods=['POST'])
def save():
    try:
        data = request.get_json()
        resp = service.save(data, request.headers['ws-siteid'])
    except AttributeError:
        return jsonify({
            'status': 400,
            'message': 'Please provide valid data in json format'
        }), 400
    return jsonify(resp)