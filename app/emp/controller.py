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
        data = service.save(data, request.headers['ws-siteid'])
    except AttributeError:
        return jsonify({
            'status': 400,
            'message': 'Please provide valid data in json format'
        }), 400
    except RuntimeError:
        return jsonify({
            'status': 500,
            'message': 'Unable to save the employee at this moment'
        }), 500
    schema = ResponseSchema()
    return resp.dump(data).data