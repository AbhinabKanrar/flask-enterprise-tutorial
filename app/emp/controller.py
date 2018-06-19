from flask import Blueprint, request

emp = Blueprint('emp', __name__, url_prefix='/emp')

@emp.route('/view', methods=['GET'])
def see():
    return "emp"