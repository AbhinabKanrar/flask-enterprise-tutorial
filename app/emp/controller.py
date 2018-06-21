from flask import Blueprint, request, jsonify
from app.common.domain.schema.error import Error
from app.common.util.resp_mapper import create_resp

import json
import app.emp.service as service


emp = Blueprint('emp', __name__, url_prefix='/emp')

@emp.route('/view', methods=['GET'])
def view():
    return "emp"

@emp.route('/save', methods=['POST'])
def save():
    try:
        payload = request.get_json()
        data = service.save(payload, request.headers['ws-siteid'])
    except AttributeError:
        return create_resp(Error('1011','Please provide valid data in json format'), 400)
    return create_resp(data, 200)