from flask import Blueprint, request

about = Blueprint('about', __name__, url_prefix='/about')

@about.route('/see', methods=['GET'])
def see():
    return "seen"