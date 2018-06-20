from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_envvar('FLASK_ENV',silent=True)

ma = Marshmallow(app)
db = SQLAlchemy(app)

from app.common.entity.emp import Employee

db.create_all()
db.session.commit()

from app.emp.controller import emp as emp

app.register_blueprint(emp)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }), 404

@app.errorhandler(400)
def bad_data(error):
    return jsonify({
        'status': 400,
        'message': 'Please provide valid data in json format'
    }), 400

@app.before_request
def before_request():
    try:
        request.headers['ws-siteid']
    except KeyError:
        return jsonify({
        'status': 403,
        'message': 'Not Authorized'
    }), 403