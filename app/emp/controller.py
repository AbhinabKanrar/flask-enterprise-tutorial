from flask import Blueprint, request
import app.emp.service as service

emp = Blueprint('emp', __name__, url_prefix='/emp')

@emp.route('/view', methods=['GET'])
def see():
    return "emp"

@emp.route('/save', methods=['POST'])
def save():
    service.save(request.get_json(), request.headers['ws-siteid'])
    return "done"